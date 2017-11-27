
## Installer

1. [ ] Check that installer is close to the size of last release.
2. [ ] Check the Brave version in About and make sure it is EXACTLY as expected.

## Data

1. [ ] Make sure that data from the last version appears in the new version OK.
2. [ ] Test that the previous version's cookies are preserved in the next version.

## Bookmarks

1. [ ] Test that creating a bookmark in the left well works
2. [ ] Test that clicking a bookmark in the left well loads the bookmark
3. [ ] Test that deleting a bookmark in the left well works
4. [ ] Test that creating a bookmark folder works
5. [ ] Test that creating a bookmark inside the created folder works
6. [ ] Test that you are able to add a bookmark directly inside a bookmark folder
7. [ ] Test that you are able to delete a bookmark in edit mode
8. [ ] Test that you are able to delete a bookmark folder with bookmarks inside
9. [ ] Test adding a bookmark domain subpaths is retained and you are successfully able to visit the domain subpath in a new tab

## Context menus

1. [ ] Make sure context menu items in the URL bar work
2. [ ] Make sure context menu items on content work with no selected text.
3. [ ] Make sure context menu items on content work with selected text.
4. [ ] Make sure context menu items on content work inside an editable control (input, textarea, or contenteditable).
5. [ ] Context menu: verify you can Open in Background Tab, and Open in Private Tab

## Find on page

1. [ ] Ensure search box is shown when selected via the share menu
2. [ ] Test successful find
3. [ ] Test forward and backward find navigation
4. [ ] Test failed find shows 0 results

## Private Mode

1. [ ] Create private tab, go to http://google.com, search for 'yumyums', exit private mode, go to http://google.com search box and begin typing 'yumyums' and verify that word is not in the autocomplete list

## Reader Mode
1. [ ] Visit http://m.slashdot.org, open any article, verify the reader mode icon is shown in the URL bar
2. [ ] Verify tapping on the reader mode icon opens the article in reader mode
3. [ ] Edit reader mode settings and open different pages in reader mode and verify if the setting is retained across each article

## History

1. [ ] On youtube.com, thestar.com (or any other site using push state nav), navigate the site and verify history is added. Also note if the progress bar activates and shows progress.
2. [ ] Settings > Clear Private Data, and clear all. Check history is cleared, and top sites are cleared.

## Shields Settings
1. [ ] Enable all switches in settings and visit a site and disable block scripts. Kill and relaunch app and verify if the site shield settings are retained

## Site hacks

1. [ ] Test https://www.twitch.tv/adobe sub-page loads a video and you can play it

## Downloads

1. [ ] Test that you can save an image from a site.

## Fullscreen

1. [ ] Test that entering HTML5 full screen works. And pressing restore to go back exits full screen. (youtube.com)

## Gestures

1. [ ] Test zoom in / out gestures work
2. [ ] Test that navigating to a different origin resets the zoom
3. [ ] Swipe back and forward to navigate, verify this works as expected

## Password Managers
1. [ ] Test tapping on 1Password on the slide out keyboard launches 1Password App and able to select the stored credentials
2. [ ] Test tapping on bitwarden password manager in the autofill field launches the app and autofills the stored data

## Sync
1. [ ] Ensure you are able to scan the QR code and sync with laptop
2. [ ] Ensure the bookmarks from laptop shows up on the mobile after sync completes
3. [ ] Add a bookmark on mobile and check if it gets synced to the laptop

## Bravery settings

1. [ ] Check that HTTPS Everywhere works by loading https://https-everywhere.badssl.com/
2. [ ] Turning HTTPS Everywhere off and shields off both disable the redirect to https://https-everywhere.badssl.com/
3. [ ] Check that block ad and unblock ad works on http://slashdot.org
4. [ ] Check that toggling to blocking and allow ads works as expected.
5. [ ] Test that clicking through a cert error in https://badssl.com/ works.
6. [ ] Test that Safe Browsing works (http://downloadme.org/)
7. [ ] Turning Safe Browsing off and shields off both disable safe browsing for http://downloadme.org/.
8. [ ] Enable block script globally from settings, Visit https://brianbondy.com/, nothing should load. Tap on Shields and disable block script, page should load properly
9. [ ] Test that preferences default Bravery settings take effect on pages with no site settings.
10. [ ] Test that turning on fingerprinting protection in preferences shows 1 fingerprints blocked at https://browserleaks.com/canvas . Test that turning it off in the Bravery menu shows 0 fingerprints blocked.
11. [ ] Test that 3rd party storage results are blank at https://jsfiddle.net/7ke9r14a/7/ when 3rd party cookies are blocked.
12. [ ] Test that audio fingerprint is blocked at https://audiofingerprint.openwpm.com/ when fingerprinting protection is on.


## Content tests

1. [ ] Go to https://brianbondy.com/ and click on the twitter icon on the top right. Test that context menus work in the new twitter tab
2. [ ] Load twitter and click on a tweet so the popup div shows.   Click to dismiss and repeat with another div. Make sure it shows
3. [ ] Go to https://trac.torproject.org/projects/tor/login and make sure that the password can be saved.  Make sure the saved password is auto-populated when you visit the site again.
4. [ ] Open an email on http://mail.google.com/ or inbox.google.com and click on a link. Make sure it works
5. [ ] Test that PDF is loaded at http://www.orimi.com/pdf-test.pdf
6. [ ] Test that https://mixed-script.badssl.com/ shows up as grey not red (no mixed content scripts are run)
7. [ ] Test that https://news.google.com/ sites open in a new tab (due to target being _blank)

## Top sites view

1. [ ] Long-press on top sites to get to deletion mode, and delete a top site (note this will stop that site from showing up again on top sites, so you may not want to do this a site you want to keep there)

## Background

1. [ ] Start loading a page, background the app, wait >5 sec, then bring to front, ensure splash screen is not shown

## Session storage

1. [ ] Test that tabs restore when closed, including active tab.
