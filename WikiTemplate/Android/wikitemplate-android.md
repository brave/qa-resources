
## Installer

- [ ] Verify that the installer is close to the size of the last release
- [ ] Verify that the Brave version is in About and make sure it is EXACTLY as expected

## Startup

- [ ] Verify that Brave is only contacting `*.brave.com` endpoints on first launch using either `Charles Proxy`, `Fiddler` or `Wireshark` (or a similar application)
  - [ ] Verify that opening a NTP doesn't trigger any outbound connections related to widgets without user interaction

## Visual look

- [ ] Verify that thereafter every merge:
  - [ ] No Chrome/Chromium words appear on `brave://version`
  - [ ] No Chrome/Chromium words appear on normal or private tabs
  - [ ] No Chrome/Chromium words appear in site settings for `Location` / `Camera` / `Microphone` / `Augmented Reality`
  - [ ] No Chrome/Chromium icons are shown in normal or private tabs

## Custom tabs

- [ ] Verify that Brave handles links from Gmail, Slack
- [ ] Verify that custom tabs work even with sync enabled/disabled

## Tab Groups

- [ ] Verify that tab-group is disabled by default
- [ ] Verify that tab-group is not reverted back to the default setting when changing it and then restarting the browser

## Developer Tools

- [ ] Verify that you can inspect sub-links via dev tools

## Clear Data

- [ ] Verify that Clear Data on exit works as intended

## Settings and Bottom bar

- [ ] Verify that changing default settings are retained and don't cause the browser to crash
- [ ] Verify that bottom bar buttons (Home/Bookmark/Search/Tabs) work as expected
- [ ] Verify that items in the hamburger menu/share menu to ensure nothing unexpected has been added

## Unstoppable Domains, ENS and SNS

- [ ] Verify that settings for Unstoppable Domains, ENS and SNS show up under Brave Shields & Privacy settings

## Downloads

- [ ] Verify that downloading a file works and that all actions on the download item work.
- [ ] Verify that PDF is downloaded over HTTPS at `https://basicattentiontoken.org/BasicAttentionTokenWhitePaper-4.pdf`
- [ ] Verify that PDF is downloaded over HTTP at `http://www.pdf995.com/samples/pdf.pdf`

## Bravery settings

- [ ] Verify that HTTPS Everywhere works by loading `http://https-everywhere.badssl.com/`
- [ ] Verify that turning HTTPS Everywhere off and shields off both disable the redirect to `https://https-everywhere.badssl.com/`
- [ ] Verify that toggling to blocking and allow ads works as expected
- [ ] Verify that clicking through a cert error in `https://badssl.com/` works
- [ ] Verify that Safe Browsing protection is enabled in `https://testsafebrowsing.appspot.com`
- [ ] Verify that nothing should load by visiting `https://twitter.com/` and then turning on script blocking. Allow it from the script blocking UI in the URL bar and it should work.
- [ ] Verify that default Bravery settings take effect on pages with no site settings
- [ ] Verify that 3rd party storage results are blank at `https://jsfiddle.net/7ke9r14a/7/` when 3rd party cookies are blocked
- [ ] Verify that your ISP's DNS resolvers aren't detected and not shown, but only your chosen DoH provider should appear by choosing a DNS provider from the list in Settings | Privacy | Use Secure DNS and loading `https://browserleaks.com/dns`.
- [ ] Verify that results are as expected per each test listed by running all six test configurations on `https://dev-pages.brave.software/storage/ephemeral-storage.html`
### Fingerprint Tests
  - [ ] Verify that 2 blocked items are listed in shields by visiting `https://browserleaks.com/webrtc`
  - [ ] Verify that `https://diafygi.github.io/webrtc-ips/` doesn't leak the IP address for each option under `Settings -> Privacy and Security -> WebRTC IP handling policy`

### Query Filter

- [ ] Verify that results are as expected per each test listed by visiting `https://fmarier.github.io/brave-testing/query-filter.html` in a Private window and running the tests as directed

## Content Tests

- [ ] Verify that context menus work in the new X (Twitter) tab by going to `https://brianbondy.com/` and tapping on the Twitter icon on the top right
- [ ] Verify that the password can be saved by going to `https://feedly.com` and signing in to the account. Verify that the saved password is auto-populated when you visit the site again
- [ ] Verify that `https://mixed-script.badssl.com/` shows up as grey not red (no mixed content scripts are run)

## Brave Rewards

- [ ] Verify that none of the reward endpoints are being contacted when a user visits a media creator (`youtube.com`, `reddit.com`, `twitter.com`, `github.com`) and hasn't joined rewards
  - [ ] Verify that `rewards.brave.com`, `pcdn.brave.com`, `grant.rewards.brave.com` or `api.rewards.brave.com` are not being contacted
- [ ] Verify that you are able to create a new Rewards profile and you are in the unverified state by default
  - [ ] Verify that when you visit a creator in this state the panel shows a prompt to connect a custodian and no BAT information (earnings, balance, etc) is displayed
  - [ ] Verify that when you visit `brave://rewards` in this state there are no Auto Contribution, Tipping, or summary panels on this page
  - [ ] Verify that you can toggle notification ads off/on from the "Manage Brave Ads" panel on `brave://rewards`
- [ ] Verify that you are able to connect a custodian
  - [ ] Verify that the Rewards balance shows the correct BAT and USD value on brave://rewards and panel after you connect
  - [ ] Verify that when you tap on the BR panel while on a site, the panel displays site-specific information (site favicon, domain, attention %)
  - [ ] Verify that the BR panel shows a message about an unverified creator
  - [ ] Verify that the "Send Contribution" button is grayed out on the panel for an unverified creator and the tip banner cannot be accessed
  - [ ] Verify that the tip banner shows a message about a creator with a different custodian
  - [ ] Verify that you are able to tip a creator who has the same custodian as you
  - [ ] Verify that there is no "Disconnect" option once connected to a custodian
- [ ] Verify that you are able to reset rewards
  - [ ] Verify that after rewards are reset, you are now in the non-opted in state
  - [ ] Verify that you can re-join rewards, the panel and brave://rewards page are now in the unverified state

## Brave Ads

- [ ] Verify that ads are auto-enabled when rewards are enabled for the supported region
- [ ] Verify that ads are only shown when the app is being used
- [ ] Verify that ad notifications are shown based on ads per hour setting
- [ ] Verify that ad notifications stack up in the notification tray
- [ ] Verify that swiping left/right dismisses the ad notification when shown and is not stored in the notification tray
- [ ] Verify that tapping on an ad notification shows the landing page
- [ ] Verify that `view`,`clicked`, `landed` and `dismiss` states are logged based on the action

## Sync

- [ ] Verify that you are able to join the Sync chain by scanning the QR code
- [ ] Verify that you are able to join the Sync chain using code words
- [ ] Verify that you are able to create a Sync chain on the device and add other devices to the chain via QR code/Code words
- [ ] Verify that once the Sync chain is created, `Categories` option is shown in the devices list
- [ ] Verify that only `Bookmarks` is enabled in `Categories` by default
- [ ] Verify that enabling `Sync everything` enables all other switches
- [ ] Verify that existing bookmarks before joining the Sync chain also get synced to all devices on the Sync chain
- [ ] Verify that `Autofill` data is synced to all devices when enabled
- [ ] Verify that `History` is synced to all devices
- [ ] Verify that `Open tab` from other devices shows up under history below the device name
- [ ] Verify that `Password` is synced to all devices
- [ ] Verify that `Settings` syncs site settings on all devices
- [ ] Verify that sync works on an upgrade profile and new bookmarks added post-upgrade syncs across devices on the chain
- [ ] Verify that adding a bookmark on a custom tab gets synced across all devices in the chain
- [ ] Verify that you are able to create a standalone Sync chain with one device
- [ ] Verify that `Remove this device` shows a confirmation alert before removing the sync chain on the device

## Top sites view

- [ ] Verify that you are able to Long-press on Top sites to get to deletion mode, and delete a Top site (note this will stop that site from showing up again on Top sites, so you may not want to do this a site you want to keep there)

## Session storage

- [ ] Verify that tabs restore when closed, including active tab

## Upgrade from previous version

Examples of pre-requisites before upgrading from the previous version to the build being tested:

 * visit several websites so `Top Tiles` under New Tab Page gets updated/populated
 * add several websites to the Android home screen via `Add to Home screen` (from the hamburger/setting menu)
 * add several bookmarks including folders
 * change/update several settings (Example: default search engine, adding a custom home page, changing site settings, changing several privacy settings, etc..)
 * create/enable a Brave Wallet (or restore if an individual who's going through the upgrade has one available)
 * enable Brave News and add/remove several sources
 * change the default shield settings on various websites (Example: enable script blocking/change FP/Ad blocking to strict, disable shields)
 * Login into several websites and leave them opened
 * Login into several websites and close the tabs so they're not opened when upgrading
 * Login into a website and leave it as the active tab while upgrading
 * enable/create a sync chain with several devices

 **`Upgrade Cases`**

- [ ] Verify that `brave://version` displays both the correct Brave version and the expected Chromium version
- [ ] Verify that bookmarks and folders from the previous release have been retained/can be loaded without issues
- [ ] Verify that previously opened tabs are retained and can be lazy loaded without issues
  - [ ] Verify that websites that have been logged into and were opened while upgrading are still logged in (ensure cookies are not cleared/lost)
- [ ] Verify that websites that have been logged into but weren't open when upgrading are still logged in when loading in a new tab (ensure cookies are not cleared/lost)
- [ ] Verify that the correct website loads as the active tab (as per the pre-requisites, this tab should be logged into a website)
- [ ] Verify that the Shields settings from the previous versions are retained on each website
- [ ] Verify that saved passwords are being displayed under `Settings` -> `Passwords` and can be auto-filled without issues
- [ ] Verify that the Sync chain is preserved and that syncing still works across the devices that have been added
  - [ ] Verify that sharing links/tabs using `Send to your device` works as expected
- [ ] Verify that Brave News is still enabled and source changes from the previous release are retained
- [ ] Verify that the various setting changes via  `Settings` are retained (Example: enable script blocking/change FP/Ad blocking to strict, disable shields)
  - [ ] Verify that Unstoppable Domains, ENS and SNS settings are retained from the previous version
- [ ] Verify that `History` is retained from the previous version
- [ ] Verify that the website shortcuts added via `Add to Home screen` are still visible on the Android home screen and tapping on icons loads the appropriate webpage
- [ ] Verify that the `Tab Group` setting doesn't reset/change after upgrading
- [ ] Verify that `Clear data on exit` is retained from the previous version
- [ ] Rewards
  - [ ] Verify that BAT balance is retained
  - [ ] Verify that both Tips and Monthly Contributions are retained
  - [ ] Verify that the Summary panel transactions list is retained
- [ ] Ads
  - [ ] Verify that both `Estimated pending rewards` & `Ad notifications received this month` are retained
  - [ ] Verify that changes to Ads settings are retained
  - [ ] Verify that Ads are not being enabled when upgrading to a new version if they were disabled
  - [ ] Verify that Ads are not being disabled when upgrading to a new version if they were enabled
