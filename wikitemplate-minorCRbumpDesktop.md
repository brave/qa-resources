### Installer

- [ ]  Check signature: If OS Run `spctl --assess --verbose /Applications/Brave-Browser-Beta.app/` and make sure it returns `accepted`.  If Windows right click on the `brave_installer-x64.exe` and go to Properties, go to the Digital Signatures tab and double click on the signature.  Make sure it says "The digital signature is OK" in the popup window

### Widevine

- [ ]  Verify `Widevine Notification` is shown when you visit Netflix for the first time
- [ ]  Test that you can stream on Netflix on a fresh profile after installing Widevine
- [ ]  Verify `Widevine Notification` is shown when you visit HBO Max for the first time
- [ ]  Test that you can stream on HBO Max on a fresh profile after installing Widevine

### Rewards

- [ ]  Verify account balance shows correct BAT and USD value
- [ ]  Verify you are able to restore a wallet
- [ ]  Verify actions taken (claiming grant, tipping, auto-contribute) display in wallet panel
- [ ]  Verify when you click on the BR panel while on a site, the panel displays site specific information (site favicon, domain, attention %)
- [ ]  Verify you are able to make one-time tip and they display in tips panel
- [ ]  Verify you are able to make recurring tip and they display in tips panel
- [ ]  Verify you can tip a verified publisher
- [ ]  Verify you can tip a verified YouTube creator
- [ ]  Verify you are able to perform a contribution
- [ ]  Verify if you disable auto-contribute you are still able to tip regular sites and YouTube creators

## Update tests

- [ ]  Verify visiting `brave://settings/help` triggers update check
- [ ]  Verify once update is downloaded, prompts to `Relaunch` to install update

#### Components
- [ ]   Delete Adblock folder from browser profile and restart browser. Visit `brave://components` and verify `Brave Ad Block Updater` downloads and update the component. Repeat for all Brave components

### Upgrade

- [ ] Make sure that data from the last version appears in the new version OK
- [ ] Ensure that `brave://version` lists the expected Brave & Chromium versions
- [ ] With data from the last version, verify that
  - [ ] Bookmarks on the bookmark toolbar and bookmark folders can be opened
  - [ ] Cookies are preserved
  - [ ] Installed extensions are retained and work correctly
  - [ ] Opened tabs can be reloaded
  - [ ] Stored passwords are preserved
  - [ ] Sync chain created in previous version is retained
  - [ ] Social media blocking buttons changes are retained
  - [ ] Rewards
    - [ ] Wallet balance is retained
    - [ ] Auto-contribute list is retained
    - [ ] Both Tips and Monthly Contributions are retained
    - [ ] Wallet panel transactions list is retained
    - [ ] Changes to rewards settings are retained
    - [ ] Ensure that Auto Contribute is not being enabled when upgrading to a new version if AC was disabled
  - [ ] Ads
    - [ ] Both `Estimated pending rewards` & `Ad notifications received this month` are retained
    - [ ] Changes to ads settings are retained
    - [ ] Ensure that ads are not being enabled when upgrading to a new version if they were disabled
    - [ ] Ensure that ads are not disabled when upgrading to a new version if they were enabled
