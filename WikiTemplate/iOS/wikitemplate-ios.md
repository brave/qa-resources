
## Installer

- [ ] Check that installer is close to the size of the last release
- [ ] Check the Brave version in About and make sure it is EXACTLY as expected

## Data

- [ ] Verify that data from the previous build appears in the updated build as expected (bookmarks, history, etc.)
- [ ] Verify that cookies from the previous build are preserved after upgrade
- [ ] Verify saved passwords are retained after upgrade
- [ ] Verify stats are retained after upgrade
- [ ] Verify sync chain created in the previous version is still retained on upgrade
- [ ] Verify per-site settings are preserved after upgrade

## Bookmarks

- [ ] Verify that creating a bookmark works
- [ ] Verify that tapping a bookmark from bookmark manager loads the bookmark
- [ ] Verify that deleting a bookmark works
- [ ] Verify that creating a bookmark folder works
- [ ] Verify that creating a bookmark inside the created folder works
- [ ] Verify that you can add a bookmark directly inside a bookmark folder
- [ ] Verify that you can delete a bookmark in edit mode
- [ ] Verify that you can delete a bookmark folder with bookmarks inside
- [ ] Verify adding a bookmark domain, subpaths is retained and you are successfully able to visit the domain subpath in a new tab
- [ ] Verify adding bookmark for many open tabs works
- [ ] Verify import/export bookmarks works

## Favourites

- [ ] Verify editing favourites and changing their URLs updates the favicons accordingly
- [ ] Verify that you can remove favourites
- [ ] Verify that you can add new favourites from the `Share with...` menu
- [ ] Verify adding Favorites Widget to home screen and ensured favorites are updated

## Context menus

- [ ] Make sure context menu items in the URL bar work
- [ ] Make sure context menu items on content work with no selected text
- [ ] Make sure context menu items on content work with selected text
- [ ] Make sure context menu items on content work inside an editable control (input, textarea, or contenteditable)
- [ ] Verify you can open links in a new tab or private tab. Ensure you can open links in background tabs
- [ ] Verify all actions work in context menu when long pressing on `+` in the tool bar
- [ ] Verify all actions work in context menu when long pressing on tab icon
- [ ] Verify `Recently Closed Tabs` is opened when long pressing `+` icon in tab view

## Navigation

- [ ] Verify search works from the search box on NTP
- [ ] Verify searching using voice search icon
- [ ] Verify changing search engine in settings will update search queries for regular and private tabs
- [ ] Verify tapping on arrow icon for the suggested searches will only populate that search query in the search box
- [ ] Verify scanning QR Code from the search box will higlight scanned url
- [ ] Verify all actions in tool bar using Top Bar mode
- [ ] Verify searching page content using `Find in Page`
- [ ] Verify certificate viewer works in url bar
- [ ] Verify navigating social media and video sites does not cause loading issues when scrolling or reloading pages.
      
## Downloads

- [ ] Verify that you can save an image from a site
- [ ] Verify that you are able to save a GIF image

## Reader Mode

- [ ] Visit `http://theverge.com`, open any article, verify the reader mode icon is shown in the URL bar
- [ ] Verify tapping on the reader mode icon opens the article in reader mode
- [ ] Edit reader mode settings and open different pages in reader mode and verify if the setting is retained across each article
- [ ] Verify reader mode works with Top bar enabled

## Gestures

- [ ] Verify pinch to zoom in/out gestures work on `https://www.homedepot.com`
- [ ] Verify that navigating to a different origin resets the zoom
- [ ] Swipe back and forward to navigate, verify this works as expected

## Password Managers

- [ ] Verify tapping on 1Password on the slide-out keyboard launches 1Password app and you're able to select the stored credentials
- [ ] Verify tapping on Bitwarden password manager in the autofill field launches the app and auto-fills the stored data

## Shields Settings

- [ ] Enable all switches in `Settings` and visit a site and disable `Block Scripts`. Kill and relaunch the app and verify if the site Shields settings are retained

## Browser Lock

- [ ] Verify browser lock enables device passcode to lock/unlock the browser
- [ ] Verify swipe up/swipe down with browser in focus doesn't ask for device passcode
- [ ] Verify cancel passcode shows unlock message
- [ ] Remove the app from memory and relaunch, enter a wrong passcode, the browser should not be unlocked
- [ ] Verify cancel fingerprint confirmation/face unlock shows enter passcode window when fingerprint/face unlock is set up on the device

## Brave Rewards/Ads

- [ ] Verify wallet is auto-created after enabling Rewards
- [ ] Verify when you click on the Brave Rewards panel while on a site, the panel displays if the site is verified or not
- [ ] Verify ads are only shown while the app is being used
- [ ] Verify tapping on an ad notification shows the landing page
- [ ] Verify inline-content ads show on Brave News and are correctly redeemed from the server
- [ ] Verify `view`, `clicked`, `landed`, `dismiss`, and `downvote` confirmation states are logged based on the action. Ensured these are working for inline ads, ad notifications and NTP-SI Images.

## Sync

- [ ] Verify you are able to join Sync chain by scanning the QR code
- [ ] Verify you are able to join Sync chain using code words
- [ ] Verify you are able to create a Sync chain on the device and add other devices to the chain via QR code/code words
- [ ] Verify that bookmarks from other devices on the chain show up on the mobile device after sync completes
- [ ] Verify newly created bookmarks get synced to all devices on the Sync chain
- [ ] Verify existing bookmarks before joining Sync chain also gets sync'd to all devices on the Sync chain
- [ ] Verify history sync is disabled by default. Enabling it starts sync'ing history items as well (limited to 200 entries)
- [ ] Verify sync works on an upgraded profile and new bookmarks added post-upgrade sync across devices on the chain
- [ ] Verify you can create a standalone Sync chain with one device
- [ ] Verify starting sync chain using Other Devices segmented tab. Ensured enabling `open tabs` will display tabs from other devices
- [ ] Verify sharing pages with `Send To Your Devices`
- [ ] Verify `Sync Internals` page data is populated when connected to sync chain
- [ ] Verify when using `Delete Sync Account` will remove all devices from sync chain

## Playlist & Autoplay

- [ ] Verify Playlist is enabled by default on a clean install
- [ ] Verify when a site with audio/video is detected, `Playlist` button is shown in URL bar and a notification badge on the menu
- [ ] Verify clicking the `Playlist` button adds audio/video to playlist and initiates offline play
- [ ] Verify adding audio/video to playlist via share menu
- [ ] Verify adding audio/video to playlist via long press context menu
- [ ] Verify Autoplay is enabled by default
- [ ] Verify with Autoplay enabled, able to play audio/video automatically
- [ ] Verify with background audio enabled, able to play audio/video with device locked or app in background
- [ ] Verify Playlist media works with CarPlay on iOS devices
- [ ] Verify playback gestures are working in Playlist
- [ ] Verify adding shared folder to playlist using `https://playlist.brave.com/bsa-sample`. Verify all actions on shared folder are working

## Brave News

- [ ] Verify Brave News opt-in is shown on a clean install
- [ ] Verify once opted-in Brave News starts showing articles
- [ ] Verify inline-content ads are shown on Brave News
- [ ] Verify able to add custom RSS feed to the list of sources. Ensure this is working when entering custom URL manually and through the share menu when at a blog page
- [ ] Verify able to hide content from sources within the `Popular Sources` and `Suggested` categories by long-press on the card
- [ ] Verify adding Top News Brave widget to home screen will display news articles. Ensure tapping on news articles will load in brave.

## VPN

- [ ] Verify purchasing VPN subscription will install VPN profile and establish connection
- [ ] Verify tunneling works by navigating to `https://ipinfo.io`
- [ ] Verify changing server region will update VPN connection
- [ ] Verify changing protocol from WireGuard to IKEv2
- [ ] Verify `Reset Configuration` will not change the region 

## Bravery settings

- [ ] Check that block ad and unblock ad works on `http://slashdot.org`
- [ ] Check that toggling to blocking and allow ads works as expected. Ensure pre-roll ads are removed on `youtube.com`
- [ ] Verify that tapping through a cert error in `https://badssl.com` works
- [ ] Verify Safe Browsing protection on `https://testsafebrowsing.appspot.com/` in the iOS
- [ ] Verify debounce/deAMP settings using `https://dev-pages.brave.software/navigation-tracking/debouncing.html`
- [ ] Verify Block Cookie Consent Notices works when navigating to `https://amazon.co.uk`
- [ ] Verify switch to app dialogs are suppressed when loading `reddit.com`, `twitter.com` and `google.com/maps`
- [ ] Enable `Block Scripts` globally from `Settings`.  Visit `https://blizzard.com` and confirm the carousel is disabled at the top of the page. Tap on `Shields` and disable `Block Scripts`; the page content should load properly
- [ ] Verify that default Brave Shields settings take effect on pages with no site settings

### Fingerprint Tests

- [ ] Verify that the audio fingerprint is blocked at `https://audiofingerprint.openwpm.com` when fingerprinting protection is on
- [ ] Verify that `https://diafygi.github.io/webrtc-ips/` doesn't leak IP address when `Block all fingerprinting protection` is on
- [ ] Verify fingerprinting test cases in `https://dev-pages.brave.software/fingerprinting/farbling.html`

## Content tests

- [ ] Go to `https://feedly.com` and make sure that the password can be saved.  Make sure the saved password is auto-populated when you visit the site again.
- [ ] Open an email on `https://mail.google.com` and tap on a link. Make sure it works.
- [ ] Verify that PDF is loaded over `HTTPS` at `https://basicattentiontoken.org/BasicAttentionTokenWhitePaper-4.pdf`
- [ ] Verify that PDF is loaded over `HTTP` at `http://www.pdf995.com/samples/pdf.pdf`
- [ ] Verify that `https://mixed-script.badssl.com` shows up as grey, not red (no mixed-content scripts are run)
- [ ] Verify that search results from `https://startpage.com` open in a new tab (due to target being _blank_)

## WebAuthn

- [ ] Verify browser prompts for security key when trying to log in to accounts 
- [ ] Verify you are able to successfully authenticate an account using security key when prompted
- [ ] Verify quickly connecting and disconnecting doesn't cause issues authenticating using security keys
- [ ] Verify you are able to use security keys on both normal and private tabs
- [ ] Verify you are able to use security keys to authenticate using NFC 

## App linker

- [ ] Long-press on a link in the Twitter app to get the share picker, choose Brave. Verify Brave doesn't crash after opening the link.

## Session storage

- [ ] Verify that tabs restore when closed, including active tab

## Navigation [iPad]

- [ ] Verify user is able to navigate/search using connected hardware keyboard
- [ ] Verify long pressing CMD key will display keyboard shortcuts
- [ ] Ensure the keyboard shortcuts are working
- [ ] Ensure using Brave with `Split View` & `Split Over` works with other apps
