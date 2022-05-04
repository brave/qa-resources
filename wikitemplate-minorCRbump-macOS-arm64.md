### Installer

- [ ]  Check signature: If OS Run `"spctl --assess --verbose /Applications/Brave Browser.app"` and make sure it returns `accepted`.
- [ ] Ensured that the following executables work as expected
   - [ ] `Brave-Browser-arm64.dmg`
      - [ ] Check executable size, should be `~290mb`
   - [ ] `Brave-Browser-x64.dmg`
       - [ ] Check executable size, should be `~290mb`
- [ ] Visited `brave://version` and ensure the following:
   - [ ] `arm64` is being displayed when installing via `arm64` binary on `M1` mac
   - [ ] `x86_64 translated` is being displayed when installing via `x64` binary on `M1` mac using `Rosetta`

### Widevine

- [ ]  Verify `Widevine Notification` is shown when you visit Netflix for the first time
- [ ]  Test that you can stream on Netflix on a fresh profile after installing Widevine 

#### Components
- [ ]   Delete Adblock folder from browser profile and restart browser. Visit `brave://components` and verify `Brave Ad Block Updater` downloads and update the component. Repeat for all Brave components

#### Upgrade - `Brave-Browser-arm64.dmg`

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
    - [ ] BAT balance is retained
    - [ ] Auto-contribute list is retained
    - [ ] Both Tips and Monthly Contributions are retained
    - [ ] Panel transactions list is retained
    - [ ] Changes to rewards settings are retained
    - [ ] Ensure that Auto Contribute is not being enabled when upgrading to a new version if AC was disabled
  - [ ] Ads
    - [ ] Both `Estimated pending rewards` & `Ad notifications received this month` are retained
    - [ ] Changes to ads settings are retained
    - [ ] Ensure that ads are not being enabled when upgrading to a new version if they were disabled
    - [ ] Ensure that ads are not disabled when upgrading to a new version if they were enabled 
