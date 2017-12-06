from github import Github
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", help="Test Mode, do not create Github issues")

args = parser.parse_args()



secret_file = open('github.secret', 'r')
token_string = secret_file.readline().rstrip("\n\r")

wiki_file = open('wikitemplate.md', 'r')
template = wiki_file.read()

g = Github(token_string, timeout=1000)
rate = g.get_rate_limit()
limit = rate.rate.limit
remaining = rate.rate.remaining

print("Rate Limit: " + str(limit))
print("Rate Remaining: " + str(remaining))

repo = g.get_organization("brave").get_repo("browser-laptop")

milestone_dictionary = {}
for milestone in repo.get_milestones(state="open"):
  milestone_dictionary.update({milestone.title:milestone})

key = sorted(milestone_dictionary.keys())[0]
print(key)

checklist = []
release_notes = []
exclusion_list = []
mac_checklist = []
win32_checklist = []
win64_checklist = []
linux_checklist = []

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

    if('QA/test-plan-specified' in label_names and 'QA/no-qa-needed' not in label_names):
      output_line = ' - [ ] ' + issue_title + '. ([#' + str(issue.number) + '](' + issue.html_url + '))'
      checklist.append(output_line)
      checklist.append(issue.html_url)
      if('QA/checked-macOS' not in label_names and 'QA/checked' not in label_names and 'OS/Windows' not in label_names and 'OS/unix-like/linux' not in label_names):
        mac_checklist.append(output_line)

      if('QA/checked-Win64' not in label_names and 'OS/macOS' not in label_names and 'OS/unix-like/linux' not in label_names):
        win64_checklist.append(output_line)

      if('QA/checked-Linux' not in label_names and 'OS/Windows' not in label_names and 'OS/macOS' not in label_names):
        linux_checklist.append(output_line)

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

print("Mac Checklist:")
bigline = "## Per release specialty tests\n"
for line in mac_checklist:
  bigline += line + "\n"
bigline = bigline + template
print(bigline)
print("")
mactitle = "Manual test run on OS X for " + key
maclist = ['OS/macOS', 'release-notes/exclude', 'tests']

if args.test is None:
  repo.create_issue(title=mactitle,body=bigline,assignee="LaurenWags",milestone=milestone_dictionary[key] ,labels=maclist)

print("Winx64 Checklist:")
bigline = "## Per release specialty tests\n"
for line in win64_checklist:
  bigline += line + "\n"
bigline = bigline + template
print(bigline)
print("")
wintitle = "Manual test run on Windows x64 for " + key
winlist = ['OS/Windows', 'release-notes/exclude', 'tests']

if args.test is None:
  repo.create_issue(title=wintitle,body=bigline,assignee="srirambv",milestone=milestone_dictionary[key] ,labels=winlist)

print("Linux Checklist:")
bigline = "## Per release specialty tests\n"
for line in linux_checklist:
  bigline += line + "\n"
bigline = bigline + template
print(bigline)
print("")
lintitle = "Manual test run on Linux for " + key
linlist = ['OS/unix-like/linux', 'release-notes/exclude', 'tests']

if args.test is None:
  repo.create_issue(title=lintitle,body=bigline,assignee="kjozwiak",milestone=milestone_dictionary[key] ,labels=linlist)
