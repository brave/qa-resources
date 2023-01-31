### Installer

- [ ]  Check signature: 
  - [ ] If macOS, using x64 binary run `spctl --assess --verbose` for the installed version and make sure it returns `accepted` 
  - [ ] If macOS, using universal binary run `spctl --assess --verbose` for the installed version and make sure it returns `accepted` 
  - [ ] If Windows right click on the `brave_installer-x64.exe` and go to Properties, go to the Digital Signatures tab and double click on the signature.  Make sure it says "The digital signature is OK" in the popup window

### Widevine

- [ ]  Verify `Widevine Notification` is shown when you visit Netflix for the first time
- [ ]  Test that you can stream on Netflix on a fresh profile after installing Widevine
- [ ]  Verify `Widevine Notification` is shown when you visit HBO Max for the first time
- [ ]  Test that you can stream on HBO Max on a fresh profile after installing Widevine
- [ ]  If macOS, run the above Widevine tests for both `x64` and `universal` builds

### Rewards

- [ ] Verify that none of the reward endpoints are being contacted when a user visits a media creator (`youtube.com`, `reddit.com`, `twitter.com`, `github.com`) and hasn't joined rewards
  - [ ] Verify that `rewards.brave.com`, `pcdn.brave.com`, `grant.rewards.brave.com` or `api.rewards.brave.com` are not being contacted
- [ ] Verify you are able to create a new Rewards profile and are in the unverified state by default
  - [ ] Verify when you visit a creator in this state the panel shows a prompt to connect a custodian and no BAT information (earnings, balance, etc) is displayed
  - [ ] Verify when you visit brave://rewards in this state there are no Auto Contribution, Tipping, or wallet panels on this page
  - [ ] Verify you can toggle ads off/on from this page and the panel and NTP widget respond accordingly
  - [ ] Verify you can toggle rewards off/on from the panel and the brave://rewards page and NTP widget respond accordingly
- [ ] Verify you are able to connect a custodian
  - [ ] Verify Rewards balance shows correct BAT and USD value on brave://rewards, panel, and NTP widget after you connect
  - [ ] Verify when you click on the BR panel while on a site, the panel displays site-specific information (site favicon, domain, attention %)
  - [ ] Verify you are able to tip a creator who has the same custodian as you
  - [ ] Verify you are able to perform an auto contribution
  - [ ] Verify if you disable auto-contribute you are still able to tip creators

### TLS Pinning

- [ ] Visit https://ssl-pinning.someblog.org/ and verify a pinning error is displayed
- [ ] Visit https://pinning-test.badssl.com/ and verify a pinning error is **not** displayed

## Update tests

- [ ]  Verify visiting `brave://settings/help` triggers update check
- [ ]  Verify once update is downloaded, prompts to `Relaunch` to install update

#### Startup & Components

- [ ] Verify that Brave is only contacting `*.brave.com` endpoints on first launch using either `Charles Proxy`, `Fiddler`, `Wireshark` or `LittleSnitch` (or a similar application)
  - [ ] Verify that opening a NTP doesn't trigger any outbound connections related to widgets without user interaction
- [ ] Delete Adblock folder from browser profile and restart browser. Visit `brave://components` and verify `Brave Ad Block Updater` downloads and update the component. Repeat for all Brave components

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
