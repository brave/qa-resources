### Installer

- [ ]  Check signature: If OS Run `spctl --assess --verbose /Applications/Brave-Browser-Beta.app/` and make sure it returns `accepted`.  If Windows right click on the `brave_installer-x64.exe` and go to Properties, go to the Digital Signatures tab and double click on the signature.  Make sure it says "The digital signature is OK" in the popup window

### Data(Upgrade from previous release)

- [ ]  Make sure that data from the last version appears in the new version OK
- [ ]  With data from the last version, verify that
  - [ ]  bookmarks on the bookmark toolbar and bookmark folders can be opened
  - [ ]  cookies are preserved
  - [ ]  installed extensions are retained and work correctly
  - [ ]  opened tabs can be reloaded
  - [ ]  stored passwords are preserved
  - [ ]  unpinned tabs can be pinned

### Widevine

- [ ]  Verify `Widevine Notification` is shown when you visit Netflix for the first time
- [ ]  Test that you can stream on Netflix on a fresh profile after installing Widevine 

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
- [ ]  Upgrade from older version
  - [ ]  Verify the wallet balance is retained and wallet backup code isn't corrupted
  - [ ]  Verify auto-contribute list is not lost after upgrade
  - [ ]  Verify tips list is not lost after upgrade
  - [ ]  Verify wallet panel transactions list is not lost after upgrade

## Update tests

- [ ]  Verify visiting `brave://settings/help` triggers update check
- [ ]  Verify once update is downloaded, prompts to `Relaunch` to install update

#### Components
- [ ]   Delete Adblock folder from browser profile and restart browser. Visit `brave://components` and verify `Brave Ad Block Updater` downloads and update the component. Repeat for all Brave components