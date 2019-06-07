
## Installer

- [ ] Check that installer is close to the size of last release
- [ ] Check the Brave version in About and make sure it is EXACTLY as expected

## Visual look

- [ ] Make sure there is no words of Chromium after any merge

## Data
Pre-Requisite: Put previous build shortcut on home screen. Also have several sites 'Added to home screen' (from 3 dots menu). Then update previous build to Verify build
- [ ] Verify that data from the previous build appears in the updated build as expected (bookmarks, etc)
- [ ] Verify that the cookies from the previous build are preserved after upgrade
- [ ] Verify shortcut is still available on home screen after upgrade
- [ ] Verify sites added to home screen are still visible and able to be used after upgrade
- [ ] Verify sync chain created in previous version is still retained on upgrade
- [ ] Verify settings changes done in previous version is still retained on upgrade

## Bookmarks

- [ ] Verify that creating a bookmark works
- [ ] Verify that clicking a bookmark loads the bookmark
- [ ] Verify that deleting a bookmark works
- [ ] Verify that creating a bookmark folder works

## Custom tabs

- [ ] Make sure Brave handles links from gmail, slack
- [ ] Make sure Brave works as custom tabs provide with Chromer browser
- [ ] Ensure custom tabs work even with sync enabled/disabled

## Context menus

- [ ] Make sure context menu items in the URL bar work
- [ ] Make sure context menu items on content work with no selected text
- [ ] Make sure context menu items on content work with selected text
- [ ] Make sure context menu items on content work inside an editable control (input, textarea, or contenteditable)

## Developer Tools

- [ ] Verify you are able to inspect sublinks via dev tools

## Find in page

- [ ] Ensure search box is shown when selected via the hamburger menu
- [ ] Verify successful find
- [ ] Verify forward and backward find navigation
- [ ] Verify failed find shows 0 results

## Site hacks

- [ ] Verify https://www.twitch.tv/adobe sub-page loads a video and you can play it

## Settings

- [ ] Verify settings changes are retained during upgrade and any changes made doesn't cause the browser to crash

## Downloads

- [ ] Verify downloading a file works and that all actions on the download item works.
- [ ] Verify that PDF is downloaded over https at https://basicattentiontoken.org/BasicAttentionTokenWhitePaper-4.pdf
- [ ] Verify that PDF is downloaded over http at http://www.pdf995.com/samples/pdf.pdf

## Fullscreen

- [ ] Verify that entering HTML5 full screen works. And pressing restore to go back exits full screen. (youtube.com)

## Autofill Tests

- [ ] Verify that autofill works on https://srirambv.github.io/formfiller.html

## Zoom

- [ ] Verify zoom in / out gestures work
- [ ] Verify that navigating to a different origin resets the zoom

## Sync

- [ ] Verify you are able to join sync chain by scanning the QR code
- [ ] Verify you are able to join sync chain using code words
- [ ] Verify you are able to create a sycn chain on the device and add other devices to the chain via QR code/Code words
- [ ] Verify that bookmarks from other devices on the chain show up on the mobile device after sync completes
- [ ] Verify newly created bookmarks gets sync'd to all devices on the sync chain
- [ ] Verify existing bookmarks before joining sync chain also gets sync'd to all devices on the sync chain
- [ ] Verify sync works on a upgrade profile and new bookmarks added post upgrade sync's across devices on the chain
- [ ] Verify add a bookmark on custom tab gets sync'd across all devices in the chain
- [ ] Verify you are able to create a standalone sync chain with one device

## Bravery settings

- [ ] Check that HTTPS Everywhere works by loading http://https-everywhere.badssl.com/
- [ ] Turning HTTPS Everywhere off and shields off both disable the redirect to https://https-everywhere.badssl.com/
- [ ] Check that toggling to blocking and allow ads works as expected
- [ ] Verify that clicking through a cert error in https://badssl.com/ works
- [ ] Visit https://brianbondy.com/ and then turn on script blocking, nothing should load. Allow it from the script blocking UI in the URL bar and it should work.
- [ ] Verify that about:preferences default Bravery settings take effect on pages with no site settings
- [ ] Verify that 3rd party storage results are blank at https://jsfiddle.net/7ke9r14a/7/ when 3rd party cookies are blocked
### Fingerprint Tests
  - [ ] Visit https://browserleaks.com/webrtc, ensure 2 blocked items are listed in shields
  - [ ] Verify that https://diafygi.github.io/webrtc-ips/ doesn't leak IP address when `Block all fingerprinting protection` is on

## Content Tests

- [ ] Go to https://brianbondy.com/ and click on the twitter icon on the top right. Verify that context menus work in the new twitter tab
- [ ] Go to https://trac.torproject.org/projects/tor/login and make sure that the password can be saved. Make sure the saved password is auto-populated when you visit the site again
- [ ] Open a github issue and type some misspellings, make sure they aren't autocorrected
- [ ] Open an email on http://mail.google.com/ or inbox.google.com and click on a link. Make sure it works
- [ ] Verify that https://mixed-script.badssl.com/ shows up as grey not red (no mixed content scripts are run)

## Top sites view

- [ ] Long-press on top sites to get to deletion mode, and delete a top site (note this will stop that site from showing up again on top sites, so you may not want to do this a site you want to keep there)

## Background

- [ ] Start loading a page, background the app, wait > 5 sec, then bring to front, ensure splash screen is not shown


## Session storage

- [ ] Verify that tabs restore when closed, including active tab

## Yet to be implemented

- Check that ad replacement works on http://slashdot.org
- Verify that Safe Browsing works (https://www.raisegame.com/)
- Turning Safe Browsing off and shields off both disable safe browsing for https://www.raisegame.com/
- Verify that turning on fingerprinting protection in about:preferences shows 3 fingerprints blocked at https://jsfiddle.net/bkf50r8v/13/. Verify that turning it off in the Bravery menu shows 0 fingerprints blocked
- Verify that audio fingerprint is blocked at https://audiofingerprint.openwpm.com/ when fingerprinting protection is on
