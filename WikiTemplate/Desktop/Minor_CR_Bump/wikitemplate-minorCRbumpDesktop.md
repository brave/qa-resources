### Installer

- [ ]  Check signature: 
  - [ ] If macOS, using x64 binary run `spctl --assess --verbose` for the installed version and make sure it returns `accepted` 
  - [ ] If macOS, using universal binary run `spctl --assess --verbose` for the installed version and make sure it returns `accepted` 
  - [ ] If Windows right click on the `brave_installer-x64.exe` and go to Properties, go to the Digital Signatures tab and double click on the signature.  Make sure it says "The digital signature is OK" in the popup window

### Widevine

- [ ]  Verify `Widevine Notification` is shown when you visit Netflix for the first time
- [ ]  Test that you can stream on Netflix on a fresh profile after installing Widevine
- [ ]  If macOS, run the above Widevine tests for both `x64` and `universal` builds

### Rewards

- [ ] Verify that you are able to successfully join Rewards on a fresh profile

### TLS Pinning

- [ ] Visit https://ssl-pinning.someblog.org/ and verify a pinning error is displayed
- [ ] Visit https://pinning-test.badssl.com/ and verify a pinning error is **not** displayed

## Update tests

- [ ]  Verify visiting `brave://settings/help` triggers update check
- [ ]  Verify once update is downloaded, prompts to `Relaunch` to install update

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
  - [ ] Custom filters under brave://settings/shields/filters are retained
  - [ ] Custom lists under brave://settings/shields/filters are retained
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
