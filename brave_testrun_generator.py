from github import Github
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", help="Test Mode, do not create Github issues")

args = parser.parse_args()

secret_file = open('github.secret', 'r')
token_string = secret_file.readline().rstrip("\n\r")

g = Github(token_string, timeout=1000)
rate = g.get_rate_limit()
limit = rate.rate.limit
remaining = rate.rate.remaining

print("Rate Limit: " + str(limit))
print("Rate Remaining: " + str(remaining))

laptop_repo = g.get_organization("brave").get_repo("brave-browser")
ios_repo = g.get_organization("brave").get_repo("brave-ios")
android_repo = g.get_organization("brave").get_repo("browser-android-tabs")

checklist = []
release_notes = []
mac_checklist = []
win32_checklist = []
win64_checklist = []
linux_checklist = []
iOS10_iPad_checklist = []
iOS11_iPad_checklist = []
iOS10_iPhone6_checklist = []
iOS11_iPhone7_checklist = []
android_x86_checklist = []
android_arm_checklist = []

laptop_milestone = {}
for laptopmilestone in laptop_repo.get_milestones(state="open"):
  laptop_milestone.update({laptopmilestone.title:laptopmilestone})

ios_milestone = {}
for iosmilestone in ios_repo.get_milestones(state="open"):
    ios_milestone.update({iosmilestone.title:iosmilestone})

android_milestone = {}
for androidmilestone in android_repo.get_milestones(state="open"):
    android_milestone.update({androidmilestone.title:androidmilestone})

wiki_laptop_file = open('wikitemplate.md', 'r')
laptop_template = wiki_laptop_file.read()
  
laptop_key = sorted(laptop_milestone.keys())
key1 = sorted(laptop_milestone.keys())[0]
key2 = sorted(laptop_milestone.keys())[1]
key3 = sorted(laptop_milestone.keys())[2]
key4 = sorted(laptop_milestone.keys())[3]
key5 = sorted(laptop_milestone.keys())[4]

def laptop_testruns(milestonever):
	
	for issue in laptop_repo.get_issues(milestone=laptop_milestone[milestonever], sort="created", direction="asc", state="closed"):
		if('pull' not in issue.html_url):
			original_issue_title =  issue.title
			issue_title = original_issue_title
			if(original_issue_title[0].islower()):
				lower = original_issue_title[0]
				upper = original_issue_title[0].upper()
				issue_title = original_issue_title.replace(lower, upper, 1)

			labels = issue.get_labels()
			label_names = []

			for label in labels:
				label_names.append(label.name)
			if('release-notes/include' in label_names and 'QA/No' not in label_names and 'tests' not in label_names):
				output_line = ' - ' + issue_title + '.([#' + str(issue.number) + '](' + issue.html_url + '))'
				release_notes.append(output_line)

			if('QA/Yes' in label_names and 'QA/No' not in label_names and 'tests' not in label_names ):
				output_line = ' - [ ] ' + issue_title + '.([#' + str(issue.number) + '](' + issue.html_url + '))'
				checklist.append(output_line)
				if('QA Pass-macOS' not in label_names and 'OS/Windows' not in label_names and 'OS/Linux' not in label_names and 'QA/No' not in label_names):
					mac_checklist.append(output_line)

				if('QA Pass-Win64' not in label_names and 'OS/macOS' not in label_names and 'OS/Linux' not in label_names and 'QA/No' not in label_names):
					win64_checklist.append(output_line)

				if('QA Pass-Linux' not in label_names and 'OS/Windows' not in label_names and 'OS/macOS' not in label_names and 'QA/No' not in label_names):
					linux_checklist.append(output_line)

	print("Release Notes ")
	for line in release_notes:
		print(line)
	print("")

	print("Checklist: ")
	for line in checklist:
		print(line)
	print("")
	
	print("Mac Checklist:")
	bigline = "## Per release specialty tests\n"
	for line in mac_checklist:
	  bigline += line + "\n"
	bigline = bigline + laptop_template
	print(bigline)
	print("")
	macTitle = "Manual test run on OS X for " + milestonever
	macList = ['OS/macOS', 'release-notes/exclude', 'tests']

	if args.test is None:
	  laptop_repo.create_issue(title=macTitle, body=bigline, assignee="LaurenWags", milestone=laptop_milestone[milestonever], labels=macList)

	print("Win64 Checklist:")
	bigline = "## Per release specialty tests\n"
	for line in win64_checklist:
	  bigline += line + "\n"
	bigline = bigline + laptop_template
	print(bigline)
	print("")
	winTitle = "Manual test run on Windows x64 for " + milestonever
	winList = ['OS/Windows', 'release-notes/exclude', 'tests']

	if args.test is None:
	  laptop_repo.create_issue(title=winTitle, body=bigline, assignee="srirambv", milestone=laptop_milestone[milestonever], labels=winList)

	print("Linux Checklist:")
	bigline = "## Per release specialty tests\n"
	for line in linux_checklist:
	  bigline += line + "\n"
	bigline = bigline + laptop_template
	print(bigline)
	print("")
	linTitle = "Manual test run on Linux for " + milestonever
	linList = ['OS/unix-like/linux', 'release-notes/exclude', 'tests']

	if args.test is None:
	  laptop_repo.create_issue(title=linTitle, body=bigline, assignee="btlechowski", milestone=laptop_milestone[milestonever], labels=linList)

	return 0 

def laptop_perrel_checklist(milestonever):
	
	for issue in laptop_repo.get_issues(milestone=laptop_milestone[milestonever], sort="created", direction="asc", state="closed"):
		if('pull' not in issue.html_url):
			original_issue_title =  issue.title
			issue_title = original_issue_title
			if(original_issue_title[0].islower()):
				lower = original_issue_title[0]
				upper = original_issue_title[0].upper()
				issue_title = original_issue_title.replace(lower, upper, 1)

			labels = issue.get_labels()
			label_names = []

			for label in labels:
				label_names.append(label.name)
			if('release-notes/include' in label_names or 'release-notes/exclude' in label_names and 'tests' not in label_names):
				output_line = ' - ' + issue_title + '.([#' + str(issue.number) + '](' + issue.html_url + '))'
				release_notes.append(output_line)

			if('QA/Yes' in label_names and 'QA/No' not in label_names and 'tests' not in label_names):
				output_line = ' - [ ] ' + issue_title + '.([#' + str(issue.number) + '](' + issue.html_url + '))'
				checklist.append(output_line)
				if('QA/checked-macOS' not in label_names and 'QA/checked' not in label_names and 'OS/Windows' not in label_names and 'OS/unix-like/linux' not in label_names):
					mac_checklist.append(output_line)

				if('QA/checked-Win64' not in label_names and 'QA/checked' not in label_names and 'OS/macOS' not in label_names and 'OS/unix-like/linux' not in label_names):
					win64_checklist.append(output_line)

				if('QA/checked-Linux' not in label_names and 'QA/checked' not in label_names and 'OS/Windows' not in label_names and 'OS/macOS' not in label_names):
					linux_checklist.append(output_line)

	print("Release Notes ")
	for line in release_notes:
		print(line)
	print("")

	print("Checklist: ")
	for line in checklist:
		print(line)
	print("")
	
	print("Mac Checklist:")
	bigline = "## Per release specialty tests\n"
	for line in mac_checklist:
	  bigline += line + "\n"
	print(bigline)
	print("")
	macTitle = "Manual test run on OS X for " + milestonever
	macList = ['OS/macOS', 'release-notes/exclude', 'tests']

	if args.test is None:
	  repo.create_issue(title=macTitle, body=bigline, assignees="LaurenWags,kjozwiak", milestone=laptop_milestone[milestonever], labels=macList)

	print("Win64 Checklist:")
	bigline = "## Per release specialty tests\n"
	for line in win64_checklist:
	  bigline += line + "\n"
	print(bigline)
	print("")
	winTitle = "Manual test run on Windows x64 for " + milestonever
	winList = ['OS/Windows', 'release-notes/exclude', 'tests']

	if args.test is None:
	  repo.create_issue(title=winTitle, body=bigline, assignees="srirambv,GeetaSarvadnya", milestone=laptop_milestone[milestonever], labels=winList)

	print("Linux Checklist:")
	bigline = "## Per release specialty tests\n"
	for line in linux_checklist:
	  bigline += line + "\n"
	print(bigline)
	print("")
	linTitle = "Manual test run on Linux for " + milestonever
	linList = ['OS/unix-like/linux', 'release-notes/exclude', 'tests']

	if args.test is None:
	  repo.create_issue(title=linTitle, body=bigline, assignees="kjozwiak,btlechowski", milestone=laptop_milestone[milestonever], labels=linList)

	return 0 

def ios_testruns():

  wikitemplate_ios = open('wikitemplate-ios.md', 'r')
  ios_template = wikitemplate_ios.read()

  print(sorted(ios_milestone.keys()))
  
  ios_key = sorted(ios_milestone.keys())[0]

  for issue in ios_repo.get_issues(milestone=ios_milestone[ios_key],  sort="created", direction="asc", state="closed"):
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
      if('release-notes/include' in label_names and 'QA/No' in label_names and 'tests' not in label_names):
        output_line = ' - ' + issue_title + '. ([#' + str(issue.number) + '](' + issue.html_url + '))'
        release_notes.append(output_line)

      if('QA/Yes' in label_names and 'QA/No' not in label_names):
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

  print("Release Note:")
  for line in release_notes:
    print(line)
  print("")

  print("Release Checklist:")
  for line in checklist:
    print(line)
  print("")

  print("iOS10 iPad Checklist:")
  bigline = "## Per release speciality tests\n"
  for line in iOS10_iPad_checklist:
    bigline += line + "\n"
  bigline = bigline + ios_template
  print(bigline)
  print("")
  iOS10iPadTitle = "Manual test run for iOS10 iPad for " + ios_key
  iOS10iPadList = ['ipad', 'release-notes/exclude', 'tests']

  if args.test is None:
    ios_repo.create_issue(title=iOS10iPadTitle,body=bigline,assignee="LaurenWags",milestone=ios_milestone[ios_key],labels=iOS10iPadList)

  print("iOS11 iPad Checklist:")
  bigline = "## Per release speciality tests\n"
  for line in iOS11_iPad_checklist:
    bigline += line + "\n"
  bigline = bigline + ios_template
  print(bigline)
  print("")
  iOS11iPadTitle = "Manual test run for iOS11 iPad for " + ios_key
  iOS11iPadList = ['ipad', 'release-notes/exclude', 'tests']

  if args.test is None:
    ios_repo.create_issue(title=iOS11iPadTitle,body=bigline,assignee="srirambv",milestone=ios_milestone[ios_key],labels=iOS11iPadList)

  print("iOS10 iPhone6 Checklist:")
  bigline = "## Per release speciality tests\n"
  for line in iOS10_iPhone6_checklist:
    bigline += line + "\n"
  bigline = bigline + ios_template
  print(bigline)
  print("")
  iOS10iPhone6Title = "Manual test run for iOS10 iPhone 6 for " + ios_key
  iOS10iPhone6List = ['iPhone', 'release-notes/exclude', 'tests']

  if args.test is None:
    ios_repo.create_issue(title=iOS10iPhone6Title,body=bigline,assignee="LaurenWags",milestone=ios_milestone[ios_key],labels=iOS10iPhone6List)

  print("iOS11 iPhone7 Checklist:")
  bigline = "## Per release speciality tests\n"
  for line in iOS11_iPhone7_checklist:
    bigline += line + "\n"
  bigline = bigline + ios_template
  print(bigline)
  print("")
  iOS11iPhone7Title = "Manual test run for iOS11 iPhone7+ for " + ios_key
  iOS11iPhone7List = ['iPhone', 'release-notes/exclude', 'tests']

  if args.test is None:
    ios_repo.create_issue(title=iOS11iPhone7Title,body=bigline,assignee="srirambv",milestone=ios_milestone[ios_key],labels=iOS11iPhone7List)

  return

def android_testruns():

  wikitemplate_android = open('wikitemplate-android.md','r')
  android_template = wikitemplate_android.read()

  android_key = sorted(android_milestone.keys())[0]

  for issue in android_repo.get_issues(milestone=android_milestone[android_key],  sort="created", direction="asc", state="closed"):
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
      if('QA/Yes' in label_names ):
        output_line = ' - ' + issue_title + '.([#' + str(issue.number) + '])' + issue.html_url + '))'
        release_notes.append(output_line)

      if('QA/Yes' in label_names and 'QA/No' not in label_names):
        output_line = ' - [ ] ' + issue_title + '. ([#' + str(issue.number) + '](' + issue.html_url + '))'
        checklist.append(output_line)
        checklist.append(issue.html_url)
        if('checked by qa - Android ARM' not in label_names and 'checked by qa' not in label_names):
          android_arm_checklist.append(output_line)

        if('checked by qa - android x86' not in label_names and 'checked by qa' not in label_names):
          android_x86_checklist.append(output_line)

  print("Release Notes:")
  for line in release_notes:
    print(line)
  print("")

  print("Checklist:")
  for line in checklist:
    print(line)
  print("")

  print("Android ARM Checklist:")
  bigline = "## Per release specialty tests\n"
  for line in android_arm_checklist:
    bigline += line + "\n"
  bigline = bigline + android_template
  print(bigline)
  print("")
  AndroidARMtitle = "Manual test run on Android ARM  for " + android_key
  AndroidARMlist = ['ARM', 'release-notes/exclude', 'tests']

  if args.test is None:
    android_repo.create_issue(title=AndroidARMtitle,body=bigline,assignee="LaurenWags",milestone=android_milestone[android_key] ,labels=AndroidARMlist)

  print("Android x86 Checklist:")
  bigline = "## Per release specialty tests\n"
  for line in android_x86_checklist:
    bigline += line + "\n"
  bigline = bigline + android_template
  print(bigline)
  print("")
  Androidx86title = "Manual test run on Android x86 for " + android_key
  Androidx86list = ['x86', 'release-notes/exclude', 'tests']

  if args.test is None:
    android_repo.create_issue(title=Androidx86title,body=bigline,assignee="srirambv",milestone=android_milestone[android_key] ,labels=Androidx86list)

  return

print('**************************************************************************************************************************')
print('                         Few things to check before generating test runs')
print('')
print('1. Ensure all closed items have QA/Yes and QA/No labels added to include in the test run')
print('')
print('2. For Laptop - Test runs will be generated upto 5 milestones')
print('')
print('3. Manually change milestone.keys value to generate for a specific milestone on any platform')
print('**************************************************************************************************************************')

header = print("Create test runs for:\n")
laptop = print("1. Laptop Release")
laptop_per = print("2. Laptop Per-release Checklist")
ios = print("3. iOS")
android = print("4. Android\n")

select_checklist = input("Choose the platform for which you want to generate the test run: ")

if(select_checklist == '1' or select_checklist == '2'):
  print("\nSelect the milestone to create tests \n")

  length = 0
  while length < len(laptop_key):
  	print(str(length+1) + ". " + sorted(laptop_milestone.keys())[length])
  	length += 1

  generate_test = input("\nCreate test runs for: ")

  if(select_checklist == "1" and generate_test == "1"):
  	print("\nGenerating test runs for " + str(sorted(laptop_milestone.keys())[0]) +  " on all platforms")
  	print(sorted(laptop_milestone.keys())[0])
  	laptop_testruns(key1)
  elif(select_checklist == "1" and generate_test == "2"):
  	print("\nGenerating test runs for " + str(sorted(laptop_milestone.keys())[1]) +  " on all platforms")
  	print(sorted(laptop_milestone.keys())[1])
  	laptop_testruns(key2)
  elif(select_checklist == "1" and generate_test == "3"):
  	print("\nGenerating test runs for " + str(sorted(laptop_milestone.keys())[2]) +  " on all platforms")
  	print(sorted(laptop_milestone.keys())[2])
  	laptop_testruns(key3)
  elif(select_checklist == "1" and generate_test == "4"):
    print("\nGenerating test runs for " + str(sorted(laptop_milestone.keys())[3]) +  " on all platforms")
    print(sorted(laptop_milestone.keys())[3])
    laptop_testruns(key4)
  elif(select_checklist == "1" and generate_test == "5"):
    print("\nGenerating test runs for " + str(sorted(laptop_milestone.keys())[4]) +  " on all platforms")
    print(sorted(laptop_milestone.keys())[4])
    laptop_testruns(key5)
  elif(select_checklist == "2" and generate_test == "1"):
  	print("\nGenerating Per-release checklist for " + str(sorted(laptop_milestone.keys())[0]) +  " on all platforms")
  	print(sorted(laptop_milestone.keys())[0])
  	laptop_perrel_checklist(key1)
  elif(select_checklist == "2" and generate_test == "2"):
  	print("\nGenerating Per-release checklist for " + str(sorted(laptop_milestone.keys())[1]) +  " on all platforms")
  	print(sorted(laptop_milestone.keys())[1])
  	laptop_perrel_checklist(key2)
  elif(select_checklist == "2" and generate_test == "3"):
  	print("\nGenerating Per-release checklist for " + str(sorted(laptop_milestone.keys())[2]) +  " on all platforms")
  	print(sorted(laptop_milestone.keys())[2])
  	laptop_perrel_checklist(key3)
  elif(select_checklist == "2" and generate_test == "4"):
    print("\nGenerating Per-release checklist for " + str(sorted(laptop_milestone.keys())[3]) +  " on all platforms")
    print(sorted(laptop_milestone.keys())[3])
    laptop_perrel_checklist(key4)
  elif(select_checklist == "2" and generate_test == "5"):
    print("\nGenerating Per-release checklist for " + str(sorted(laptop_milestone.keys())[4]) +  " on all platforms")
    print(sorted(laptop_milestone.keys())[4])
    laptop_perrel_checklist(key5)
  else:
  	print("Nothing to create in this milestone. Run the script again.")
  	exit()

elif (select_checklist == '3'):
	generate_ios_test = print("Generating test runs for iOS ",sorted(ios_milestone.keys())[0])
	ios_testruns()
elif (select_checklist == '4'):
	generate_android_test = print("Generating test runs for android",sorted(android_milestone.keys())[0])
	android_testruns()
else:
	print("Incorrect selection. Exiting test creation...")
	exit()