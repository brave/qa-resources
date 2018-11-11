from github import Github
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test",
                    help="Test Mode, do not create Github issues")

args = parser.parse_args()

secret_file = open("github.secret", "r")
token_string = secret_file.readline().rstrip("\n\r")

g = Github(token_string, timeout=1000)
rate = g.get_rate_limit()
limit = rate.rate.limit
remaining = rate.rate.remaining

print("Connecting to GitHub")
print("Fetching Data")

laptop_repo = g.get_organization("brave").get_repo("brave-browser")
ios_repo = g.get_organization("brave").get_repo("brave-ios")
android_repo = g.get_organization("brave").get_repo("browser-android-tabs")

changelog = []
crash_list = []
general_list = []
privacy_list = []
regression_list = []
rewards_list = []
shields_list = []
sync_list = []
webcompat_list = []
iPad_list = []
iPhone_list = []
android_list = []

laptop_milestone = {}
for laptopmilestone in laptop_repo.get_milestones(state="open"):
    laptop_milestone.update({laptopmilestone.title: laptopmilestone})

ios_milestone = {}
for iosmilestone in ios_repo.get_milestones(state="open"):
    ios_milestone.update({iosmilestone.title: iosmilestone})

android_milestone = {}
for androidmilestone in android_repo.get_milestones(state="open"):
    android_milestone.update({androidmilestone.title: androidmilestone})

laptop_key = sorted(laptop_milestone.keys())
key1 = sorted(laptop_milestone.keys())[0]
key2 = sorted(laptop_milestone.keys())[1]
key3 = sorted(laptop_milestone.keys())[2]
key4 = sorted(laptop_milestone.keys())[3]
key5 = sorted(laptop_milestone.keys())[4]


def laptop_changelog(mlsver):

    for issue in laptop_repo.get_issues(milestone=laptop_milestone[mlsver],
                                        sort="created", direction="asc",
                                        state="closed"):
        if "pull" not in issue.html_url:
            original_issue_title = issue.title
            issue_title = original_issue_title
            if original_issue_title[0].islower():
                lower = original_issue_title[0]
                upper = original_issue_title[0].upper()
                issue_title = original_issue_title.replace(lower, upper, 1)

            labels = issue.get_labels()
            label_names = []

            for label in labels:
                label_names.append(label.name)
            if "crash" in label_names and "crash/webview" in label_names:
                crash_line = " - " +\
                    issue_title + ".(#" + str(issue.number) + ")"
                crash_list.append(crash_line)
            if "crash" not in label_names\
                    and "crash/webview" not in label_names\
                    and "webcompat" not in label_names\
                    and "audio" not in label_names\
                    and "feature/video" not in label_names\
                    and "regression" not in label_names\
                    and "privacy/connect" not in label_names\
                    and "privacy" not in label_names\
                    and "privacy/feature" not in label_names\
                    and "feature/sync" not in label_names\
                    and "feature/tor/guest-semantics" not in label_names\
                    and "feature/tor" not in label_names\
                    and "feature/shields" not in label_names\
                    and "feature/tor/leakproofing" not in label_names\
                    and "feature/shields/panel" not in label_names\
                    and "feature/private-browsing" not in label_names\
                    and "feature/rewards" not in label_names\
                    and "privacy/tracking" not in label_names\
                    and "feature/shields/!scripts" not in label_names\
                    and "feature/shields/adblock" not in label_names\
                    and "feature/shields/webcompat" not in label_names\
                    and "feature/shields/fingerprint" not in label_names:
                general_line = " - " +\
                    issue_title + ".(#" + str(issue.number) + ")"
                general_list.append(general_line)
            if "feature/tor/guest-semantics" in label_names\
                    or "feature/tor/leakproofing" in label_names\
                    or "feature/tor" in label_names\
                    or "feature/private-browsing" in label_names\
                    or "privacy/connect" in label_names\
                    or "privacy" in label_names\
                    or "privacy/feature" in label_names\
                    or "privacy/tracking" in label_names:
                privacy_line = " - " +\
                    issue_title + ".(#" + str(issue.number) + ")"
                privacy_list.append(privacy_line)
            if "feature/rewards" in label_names:
                rewards_line = " - " +\
                    issue_title + ".(#" + str(issue.number) + ")"
                rewards_list.append(rewards_line)
            if "feature/shields" in label_names\
                    or "feature/shields/!scripts" in label_names\
                    or "feature/shields/adblock" in label_names\
                    or "feature/shields/webcompat" in label_names\
                    or "feature/shields/fingerprint" in label_names\
                    or "feature/shields/panel" in label_names:
                shields_line = " - " +\
                    issue_title + ".(#" + str(issue.number) + ")"
                shields_list.append(shields_line)
            if "feature/sync" in label_names:
                sync_line = " - " +\
                    issue_title + ".(#" + str(issue.number) + ")"
                sync_list.append(sync_line)
            if "regression" in label_names:
                regression_line = " - " +\
                    issue_title + ".(#" + str(issue.number) + ")"
                regression_list.append(regression_line)
            if "webcompat" in label_names\
                    or "audio" in label_names\
                    or "feature/video" in label_names:
                webcompat_line = " - " +\
                    issue_title + ".(#" + str(issue.number) + ")"
                webcompat_list.append(webcompat_line)

    if rewards_list:
        print("## Brave Rewards")
        for line in sorted(rewards_list):
            print(line)
        print("")

    if crash_list:
        print("## Crash Fixes")
        for line in sorted(crash_list):
            print(line)
        print("")

    if privacy_list:
        print("## Private Windows/Tor Windows")
        for line in sorted(privacy_list):
            print(line)
        print("")

    if shields_list:
        print("## Shields ")
        for line in sorted(shields_list):
            print(line)
        print("")

    if sync_list:
        print("## Sync")
        for line in sorted(sync_list):
            print(line)
        print("")

    if regression_list:
        print("## Regression fixes")
        for line in sorted(regression_list):
            print(line)
        print("")

    if webcompat_list:
        print("## Webcompat fixes")
        for line in sorted(webcompat_list):
            print(line)
        print("")

    if general_list:
        print("## Other fixes")
        for line in sorted(general_list):
            print(line)
        print("")

    return


def ios_changelog():

    ios_key = sorted(ios_milestone.keys())[0]
    for issue in ios_repo.get_issues(milestone=ios_milestone[ios_key],
                                     sort="created", direction="asc",
                                     state="closed"):
        if 'pull' not in issue.html_url:
            original_issue_title = issue.title
            issue_title = original_issue_title
            if original_issue_title[0].islower():
                lower = original_issue_title[0]
                upper = original_issue_title[0].upper()
                issue_title = original_issue_title.replace(lower, upper, 1)

            labels = issue.get_labels()
            label_names = []

            for label in labels:
                label_names.append(label.name)
            if "crash" in label_names and "tests" not in label_names:
                crash_line = " - " +\
                    issue_title + ".(#" + str(issue.number) + ")"
                crash_list.append(crash_line)
            if "crash" not in label_names and "webcompat" not in label_names\
                    and "regression" not in label_names\
                    and "feature/private-tabs" not in label_names\
                    and "feature/sync" not in label_names\
                    and "feature/rewards" not in label_names\
                    and "feature/shields" not in label_names\
                    and "tests" not in label_names:
                general_line = " - " +\
                    issue_title + ".(#" + str(issue.number) + ")"
                general_list.append(general_line)
            if "regression" in label_names and "tests" not in label_names:
                regression_line = " - " +\
                    issue_title + ".(#" + str(issue.number) + ")"
                regression_list.append(regression_line)
            if "feature/shields" in label_names and "tests" not in label_names:
                shields_line = " - " +\
                    issue_title + ".(#" + str(issue.number) + ")"
                shields_list.append(shields_line)
            if "iPad" in label_names or "iPad Specific" in label_names:
                iPad_line = " - " +\
                    issue_title + ".(#" + str(issue.number) + ")"
                iPad_list.append(iPad_line)
            if "iPhone" in label_names\
                    or "iPhone X Specific" in label_names\
                    or "iPhone Specific" in label_names\
                    and "tests" not in label_names:
                iPhone_line = " - " +\
                    issue_title + ".(#" + str(issue.number) + ")"
                iPhone_list.append(iPhone_line)
            if "webcompat" in label_names\
                    or "audio" in label_names\
                    or "feature/video" in label_names\
                    and "tests" not in label_names:
                webcompat_line = " - " +\
                    issue_title + ".(#" + str(issue.number) + ")"
                webcompat_list.append(webcompat_line)
            if "feature/sync" in label_names:
                sync_line = " - " +\
                    issue_title + ".(#" + str(issue.number) + ")"
                sync_list.append(sync_line)

    if iPad_list:
        print("## iPad Specific Fixes")
        for line in sorted(iPad_list):
            print(line)
        print("")

    if iPhone_list:
        print("## iPhone Specific Fixes")
        for line in sorted(iPhone_list):
            print(line)
        print("")

    if crash_list:
        print("## Crash Fixes")
        for line in sorted(crash_list):
            print(line)
        print("")

    if shields_list:
        print("## Shields Fixes")
        for line in sorted(shields_list):
            print(line)
        print("")

    if sync_list:
        print("## Sync")
        for line in sorted(sync_list):
            print(line)
        print("")

    if regression_list:
        print("## Regression fixes")
        for line in sorted(regression_list):
            print(line)
        print("")

    if webcompat_list:
        print("## Webcompat fixes")
        for line in sorted(webcompat_list):
            print(line)
        print("")

    if general_list:
        print("## Other Fixes")
        for line in sorted(general_list):
            print(line)
        print("")

    return


def android_changelog():

    andrky = sorted(android_milestone.keys())[0]
    for issue in android_repo.get_issues(
                                         milestone=android_milestone[andrky],
                                         sort="created", direction="asc",
                                         state="closed"):
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
            if "crash" in label_names and "tests" not in label_names:
                crash_line = " - " +\
                    issue_title + ".(#" + str(issue.number) + ")"
                crash_list.append(crash_line)
            if "crash" not in label_names and "webcompat" not in label_names\
                    and "regression" not in label_names\
                    and "feature/private-tabs" not in label_names\
                    and "feature/sync" not in label_names\
                    and "feature/rewards" not in label_names\
                    and "feature/shields" not in label_names\
                    and "tests" not in label_names:
                general_line = " - " + issue_title +\
                    ".(#" + str(issue.number) + ")"
                general_list.append(general_line)
            if "regression" in label_names and "tests" not in label_names:
                regression_line = " - " +\
                    issue_title + ".(#" + str(issue.number) + ")"
                regression_list.append(regression_line)
            if "feature/shields" in label_names and "tests" not in label_names:
                shields_line = " - " +\
                    issue_title + ".(#" + str(issue.number) + ")"
                shields_list.append(shields_line)

    if crash_list:
        print("## Crash Fixes")
        for line in sorted(crash_list):
            print(line)
        print("")

    if shields_list:
        print("## Shields Fixes")
        for line in sorted(shields_list):
            print(line)

    if sync_list:
        print("## Sync")
        for line in sorted(sync_list):
            print(line)
        print("")
        print("")

    if regression_list:
        print("## Regression fixes")
        for line in sorted(regression_list):
            print(line)
        print("")

    return


print("*********************************************************************\
      ********************************")
print("								Changelog Generator														")
print("*********************************************************************\
      ********************************")

header = print("Generate changelog for:\n")
laptop = print("1. Laptop Release")
ios = print("2. iOS")
android = print("3. Android\n")

select_checklist = input("Choose the platform for which you want to generate\
                         the changelog: ")

if select_checklist == "1":
    print("\nSelect the milestone to generate changelog \n")

    length = 0
    while length < len(laptop_key):
        print(str(length+1) + ". " + sorted(laptop_milestone.keys())[length])
        length += 1

    generate_test = input("\nGenerate changelog for: ")

    if select_checklist == "1" and generate_test == "1":
        print("\nGenerating changelog for "
              + str(sorted(laptop_milestone.keys())[0]))
        laptop_changelog(key1)
    elif select_checklist == "1" and generate_test == "2":
        print("\nGenerating changelog for "
              + str(sorted(laptop_milestone.keys())[1]))
        laptop_changelog(key2)
    elif select_checklist == "1" and generate_test == "3":
        print("\nGenerating changelog for "
              + str(sorted(laptop_milestone.keys())[2]))
        laptop_changelog(key3)
    elif select_checklist == "1" and generate_test == "4":
        print("\nGenerating changelog for "
              + str(sorted(laptop_milestone.keys())[3]))
        laptop_changelog(key4)
    elif select_checklist == "1" and generate_test == "5":
        print("\nGenerating changelog for "
              + str(sorted(laptop_milestone.keys())[4]))
        laptop_changelog(key5)
    else:
        print("Nothing to create in this milestone. Run the script again.")
        exit()

elif select_checklist == "2":
    generate_ios_test = print("Generating changelog for iOS Release",
                              sorted(ios_milestone.keys())[0])
    ios_changelog()
elif select_checklist == "3":
    generate_android_test = print("Generating changelog for Android Release",
                                  sorted(android_milestone.keys())[0])
    android_changelog()
else:
    print("Incorrect selection. Exiting test creation...")
    exit()
