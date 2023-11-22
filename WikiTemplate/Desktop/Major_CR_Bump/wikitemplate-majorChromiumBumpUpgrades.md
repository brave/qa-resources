As per process, QA runs through the following cases to ensure that the major chromium bump that's about to get merged into `master` doesn't regress the `Nightly` channel. Once the major chromium bump is merged into `master`, QA will run through a full manual pass on `Windows` & `Android`.

### Startup & Components

- [ ] Verify that Brave is only contacting `*.brave.com` endpoints on first launch using either `Charles Proxy`, `Fiddler`, `Wireshark` or `LittleSnitch` (or a similar application)
  - [ ] Verify that opening a NTP doesn't trigger any outbound connections related to widgets without user interaction
- [ ] Remove the following component folders and ensure that they're being re-downloaded after restarting the browser:
  - [ ] `afalakplffnnnlkncjhbmahjfjhmlkal`: `AutoplayWhitelist.dat`, `ExtensionWhitelist.dat`, `ReferrerWhitelist.json` and `Greaselion.json`
  - [ ] `CertificateRevocation`
  - [ ] `gccbbckogglekeggclmmekihdgdpdgoe`: (Sponsored New Tab Images)
  - [ ] `gkboaolpopklhgplhaaiboijnklogmbc`: Brave Ad Block List Catalog
  - [ ] `iodkpdagapdfkphljnddpjlldadblomo`: Brave Ad Block Updater
  - [ ] `mfddibmblmbccpadfndgakiopmmhebop`: Brave Ad Block List Catalog
  - [ ] `Safe Browsing`
- [ ] Restart the browser, load `brave://components`, wait for 8 mins and verify that no component shows any errors

**Note:** Always double check `brave://components` to make sure there's no errors/missing version numbers

### Upgrade

- [ ] Make sure that data from the last version appears in the new version OK
- [ ] Ensure that `brave://version` lists the expected Brave & Chromium versions
- [ ] With data from the last version, verify that:
  - [ ] Bookmarks on the bookmark toolbar and bookmark folders can be opened
  - [ ] Cookies are preserved
  - [ ] Installed extensions are retained and work correctly
  - [ ] Opened tabs can be reloaded
  - [ ] Stored passwords are preserved
  - [ ] Sync chain created in previous version is retained
  - [ ] Social media-blocking buttons changes are retained
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
