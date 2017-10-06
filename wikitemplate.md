## Installer

1. [ ] Check that installer is close to the size of last release.
2. [ ] Check signature: If OS Run `spctl --assess --verbose /Applications/Brave.app/` and make sure it returns `accepted`.  If Windows right click on the installer exe and go to Properties, go to the Digital Signatures tab and double click on the signature.  Make sure it says "The digital signature is OK" in the popup window.
3. [ ] Check Brave, muon, and libchromiumcontent version in About and make sure it is EXACTLY as expected.

## Data

1. [ ] Make sure that data from the last version appears in the new version OK.
2. [ ] With data from the last version, test that
    - [ ] cookies are preserved
    - [ ] pinned tabs can be opened
    - [ ] pinned tabs can be unpinned
    - [ ] unpinned tabs can be re-pinned
    - [ ] opened tabs can be reloaded
    - [ ] bookmarks on the bookmark toolbar can be opened
    - [ ] bookmarks in the bookmark folder toolbar can be opened

## Last changeset test

1. [ ] Test what is covered by the last changeset (you can find this by clicking on the SHA in about:brave).

## Per release specialty tests

1. [ ]

## Widevine/Netflix test

1. [ ] Test that you can log into Netflix and start a show.

## Ledger

1. [ ] Create a wallet with a value other than $5 selected in the monthly budget dropdown. Click on the 'Add Funds' button and check that Coinbase transactions are blocked.
2. [ ] Remove all `ledger-*.json` files from `~/Library/Application\ Support/Brave/`. Go to the Payments tab in about:preferences, enable payments, click on `create wallet`. Check that the `add funds` button appears after a wallet is created.
3. [ ] Click on `add funds` and verify that adding funds through Coinbase increases the account balance.
4. [ ] Repeat the step above but add funds by scanning the QR code in a mobile bitcoin app instead of through Coinbase.
5. [ ] Visit nytimes.com for a few seconds and make sure it shows up in the Payments table.
6. [ ] Go to https://jsfiddle.net/LnwtLckc/5/ and click the register button. In the Payments tab, click `add funds`. Verify that the `transfer funds` button is visible and that clicking on `transfer funds` opens a jsfiddle URL in a new tab.
7. [ ] Go to https://jsfiddle.net/LnwtLckc/5/ and click `unregister`. Verify that the `transfer funds` button no longer appears in the `add funds` modal.
8. [ ] Check that disabling payments and enabling them again does not lose state.

## Sync

1. [ ] Verify you are able to sync two devices using the secret code
2. [ ] Visit a site on device 1 and change shield setting, ensure that the saved site preference is synced to device 2
3. [ ] Enable Browsing history sync on device 1, ensure the history is shown on device 2
4. [ ] Import/Add bookmarks on device 1, ensure it is synced on device 2
5. [ ] Ensure imported bookmark folder structure is maintained on device 2
6. [ ] Ensure bookmark favicons are shown after sync

## About pages

1. [ ] Test that about:adblock loads
2. [ ] Test that about:autofill loads
3. [ ] Test that about:bookmarks loads bookmarks
4. [ ] Test that about:downloads loads downloads
5. [ ] Test that about:extensions loads
6. [ ] Test that about:history loads history
7. [ ] Test that about:passwords loads
8. [ ] Test that about:styles loads
9. [ ] Test that about:welcome loads
10. [ ] Test that about:preferences changing a preference takes effect right away
11. [ ] Test that about:preferences language change takes effect on re-start

## Bookmarks

1. [ ] Test that creating a bookmark on the bookmarks toolbar with the star button works
2. [ ] Test that creating a bookmark on the bookmarks toolbar by dragging the un/lock icon works
3. [ ] Test that creating a bookmark folder on the bookmarks toolbar works
4. [ ] Test that moving a bookmark into a folder by drag and drop on the bookmarks folder works
5. [ ] Test that clicking a bookmark in the toolbar loads the bookmark.
6. [ ] Test that clicking a bookmark in a bookmark toolbar folder loads the bookmark.
7. [ ] Test that a bookmark on the bookmark toolbar can be removed via context menu
8. [ ] Test that a bookmark in a bookmark folder on the bookmark toolbar can be removed via context menu
9. [ ] Test that a bookmark subfolder can be removed via context menu
10. [ ] Test that a bookmark folder on the bookmark toolbar can be removed via context menu

## Context menus

1. [ ] Make sure context menu items in the URL bar work
2. [ ] Make sure context menu items on content work with no selected text.
3. [ ] Make sure context menu items on content work with selected text.
4. [ ] Make sure context menu items on content work inside an editable control on `about:styles` (input, textarea, or contenteditable).

## Find on page

1. [ ] Ensure search box is shown with shortcut
2. [ ] Test successful find
3. [ ] Test forward and backward find navigation
4. [ ] Test failed find shows 0 results
5. [ ] Test match case find

## Geolocation

1. [ ] Check that https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/Using_geolocation works

## Site hacks

1. [ ] Test https://www.twitch.tv/adobe sub-page loads a video and you can play it

## Downloads

1. [ ] Test downloading a file works and that all actions on the download item works.

## Fullscreen

1. [ ] Test that entering full screen window works View -> Toggle Full Screen. And exit back (Not Esc).
2. [ ] Test that entering HTML5 full screen works. And Esc to go back. (youtube.com)

## Tabs, Pinning and Tear off tabs

1. [ ] Test that tabs are pinnable
2. [ ] Test that tabs are unpinnable
3. [ ] Test that tabs are draggable to same tabset
4. [ ] Test that tabs are draggable to alternate tabset
5. [ ] Test that tabs can be teared off into a new window
6. [ ] Test that you are able to reattach a tab that is teared off into a new window
7. [ ] Test that tab pages can be closed
8. [ ] Test that tab pages can be muted

## Zoom

1. [ ] Test zoom in / out shortcut works
2. [ ] Test hamburger menu zooms.
3. [ ] Test zoom saved when you close the browser and restore on a single site.
4. [ ] Test zoom saved when you navigate within a single origin site.
5. [ ] Test that navigating to a different origin resets the zoom

## Bravery settings

1. [ ] Check that HTTPS Everywhere works by loading https://https-everywhere.badssl.com/
2. [ ] Turning HTTPS Everywhere off and shields off both disable the redirect to https://https-everywhere.badssl.com/
3. [ ] Check that ad replacement works on http://slashdot.org
4. [ ] Check that toggling to blocking and allow ads works as expected.
5. [ ] Test that clicking through a cert error in https://badssl.com/ works.
6. [ ] Test that Safe Browsing works (https://www.raisegame.com/)
7. [ ] Turning Safe Browsing off and shields off both disable safe browsing for https://www.raisegame.com/.
8. [ ] Visit https://brianbondy.com/ and then turn on script blocking, nothing should load. Allow it from the script blocking UI in the URL bar and it should work.
9. [ ] Test that about:preferences default Bravery settings take effect on pages with no site settings.
10. [ ] Test that turning on fingerprinting protection in about:preferences shows 3 fingerprints blocked at https://jsfiddle.net/bkf50r8v/13/. Test that turning it off in the Bravery menu shows 0 fingerprints blocked.
11. [ ] Test that 3rd party storage results are blank at https://jsfiddle.net/7ke9r14a/9/ when 3rd party cookies are blocked and not blank when 3rd party cookies are unblocked.
12. [ ] Test that audio fingerprint is blocked at https://audiofingerprint.openwpm.com/ when fingerprinting protection is on.
13. [ ] Test that browser is not detected on https://extensions.inrialpes.fr/brave/


## Content tests

1. [ ] Go to https://brianbondy.com/ and click on the twitter icon on the top right. Test that context menus work in the new twitter tab.
2. [ ] Load twitter and click on a tweet so the popup div shows.   Click to dismiss and repeat with another div. Make sure it shows.
3. [ ] Go to http://www.bennish.net/web-notifications.html and test that clicking on 'Show' pops up a notification asking for permission. Make sure that clicking 'Deny' leads to no notifications being shown.
4. [ ] Go to https://trac.torproject.org/projects/tor/login and make sure that the password can be saved. Make sure the saved password shows up in `about:passwords`. Then reload https://trac.torproject.org/projects/tor/login and make sure the password is autofilled.
5. [ ] Open `about:styles` and type some misspellings on a textbox, make sure they are underlined.
6. [ ] Make sure that right clicking on a word with suggestions gives a suggestion and that clicking on the suggestion replaces the text.
7. [ ] Make sure that Command + Click (Control + Click on Windows, Control + Click on Ubuntu) on a link opens a new tab but does NOT switch to it.  Click on it and make sure it is already loaded.
8. [ ] Open an email on http://mail.google.com/ or inbox.google.com and click on a link. Make sure it works.
9. [ ] Test that PDF is loaded at http://www.orimi.com/pdf-test.pdf
10. [ ] Test that https://mixed-script.badssl.com/ shows up as grey not red (no mixed content scripts are run).
11. [ ] Test that extension icons can be displayed on the navigation bar

## Flash tests

1. [ ] Turn on Flash in about:preferences#security. Test that clicking on 'Install Flash' banner on myspace.com shows a notification to allow Flash and that the banner disappears when 'Allow' is clicked.
2. [ ] Test that flash placeholder appears on http://www.homestarrunner.com

## Autofill tests

1. [ ] Test that autofill works on http://www.roboform.com/filling-test-all-fields

## Session storage

Do not forget to make a backup of your entire `~/Library/Application\ Support/Brave` folder.

1. [ ] Temporarily move away your `~/Library/Application\ Support/Brave/session-store-1` and test that clean session storage works. (`%appdata%\Brave in Windows`, `./config/brave` in Ubuntu)
2. [ ] Test that windows and tabs restore when closed, including active tab.
3. [ ] Move away your entire `~/Library/Application\ Support/Brave` folder (`%appdata%\Brave in Windows`, `./config/brave` in Ubuntu)

## Cookie and Cache

1. [ ] Make a backup of your profile, turn on all clearing in preferences and shut down.  Make sure when you bring the browser back up everything is gone that is specified.
2. [ ] Go to http://samy.pl/evercookie/ and set an evercookie. Check that going to prefs, clearing site data and cache, and going back to the Evercookie site does not remember the old evercookie value.

## Update tests

1. [ ] Test that updating using `BRAVE_UPDATE_VERSION=0.8.3` env variable works correctly.
