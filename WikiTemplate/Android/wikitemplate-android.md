
## Installer

- [ ] Check that installer is close to the size of the last release
- [ ] Check the Brave version in About and make sure it is EXACTLY as expected

## Startup

- [ ] Verify that Brave is only contacting `*.brave.com` endpoints on first launch using either `Charles Proxy`, `Fiddler` or `Wireshark` (or a similar application)
  - [ ] Verify that opening a NTP doesn't trigger any outbound connections related to widgets without user interaction

## Visual look

- [ ] Make sure thereafter every merge
  - [ ] No Chrome/Chromium words appear on `brave://version`
  - [ ] No Chrome/Chromium words appear on normal or private tabs
  - [ ] No Chrome/Chromium words appear in site settings for `Location` / `Camera` / `Microphone` / `Augmented Reality`
  - [ ] No Chrome/Chromium icons are shown in normal or private tabs

## Custom tabs

- [ ] Make sure Brave handles links from Gmail, Slack
- [ ] Ensure custom tabs work even with sync enabled/disabled

## Tab Groups

- [ ] Ensure tab-group is enabled by default
- [ ] Verify toggling tab-group setting doesn't trigger a relaunch request
- [ ] Verify tab-group is not reverted back to default setting after browser restart

## Developer Tools

- [ ] Verify you can inspect sub-links via dev tools

## Clear Data

- [ ] Verify Clear Data on exit works as intended

## Settings and Bottom bar

- [ ] Verify changing default settings are retained and don't cause the browser to crash
- [ ] Verify bottom bar buttons (Home/Bookmark/Search/Tabs) work as expected
- [ ] Verify items in hamburger menu/share menu to ensure nothing unexpected has been added

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
- [ ] Visit `https://twitter.com/` and then turn on script blocking, nothing should load. Allow it from the script blocking UI in the URL bar and it should work.
- [ ] Verify that default Bravery settings take effect on pages with no site settings
- [ ] Verify that 3rd party storage results are blank at `https://jsfiddle.net/7ke9r14a/7/` when 3rd party cookies are blocked
- [ ] Choose a DNS provider from the list in Settings | Privacy | Use Secure DNS, load `https://browserleaks.com/dns`, and verify your ISP's DNS resolvers aren't detected and shown; only your chosen DoH provider should appear.
- [ ] Run all six test configurations on `https://dev-pages.brave.software/storage/ephemeral-storage.html` and confirm results are as expected per each test listed.
### Fingerprint Tests
  - [ ] Visit `https://browserleaks.com/webrtc`, ensure 2 blocked items are listed in shields
  - [ ] Test that `https://diafygi.github.io/webrtc-ips/` doesn't leak IP address for each option under `Settings -> Privacy and Security -> WebRTC IP handling policy`

### Query Filter

- [ ] Visit https://fmarier.github.io/brave-testing/query-filter.html in a Private window and run the tests as directed

## Content Tests

- [ ] Go to `https://brianbondy.com/` and click on the twitter icon on the top right. Verify that context menus work in the new twitter tab
- [ ] Go to `https://feedly.com` and make sure that the password can be saved. Make sure the saved password is auto-populated when you visit the site again
- [ ] Verify that `https://mixed-script.badssl.com/` shows up as grey not red (no mixed content scripts are run)

## Brave Rewards

- [ ] Verify that none of the reward endpoints are being contacted when a user visits a media creator (`youtube.com`, `reddit.com`, `twitter.com`, `github.com`) and hasn't joined rewards
  - [ ] Verify that `rewards.brave.com`, `pcdn.brave.com`, `grant.rewards.brave.com` or `api.rewards.brave.com` are not being contacted
- [ ] Verify you are able to create a new Rewards profile and are in the unverified state by default
  - [ ] Verify when you visit a creator in this state the panel shows a prompt to connect a custodian and no BAT information (earnings, balance, etc) is displayed
  - [ ] Verify when you visit brave://rewards in this state there are no Auto Contribution, Tipping, or summary panels on this page
  - [ ] Verify you can toggle notification ads off/on from the "Manage Brave Ads" panel on brave://rewards
- [ ] Verify you are able to connect a custodian
  - [ ] Verify Rewards balance shows correct BAT and USD value on brave://rewards and panel after you connect
  - [ ] Verify when you click on the BR panel while on a site, the panel displays site-specific information (site favicon, domain, attention %)
  - [ ] Verify BR panel shows message about an unverified creator
  - [ ] Verify "Send Contribution" button is grayed out on the panel for an unverified creator and the tip banner cannot be accessed
  - [ ] Verify tip banner shows message about a creator with a different custodian
  - [ ] Verify you are able to tip a creator who has the same custodian as you
  - [ ] Verify you are able to perform an auto contribution
  - [ ] Verify if you disable auto-contribute you are still able to tip creators
  - [ ] Verify if auto-contribute is disabled AC does not occur
  - [ ] Verify that there is no "Disconnect" option once connected to a custodian
- [ ] Verify that you are able to reset rewards
  - [ ] Verify that after rewards are reset, you are now in the non-opted in state
  - [ ] Verify you can re-join rewards, the panel and brave://rewards page are now in the unverified state

## Brave Ads

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

## Upgrade from previous version

Examples of pre-requisites before upgrading from previous version to the build being tested:

 * visit several websites so `Top Tiles` under New Tab Page get updated/populated
 * add several websites to the Android home screen via `Add to Home screen` (from the hamburger/setting menu)
 * add several bookmarks include folders
 * change/update several settings (Example: default search engine, adding a custom home page, changing site settings, changing several privacy settings etc..)
 * create/enable a Brave Wallet (or restore if individual who's going through the upgrade has one available)
 * enable Brave News and add/remove several sources
 * change the default shield settings on varios websites (Example: enable script blocking/change FP/Ad blocking to strict, disable shields)
 * Login into several websites and leave them opened
 * Login into several websites and close the tabs so they're not opened when upgrading
 * Login into a website and leave it as the active tab while upgrading
 * enable/create a sync chain with several devices

 **`Upgrade Cases`**

- [ ] Ensure that `brave://version` displays both the correct Brave version and expected Chromium version
- [ ] Ensure that bookmarks and folders from the previous release have been retained/can be loaded without issues
- [ ] Ensure that previously opened tabs are retained and can be lazy loaded with out issues
  - [ ] Ensure that websites that have been logged into and were opened while upgrading are still logged in (ensure cookies are not cleared/lost)
- [ ] Ensure that websites that have been logged into but weren't open when upgrading are still logged in when loading in new tab (ensure cookies are not cleared/lost)
- [ ] Ensure that the correct website loads as the active tab (as per the pre-requisites, this tab should be logged into a website)
- [ ] Ensure that the shields settings from the previous versions are retained on each website
- [ ] Ensure that saved passwords are being displayed under `Settings` -> `Passwords` and can be autofilled without issues
- [ ] Ensure that the sync chain is preserved and syncing still works across the devices that have been added
  - [ ] Ensure that sharing a links/tabs using `Send to your device` works as expected
- [ ] Ensure that Brave News is still enabled and the sources changes from the previous release are retained
- [ ] Ensure that the various setting changes via  `Settings` are retained (Example: enable script blocking/change FP/Ad blocking to strict, disable shields)
  - [ ] Ensure that IPFS, ENS and Unstoppable Domain settings are retained from the previous version
- [ ] Ensure that `History` is retained from the previous version
- [ ] Ensure that the website shortcuts added via `Add to Home screen` are still visible on the Android home screen and tapping on icons loads the appropriate webpage
- [ ] Ensure that the `Tab Group` setting doesn't reset/change after upgrading
- [ ] Ensure that `Clear data on exit` is retained from the previous version
- [ ] Rewards
  - [ ] BAT balance is retained
  - [ ] Auto-contribute list is retained
  - [ ] Both Tips and Monthly Contributions are retained
  - [ ] Summary panel transactions list is retained
  - [ ] Changes to rewards settings are retained
- [ ] Ads
  - [ ] Both `Estimated pending rewards` & `Ad notifications received this month` are retained
  - [ ] Changes to ads settings are retained
  - [ ] Ensure that ads are not being enabled when upgrading to a new version if they were disabled
  - [ ] Ensure that ads are not disabled when upgrading to a new version if they were enabled
