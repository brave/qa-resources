from github import Github
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t",  "--test",
                    help="Test Mode, do not create Github issues")

args = parser.parse_args()

secret_file = open("github.secret", "r")
token_string = secret_file.readline().rstrip("\n\r")

g = Github(token_string, timeout=1000)
rate = g.get_rate_limit()
limit = rate.core.limit
remaining = rate.core.remaining

print("Rate Limit: " + str(limit))
print("Rate Remaining: " + str(remaining))

bc_repo = g.get_organization("brave").get_repo("brave-browser")
ios_repo = g.get_organization("brave").get_repo("brave-ios")

checklist = []
release_notes = []
mac_checklist = []
macarm64_checklist = []
win32_checklist = []
win64_checklist = []
linux_checklist = []
iPad_checklist = []
iPhone_checklist = []
iPhoneX_checklist = []
android_arm_checklist = []
android_tab_checklist = []
crypto_wallet_checklist = []

bc_milestone = {}
for bcmilestone in bc_repo.get_milestones(state="open"):
    bc_milestone.update({bcmilestone.title: bcmilestone})

ios_milestone = {}
for iosmilestone in ios_repo.get_milestones(state="open"):
    ios_milestone.update({iosmilestone.title: iosmilestone})

laptop_key = sorted(bc_milestone.keys())
ios_key = sorted(ios_milestone.keys())

def laptop_testruns(milestonever):

    wiki_laptop_file = open("wikitemplate.md", "r")
    laptop_template = wiki_laptop_file.read()
    wiki_macOS_arm = open("wikitemplate-macOS-arm64.md", "r")
    macOS_arm64 = wiki_macOS_arm.read()

    for issue in bc_repo.get_issues(
        milestone=bc_milestone[milestonever], sort="created",
            direction="asc", state="closed"):
        if("pull" not in issue.html_url):
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
            if("release-notes/include" in label_names and
                    "QA/No" not in label_names and
                    "tests" not in label_names):
                output_line = " - " + issue_title + ".([#" +\
                    str(issue.number) + "](" + issue.html_url + "))"
                release_notes.append(output_line)

            if("QA/Yes" in label_names and "QA/No" not in label_names and
                    "tests" not in label_names):
                output_line = " - [ ] " + issue_title + ".([#" +\
                        str(issue.number) + "](" + issue.html_url + "))"
                checklist.append(output_line)
                if("QA Pass-macOS" not in label_names and
                        "OS/Windows" not in label_names and
                        "OS/Linux" not in label_names and
                        "QA/No" not in label_names and
                        "tests" not in label_names):
                    mac_checklist.append(output_line)

                if("QA Pass-Win64" not in label_names and
                        "OS/macOS" not in label_names and
                        "OS/Linux" not in label_names and
                        "QA/No" not in label_names and
                        "tests" not in label_names):
                    win64_checklist.append(output_line)

                if("QA Pass-Linux" not in label_names and
                        "OS/Windows" not in label_names and
                        "OS/macOS" not in label_names and
                        "QA/No" not in label_names and
                        "tests" not in label_names):
                    linux_checklist.append(output_line)

    print("\nRelease Notes ")
    for line in release_notes:
        print(line)
    print("")

    print("\nChecklist: ")
    for line in checklist:
        print(line)
    print("")

    print("\nMac Checklist (Intel):")
    print(laptop_template)
    print("")
    macTitle = "Manual test run on macOS (Intel) for " + milestonever
    macList = ["OS/macOS",
               "release-notes/exclude",
               "tests",
               "QA/Yes",
               "OS/Desktop"]

    if args.test is None:
        bc_repo.create_issue(title=macTitle,
                                 body=laptop_template,
                                 milestone=bc_milestone[milestonever],
                                 labels=macList)

    print("--------------------------------------------------------\n")

    print("Mac Checklist (arm64):")
    print(macOS_arm64)
    print("")
    macarm64Title = "Manual test run on macOS (arm64) for " + milestonever
    macarm64List = ["OS/macOS-arm64",
               "release-notes/exclude",
               "tests",
               "QA/Yes",
               "OS/Desktop"]

    if args.test is None:
        bc_repo.create_issue(title=macarm64Title,
                                 body=macOS_arm64,
                                 milestone=bc_milestone[milestonever],
                                 labels=macarm64List)

    print("--------------------------------------------------------\n")

    print("Win64 Checklist:")
    print(laptop_template)
    print("")
    winTitle = "Manual test run on Windows x64 for " + milestonever
    winList = ["OS/Windows",
               "release-notes/exclude",
               "tests", 
               "QA/Yes",
               "OS/Desktop"]

    if args.test is None:
        bc_repo.create_issue(title=winTitle,
                                 body=laptop_template,
                                 milestone=bc_milestone[milestonever],
                                 labels=winList)

    print("--------------------------------------------------------\n")

    print("Linux Checklist:")
    print(laptop_template)
    print("")
    linTitle = "Manual test run on Linux for " + milestonever
    linList = ["OS/Linux",
               "release-notes/exclude",
               "tests",
               "QA/Yes",
               "OS/Desktop"]

    if args.test is None:
        bc_repo.create_issue(title=linTitle,
                                 body=laptop_template,
                                 milestone=bc_milestone[milestonever],
                                 labels=linList)

    return 0 

def laptop_hf_testruns(milestonever):

    wiki_laptop_hf = open("wikitemplate-ReducedDesktop.md", "r")
    laptop_hf_template = wiki_laptop_hf.read()
    wiki_macOS_arm = open("wikitemplate-macOS-arm64.md", "r")
    macOS_arm64 = wiki_macOS_arm.read()

    for issue in bc_repo.get_issues(
        milestone=bc_milestone[milestonever], sort="created",
            direction="asc", state="closed"):
        if("pull" not in issue.html_url):
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
            if("release-notes/include" in label_names and
                    "QA/No" not in label_names and
                    "tests" not in label_names):
                output_line = " - " + issue_title + ".([#" +\
                    str(issue.number) + "](" + issue.html_url + "))"
                release_notes.append(output_line)

            if("QA/Yes" in label_names and "QA/No" not in label_names and
                    "tests" not in label_names):
                output_line = " - [ ] " + issue_title + ".([#" +\
                        str(issue.number) + "](" + issue.html_url + "))"
                checklist.append(output_line)
                if("QA Pass-macOS" not in label_names and
                        "OS/Windows" not in label_names and
                        "OS/Linux" not in label_names and
                        "QA/No" not in label_names and
                        "tests" not in label_names):
                    mac_checklist.append(output_line)

                if("QA Pass-Win64" not in label_names and
                        "OS/macOS" not in label_names and
                        "OS/Linux" not in label_names and
                        "QA/No" not in label_names and
                        "tests" not in label_names):
                    win64_checklist.append(output_line)

                if("QA Pass-Linux" not in label_names and
                        "OS/Windows" not in label_names and
                        "OS/macOS" not in label_names and
                        "QA/No" not in label_names and
                        "tests" not in label_names):
                    linux_checklist.append(output_line)

    print("\nRelease Notes ")
    for line in release_notes:
        print(line)
    print("")

    print("\nMac Checklist (Intel):")
    print(laptop_hf_template)
    print("")
    macTitle = "Manual test run on macOS (Intel) for " + milestonever
    macList = ["OS/macOS",
               "release-notes/exclude",
               "tests",
               "QA/Yes",
               "OS/Desktop"]

    if args.test is None:
        bc_repo.create_issue(title=macTitle,
                                 body=laptop_hf_template,
                                 milestone=bc_milestone[milestonever],
                                 labels=macList)

    print("--------------------------------------------------------\n")

    print("Mac Checklist(arm64):")
    print(macOS_arm64)
    print("")
    macarm64Title = "Manual test run on macOS (arm64) for " + milestonever
    macarm64List = ["OS/macOS-arm64",
               "release-notes/exclude",
               "tests",
               "QA/Yes",
               "OS/Desktop"]

    if args.test is None:
        bc_repo.create_issue(title=macarm64Title,
                                 body=macOS_arm64,
                                 milestone=bc_milestone[milestonever],
                                 labels=macarm64List)

    print("--------------------------------------------------------\n")

    print("Win64 Checklist:")
    print(laptop_hf_template)
    print("")
    winTitle = "Manual test run on Windows x64 for " + milestonever
    winList = ["OS/Windows",
               "release-notes/exclude",
               "tests", 
               "QA/Yes",
               "OS/Desktop"]

    if args.test is None:
        bc_repo.create_issue(title=winTitle,
                                 body=laptop_hf_template,
                                 milestone=bc_milestone[milestonever],
                                 labels=winList)

    print("--------------------------------------------------------\n")

    print("Linux Checklist:")
    print(laptop_hf_template)
    print("")
    linTitle = "Manual test run on Linux for " + milestonever
    linList = ["OS/Linux",
               "release-notes/exclude",
               "tests",
               "QA/Yes",
               "OS/Desktop"]

    if args.test is None:
        bc_repo.create_issue(title=linTitle,
                                 body=laptop_hf_template,
                                 milestone=bc_milestone[milestonever],
                                 labels=linList)

    return 0

def laptop_CRminor_testruns(milestonever):

    wiki_laptop_CRminor = open("wikitemplate-minorCRbumpDesktop.md", "r")
    laptop_CRminor_template = wiki_laptop_CRminor.read()
    wiki_macOS_arm = open("wikitemplate-macOS-arm64.md", "r")
    macOS_arm64 = wiki_macOS_arm.read()

    for issue in bc_repo.get_issues(
        milestone=bc_milestone[milestonever], sort="created",
            direction="asc", state="closed"):
        if("pull" not in issue.html_url):
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
            if("release-notes/include" in label_names and
                    "QA/No" not in label_names and
                    "tests" not in label_names):
                output_line = " - " + issue_title + ".([#" +\
                    str(issue.number) + "](" + issue.html_url + "))"
                release_notes.append(output_line)

            if("QA/Yes" in label_names and "QA/No" not in label_names and
                    "tests" not in label_names):
                output_line = " - [ ] " + issue_title + ".([#" +\
                        str(issue.number) + "](" + issue.html_url + "))"
                checklist.append(output_line)
                if("QA Pass-macOS" not in label_names and
                        "OS/Windows" not in label_names and
                        "OS/Linux" not in label_names and
                        "QA/No" not in label_names and
                        "tests" not in label_names):
                    mac_checklist.append(output_line)

                if("QA Pass-Win64" not in label_names and
                        "OS/macOS" not in label_names and
                        "OS/Linux" not in label_names and
                        "QA/No" not in label_names and
                        "tests" not in label_names):
                    win64_checklist.append(output_line)

                if("QA Pass-Linux" not in label_names and
                        "OS/Windows" not in label_names and
                        "OS/macOS" not in label_names and
                        "QA/No" not in label_names and
                        "tests" not in label_names):
                    linux_checklist.append(output_line)

    print("\nRelease Notes ")
    for line in release_notes:
        print(line)
    print("")

    print("\nMac Checklist (Intel):")
    print(laptop_CRminor_template)
    print("")
    macTitle = "Manual test run on macOS (Intel) for " + milestonever
    macList = ["OS/macOS",
               "release-notes/exclude",
               "tests",
               "QA/Yes",
               "OS/Desktop"]

    if args.test is None:
        bc_repo.create_issue(title=macTitle,
                                 body=laptop_CRminor_template,
                                 milestone=bc_milestone[milestonever],
                                 labels=macList)

    print("--------------------------------------------------------\n")

    print("Mac Checklist(arm64):")
    print(macOS_arm64)
    print("")
    macarm64Title = "Manual test run on macOS (arm64) for " + milestonever
    macarm64List = ["OS/macOS-arm64",
               "release-notes/exclude",
               "tests",
               "QA/Yes",
               "OS/Desktop"]

    if args.test is None:
        bc_repo.create_issue(title=macarm64Title,
                                 body=macOS_arm64,
                                 milestone=bc_milestone[milestonever],
                                 labels=macarm64List)

    print("--------------------------------------------------------\n")

    print("Win64 Checklist:")
    print(laptop_CRminor_template)
    print("")
    winTitle = "Manual test run on Windows x64 for " + milestonever
    winList = ["OS/Windows",
               "release-notes/exclude",
               "tests", 
               "QA/Yes",
               "OS/Desktop"]

    if args.test is None:
        bc_repo.create_issue(title=winTitle,
                                 body=laptop_CRminor_template,
                                 milestone=bc_milestone[milestonever],
                                 labels=winList)

    print("--------------------------------------------------------\n")

    print("Linux Checklist:")
    print(laptop_CRminor_template)
    print("")
    linTitle = "Manual test run on Linux for " + milestonever
    linList = ["OS/Linux",
               "release-notes/exclude",
               "tests",
               "QA/Yes",
               "OS/Desktop"]

    if args.test is None:
        bc_repo.create_issue(title=linTitle,
                                 body=laptop_CRminor_template,
                                 milestone=bc_milestone[milestonever],
                                 labels=linList)

    return 0

def android_testruns(milestonever):

    wiki_android_file = open("wikitemplate-android.md", "r")
    android_template = wiki_android_file.read()

    for issue in bc_repo.get_issues(
            milestone=bc_milestone[milestonever],
            sort="created",
            direction="asc",
            state="closed"):
        if("pull" not in issue.html_url):
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
            if("QA/Yes" in label_names and 
                    "OS/Android" in label_names and
                    "tests" not in label_names and
                    "QA/No" not in label_names):
                output_line = " - " + issue_title + ".([#" +\
                    str(issue.number) + "])" + issue.html_url + "))"
                release_notes.append(output_line)

            if("QA/Yes" in label_names and "QA/No" not in label_names):
                output_line = " - [ ] " + issue_title + ". ([#" +\
                    str(issue.number) + "](" + issue.html_url + "))"
                checklist.append(output_line)
                checklist.append(issue.html_url)
                if("QA Pass - Android ARM" not in label_names and
                        "checked by qa" not in label_names and
                        "tests" not in label_names and
                        "x86" not in label_names and
                        "tablet-specific" not in label_names):
                    android_arm_checklist.append(output_line)


                if("QA Pass - Android Tab" not in label_names and
                        "checked by qa" not in label_names and
                        "tests" not in label_names and
                        "x86" not in label_names and
                        "phone-specific" not in label_names):
                    android_tab_checklist.append(output_line)

    print("\nRelease Notes:")
    for line in release_notes:
        print(line)
    print("")

    print("\nChecklist:")
    for line in checklist:
        print(line)
    print("")

    print("\nAndroid ARM Checklist:")
    print(android_template)
    print("")
    AndroidARMtitle = "Manual test run on Android ARM  for " + milestonever
    AndroidARMlist = ["ARM",
                      "release-notes/exclude",
                      "tests",
                      "QA/Yes",
                      "OS/Android"]

    if args.test is None:
        bc_repo.create_issue(title=AndroidARMtitle,
                                  body=android_template,
                                  milestone=bc_milestone[milestonever],
                                  labels=AndroidARMlist)

    print("--------------------------------------------------------\n")

    print("Android Tab Checklist:")
    print(android_template)
    print("")
    AndroidTabtitle = "Manual test run on Android Tab  for " + milestonever
    AndroidTablist = ["ARM",
                      "release-notes/exclude",
                      "tests",
                      "QA/Yes",
                      "OS/Android"]

    if args.test is None:
        bc_repo.create_issue(title=AndroidTabtitle,
                                  body=android_template,
                                  milestone=bc_milestone[milestonever],
                                  labels=AndroidTablist)

    print("--------------------------------------------------------\n")

    return 0

def android_hf_testruns(milestonever):

    wiki_android_hf = open("wikitemplate-ReducedAndroid.md", "r")
    android_hf_template = wiki_android_hf.read()

    for issue in bc_repo.get_issues(
            milestone=bc_milestone[milestonever],
            sort="created",
            direction="asc",
            state="closed"):
        if("pull" not in issue.html_url):
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
            if("QA/Yes" in label_names and 
                    "OS/Android" in label_names and
                    "tests" not in label_names and
                    "QA/No" not in label_names):
                output_line = " - " + issue_title + ".([#" +\
                    str(issue.number) + "])" + issue.html_url + "))"
                release_notes.append(output_line)

            if("QA/Yes" in label_names and "QA/No" not in label_names):
                output_line = " - [ ] " + issue_title + ". ([#" +\
                    str(issue.number) + "](" + issue.html_url + "))"
                checklist.append(output_line)
                checklist.append(issue.html_url)
                if("QA Pass - Android ARM" not in label_names and
                        "checked by qa" not in label_names and
                        "tests" not in label_names and
                        "x86" not in label_names and
                        "tablet-specific" not in label_names):
                    android_arm_checklist.append(output_line)

                if("QA Pass - Android Tab" not in label_names and
                        "checked by qa" not in label_names and
                        "tests" not in label_names and
                        "x86" not in label_names and
                        "phone-specific" not in label_names):
                    android_tab_checklist.append(output_line)

    print("\nRelease Notes:")
    for line in release_notes:
        print(line)
    print("")

    print("\nChecklist:")
    for line in checklist:
        print(line)
    print("")

    print("\nAndroid ARM Checklist:")
    print(android_hf_template)
    print("")
    AndroidARMtitle = "Manual test run on Android ARM  for " + milestonever
    AndroidARMlist = ["ARM",
                      "release-notes/exclude",
                      "tests",
                      "QA/Yes",
                      "OS/Android"]

    if args.test is None:
        bc_repo.create_issue(title=AndroidARMtitle,
                                  body=android_hf_template,
                                  milestone=bc_milestone[milestonever],
                                  labels=AndroidARMlist)

    print("--------------------------------------------------------\n")

    print("Android Tab Checklist:")
    print(android_hf_template)
    print("")
    AndroidTabtitle = "Manual test run on Android Tab  for " + milestonever
    AndroidTablist = ["ARM",
                      "release-notes/exclude",
                      "tests",
                      "QA/Yes",
                      "OS/Android"]

    if args.test is None:
        bc_repo.create_issue(title=AndroidTabtitle,
                                  body=android_hf_template,
                                  milestone=bc_milestone[milestonever],
                                  labels=AndroidTablist)


    print("--------------------------------------------------------\n")

    return 0

def android_CRminor_testruns(milestonever):

    wiki_android_CRminor = open("wikitemplate-minorCRbumpAndroid.md", "r")
    android_CRminor_template = wiki_android_CRminor.read()

    for issue in bc_repo.get_issues(
            milestone=bc_milestone[milestonever],
            sort="created",
            direction="asc",
            state="closed"):
        if("pull" not in issue.html_url):
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
            if("QA/Yes" in label_names and 
                    "OS/Android" in label_names and
                    "tests" not in label_names and
                    "QA/No" not in label_names):
                output_line = " - " + issue_title + ".([#" +\
                    str(issue.number) + "])" + issue.html_url + "))"
                release_notes.append(output_line)

            if("QA/Yes" in label_names and "QA/No" not in label_names):
                output_line = " - [ ] " + issue_title + ". ([#" +\
                    str(issue.number) + "](" + issue.html_url + "))"
                checklist.append(output_line)
                checklist.append(issue.html_url)
                if("QA Pass - Android ARM" not in label_names and
                        "checked by qa" not in label_names and
                        "tests" not in label_names and
                        "x86" not in label_names and
                        "tablet-specific" not in label_names):
                    android_arm_checklist.append(output_line)

                if("QA Pass - Android Tab" not in label_names and
                        "checked by qa" not in label_names and
                        "tests" not in label_names and
                        "x86" not in label_names and
                        "phone-specific" not in label_names):
                    android_tab_checklist.append(output_line)

    print("\nRelease Notes:")
    for line in release_notes:
        print(line)
    print("")

    print("\nChecklist:")
    for line in checklist:
        print(line)
    print("")

    print("\nAndroid ARM Checklist:")
    print(android_CRminor_template)
    print("")
    AndroidARMtitle = "Manual test run on Android ARM for " + milestonever
    AndroidARMlist = ["ARM",
                      "release-notes/exclude",
                      "tests",
                      "QA/Yes",
                      "OS/Android"]

    if args.test is None:
        bc_repo.create_issue(title=AndroidARMtitle,
                                  body=android_CRminor_template,
                                  milestone=bc_milestone[milestonever],
                                  labels=AndroidARMlist)

    print("--------------------------------------------------------\n")

    print("Android Tab Checklist:")
    print(android_CRminor_template)
    print("")
    AndroidTabtitle = "Manual test run on Android Tab for " + milestonever
    AndroidTablist = ["ARM",
                      "release-notes/exclude",
                      "tests",
                      "QA/Yes",
                      "OS/Android"]

    if args.test is None:
        bc_repo.create_issue(title=AndroidTabtitle,
                                  body=android_CRminor_template,
                                  milestone=bc_milestone[milestonever],
                                  labels=AndroidTablist)


    print("--------------------------------------------------------\n")

    return 0

def iOS_testruns():

    wikitemplate_ios = open("wikitemplate-ios.md", "r")
    ios_template = wikitemplate_ios.read()
    ios_key = sorted(ios_milestone.keys())[0]


    for issue in ios_repo.get_issues(milestone=ios_milestone[ios_key],
                                     sort="created",
                                     direction="asc",
                                     state="closed"):
       
        if("pull" not in issue.html_url):
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
        if("release-notes/include" in label_names and 
                           "QA/No" in label_names and
                           "tests" not in label_names):
            output_line = " - " + issue_title + ". ([#" +\
                            str(issue.number) + "](" + issue.html_url + "))"
            release_notes.append(output_line)            
            release_notes.append(issue.html_url)
        #print(release_notes)

        if("QA/Yes" in label_names and "QA/No" not in label_names):
            output_line = " - [ ] " + issue_title + ". ([#" +\
                str(issue.number) + "](" + issue.html_url + "))"
            checklist.append(output_line)
            checklist.append(issue.html_url)
            if("QA Pass - iPad" not in label_names and
                    "iPhone" not in label_names and
                    "tests" not in label_names):
                iPad_checklist.append(output_line)

            if("QA Pass - iPhone" not in label_names and
                    "iPad" not in label_names and
                    "tests" not in label_names):
                iPhone_checklist.append(output_line)

            if("QA Pass - iPhone X" not in label_names and
                    "iPad" not in label_names and
                    "tests" not in label_names):
                iPhoneX_checklist.append(output_line)

    print("\nRelease Notes:")
    print(release_notes)
    for line in release_notes:
        relline += line +"\n"
        print(relline)
    print("")

    print("\niPad Checklist:")
    print(ios_template)
    print("")
    iPad_Title = "Manual test run for " + ios_key +\
        " on iPad"
    iPad_List = ["ipad",
                 "release-notes/exclude",
                 "tests",
                 "QA/Yes"]

    if args.test is None:
        ios_repo.create_issue(title=iPad_Title,
                              body=ios_template,
                              milestone=ios_milestone[ios_key],
                              labels=iPad_List)

    print("--------------------------------------------------------\n")

    print("iPhone Checklist:")
    print(ios_template)
    print("")
    iPhone_Title = "Manual test run for " + ios_key +\
        " on iPhone"
    iPhone_List = ["iPhone",
                   "release-notes/exclude",
                   "tests",
                   "QA/Yes"]

    if args.test is None:
        ios_repo.create_issue(title=iPhone_Title,
                              body=ios_template,
                              milestone=ios_milestone[ios_key],
                              labels=iPhone_List)

    print("--------------------------------------------------------\n")

    print("iPhone X Checklist:")
    print(ios_template)
    print("")
    iPhoneX_Title = "Manual test run for " + ios_key +\
        " on iPhone X"
    iPhoneX_List = ["iPhone",
                    "release-notes/exclude",
                    "tests",
                    "QA/Yes"]

    if args.test is None:
        ios_repo.create_issue(title=iPhoneX_Title,
                              body=ios_template,
                              milestone=ios_milestone[ios_key],
                              labels=iPhoneX_List)

    return 

def tor_testruns(tor_rel):


    macOS_intel_wiki = open("wikitemplate-tor-macOS(Intel).md", "r")
    macOS_intel_template = macOS_intel_wiki.read()
    macOS_arm64_wiki = open("wikitemplate-tor-macOS(arm64).md", "r")
    macOS_arm64_template = macOS_arm64_wiki.read()
    win_tor_wiki = open("wikitemplate-tor-Windows.md", "r")
    windows_template = win_tor_wiki.read()
    linux_tor_wiki = open("wikitemplate-tor-Linux.md", "r")
    linux_template = linux_tor_wiki.read()

    print("\nMac Checklist (Intel):")
    print(macOS_intel_template)
    print("")
    macTitle = "Manual test run on macOS (Intel) for " + tor_rel
    macList = ["OS/macOS",
               "release-notes/exclude",
               "tests",
               "QA/Yes",
               "OS/Desktop",
               "feature/tor"]

    if args.test is None:
        bc_repo.create_issue(title=macTitle,
                                 body=macOS_intel_template,
                                 milestone=bc_milestone[tor_rel],
                                 labels=macList)

    print("--------------------------------------------------------\n")

    print("Mac Checklist(arm64):")
    print(macOS_arm64_template)
    print("")
    macarm64Title = "Manual test run on macOS (arm64) for " + tor_rel
    macarm64List = ["OS/macOS-arm64",
               "release-notes/exclude",
               "tests",
               "QA/Yes",
               "OS/Desktop",
               "feature/tor"]

    if args.test is None:
        bc_repo.create_issue(title=macarm64Title,
                                 body=macOS_arm64_template,
                                 milestone=bc_milestone[tor_rel],
                                 labels=macarm64List)

    print("--------------------------------------------------------\n")

    print("Win64 Checklist:")
    print(windows_template)
    print("")
    winTitle = "Manual test run on Windows x64 & x86 for " + tor_rel
    winList = ["OS/Windows",
               "release-notes/exclude",
               "tests", 
               "QA/Yes",
               "OS/Desktop",
               "feature/tor"]

    if args.test is None:
        bc_repo.create_issue(title=winTitle,
                                 body=windows_template,
                                 milestone=bc_milestone[tor_rel],
                                 labels=winList)

    print("--------------------------------------------------------\n")

    print("Linux Checklist:")
    print(linux_template)
    print("")
    linTitle = "Manual test run on Linux for " + tor_rel
    linList = ["OS/Linux",
               "release-notes/exclude",
               "tests",
               "QA/Yes",
               "OS/Desktop",
               "feature/tor"]

    if args.test is None:
        bc_repo.create_issue(title=linTitle,
                                 body=linux_template,
                                 milestone=bc_milestone[tor_rel],
                                 labels=linList)

    return 0

def ipfs_testruns(ipfs_rel):

    ipfs_wiki = open("wikitemplate-IPFS.md", "r")
    ipfs_template = ipfs_wiki.read()

    print("\nMac Checklist (Intel/arm64):")
    print(ipfs_template)
    print("")
    macTitle = "Manual test run on macOS (Intel/arm64) for " + ipfs_rel
    macList = ["OS/macOS",
               "release-notes/exclude",
               "tests",
               "QA/Yes",
               "OS/Desktop",
               "feature/ipfs"]

    if args.test is None:
        bc_repo.create_issue(title=macTitle,
                                 body=ipfs_template,
                                 milestone=bc_milestone[ipfs_rel],
                                 labels=macList)

    print("--------------------------------------------------------\n")

    print("Win64 Checklist:")
    print(ipfs_template)
    print("")
    winTitle = "Manual test run on Windows x64 & x86 for " + ipfs_rel
    winList = ["OS/Windows",
               "release-notes/exclude",
               "tests", 
               "QA/Yes",
               "OS/Desktop",
               "feature/ipfs"]

    if args.test is None:
        bc_repo.create_issue(title=winTitle,
                                 body=ipfs_template,
                                 milestone=bc_milestone[ipfs_rel],
                                 labels=winList)

    print("--------------------------------------------------------\n")

    print("Linux Checklist:")
    print(ipfs_template)
    print("")
    linTitle = "Manual test run on Linux for " + ipfs_rel
    linList = ["OS/Linux",
               "release-notes/exclude",
               "tests",
               "QA/Yes",
               "OS/Desktop",
               "feature/ipfs"]

    if args.test is None:
        bc_repo.create_issue(title=linTitle,
                                 body=ipfs_template,
                                 milestone=bc_milestone[ipfs_rel],
                                 labels=linList)

    return 0

print("\n#######################################################################"
      "###################################################")
print("\n For Desktop or Android minor CR bump only use the basic checks selection to "
      "generate testruns\n")

length = 0
print("Current open milestones for Desktop/Android")
while length < len(laptop_key):
    print(str(length+1) + ". " + sorted(bc_milestone.keys())[length])
    length += 1

ioslength=0
print("\nCurrent open milestones for iOS")
while ioslength < len(ios_key):
    print(str(ioslength+1) + ". " + sorted(ios_milestone.keys())[ioslength])
    ioslength += 1

print("\nNOTE:")
print("\n For Tor Release make sure you type \"Tor\" or \"tor\" instead "
      "of the number")
print("\n For IPFS Release make sure you type \"IPFS\" or \"ipfs\" instead "
      "of the number")

print("#######################################################################"
      "###################################################")

header = print("\nCreate test runs for:\n")
laptop = print("1. Desktop Release (Full manual pass)")
laptop_hf = print("2. Desktop Release (Reduced manual pass for" 
                  " Hotfix)")
laptop_CRminor = print("3. Desktop Release (Basic checks for" 
                  " minor Chromium bump)")
android = print("4. Android Release (Full manual pass)")
android_hf = print("5. Android Release (Reduced manual pass for" 
                  " Hotfix)")
android_hf = print("6. Android Release (Basic checks for" 
                  " minor Chromium bump)")
ios = print("7. iOS Release")
tor = print("8. Tor Release")
ipfs = print("9. IPFS Release")

select_checklist = input("\nChoose the platform for which you want to" +
                         " generate the test run: ")

if(select_checklist == "1"):
    print("\nGenerating test runs for " +
          str(sorted(bc_milestone.keys())[0]))
    laptop_testruns(sorted(bc_milestone.keys())[0])
elif(select_checklist == "2"):
    print("\nGenerating test runs for " +
          str(sorted(bc_milestone.keys())[0]))
    laptop_hf_testruns(sorted(bc_milestone.keys())[0])
elif(select_checklist == "3"):
    print("\nGenerating test runs for " +
          str(sorted(bc_milestone.keys())[0]))
    laptop_CRminor_testruns(sorted(bc_milestone.keys())[0])
elif(select_checklist == "4"):
    print("\nGenerating test runs for " +
          str(sorted(bc_milestone.keys())[0]))
    android_testruns(sorted(bc_milestone.keys())[0])
elif(select_checklist == "5"):
    print("\nGenerating test runs for " +
          str(sorted(bc_milestone.keys())[0]))
    android_hf_testruns(sorted(bc_milestone.keys())[0])
elif(select_checklist == "6"):
    print("\nGenerating test runs for " +
          str(sorted(bc_milestone.keys())[0]))
    android_CRminor_testruns(sorted(bc_milestone.keys())[0])
elif (select_checklist == "7"):
    generate_ios_test = print("\nGenerating test runs for iOS ",
                              sorted(ios_milestone.keys())[0])
    iOS_testruns()
elif (select_checklist == "Tor" or select_checklist == "tor"):
    tormilestone = [s for s in bc_milestone if "Tor" in s]
    if (len(tormilestone) == 0):
        torkey = ""
        print("No Tor milestone exists. Please create milestone "
              "and then generate test runs")
    else:
        torkey = tormilestone[0]
        generate_ios_test = print("\nGenerating test runs for Tor",
                              (tormilestone)[0])
        tor_testruns(torkey)
elif (select_checklist == "IPFS" or select_checklist == "ipfs"):
    ipfsmilestone = [i for i in bc_milestone if "IPFS" in i]
    if (len(ipfsmilestone) == 0):
        ipfskey = ""
        print("No IPFS milestone exists. Please create milestone "
              "and then generate test runs")
    else:
        ipfskey = ipfsmilestone[0]
        generate_ipfs_test = print("\nGenerating test runs for",
                                (ipfsmilestone)[0])
        ipfs_testruns(ipfskey)
else:
    print("Incorrect selection. " + select_checklist + " is not a valid input\n")
    exit()
