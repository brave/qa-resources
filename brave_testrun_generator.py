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

laptop_repo = g.get_organization("brave").get_repo("brave-browser")
ios_repo = g.get_organization("brave").get_repo("brave-ios")
android_repo = g.get_organization("brave").get_repo("browser-android-tabs")

checklist = []
release_notes = []
mac_checklist = []
win32_checklist = []
win64_checklist = []
linux_checklist = []
iPad_checklist = []
iPhone_checklist = []
iPhoneX_checklist = []
android_x86_checklist = []
android_arm_checklist = []
android_tab_checklist = []
crypto_wallet_checklist = []

laptop_milestone = {}
for laptopmilestone in laptop_repo.get_milestones(state="open"):
    laptop_milestone.update({laptopmilestone.title: laptopmilestone})

ios_milestone = {}
for iosmilestone in ios_repo.get_milestones(state="open"):
    ios_milestone.update({iosmilestone.title: iosmilestone})

wiki_laptop_file = open("wikitemplate.md", "r")
laptop_template = wiki_laptop_file.read()
wiki_laptop_hf = open("wikitemplate-hotfix.md", "r")
laptop_hf_template = wiki_laptop_hf.read()

laptop_key = sorted(laptop_milestone.keys())
key1 = sorted(laptop_milestone.keys())[0]
key2 = sorted(laptop_milestone.keys())[1]
key3 = sorted(laptop_milestone.keys())[2]
key4 = sorted(laptop_milestone.keys())[3]

ethmilestone = [s for s in laptop_milestone if "Ethereum" in s]
if (len(ethmilestone) == 0):
    ethkey = ""
else:
    ethkey = ethmilestone[0]

androidmilestone = [s for s in laptop_milestone if "Android" in s]
if (len(androidmilestone) == 0):
    androidkey = ""
else:
    androidkey = androidmilestone[0]

def laptop_testruns(milestonever):

    for issue in laptop_repo.get_issues(
        milestone=laptop_milestone[milestonever], sort="created",
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
    macList = ["OS/macOS", "release-notes/exclude", "tests", "QA/Yes"]

    if args.test is None:
        laptop_repo.create_issue(title=macTitle,
                                 body=bigline,
                                 assignees=["LaurenWags", "kjozwiak"],
                                 milestone=laptop_milestone[milestonever],
                                 labels=macList)

    print("Win64 Checklist:")
    bigline = "## Per release specialty tests\n"
    for line in win64_checklist:
        bigline += line + "\n"
    bigline = bigline + laptop_template
    print(bigline)
    print("")
    winTitle = "Manual test run on Windows x64 for " + milestonever
    winList = ["OS/Windows", "release-notes/exclude", "tests", "QA/Yes"]

    if args.test is None:
        laptop_repo.create_issue(title=winTitle,
                                 body=bigline,
                                 assignees=["btlechowski", "GeetaSarvadnya"],
                                 milestone=laptop_milestone[milestonever],
                                 labels=winList)

    print("Linux Checklist:")
    bigline = "## Per release specialty tests\n"
    for line in linux_checklist:
        bigline += line + "\n"
    bigline = bigline + laptop_template
    print(bigline)
    print("")
    linTitle = "Manual test run on Linux for " + milestonever
    linList = ["OS/unix-like/linux",
               "release-notes/exclude",
               "tests",
               "QA/Yes"]

    if args.test is None:
        laptop_repo.create_issue(title=linTitle,
                                 body=bigline,
                                 assignee="srirambv",
                                 milestone=laptop_milestone[milestonever],
                                 labels=linList)

    return 0


def laptop_perrel_checklist(milestonever):

    for issue in laptop_repo.get_issues(
            milestone=laptop_milestone[milestonever],
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
            if("release-notes/include" in label_names or
                    "release-notes/exclude" in label_names and
                    "tests" not in label_names):
                output_line = " - " + issue_title + ".([#" +\
                    str(issue.number) + "](" + issue.html_url + "))"

            if("QA/Yes" in label_names and
                    "QA/No" not in label_names and
                    "tests" not in label_names):
                output_line = " - [ ] " + issue_title + ".([#" +\
                    str(issue.number) + "](" + issue.html_url + "))"

                if("QA/checked-macOS" not in label_names and
                        "QA/checked" not in label_names and
                        "OS/Windows" not in label_names and
                        "OS/unix-like/linux" not in label_names):
                    mac_checklist.append(output_line)

                if("QA/checked-Win64" not in label_names and
                        "QA/checked" not in label_names and
                        "OS/macOS" not in label_names and
                        "OS/unix-like/linux" not in label_names):
                    win64_checklist.append(output_line)

                if("QA/checked-Linux" not in label_names and
                        "QA/checked" not in label_names and
                        "OS/Windows" not in label_names and
                        "OS/macOS" not in label_names):
                    linux_checklist.append(output_line)
    print("Mac Checklist:")
    bigline = "## Per release specialty tests\n"
    for line in mac_checklist:
        bigline += line + "\n"
    print(bigline)
    print("")
    macTitle = "Manual test run on OS X for " + milestonever
    macList = ["OS/macOS", "release-notes/exclude", "tests"]

    if args.test is None:
        repo.create_issue(title=macTitle,
                          body=bigline,
                          assignees="LaurenWags, kjozwiak",
                          milestone=laptop_milestone[milestonever],
                          labels=macList)

    print("Win64 Checklist:")
    bigline = "## Per release specialty tests\n"
    for line in win64_checklist:
        bigline += line + "\n"
    print(bigline)
    print("")
    winTitle = "Manual test run on Windows x64 for " + milestonever
    winList = ["OS/Windows", "release-notes/exclude", "tests", "QA/Yes"]

    if args.test is None:
        repo.create_issue(title=winTitle,
                          body=bigline,
                          assignees="srirambv, GeetaSarvadnya",
                          milestone=laptop_milestone[milestonever],
                          labels=winList)

    print("Linux Checklist:")
    bigline = "## Per release specialty tests\n"
    for line in linux_checklist:
        bigline += line + "\n"
    print(bigline)
    print("")
    linTitle = "Manual test run on Linux for " + milestonever
    linList = ["OS/unix-like/linux",
               "release-notes/exclude",
               "tests",
               "QA/Yes"]

    if args.test is None:
        repo.create_issue(title=linTitle,
                          body=bigline,
                          assignees="kjozwiak, btlechowski",
                          milestone=laptop_milestone[milestonever],
                          labels=linList)

    return 0


def laptop_hf_testruns(milestonever):

    for issue in laptop_repo.get_issues(
            milestone=laptop_milestone[milestonever],
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
                        "QA/No" not in label_names and
                        "tests" not in label_names):
                    output_line = " - " + issue_title + ".([#" +\
                        str(issue.number) + "](" + issue.html_url + "))"

            if("QA/Yes" in label_names and
                    "QA/No" not in label_names and
                    "tests" not in label_names):
                output_line = " - [ ] " + issue_title + ".([#" +\
                    str(issue.number) + "](" + issue.html_url + "))"
                checklist.append(output_line)
            if("QA Pass-macOS" not in label_names and
                    "OS/Windows" not in label_names and
                    "OS/Linux" not in label_names and
                    "QA/No" not in label_names):
                mac_checklist.append(output_line)

            if("QA Pass-Win64" not in label_names and
                    "OS/macOS" not in label_names and
                    "OS/Linux" not in label_names and
                    "QA/No" not in label_names):
                win64_checklist.append(output_line)

            if("QA Pass-Linux" not in label_names and
                    "OS/Windows" not in label_names and
                    "OS/macOS" not in label_names and
                    "QA/No" not in label_names and
                    "tests" not in label_names):
                linux_checklist.append(output_line)

    print("Checklist: ")
    for line in checklist:
        print(line)
    print("")

    print("Mac Checklist:")
    if(len(mac_checklist) != 0):
        bigline = "## Per release specialty tests\n"
        for line in mac_checklist:
            bigline += line + "\n"
        bigline = bigline + laptop_hf_template
        print(bigline)
        print("")
        macTitle = "Manual test run on OS X for " + milestonever
        macList = ["OS/macOS", "release-notes/exclude", "tests", "QA/Yes"]
    else:
        print(laptop_hf_template)
        print("")
        macTitle = "Manual test run on OS X for " + milestonever
        macList = ["OS/macOS", "release-notes/exclude", "tests", "QA/Yes"]

    if args.test is None:
        laptop_repo.create_issue(title=macTitle,
                                 body=bigline,
                                 assignees=["LaurenWags", "kjozwiak"],
                                 milestone=laptop_milestone[milestonever],
                                 labels=macList)

    print("Win64 Checklist:")
    if(len(win64_checklist) != 0):
        bigline = "## Per release specialty tests\n"
        for line in win64_checklist:
            bigline += line + "\n"
        bigline = bigline + laptop_hf_template
        print(bigline)
        print("")
        winTitle = "Manual test run on Windows x64 for " + milestonever
        winList = ["OS/Windows", "release-notes/exclude", "tests", "QA/Yes"]
    else:
        print(laptop_hf_template)
        print("")
        winTitle = "Manual test run on Windows x64 for " + milestonever
        winList = ["OS/Windows", "release-notes/exclude", "tests", "QA/Yes"]

    if args.test is None:
        laptop_repo.create_issue(title=winTitle,
                                 body=bigline,
                                 assignees=["btlechowski", "GeetaSarvadnya"],
                                 milestone=laptop_milestone[milestonever],
                                 labels=winList)

    print("Linux Checklist:")
    if(len(linux_checklist) != 0):
        bigline = "## Per release specialty tests\n"
        for line in linux_checklist:
            bigline += line + "\n"
        bigline = bigline + laptop_hf_template
        print(bigline)
        print("")
        linTitle = "Manual test run on Linux for " + milestonever
        linList = ["OS/unix-like/linux",
                   "release-notes/exclude",
                   "tests",
                   "QA/Yes"]
    else:
        print(laptop_hf_template)
        print("")
        linTitle = "Manual test run on Linux for " + milestonever
        linList = ["OS/unix-like/linux",
                   "release-notes/exclude",
                   "tests",
                   "QA/Yes"]

    if args.test is None:
        laptop_repo.create_issue(title=linTitle,
                                 body=bigline,
                                 assignee="srirambv",
                                 milestone=laptop_milestone[milestonever],
                                 labels=linList)

    return 0


def ios_testruns():
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

    print("Release Note:")
    for line in release_notes:
        print(line)
    print("")

    print("Release Checklist:")
    for line in checklist:
        print(line)
    print("")

    print("iPad Checklist:")
    bigline = "## Per release speciality tests\n"
    for line in iPad_checklist:
        bigline += line + "\n"
    bigline = bigline + ios_template
    print(bigline)
    print("")
    iPad_Title = "Manual test run for " + ios_key +\
        " on iPad running iOS12"
    iPad_List = ["ipad", "release-notes/exclude", "tests", "QA/Yes"]

    if args.test is None:
        ios_repo.create_issue(title=iPad_Title,
                              body=bigline,
                              assignees=["srirambv", "kjozwiak"],
                              milestone=ios_milestone[ios_key],
                              labels=iPad_List)

    print("iPhone Checklist:")
    bigline = "## Per release speciality tests\n"
    for line in iPhone_checklist:
        bigline += line + "\n"
    bigline = bigline + ios_template
    print(bigline)
    print("")
    iPhone_Title = "Manual test run for " + ios_key +\
        " on iPhone running iOS12"
    iPhone_List = ["iPhone", "release-notes/exclude", "tests", "QA/Yes"]

    if args.test is None:
        ios_repo.create_issue(title=iPhone_Title,
                              body=bigline,
                              assignee="srirambv",
                              milestone=ios_milestone[ios_key],
                              labels=iPhone_List)

    print("iPhone X Checklist:")
    bigline = "## Per release speciality tests\n"

    for line in iPhoneX_checklist:
        bigline += line + "\n"
    bigline = bigline + ios_template
    print(bigline)
    print("")
    iPhoneX_Title = "Manual test run for " + ios_key +\
        " on iPhone X running iOS12"
    iPhoneX_List = ["iPhone", "release-notes/exclude", "tests", "QA/Yes"]

    if args.test is None:
        ios_repo.create_issue(title=iPhoneX_Title,
                              body=bigline,
                              assignee="srirambv",
                              milestone=ios_milestone[ios_key],
                              labels=iPhoneX_List)

    return


def android_testruns(milestonever):

    wikitemplate_android = open("wikitemplate-android.md", "r")
    android_template = wikitemplate_android.read()

    for issue in laptop_repo.get_issues(
            milestone=laptop_milestone[milestonever],
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

                if("QA Pass - Android x86" not in label_names and
                        "checked by qa" not in label_names and
                        "tests" not in label_names and
                        "ARM" not in label_names and
                        "tablet-specific" not in label_names and
                        "bug/ads" not in label_names and
                        "bug/BR" not in label_names):
                    android_x86_checklist.append(output_line)

                if("QA Pass - Android Tab" not in label_names and
                        "checked by qa" not in label_names and
                        "tests" not in label_names and
                        "x86" not in label_names and
                        "phone-specific" not in label_names):
                    android_tab_checklist.append(output_line)

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
    AndroidARMtitle = "Manual test run on Android ARM  for " + androidkey
    AndroidARMlist = ["ARM", "release-notes/exclude", "tests", "QA/Yes"]

    if args.test is None:
        android_repo.create_issue(title=AndroidARMtitle,
                                  body=bigline,
                                  assignee="srirambv",
                                  milestone=laptop_milestone[androidkey],
                                  labels=AndroidARMlist)

    print("Android x86 Checklist:")
    bigline = "## Per release specialty tests\n"
    for line in android_x86_checklist:
        bigline += line + "\n"
    bigline = bigline + android_template
    print(bigline)
    print("")
    Androidx86title = "Manual test run on Android x86 for " + androidkey
    Androidx86list = ["x86", "release-notes/exclude", "tests", "QA/Yes"]

    if args.test is None:
        android_repo.create_issue(title=Androidx86title,
                                  body=bigline,
                                  assignee="LaurenWags",
                                  milestone=laptop_milestone[androidkey],
                                  labels=Androidx86list)

    print("Android Tab Checklist:")
    bigline = "## Per release specialty tests\n"
    for line in android_tab_checklist:
        bigline += line + "\n"
    bigline = bigline + android_template
    print(bigline)
    print("")
    AndroidTabtitle = "Manual test run on Android Tab  for " + androidkey
    AndroidTablist = ["ARM", "release-notes/exclude", "tests", "QA/Yes"]

    if args.test is None:
        android_repo.create_issue(title=AndroidTabtitle,
                                  body=bigline,
                                  assignee="srirambv",
                                  milestone=laptop_milestone[androidkey],
                                  labels=AndroidTablist)

    return 0


def cryptowallet_testruns(milestonever):

    wikitemplate_crypto = open("wikitemplate-crypto.md", "r")
    cryptowallet_template = wikitemplate_crypto.read()

    for issue in laptop_repo.get_issues(
        milestone=laptop_milestone[milestonever], sort="created",
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
                    "feature/crypto-wallets" in label_names and
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
                        "feature/crypto-wallets" in label_names and
                        "OS/Windows" not in label_names and
                        "OS/Linux" not in label_names and
                        "QA/No" not in label_names and
                        "tests" not in label_names):
                    mac_checklist.append(output_line)

                if("QA Pass-Win64" not in label_names and
                        "feature/crypto-wallets" in label_names and
                        "OS/macOS" not in label_names and
                        "OS/Linux" not in label_names and
                        "QA/No" not in label_names and
                        "tests" not in label_names):
                    win64_checklist.append(output_line)

                if("QA Pass-Linux" not in label_names and
                        "feature/crypto-wallets" in label_names and
                        "OS/Windows" not in label_names and
                        "OS/macOS" not in label_names and
                        "QA/No" not in label_names and
                        "tests" not in label_names):
                    linux_checklist.append(output_line)

    print("Mac Checklist:\n")
    bigline = "## Per release specialty tests\n"
    for line in mac_checklist:
        bigline += line + "\n"
    bigline = bigline + cryptowallet_template
    print(bigline)
    print("")
    macTitle = "Manual test run on OS X for " + milestonever
    macList = ["OS/macOS", "release-notes/exclude", "tests", "QA/Yes"]

    if args.test is None:
        laptop_repo.create_issue(title=macTitle,
                                 body=bigline,
                                 assignee="kjozwiak",
                                 milestone=laptop_milestone[milestonever],
                                 labels=macList)

    print("Win64 Checklist:\n")
    bigline = "## Per release specialty tests\n"
    for line in win64_checklist:
        bigline += line + "\n"
    bigline = bigline + cryptowallet_template
    print(bigline)
    print("")
    winTitle = "Manual test run on Windows x64 for " + milestonever
    winList = ["OS/Windows", "release-notes/exclude", "tests", "QA/Yes"]

    if args.test is None:
        laptop_repo.create_issue(title=winTitle,
                                 body=bigline,
                                 assignee="srirambv",
                                 milestone=laptop_milestone[milestonever],
                                 labels=winList)

    print("Linux Checklist:\n")
    bigline = "## Per release specialty tests\n"
    for line in linux_checklist:
        bigline += line + "\n"
    bigline = bigline + cryptowallet_template
    print(bigline)
    print("")
    linTitle = "Manual test run on Linux for " + milestonever
    linList = ["OS/unix-like/linux",
               "release-notes/exclude",
               "tests",
               "QA/Yes"]

    if args.test is None:
        laptop_repo.create_issue(title=linTitle,
                                 body=bigline,
                                 assignee="srirambv",
                                 milestone=laptop_milestone[milestonever],
                                 labels=linList)

    return 0


print("*********************************************************************"
      "*****************************************************")
print("                         Few things to check before generating test"
      "runs")
print("")
print("1. Ensure all closed items have QA/Yes and QA/No labels added to"
      "include in the test run")
print("")
print("2. For Laptop - Test runs will be generated upto 5 milestones")
print("")
print("3. Manually change ""milestone.keys"" value to generate for a specific"
      "milestone on any platform")
print("***********************************************************************"
      "***************************************************")

header = print("Create test runs for:\n")
laptop = print("1. Laptop Release")
laptop_per = print("2. Laptop Per-release Checklist")
laptop_hf = print("3. Laptop HotFix Checklist")
ios = print("4. iOS")
android = print("5. Android")
cryptowallet = print("6. Brave Crypto Wallet - Ethereum Client\n")

select_checklist = input("Choose the platform for which you want to" +
                         " generate the test run: ")

if(select_checklist == "1" or select_checklist == "2"):
    print("\nSelect the milestone to create tests \n")

    length = 0
    while length < len(laptop_key):
        print(str(length+1) + ". " + sorted(laptop_milestone.keys())[length])
        length += 1

    generate_test = input("\nCreate test runs for: ")

    if(select_checklist == "1" and generate_test == "1"):
        print("\nGenerating test runs for " +
              str(sorted(laptop_milestone.keys())[0]) + " on all platforms")
        print(sorted(laptop_milestone.keys())[0])
        laptop_testruns(key1)
    elif(select_checklist == "1" and generate_test == "2"):
        print("\nGenerating test runs for " +
              str(sorted(laptop_milestone.keys())[1]) + " on all platforms")
        print(sorted(laptop_milestone.keys())[1])
        laptop_testruns(key2)
    elif(select_checklist == "1" and generate_test == "3"):
        print("\nGenerating test runs for " +
              str(sorted(laptop_milestone.keys())[2]) + " on all platforms")
        print(sorted(laptop_milestone.keys())[2])
        laptop_testruns(key3)
    elif(select_checklist == "1" and generate_test == "4"):
        print("\nGenerating test runs for " +
              str(sorted(laptop_milestone.keys())[3]) + " on all platforms")
        print(sorted(laptop_milestone.keys())[3])
        laptop_testruns(key4)
    elif(select_checklist == "2" and generate_test == "1"):
        print("\nGenerating Per-release checklist for " +
              str(sorted(laptop_milestone.keys())[0]) + " on all platforms")
        print(sorted(laptop_milestone.keys())[0])
        laptop_perrel_checklist(key1)
    elif(select_checklist == "2" and generate_test == "2"):
        print("\nGenerating Per-release checklist for " +
              str(sorted(laptop_milestone.keys())[1]) + " on all platforms")
        print(sorted(laptop_milestone.keys())[1])
        laptop_perrel_checklist(key2)
    elif(select_checklist == "2" and generate_test == "3"):
        print("\nGenerating Per-release checklist for " +
              str(sorted(laptop_milestone.keys())[2]) + " on all platforms")
        print(sorted(laptop_milestone.keys())[2])
        laptop_perrel_checklist(key3)
    elif(select_checklist == "2" and generate_test == "4"):
        print("\nGenerating Per-release checklist for " +
              str(sorted(laptop_milestone.keys())[3]) + " on all platforms")
        print(sorted(laptop_milestone.keys())[3])
        laptop_perrel_checklist(key4)
    else:
        print("Nothing to create in this milestone. Run the script again.")
        exit()
elif(select_checklist == "3"):
    print("\nGenerating test runs for " +
          str(sorted(laptop_milestone.keys())[0]) + " on all platforms")
    print(sorted(laptop_milestone.keys())[0])
    laptop_hf_testruns(key1)
elif (select_checklist == "4"):
    generate_ios_test = print("\nGenerating test runs for iOS ",
                              sorted(ios_milestone.keys())[0])
    ios_testruns()
elif (select_checklist == "5"):
    generate_android_test = print("\nGenerating test runs for " + androidkey)
    android_testruns(androidkey)
elif (select_checklist == "6"):
    if (ethkey == ""):
        print("No open milestone to generate tests")
    else:
        generate_cryptowallet_test = print("\nGenerating test runs for "
            "Brave Crypto wallet release " + ethkey)
        cryptowallet_testruns(ethkey)
else:
    print("Incorrect selection. Exiting test creation...")
    exit()
