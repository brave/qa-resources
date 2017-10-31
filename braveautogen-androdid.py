from github import Github
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", help="Test Mode, do not create Github issues")

args = parser.parse_args()



secret_file = open('github.secret', 'r')
token_string = secret_file.readline().rstrip("\n\r")

wiki_file = open('wikitemplate-android.md', 'r')
template = wiki_file.read()

g = Github(token_string, timeout=1000)
rate = g.get_rate_limit()
limit = rate.rate.limit
remaining = rate.rate.remaining

print("Rate Limit: " + str(limit))
print("Rate Remaining: " + str(remaining))

repo = g.get_organization("brave").get_repo("browser-android-tabs")

milestone_dictionary = {}
for milestone in repo.get_milestones(state="open"):
  milestone_dictionary.update({milestone.title:milestone})

key = sorted(milestone_dictionary.keys())[0]
print(key)

checklist = []
release_notes = []
exclusion_list = []
android_arm_checklist = []
android_x86_checklist = []

for issue in repo.get_issues(milestone=milestone_dictionary[key], state="closed"):
  if('pull' not in issue.html_url):
    original_issue_title = issue.title
    issue_title = original_issue_title
    if(original_issue_title[0].islower()):
      lower = original_issue_title[0]
      upper = original_issue_title[0].upper()
      issue_title = original_issue_title.replace(lower, upper, 1)

    labels = issue.get_labels()
    label_names = []
    for label in labels:
      label_names.append(label.name)
    if('release-notes/include' in label_names):
      output_line = ' - ' + issue_title + '. ([#' + str(issue.number) + '](' + issue.html_url + '))'
      release_notes.append(output_line)

    if('QA/steps-specified' in label_names and 'QA/no-qa-needed' not in label_names):
      output_line = ' - [ ] ' + issue_title + '. ([#' + str(issue.number) + '](' + issue.html_url + '))'
      checklist.append(output_line)
      checklist.append(issue.html_url)
      if('checked by qa - Android ARM' not in label_names and 'checked by qa' not in label_names):
        android_arm_checklist.append(output_line)

      if('checked by qa - Android x86' not in label_names and 'checked by qa' not in label_names):
        android_x86_checklist.append(output_line)

    else:
      output_line = ' - [ ] ' + issue_title + '. ([#' + str(issue.number) + '](' + issue.html_url + '))'
      exclusion_list.append(output_line)
      exclusion_list.append(issue.html_url)

print("Release Notes:")
for line in release_notes:
  print(line)
print("")

print("Checklist:")
for line in checklist:
  print(line)
print("")

print("Exclusion List:")
for line in exclusion_list:
  print(line)
print("")

print("Android ARM Checklist:")
bigline = "## Per release specialty tests\n"
for line in android_arm_checklist:
  bigline += line + "\n"
bigline = bigline + template
print(bigline)
print("")
AndroidARMtitle = "Manual test run on Android ARM  for " + key
AndroidARMlist = ['ARM', 'release-notes/exclude', 'tests']

if args.test is None:
  repo.create_issue(title=AndroidARMtitle,body=bigline,assignee="LaurenWags",milestone=milestone_dictionary[key] ,labels=AndroidARMlist)

print("Android x86 Checklist:")
bigline = "## Per release specialty tests\n"
for line in android_x86_checklist:
  bigline += line + "\n"
bigline = bigline + template
print(bigline)
print("")
Androidx86title = "Manual test run on Android x86 for " + key
Androidx86list = ['x86', 'release-notes/exclude', 'tests']

if args.test is None:
  repo.create_issue(title=Androidx86title,body=bigline,assignee="srirambv",milestone=milestone_dictionary[key] ,labels=Androidx86list)

