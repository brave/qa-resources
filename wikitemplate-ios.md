
## Installer

- [ ] Check that installer is close to the size of the last release
- [ ] Check the Brave version in About and make sure it is EXACTLY as expected

## Data

- [ ] Verify that data from the previous build appears in the updated build as expected (bookmarks, etc)
- [ ] Verify that the cookies from the previous build are preserved after upgrade
- [ ] Verify saved password are retained after upgrade
- [ ] Verify stats are retained after upgrade
- [ ] Verify sync chain created in the previous version is still retained on upgrade
- [ ] Verify per-site settings are preserved after upgrade

## Bookmarks

- [ ] Verify that creating a bookmark works
- [ ] Verify that clicking a bookmark from bookmark manager loads the bookmark
- [ ] Verify that deleting a bookmark works
- [ ] Verify that creating a bookmark folder works
- [ ] Verify that creating a bookmark inside the created folder works
- [ ] Verify that you can add a bookmark directly inside a bookmark folder
- [ ] Verify that you can delete a bookmark in edit mode
- [ ] Verify that you can delete a bookmark folder with bookmarks inside
- [ ] Verify adding a bookmark domain, subpaths is retained and you are successfully able to visit the domain subpath in a new tab

## Favourites

- [ ] Verify editing favourite and changing URL updates the favicons accordingly
- [ ] Verify that you can remove favourites
- [ ] Verify that you can add new favourites from the share menu

## Context menus

- [ ] Make sure context menu items in the URL bar work
- [ ] Make sure context menu items on content work with no selected text
- [ ] Make sure context menu items on content work with selected text
- [ ] Make sure context menu items on content work inside an editable control (input, textarea, or contenteditable)
- [ ] Context menu: verify you can Open in Background Tab, and Open in Private Tab

## Downloads

- [ ] Verify that you can save an image from a site
- [ ] Verify that you are able to save a gif image

## Reader Mode

- [ ] Visit http://theverge.com, open any article, verify the reader mode icon is shown in the URL bar
- [ ] Verify tapping on the reader mode icon opens the article in reader mode
- [ ] Edit reader mode settings and open different pages in reader mode and verify if the setting is retained across each article

## Gestures

- [ ] Verify zoom in / out gestures work on https://www.homedepot.com/
- [ ] Verify that navigating to a different origin resets the zoom
- [ ] Swipe back and forward to navigate, verify this works as expected

## Password Managers

- [ ] Verify tapping on 1Password on the slide-out keyboard launches 1Password App and able to select the stored credentials
- [ ] Verify tapping on bitwarden password manager in the autofill field launches the app and auto-fills the stored data

## Shields Settings

- [ ] Enable all switches in settings and visit a site and disable block scripts. Kill and relaunch the app and verify if the site shield settings are retained

## Browser Lock

- [ ] Verify browser lock enables device passcode to be lock/unlock the browser
- [ ] Verify swipe up/swipe down with browser in focus doesn't ask for device passcode
- [ ] Verify cancel passcode shows unlock message
- [ ] Remove the app from memory and relaunch, enter a wrong passcode, the browser should not be unlocked
- [ ] Verify cancel fingerprint confirmation/face unlock shows enter passcode window when fingerprint/face unlock is set up on the device

## Brave Rewards/Ads

- [ ] Verify wallet is auto-created after enabling rewards
- [ ] Verify when you click on the BR panel while on a site, the panel displays if the site is verified or not
- [ ] Verify ads are only shown when the app is being used
- [ ] Verify clicking on an ad notification shows the landing page
- [ ] Verify inline-ads show on Brave News and is correctly redeemed from the server
- [ ] Verify `view`,`clicked` and `landed` and `dismiss` states are logged based on the action

## Sync

- [ ] Verify you are able to join sync chain by scanning the QR code
- [ ] Verify you are able to join sync chain using code words
- [ ] Verify you are able to create a sync chain on the device and add other devices to the chain via QR code/Codewords
- [ ] Verify that bookmarks from other devices on the chain show up on the mobile device after sync completes
- [ ] Verify newly created bookmarks get synced to all devices on the sync chain
- [ ] Verify existing bookmarks before joining sync chain also gets sync'd to all devices on the sync chain
- [ ] Verify history sync is disabled by default. Enabling it starts sync'ing history items as well (limited to 200 entries)
- [ ] Verify sync works on an upgrade profile and new bookmarks added post-upgrade sync's across devices on the chain
- [ ] Verify you can create a standalone sync chain with one device

## Playlist & Autoplay

- [ ] Verify Playlist is enabled by default on a clean install
- [ ] Verify when a site with audio/video is detected, playlist button is shown in URL bar and a notification badge on the menu
- [ ] Verify clicking the playlist button adds audio/video to playlist and initiates offline play
- [ ] Verify able to add audio/video to playlist via share menu
- [ ] Verify able to add audio/video to playlist via long press context menu
- [ ] Verify Autoplay is disabled by default
- [ ] Verify with Autoplay enabled, able to play audio/video automatically
- [ ] Verify with background audio enabled, able to play audio/video with device locked or app in background

## Brave News

- [ ] Verify Brave News opt-in is shown on a clean install
- [ ] Verify once opted-in Brave news starts showing articles
- [ ] Verify promoted content is shown on Brave News
- [ ] Verify in-line ads are shown on Brave News
- [ ] Verify able to add custom RSS feed to the list of sources
- [ ] Verify able to disable content from a particular publisher by long press on the card

## Bravery settings

- [ ] Check that HTTPS Everywhere works by loading http://https-everywhere.badssl.com/
- [ ] Turning HTTPS Everywhere off or shields off both disable the redirect to https://https-everywhere.badssl.com/
- [ ] Check that block ad and unblock ad works on http://slashdot.org
- [ ] Check that toggling to blocking and allow ads works as expected
- [ ] Verify that clicking through a cert error in https://badssl.com/ works
- [ ] Verify that Safe Browsing works (https://www.raisegame.com/)
- [ ] Enable block script globally from settings, Visit https://twitter.com/, nothing should load. Tap on Shields and disable block script, the page should load properly
- [ ] Verify that preferences default Brave Shields settings take effect on pages with no site settings
### Fingerprint Tests
  - [ ] Verify that turning on fingerprinting protection in preferences shows 3 fingerprint blocked at https://browserleaks.com/canvas . Verify that turning it off in the Bravery menu shows 0 fingerprints blocked
  - [ ] Verify that audio fingerprint is blocked at https://audiofingerprint.openwpm.com/ when fingerprinting protection is on
  - [ ] Verify that https://diafygi.github.io/webrtc-ips/ doesn't leak IP address when `Block all fingerprinting protection` is on

## Content tests

- [ ] Go to https://feedly.com/ and make sure that the password can be saved.  Make sure the saved password is auto-populated when you visit the site again
- [ ] Open an email on http://mail.google.com/ or `inbox.google.com` and click on a link. Make sure it works
- [ ] Verify that PDF is loaded over https at https://basicattentiontoken.org/BasicAttentionTokenWhitePaper-4.pdf
- [ ] Verify that PDF is loaded over HTTP at http://www.pdf995.com/samples/pdf.pdf
- [ ] Verify that https://mixed-script.badssl.com/ shows up as grey not red (no mixed content scripts are run)
- [ ] Verify that search results from https://startpage.com/ open in a new tab (due to target being _blank_)

## WebAuthn

- [ ] Verify browser prompts for security key when trying to login to accounts 
- [ ] Verify you are able to successfully authenticate an account using security key when prompted
- [ ] Verify quickly connect and disconnect doesn't cause issue authenticating using security keys
- [ ] Verify you are able to use security keys on both normal and private tabs
- [ ] Verify you are able to use security keys to authenticate using NFC 

## App linker

- [ ] Long press on a link in the Twitter app to get the share picker, choose Brave. Verify Brave doesn't crash after opening the link

## Session storage

- [ ] Verify that tabs restore when closed, including active tab
