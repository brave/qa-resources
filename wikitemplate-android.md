
## Installer

- [ ] Check that installer is close to the size of the last release
- [ ] Check the Brave version in About and make sure it is EXACTLY as expected

## Startup

- [ ] Verify that Brave is only contacting `*.brave.com` endpoints on first launch using either `Charles Proxy`, `Fiddler` or `Wireshark` (or a similar application)

## Visual look

- [ ] Make sure thereafter every merge
  - [ ] No Chrome/Chromium words appear on `brave://version`
  - [ ] No Chrome/Chromium words appear on normal or private tabs
  - [ ] No Chrome/Chromium words appear in site settings for `Location` / `Camera` / `Microphone` / `Augmented Reality`
  - [ ] No Chrome/Chromium icons are shown in normal or private tabs

## Data
Pre-Requisite: Put previous build shortcut on the home screen. Also, have several sites 'Added to home screen' (from 3 dots menu) and then upgrade to new build
- [ ] Verify that data from the previous build appears in the updated build as expected (bookmarks, etc)
- [ ] Verify that the cookies from the previous build are preserved after upgrade
- [ ] Verify shortcut is still available on the home screen after upgrade
- [ ] Verify sites added to home screen are still visible and able to be used after upgrade
- [ ] Verify sync chain created in the previous version is still retained on upgrade
- [ ] Verify settings changes done in the previous version are still retained on upgrade
- [ ] Verify IPFS, ENS & Unstoppable Domain settings is retained after upgrade
- [ ] Verify tab-group setting doesn't reset upon upgrade
- [ ] Verify Clear Data on exit setting state from previous build is retained upon upgrade

## Custom tabs

- [ ] Make sure Brave handles links from Gmail, Slack
- [ ] Ensure custom tabs work even with sync enabled/disabled

## Tab Groups

- [ ] Ensure tab-group is enabled by default
- [ ] Verify toggling tab-group setting triggers a relaunch request
- [ ] Verify tab-group is not reverted back to default setting after browser restart

## Developer Tools

- [ ] Verify you can inspect sub-links via dev tools

## Clear Data

- [ ] Verify Clear Data on exit works as intended

## Settings and Bottom bar

- [ ] Verify changing default settings are retained and don't cause the browser to crash
- [ ] Verify bottom bar buttons (Home/Bookmark/Search/Tabs) work as expected

## IPFS, ENS & Unstoppable Domain

- [ ] Verify settings for IPFS, ENS & Unstoppable Domain show up under Brave Shields & Privacy settings

## Downloads

- [ ] Verify downloading a file works and that all actions on the download item work.
- [ ] Verify that PDF is downloaded over HTTPS at `https://basicattentiontoken.org/BasicAttentionTokenWhitePaper-4.pdf`
- [ ] Verify that PDF is downloaded over HTTP at `http://www.pdf995.com/samples/pdf.pdf`

## Bravery settings

- [ ] Check that HTTPS Everywhere works by loading `http://https-everywhere.badssl.com/`
- [ ] Turning HTTPS Everywhere off and shields off both disable the redirect to `https://https-everywhere.badssl.com/`
- [ ] Check that toggling to blocking and allow ads works as expected
- [ ] Verify that clicking through a cert error in `https://badssl.com/` works
- [ ] Visit `https://brianbondy.com/` and then turn on script blocking, nothing should load. Allow it from the script blocking UI in the URL bar and it should work.
- [ ] Verify that default Bravery settings take effect on pages with no site settings
- [ ] Verify that 3rd party storage results are blank at `https://jsfiddle.net/7ke9r14a/7/` when 3rd party cookies are blocked
- [ ] Choose a DNS provider from the list in Settings | Privacy | Use Secure DNS, load `https://browserleaks.com/dns`, and verify your ISP's DNS resolvers aren't detected and shown; only your chosen DoH provider should appear.
- [ ] Run all six test configurations on `https://dev-pages.brave.software/storage/ephemeral-storage.html` and confirm results are as expected per each test listed.
### Fingerprint Tests
  - [ ] Visit `https://browserleaks.com/webrtc`, ensure 2 blocked items are listed in shields
  - [ ] Verify that `https://diafygi.github.io/webrtc-ips/` doesn't leak IP address when `Block all fingerprinting protection` is on

## Content Tests

- [ ] Go to `https://brianbondy.com/` and click on the twitter icon on the top right. Verify that context menus work in the new twitter tab
- [ ] Go to `https://trac.torproject.org/projects/tor/login` and make sure that the password can be saved. Make sure the saved password is auto-populated when you visit the site again
- [ ] Open a GitHub issue and type some misspellings, make sure they aren't autocorrected
- [ ] Open an email on `http://mail.google.com/` or inbox.google.com and click on a link. Make sure it works
- [ ] Verify that `https://mixed-script.badssl.com/` shows up as grey not red (no mixed content scripts are run)

## Brave Rewards/Ads

- [ ] Verify wallet is auto-created after enabling rewards(either via Panel or Rewards page)
- [ ] Verify account balance shows correct BAT and USD value
- [ ] Verify actions taken (claiming grant, tipping, auto-contribute) display in wallet panel
- [ ] Verify grant details are shown in expanded view when a grant is claimed
- [ ] Verify monthly budget shows correct BAT and USD value
- [ ] Verify you can exclude a publisher from the auto-contribute table by clicking on the trash bin icon in the auto-contribute table
- [ ] Verify you can exclude a publisher by using the toggle on the Rewards Panel
- [ ] Verify you can remove excluded sites via `Restore All` button
- [ ] Verify when you click on the BR panel while on a site, the panel displays site-specific information (site favicon, domain, attention %)
- [ ] Verify when you click on `Send a tip`, the custom tip banner displays
- [ ] Verify you can make a one-time tip and they display in tips panel
- [ ] Verify you can make a recurring tip and they display in tips panel
- [ ] Verify you can tip a verified publisher
- [ ] Verify you can tip a verified YouTube creator
- [ ] Verify tip panel shows a verified check mark for a verified publisher/verified YouTube creator
- [ ] Verify tip panel shows a message about the unverified publisher
- [ ] Verify BR panel shows the message about an unverified publisher
- [ ] Verify you can perform a contribution
- [ ] Verify if you disable auto-contribute you are still able to tip regular sites and YouTube creators
- [ ] Verify that disabling Rewards and enabling it again does not lose state
- [ ] Verify that disabling auto-contribute and enabling it again does not lose state
- [ ] Verify unchecking `Allow contribution to videos` option doesn't list any YouTube creator in ac list
- [ ] Adjust min visit/time in settings. Visit some sites and YouTube channels to verify they are added to the table after the specified settings
- [ ] Verify you can reset rewards from advance setting. Resetting should delete wallet and bring it back to the pre-optin state
- [ ] Verify on BR panel `Verify wallet` button loads verify wallet page when balance in >=15 BAT. 
- [ ] Verify user still able to connect to existing Uphold account via panel even when balance is < 15 BAT
- [ ] Verify you are able to disconnect/re-connect a user wallet when min balance is available
- [ ] Upgrade from an older version
  - [ ] Verify the wallet balance (if available) is retained
  - [ ] Verify auto-contribute list is not lost after upgrade
  - [ ] Verify tips list is not lost after upgrade
  - [ ] Verify wallet panel transactions list is not lost after upgrade
### Brave Ads
- [ ] Verify ads is auto-enabled when rewards is enabled for the supported region
- [ ] Verify ads are only shown when the app is being used
- [ ] Verify ad notification are shown based on ads per hour setting
- [ ] Verify ad notifications stack up in notification tray
- [ ] Verify swipe left/right dismisses the ad notification when shown and is not stored in the notification tray
- [ ] Verify clicking on an ad notification shows the landing page
- [ ] Verify `view`,`clicked` and `landed` and `dismiss` states are logged based on the action

## Sync

- [ ] Verify you are able to join sync chain by scanning the QR code
- [ ] Verify you are able to join sync chain using code words
- [ ] Verify you are able to create a sync chain on the device and add other devices to the chain via QR code/Code words
- [ ] Verify once sync chain is created, `Categories` option is shown in devices list
- [ ] Verify only `Bookmarks` is enabled in `Categories` by default
- [ ] Verify enabling `Sync everything` enables all other switches
- [ ] Verify existing bookmarks before joining sync chain also gets sync'd to all devices on the sync chain
- [ ] Verify `Autofill` data is sync'd to all devices when enabled
- [ ] Verify `History` is sync'd to all devices
- [ ] Verify `Open tab` form other devices shows up under history below the device name
- [ ] Verify `Password` is sync'd to all devices
- [ ] Verify `Settings` sync's site settings on all devices
- [ ] Verify sync works on an upgrade profile and new bookmarks added post-upgrade sync's across devices on the chain
- [ ] Verify adding a bookmark on custom tab gets sync'd across all devices in the chain
- [ ] Verify you are able to create a standalone sync chain with one device
- [ ] Verify `Remove this device` shows a confirmation alert before removing the sync chain on the device

## Top sites view

- [ ] Long-press on top sites to get to deletion mode, and delete a top site (note this will stop that site from showing up again on top sites, so you may not want to do this a site you want to keep there)

## Session storage

- [ ] Verify that tabs restore when closed, including active tab
