
## Installer

- [ ] Check that installer is close to the size of the last release
- [ ] Check the Brave version in About and make sure it is EXACTLY as expected

## Data

- [ ] Make sure that data from the last version appears in the new version OK
- [ ] Test that the previous version's cookies are preserved in the next version
- [ ] Test that saved passwords are retained upon upgrade
- [ ] Verify stats are retained when upgrading from the previous version
- [ ] Verify per-site settings are retained when upgrading from the previous version
- [ ] Verify sync chain created in the previous version is still retained on upgrade

## Bookmarks

- [ ] Test that creating a bookmark works
- [ ] Test that clicking a bookmark from bookmark manager loads the bookmark
- [ ] Test that deleting a bookmark works
- [ ] Test that creating a bookmark folder works
- [ ] Test that creating a bookmark inside the created folder works
- [ ] Test that you can add a bookmark directly inside a bookmark folder
- [ ] Test that you can delete a bookmark in edit mode
- [ ] Test that you can delete a bookmark folder with bookmarks inside
- [ ] Test adding a bookmark domain, subpaths is retained and you are successfully able to visit the domain subpath in a new tab

## Favourites

- [ ] Test editing favourite and changing URL updates the favicons accordingly
- [ ] Test that you can remove favourites
- [ ] Test that you can add new favourites from the share menu

## Context menus

- [ ] Make sure context menu items in the URL bar work
- [ ] Make sure context menu items on content work with no selected text
- [ ] Make sure context menu items on content work with selected text
- [ ] Make sure context menu items on content work inside an editable control (input, textarea, or contenteditable)
- [ ] Context menu: verify you can Open in Background Tab, and Open in Private Tab

## Find on page

- [ ] Verify search box is shown when selected via the share menu
- [ ] Test successful find
- [ ] Test forward and backward find navigation
- [ ] Test failed to find shows 0 results

## Private Mode

- [ ] Create private tab, go to http://google.com, search for 'yumyums', exit private mode, go to http://google.com search box and begin typing 'yumyums' and verify that word is not in the autocomplete list

## Reader Mode
- [ ] Visit http://theverge.com, open any article, verify the reader mode icon is shown in the URL bar
- [ ] Verify tapping on the reader mode icon opens the article in reader mode
- [ ] Edit reader mode settings and open different pages in reader mode and verify if the setting is retained across each article

## History

- [ ] On youtube.com, thestar.com (or any other site using push state nav), navigate the site and verify history is added. Also, note if the progress bar activates and shows progress
- [ ] Settings > Clear Private Data, and clear all. Check only the history is cleared and favourites are retained

## Shields Settings

- [ ] Enable all switches in settings and visit a site and disable block scripts. Kill and relaunch the app and verify if the site shield settings are retained

## Site hacks

- [ ] Test https://www.twitch.tv/adobe sub-page loads a video and you can play it

## Downloads

- [ ] Test that you can save an image from a site
- [ ] Test that you are able to save a gif image

## Fullscreen

- [ ] Test that entering HTML5 fullscreen works. And pressing restore to go back exits full screen. (youtube.com)

## Gestures

- [ ] Verify zoom in / out gestures work on https://www.homedepot.com/
- [ ] Verify that navigating to a different origin resets the zoom
- [ ] Swipe back and forward to navigate, verify this works as expected

## Password Managers

- [ ] Test tapping on 1Password on the slide-out keyboard launches 1Password App and able to select the stored credentials
- [ ] Test tapping on bitwarden password manager in the autofill field launches the app and auto-fills the stored data

## Browser Lock

- [ ] Test enabling browser pin settings asks for pin confirmation followed by reconfirm
- [ ] Test swipe up/swipe down with browser in focus doesn't ask for pin confirmation
- [ ] Test clicking on set pin asks for the pin to unlock before setting a new pin
- [ ] Remove the app from memory and relaunch, enter a wrong pin, the browser should not be unlocked
- [ ] Test cancel fingerprint confirmation shows enter pin window when fingerprint unlock is set up on the device

## Sync

- [ ] Verify you are able to join sync chain by scanning the QR code
- [ ] Verify you are able to join sync chain using code words
- [ ] Verify you are able to create a sync chain on the device and add other devices to the chain via QR code/Codewords
- [ ] Verify that bookmarks from other devices on the chain show up on the mobile device after sync completes
- [ ] Verify newly created bookmarks get synced to all devices on the sync chain
- [ ] Verify existing bookmarks before joining sync chain also gets sync'd to all devices on the sync chain
- [ ] Verify sync works on an upgrade profile and new bookmarks added post-upgrade sync's across devices on the chain
- [ ] Verify you can create a standalone sync chain with one device

## Bravery settings

- [ ] Check that HTTPS Everywhere works by loading http://https-everywhere.badssl.com/
- [ ] Turning HTTPS Everywhere off or shields off both disable the redirect to https://https-everywhere.badssl.com/
- [ ] Check that block ad and unblock ad works on http://slashdot.org
- [ ] Check that toggling to blocking and allow ads works as expected
- [ ] Test that clicking through a cert error in https://badssl.com/ works
- [ ] Test that Safe Browsing works (https://www.raisegame.com/)
- [ ] Turning Safe Browsing off and shields off both disable safe browsing for https://www.raisegame.com/
- [ ] Enable block script globally from settings, Visit https://brianbondy.com/, nothing should load. Tap on Shields and disable block script, the page should load properly
- [ ] Test that preferences default Bravery settings take effect on pages with no site settings
- [ ] Test that 3rd party storage results are blank at https://jsfiddle.net/7ke9r14a/7/ when 3rd party cookies are blocked
### Fingerprint Tests
  - [ ] Test that turning on fingerprinting protection in preferences shows 1 fingerprint blocked at https://browserleaks.com/canvas . Test that turning it off in the Bravery menu shows 0 fingerprints blocked
  - [ ] Test that audio fingerprint is blocked at https://audiofingerprint.openwpm.com/ when fingerprinting protection is on
  - [ ] Test that https://diafygi.github.io/webrtc-ips/ doesn't leak IP address when `Block all fingerprinting protection` is on

## Content tests

- [ ] Go to https://brianbondy.com/ and click on the twitter icon on the top right. Test that context menus work in the new twitter tab
- [ ] Load twitter and click on a tweet so the popup div shows. Click to dismiss and repeat with another div. Make sure it shows
- [ ] Go to https://trac.torproject.org/projects/tor/login and make sure that the password can be saved.  Make sure the saved password is auto-populated when you visit the site again
- [ ] Open an email on http://mail.google.com/ or inbox.google.com and click on a link. Make sure it works
- [ ] Test that PDF is loaded over https at https://basicattentiontoken.org/BasicAttentionTokenWhitePaper-4.pdf
- [ ] Test that PDF is loaded over HTTP at http://www.pdf995.com/samples/pdf.pdf
- [ ] Test that https://mixed-script.badssl.com/ shows up as grey not red (no mixed content scripts are run)
- [ ] Test that search results from https://startpage.com/ open in a new tab (due to target being _blank_)

## App linker

- [ ] Long press on a link in the Twitter app to get the share picker, choose Brave. Verify Brave doesn't crash after opening the link

## Background

- [ ] Start loading a page, background the app, wait >5 sec, then bring to front, Verify splash screen is not shown

## Session storage

- [ ] Test that tabs restore when closed, including active tab