
## Installer

- [ ] Check that installer is close to the size of last release
- [ ] Check signature: If OS Run `spctl --assess --verbose /Applications/Brave.app/` and make sure it returns `accepted`.  If Windows right click on the installer exe and go to Properties, go to the Digital Signatures tab and double click on the signature.  Make sure it says "The digital signature is OK" in the popup window
- [ ] Check Brave, muon, and libchromiumcontent version in `about:brave` and make sure it is EXACTLY as expected

## Data

- [ ] Make sure that data from the last version appears in the new version OK
- [ ] With data from the last version, test that
  - [ ] cookies are preserved
  - [ ] pinned tabs can be opened
  - [ ] pinned tabs can be unpinned
  - [ ] unpinned tabs can be re-pinned
  - [ ] opened tabs can be reloaded
  - [ ] bookmarks on the bookmark toolbar can be opened
  - [ ] bookmarks in the bookmark folder toolbar can be opened

## Last changeset test

- [ ] Test what is covered by the last changeset (you can find this by clicking on the SHA in about:brave)

## Widevine/Netflix test

- [ ] Test that you can log into Netflix and start a show

## Ledger

- [ ] Verify wallet is auto created after enabling payments
- [ ] Verify monthly budget and account balance shows correct BAT and USD value
- [ ] Click on `add funds` and click on each currency and verify it shows wallet address and QR Code
- [ ] Verify that Brave BAT wallet address can be copied
- [ ] Verify adding funds via any of the currencies flows into BAT Wallet after specified amount of time
- [ ] Verify adding funds to an existing wallet with amount, adjusts the BAT value appropriately
- [ ] Change min visit and min time in advance setting and verify if the publisher list gets updated based on new setting
- [ ] Visit nytimes.com for a few seconds and make sure it shows up in the Payments table
- [ ] Check that disabling payments and enabling them again does not lose state
- [ ] Upgrade from older version
  - [ ] Verify the wallet overlay is shown when wallet transition is happening upon upgrade
  - [ ] Verify transition overlay is shown post upgrade even if the payment is disabled before upgrade
  - [ ] Verify publishers list is not lost after upgrade when payment is disabled in the older version
### Ledger Media
  - [ ] Visit any YouTube video in a normal/session tab and ensure the video publisher name is listed in ledger table
  - [ ] Visit any YouTube video in a private tab and ensure the video publisher name is not listed in ledger table
  - [ ] Visit any live YouTube video and ensure the time spent is shown under ledger table
  - [ ] Visit any embeded YouTube video and ensure the video publisher name is listed in ledger table
  - [ ] Ensure total time spent is correctly calculated for each publisher video
  - [ ] Ensure total time spent is correctly calculated when switching to YouTube video from an embeded video
  - [ ] Ensure YouTube publishers are not listed when `Allow contributions to video` is disabled in adavanced settings
  - [ ] Ensure existing YouTube publishers are not lost when `Allow contributions to video` is disabled in adavanced settings
  - [ ] Ensure YouTube publishers is listed but not included when `auto-include` is disabled
  - [ ] Update Advanced settings to different time/visit value and ensure YouTube videos are added to ledger table once criteria is met

## Sync

- [ ] Verify you are able to sync two devices using the secret code
- [ ] Visit a site on device 1 and change shield setting, ensure that the saved site preference is synced to device 2
- [ ] Enable Browsing history sync on device 1, ensure the history is shown on device 2
- [ ] Clear browsing history on device 1, ensure the history is sync back on device 1 from device 2
- [ ] Import/Add bookmarks on device 1, ensure it is synced on device 2
- [ ] Ensure imported bookmark folder structure is maintained on device 2
- [ ] Ensure bookmark favicons are shown after sync

## About pages

- [ ] Test that about:adblock loads
- [ ] Test that about:autofill loads
- [ ] Test that about:bookmarks loads bookmarks
- [ ] Test that about:downloads loads downloads
- [ ] Test that about:extensions loads
- [ ] Test that about:history loads history
- [ ] Test that about:passwords loads
- [ ] Test that about:styles loads
- [ ] Test that about:welcome loads
- [ ] Test that about:preferences changing a preference takes effect right away
- [ ] Test that about:preferences language change takes effect on re-start

## Bookmarks

- [ ] Test that creating a bookmark on the bookmarks toolbar with the star button works
- [ ] Test that creating a bookmark on the bookmarks toolbar by dragging the un/lock icon works
- [ ] Test that creating a bookmark folder on the bookmarks toolbar works
- [ ] Test that moving a bookmark into a folder by drag and drop on the bookmarks folder works
- [ ] Test that clicking a bookmark in the toolbar loads the bookmark.
- [ ] Test that clicking a bookmark in a bookmark toolbar folder loads the bookmark.
- [ ] Test that a bookmark on the bookmark toolbar can be removed via context menu
- [ ] Test that a bookmark in a bookmark folder on the bookmark toolbar can be removed via context menu
- [ ] Test that a bookmark subfolder can be removed via context menu
- [ ] Test that a bookmark folder on the bookmark toolbar can be removed via context menu

## Context menus

- [ ] Make sure context menu items in the URL bar work
- [ ] Make sure context menu items on content work with no selected text
- [ ] Make sure context menu items on content work with selected text
- [ ] Make sure context menu items on content work inside an editable control on `about:styles` (input, textarea, or contenteditable)

## Find on page

- [ ] Ensure search box is shown with shortcut
- [ ] Test successful find
- [ ] Test forward and backward find navigation
- [ ] Test failed find shows 0 results
- [ ] Test match case find

## Keyboard Shortcuts

- [ ] Open a new window: `Command` + `n` (macOS) || `Ctrl` + `n` (Win/Linux)
- [ ] Open a new tab: `Command` + `t` (macOS) || `Ctrl` + `t` (Win/Linux)
- [ ] Open a new private tab: `Command` + `Shift` + `p` (macOS) || `Ctrl` + `Shift` + `p` (Win/Linux)
- [ ] Reopen the latest closed tab: `Command` + `Shift` + `t` (macOS) || `Ctrl` + `Shift` + `t` (Win/Linux)
- [ ] Jump to the next tab: `Command` + `Option` + `->` (macOS) || `Ctrl` + `PgDn` (Win/Linux)
- [ ] Jump to the previous tab: `Command` + `Option` + `<-` (macOS) || `Ctrl` + `PgUp` (Win/Linux)
- [ ] Jump to the next tab: `Ctrl` + `Tab` (macOS/Win/Linux)
- [ ] Jump to the previous tab: `Ctrl` + `Shift` + `Tab` (macOS/Win/Linux)
- [ ] Open Brave preferences: `Command` + `,` (macOS) || `Ctrl` + `,` (Win/Linux)
- [ ] Jump into the URL bar: `Command` + `l` (macOS) || `Ctrl` + `l` (Win/Linux)
- [ ] Reload page: `Command` + `r` (macOS) || `Ctrl` + `r` (Win/Linux)
- [ ] Select All: `Command` + `a` (macOS) || `Ctrl` + `a` (Win/Linux)
- [ ] Copying text: `Command` + `c` (macOS) || `Ctrl` + `c` (Win/Linux)
- [ ] Pasting text: `Command` + `v` (macOS) || `Ctrl` + `v` (Win/Linux)
- [ ] Minimize Brave: `Command` + `m` (macOS) || `Ctrl` + `m` (Win/Linux)
- [ ] Quit Brave: `Command` + `q` (macOS) || `Ctrl` + `q` (Win/Linux)

## Geolocation

- [ ] Check that https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/Using_geolocation is blocked due to cross-origin iframes
- [ ] Check that https://browserleaks.com/geo works and shows correct location
- [ ] Check that https://html5demos.com/geo/ works but doesn't require an accurate location

## Crash Reporting

- [ ] Check that loading `chrome://crash` causes the new tab to crash 
- [ ] Check that `chrome://crashes` lists all the crashes and includes both Crash Report ID & Local Crash ID
- [ ] Verify the crash ID matches the report on brave stats

## Site hacks

- [ ] Test https://www.twitch.tv/adobe sub-page loads a video and you can play it

## Downloads

- [ ] Test downloading a file works and that all actions on the download item works

## Fullscreen

- [ ] Test that entering full screen window works View -> Toggle Full Screen. And exit back (Not Esc)
- [ ] Test that entering HTML5 full screen works. And Esc to go back. (youtube.com)

## Tabs, Pinning and Tear off tabs

- [ ] Test that tabs are pinnable
- [ ] Test that tabs are unpinnable
- [ ] Test that tabs are draggable to same tabset
- [ ] Test that tabs are draggable to alternate tabset
- [ ] Test that tabs can be teared off into a new window
- [ ] Test that you are able to reattach a tab that is teared off into a new window
- [ ] Test that tab pages can be closed
- [ ] Test that tab pages can be muted
- [ ] Test that tabs can be cloned

## Zoom

- [ ] Test zoom in / out shortcut works
- [ ] Test hamburger menu zooms
- [ ] Test zoom saved when you close the browser and restore on a single site
- [ ] Test zoom saved when you navigate within a single origin site
- [ ] Test that navigating to a different origin resets the zoom

## Bravery settings

- [ ] Check that HTTPS Everywhere works by loading https://https-everywhere.badssl.com/
- [ ] Turning HTTPS Everywhere off and shields off both disable the redirect to https://https-everywhere.badssl.com/
- [ ] Check that ad replacement works on http://slashdot.org
- [ ] Check that toggling to blocking and allow ads works as expected
- [ ] Test that clicking through a cert error in https://badssl.com/ works
- [ ] Test that Safe Browsing works (https://www.raisegame.com/)
- [ ] Turning Safe Browsing off and shields off both disable safe browsing for https://www.raisegame.com/
- [ ] Visit https://brianbondy.com/ and then turn on script blocking, nothing should load. Allow it from the script blocking UI in the URL bar and it should work
- [ ] Test that about:preferences default Bravery settings take effect on pages with no site settings
- [ ] Test that 3rd party storage results are blank at https://jsfiddle.net/7ke9r14a/9/ when 3rd party cookies are blocked and not blank when 3rd party cookies are unblocked
### Fingerprint Tests
  - [ ] Visit https://jsfiddle.net/bkf50r8v/13/, ensure 3 blocked items are listed in shields. Result window should show `got canvas fingerprint 0`  and  `got webgl fingerprint 00`
  - [ ] Test that audio fingerprint is blocked at https://audiofingerprint.openwpm.com/ only when `Block all fingerprinting protection` is on
  - [ ] Test that Brave browser isn't detected on https://extensions.inrialpes.fr/brave/

## Content tests

- [ ] Go to https://brianbondy.com/ and click on the twitter icon on the top right. Test that context menus work in the new twitter tab
- [ ] Load twitter and click on a tweet so the popup div shows.   Click to dismiss and repeat with another div. Make sure it shows
- [ ] Go to https://www.bennish.net/web-notifications.html and test that clicking on 'Show' pops up a notification asking for permission. Make sure that clicking 'Deny' leads to no notifications being shown
- [ ] Go to https://trac.torproject.org/projects/tor/login and make sure that the password can be saved. Make sure the saved password shows up in `about:passwords`. Then reload https://trac.torproject.org/projects/tor/login and make sure the saved credentials aren't autofilled instead shows saved id as a dropdown under the login field
- [ ] Open `about:styles` and type some misspellings on a textbox, make sure they are underlined.
- [ ] Make sure that right clicking on a word with suggestions gives a suggestion and that clicking on the suggestion replaces the text
- [ ] Make sure that Command + Click (Control + Click on Windows, Control + Click on Ubuntu) on a link opens a new tab but does NOT switch to it.  Click on it and make sure it is already loaded
- [ ] Open an email on http://mail.google.com/ or inbox.google.com and click on a link. Make sure it works
- [ ] Test that PDF is loaded over https at https://basicattentiontoken.org/BasicAttentionTokenWhitePaper-4.pdf
- [ ] Test that PDF is loaded over http at http://www.pdf995.com/samples/pdf.pdf
- [ ] Test that https://mixed-script.badssl.com/ shows up as grey not red (no mixed content scripts are run).
- [ ] Test that hovering the cursor over a link changes the cursor into a pointer (hand)


## Flash tests

- [ ] Test that flash placeholder appears on http://www.homestarrunner.com
- [ ] Test with flash enabled in preferences, auto play option is shown when visiting http://www.homestarrunner.com

## Autofill tests

- [ ] Test that autofill works on http://www.roboform.com/filling-test-all-fields

## Session storage

Do not forget to make a backup of your entire `~/Library/Application\ Support/Brave` folder.

- [ ] Temporarily move away your `~/Library/Application\ Support/Brave/session-store-1` and test that clean session storage works. (`%appdata%\Brave` in Windows, `./config/brave` in Ubuntu)
- [ ] Test that windows and tabs restore when closed, including active tab.
- [ ] Move away your entire `~/Library/Application\ Support/Brave` folder (`%appdata%\Brave` in Windows, `./config/brave` in Ubuntu)

## Cookie and Cache

- [ ] Make a backup of your profile, turn on all clearing in preferences and shut down.  Make sure when you bring the browser back up everything is gone that is specified.
- [ ] Go to http://samy.pl/evercookie/ and set an evercookie. Check that going to prefs, clearing site data and cache, and going back to the Evercookie site does not remember the old evercookie value.

## Update tests

- [ ] Test that updating using `BRAVE_UPDATE_VERSION=0.8.3` env variable works correctly.
- [ ] Test that using `BRAVE_ENABLE_PREVIEW_UPDATES=TRUE` env variable works and prompts for preview build updates.
