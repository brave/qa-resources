## Installer

- [ ] Check that installer is close to the size of the last release
- [ ] Check the Brave version in About and make sure it is EXACTLY as expected

## Startup

- [ ] Verify that Brave is only contacting `*.brave.com` endpoints on first launch using either `Charles Proxy`, `Fiddler` or `Wireshark` (or a similar application)
  - [ ] Verify that opening a NTP doesn't trigger any outbound connections related to widgets without user interaction

## Custom tabs

- [ ] Make sure Brave handles links from Gmail, Slack
- [ ] Make sure Brave works as custom tabs provide with Chrome browser
- [ ] Ensure custom tabs work even with sync enabled/disabled

## Settings and Bottom bar

- [ ] Verify changing default settings are retained and don't cause the browser to crash
- [ ] Verify bottom bar buttons (Home/Bookmark/Search/Tabs) work as expected

### Rewards

- [ ] Verify you are able to create a new Rewards profile and are in the unverified state by default
  - [ ] Verify when you visit a creator in this state the panel shows a prompt to connect a custodian and no BAT information (earnings, balance, etc) is displayed
  - [ ] Verify when you visit brave://rewards in this state there are no Auto Contribution, Tipping, or summary panels on this page
  - [ ] Verify you can toggle ads off/on from this page and the panel responds accordingly
  - [ ] Verify you can toggle rewards off/on from the panel and the brave://rewards page responds accordingly
- [ ] Verify you are able to connect a custodian
  - [ ] Verify Rewards balance shows correct BAT and USD value on brave://rewards and panel after you connect
  - [ ] Verify when you click on the BR panel while on a site, the panel displays site-specific information (site favicon, domain, attention %)
  - [ ] Verify you are able to tip a creator who has the same custodian as you
  - [ ] Verify you are able to perform an auto contribution
  - [ ] Verify if you disable auto-contribute you are still able to tip creators

## Brave Shields

- [ ] Run all six test configurations on `https://dev-pages.brave.software/storage/ephemeral-storage.html` and confirm results are as expected per each test listed.

### Brave Ads

- [ ] Verify ads is auto-enabled when rewards is enabled for the supported region
- [ ] Verify ads are only shown when the app is being used
- [ ] Verify ad notification are shown based on ads per hour setting
- [ ] Verify ad notifications stack up in notification tray
- [ ] Verify swipe left/right dismisses the ad notification when shown and is not stored in the notification tray
- [ ] Verify clicking on an ad notification shows the landing page
- [ ] Verify `view`,`clicked` and `landed` and `dismiss` states are logged based on the action

## Upgrade

Pre-Requisite: Visit several websites so Top Tiles under New Tab Page get updated and add several sites via `Add to Home screen` (from 3 dots menu) using a previous build/installation before upgrading.

- [ ] Make sure that data from the last version appears in the new version OK
- [ ] Ensure that `brave://version` lists the expected Brave & Chromium versions
- [ ] With data from the last version, verify that
  - [ ] Bookmarks are preserved (Folders/Sites)
  - [ ] Cookies are preserved
  - [ ] Per site shield settings are preserved
  - [ ] Opened tabs can be reloaded
  - [ ] Stored passwords are preserved
  - [ ] Sync chain created in previous version is retained
  - [ ] Setting changes are preserved (Default SE, Shield settings, Homepage etc..)
  - [ ] Top Tiles under New Tab Page are preserved
  - [ ] Home screen shortcuts are preserved
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
