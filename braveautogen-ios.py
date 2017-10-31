from github import Github
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", help="Test Mode, do not create Github issues")

args = parser.parse_args()



secret_file = open('github.secret', 'r')
token_string = secret_file.readline().rstrip("\n\r")

wiki_file = open('wikitemplate-ios.md', 'r')
template = wiki_file.read()

g = Github(token_string, timeout=1000)
rate = g.get_rate_limit()
limit = rate.rate.limit
remaining = rate.rate.remaining

print("Rate Limit: " + str(limit))
print("Rate Remaining: " + str(remaining))

repo = g.get_organization("brave").get_repo("browser-ios")

milestone_dictionary = {}
for milestone in repo.get_milestones(state="open"):
  milestone_dictionary.update({milestone.title:milestone})

key = sorted(milestone_dictionary.keys())[0]
print(key)

checklist = []
release_notes = []
exclusion_list = []
iOS10_iPad_checklist = []
iOS11_iPad_checklist = []
iOS10_iPhone6_checklist = []
iOS11_iPhone7_checklist = []

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

    if('QA/Steps-specified' in label_names and 'QA/No-QA required' not in label_names):
      output_line = ' - [ ] ' + issue_title + '. ([#' + str(issue.number) + '](' + issue.html_url + '))'
      checklist.append(output_line)
      checklist.append(issue.html_url)
      if('checked by qa - iOS10 iPad' not in label_names and 'checked by qa' not in label_names):
        iOS10_iPad_checklist.append(output_line)

      if('checked by qa - iOS11 iPad' not in label_names and 'checked by qa' not in label_names):
        iOS11_iPad_checklist.append(output_line)

      if('checked by qa - iPhone 6 (iOS10)' not in label_names and 'checked by qa' not in label_names):
        iOS10_iPhone6_checklist.append(output_line)

      if('checked by qa - iPhone 7+ (iOS11)' not in label_names and 'checked by qa' not in label_names):
        iOS11_iPhone7_checklist.append(output_line)

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

print("iOS10 iPad Checklist:")
bigline = "## Per release specialty tests\n"
for line in iOS10_iPad_checklist:
  bigline += line + "\n"
bigline = bigline + template
print(bigline)
print("")
iOS10iPadtitle = "Manual test run on iOS10 iPad for " + key
iOS10iPadlist = ['iPad', 'release-notes/exclude', 'tests']

if args.test is None:
  repo.create_issue(title=iOS10iPadtitle,body=bigline,assignee="LaurenWags",milestone=milestone_dictionary[key] ,labels=iOS10iPadlist)

print("iOS11 iPad Checklist:")
bigline = "## Per release specialty tests\n"
for line in iOS11_iPad_checklist:
  bigline += line + "\n"
bigline = bigline + template
print(bigline)
print("")
iOS11iPadtitle = "Manual test run on iOS11 iPad for " + key
iOS11iPadlist = ['iPad', 'release-notes/exclude', 'tests']

if args.test is None:
  repo.create_issue(title=iOS11iPadtitle,body=bigline,assignee="alexwykoff",milestone=milestone_dictionary[key] ,labels=iOS11iPadlist)

print("iOS10 iPhone6 Checklist:")
bigline = "## Per release specialty tests\n"
for line in iOS10_iPhone6_checklist:
  bigline += line + "\n"
bigline = bigline + template
print(bigline)
print("")
iOS10iPhone6title = "Manual test run on iOS10 iPhone6 for " + key
iOS10iPhone6list = ['iPhone', 'release-notes/exclude', 'tests']

if args.test is None:
  repo.create_issue(title=iOS10iPhone6title,body=bigline,assignee="LaurenWags",milestone=milestone_dictionary[key] ,labels=iOS10iPhone6list)

print("iOS11 iPhone7 Checklist:")
bigline = "## Per release specialty tests\n"
for line in iOS11_iPhone7_checklist:
  bigline += line + "\n"
bigline = bigline + template
print(bigline)
print("")
iOS11iPhone7title = "Manual test run on iOS11 iPhone7 for " + key
iOS11iPhone7list = ['iPhone', 'release-notes/exclude', 'tests']

if args.test is None:
  repo.create_issue(title=iOS11iPhone7title,body=bigline,assignee="srirambv",milestone=milestone_dictionary[key] ,labels=iOS11iPhone7list)
