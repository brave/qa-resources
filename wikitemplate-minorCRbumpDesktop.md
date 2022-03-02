### Installer

- [ ]  Check signature: If OS Run `spctl --assess --verbose /Applications/Brave-Browser-Beta.app/` and make sure it returns `accepted`.  If Windows right click on the `brave_installer-x64.exe` and go to Properties, go to the Digital Signatures tab and double click on the signature.  Make sure it says "The digital signature is OK" in the popup window

### Widevine

- [ ]  Verify `Widevine Notification` is shown when you visit Netflix for the first time
- [ ]  Test that you can stream on Netflix on a fresh profile after installing Widevine

### Rewards

- [ ] Verify that you are able to successfully join Rewards on a fresh profile

#### PWA (Progressive Web Application)

- [ ] Verify that creating a PWA via `Hamburger Menu` -> `More tools` -> `Create shortcut...` with `Open as window` selected creates a shortcut and launches a new window without any issues
  - [ ] ensure that a separate PWA window is being opened (this window will not have the URL bar visible)
  - [ ] ensure that you can launch the PWA from different locations by moving around the created shortcut
  - [ ] ensure that you can launch the PWA via the created shortcut when Brave is closed
  - [ ] ensure that you can uninstall the PWA via `Hamburger Menu` -> `Uninstall PWA`
- [ ] Verify that creating a PWA via `Hamburger Menu` -> `More tools` -> `Create shortcut...` without `Open as window` selected creates a shortcut and creates a new tab
  - [ ] ensure that you can launch the PWA from different locations by moving around the created shortcut
  - [ ] ensure that you can launch the PWA via the created shortcut when Brave is closed

### Update tests

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
  - [ ] Previously created PWA shortcuts can still be used/launch without any issues
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
