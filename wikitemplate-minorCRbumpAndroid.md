## Installer

- [ ] Check that installer is close to the size of the last release
- [ ] Check the Brave version in About and make sure it is EXACTLY as expected

## Custom tabs

- [ ] Make sure Brave handles links from Gmail, Slack
- [ ] Make sure Brave works as custom tabs provide with Chrome browser
- [ ] Ensure custom tabs work even with sync enabled/disabled

## Settings and Bottom bar

- [ ] Verify changing default settings are retained and don't cause the browser to crash
- [ ] Verify bottom bar buttons (Home/Bookmark/Search/Tabs) work as expected 

### Rewards

- [ ] Verify account balance shows correct BAT and USD value
- [ ] Verify actions taken (claiming grant, tipping, auto-contribute) display in wallet panel
- [ ] Verify when you click on the BR panel while on a site, the panel displays site specific information (site favicon, domain, attention %)
- [ ] Verify you are able to make one-time tip and they display in tips panel
- [ ] Verify you are able to make recurring tip and they display in tips panel
- [ ] Verify you can tip a verified publisher
- [ ] Verify you can tip a verified YouTube creator
- [ ] Verify you are able to perform a contribution
- [ ] Verify if you disable auto-contribute you are still able to tip regular sites and YouTube creators
- [ ] Verify on BR panel that the `Verify wallet` button only enables when balance is >=25 BAT
- [ ] Verify you can reset rewards from advance setting. Resetting should delete wallet and bring it back to the pre-optin state

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
    - [ ] Wallet balance is retained
    - [ ] Auto-contribute list is retained
    - [ ] Both Tips and Monthly Contributions are retained
    - [ ] Wallet panel transactions list is retained
    - [ ] Changes to rewards settings are retained
  - [ ] Ads
    - [ ] Both `Estimated pending rewards` & `Ad notifications received this month` are retained
    - [ ] Changes to ads settings are retained
    - [ ] Ensure that ads are not being enabled when upgrading to a new version if they were disabled
    - [ ] Ensure that ads are not disabled when upgrading to a new version if they were enabled