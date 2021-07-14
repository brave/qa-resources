
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

## Find on page

- [ ] Verify search box is shown when selected via the share menu
- [ ] Verify successful find
- [ ] Verify forward and backward find navigation
- [ ] Verify failed to find shows 0 results

## Private Mode

- [ ] Create private tab, go to http://google.com, search for 'yumyums', exit private mode, go to http://google.com search box and begin typing 'yumyums' and verify that word is not in the autocomplete list
- [ ] Verify enabling `Private Browsing Only` shows warn message about sessions being lost in normal mode
- [ ] Verify switching from `Private Browsing Only` to normal mode doesn't retain any sessions from before

## Reader Mode

- [ ] Visit http://theverge.com, open any article, verify the reader mode icon is shown in the URL bar
- [ ] Verify tapping on the reader mode icon opens the article in reader mode
- [ ] Edit reader mode settings and open different pages in reader mode and verify if the setting is retained across each article

## History

- [ ] On youtube.com, thestar.com (or any other site using push state nav), navigate the site and verify history is added. Also, note if the progress bar activates and shows progress
- [ ] Settings > Brave Shields & Privacy > Clear Private Data, and clear all. Check only the history is cleared and favourites are retained

## Shields Settings

- [ ] Enable all switches in settings and visit a site and disable block scripts. Kill and relaunch the app and verify if the site shield settings are retained

## Site hacks

- [ ] Verify https://www.twitch.tv/adobe sub-page loads a video and you can play it

## Downloads

- [ ] Verify that you can save an image from a site
- [ ] Verify that you are able to save a gif image

## Fullscreen

- [ ] Verify that entering HTML5 fullscreen works. And pressing restore to go back exits full screen. (youtube.com)

## Gestures

- [ ] Verify zoom in / out gestures work on https://www.homedepot.com/
- [ ] Verify that navigating to a different origin resets the zoom
- [ ] Swipe back and forward to navigate, verify this works as expected

## Password Managers

- [ ] Verify tapping on 1Password on the slide-out keyboard launches 1Password App and able to select the stored credentials
- [ ] Verify tapping on bitwarden password manager in the autofill field launches the app and auto-fills the stored data

## Browser Lock

- [ ] Verify enabling browser passcode settings asks for passcode confirmation followed by reconfirm
- [ ] Verify swipe up/swipe down with browser in focus doesn't ask for passcode confirmation
- [ ] Verify clicking on set passcode asks for the pin to unlock before setting a new passcode
- [ ] Remove the app from memory and relaunch, enter a wrong passcode, the browser should not be unlocked
- [ ] Verify cancel fingerprint confirmation shows enter passcode window when fingerprint unlock is set up on the device

## Brave Rewards/Ads

- [ ] Verify wallet is auto-created after enabling rewards
- [ ] Verify account balance shows correct BAT and USD value
- [ ] Verify actions taken (claiming grant, tipping, auto-contribute) display in wallet panel
- [ ] Verify grant details are shown in detailed view when a grant is claimed
- [ ] Verify monthly budget shows correct BAT and USD value
- [ ] Verify you can exclude a publisher from the auto-contribute table via left swipe
- [ ] Verify you can exclude a publisher by using the toggle on the Rewards Panel
- [ ] Verify you can remove excluded sites via `Restore All` button
- [ ] Verify when you click on the BR panel while on a site, the panel displays site-specific information (site favicon, domain, attention %)
- [ ] Verify when you click on `Send a tip`, the custom tip banner displays
- [ ] Verify you can make a one-time tip and they display in tips panel
- [ ] Verify you can make a recurring tip and they display in tips panel
- [ ] Verify you can tip a verified publisher
- [ ] Verify you can tip a verified YouTube/Twitter/GitHub/Reddit creator
- [ ] Verify tip panel shows a verified checkmark for a verified publisher/verified YouTube/Twitter/GitHub/Reddit creator
- [ ] Verify tip panel shows a message about the unverified publisher
- [ ] Verify BR panel shows the message about an unverified publisher
- [ ] Verify you can perform a contribution
- [ ] Verify if you disable auto-contribute you are still able to tip regular sites and YouTube/Twitter/Github creators
- [ ] Verify that disabling Rewards and enabling it again does not lose state
- [ ] Verify that disabling auto-contribute and enabling it again does not lose state
- [ ] Verify disabling `Allow contribution to videos` option doesn't list any YouTube creator in ac list
- [ ] Adjust min page time/visit in settings. Visit some sites and YouTube channels to verify they are added to the table after the specified settings
- [ ] Verify you can `Hide Brave Rewards Icon` works and doesn't show rewards button when not enabled
- [ ] Upgrade from an older version
  - [ ] Verify the wallet balance (if available) is retained
  - [ ] Verify auto-contribute list is not lost after upgrade
  - [ ] Verify tips list is not lost after upgrade
  - [ ] Verify wallet panel transactions list is not lost after upgrade
### Brave Ads
- [ ] Verify ads is auto-enabled when rewards is enabled for the supported region
- [ ] Verify ads are only shown when the app is being used
- [ ] Verify ad notification are shown based on ads per hour setting
- [ ] Verify clicking on an ad notification shows the landing page
- [ ] Verify `view`,`clicked` and `landed` and `dismiss` states are logged based on the action

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
- [ ] Verify that clicking through a cert error in https://badssl.com/ works
- [ ] Verify that Safe Browsing works (https://www.raisegame.com/)
- [ ] Turning Safe Browsing off and shields off both disable safe browsing for https://www.raisegame.com/
- [ ] Enable block script globally from settings, Visit https://blizzard.com/, nothing should load. Tap on Shields and disable block script, the page should load properly
- [ ] Verify that preferences default Bravery settings take effect on pages with no site settings
- [ ] Verify that 3rd party storage results are blank at https://jsfiddle.net/7ke9r14a/7/ when 3rd party cookies are blocked
### Fingerprint Tests
  - [ ] Verify that turning on fingerprinting protection in preferences shows 1 fingerprint blocked at https://browserleaks.com/canvas . Verify that turning it off in the Bravery menu shows 0 fingerprints blocked
  - [ ] Verify that audio fingerprint is blocked at https://audiofingerprint.openwpm.com/ when fingerprinting protection is on
  - [ ] Verify that https://diafygi.github.io/webrtc-ips/ doesn't leak IP address when `Block all fingerprinting protection` is on

## Content tests

- [ ] Go to https://brianbondy.com/ and click on the twitter icon on the top right. Verify that context menus work in the new twitter tab
- [ ] Load twitter and click on a tweet so the popup div shows. Click to dismiss and repeat with another div. Make sure it shows
- [ ] Go to https://trac.torproject.org/projects/tor/login and make sure that the password can be saved.  Make sure the saved password is auto-populated when you visit the site again
- [ ] Open an email on http://mail.google.com/ or inbox.google.com and click on a link. Make sure it works
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

## Background

- [ ] Start loading a page, background the app, wait >5 sec, then bring to front, Verify splash screen is not shown

## Session storage

- [ ] Verify that tabs restore when closed, including active tab
