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

## Extensions/Plugins tests

- [ ]  Verify one item from Brave Update server is installable (Example: Ad-block DAT file on fresh extension)
- [ ]  Verify one item from Google Update server is installable (Example: Extensions from CWS)
- [ ]  Verify PDFJS, Torrent viewer extensions are installed automatically on fresh profile and cannot be disabled
- [ ]  Verify magnet links and .torrent files loads Torrent viewer page and able to download torrent

### CWS

- [ ]  Verify installing ABP from CWS shows warning message `NOT A RECOMMENDED BRAVE EXTENSION!` but still allows to install the extension
- [ ]  Verify installing LastPass from CWS doesn't show any warning message 

### PDF

- [ ]  Test that PDF is loaded over HTTPS at https://basicattentiontoken.org/BasicAttentionTokenWhitePaper-4.pdf
- [ ]  Test that PDF is loaded over HTTP at http://www.pdf995.com/samples/pdf.pdf

### Widevine

- [ ]  Verify `Widevine Notification` is shown when you visit Netflix for the first time
- [ ]  Test that you can stream on Netflix on a fresh profile after installing Widevine 

### Bravery settings

- [ ]  Verify that HTTPS Everywhere works by loading http://https-everywhere.badssl.com/
- [ ]  Turning HTTPS Everywhere off and shields off both disable the redirect to https://https-everywhere.badssl.com/
- [ ]  Verify that toggling `Ads and trackers blocked` works as expected
- [ ]  Visit https://testsafebrowsing.appspot.com/s/phishing.html, verify that Safe Browsing (via our Proxy) works for all the listed items
- [ ]  Visit https://brianbondy.com/ and then turn on script blocking, page should not load. Allow it from the script blocking UI in the URL bar and it should load the page correctly
- [ ]  Test that 3rd party storage results are blank at https://jsfiddle.net/7ke9r14a/9/ when 3rd party cookies are blocked and not blank when 3rd party cookies are unblocked

### Fingerprint Tests

- [ ]  Visit https://jsfiddle.net/bkf50r8v/13/, ensure 3 blocked items are listed in shields. Result window should show `got canvas fingerprint 0`  and  `got webgl fingerprint 00`
- [ ]  Test that audio fingerprint is blocked at https://audiofingerprint.openwpm.com/ only when `Block all fingerprinting protection` is on
- [ ]  Test that Brave browser isn't detected on https://extensions.inrialpes.fr/brave/
- [ ]  Test that https://diafygi.github.io/webrtc-ips/ doesn't leak IP address when `Block all fingerprinting protection` is on

### Rewards

- [ ] Verify you are able to create a new wallet.
- [ ] Verify you are able to restore a wallet.
- [ ] Verify account balance shows correct BAT and USD value.
- [ ] Verify actions taken (claiming grant, tipping, auto-contribute) display in wallet panel.
- [ ] Verify AC monthly budget shows correct BAT and USD value.
- [ ] Verify you are able to exclude a publisher from the auto-contribute table and popup list of sites.
- [ ] Verify you are able to exclude a publisher by using the toggle on the Rewards Panel.
- [ ] Verify you are able to perform an auto contribution.
  - [ ] Verify auto contribution is reflected in the rewards widget on the NTP.
- [ ] Verify monthly statement shows expected data.
- [ ] Verify when you click on the BR panel while on a site, the panel displays site specific information (site favicon, domain, attention %).
- [ ] Verify BR panel shows message about an unverified publisher.
- [ ] Verify one time and monthly tip banners show a message about unverified publisher.
- [ ] Verify one time tip and monthly tip banners show a verified checkmark for a verified creator.
- [ ] Verify when you click on `Send a tip`, the custom tip banner displays if set up.
  - [ ] Verify custom tip banner is also displayed for monthly contribution.
- [ ] Verify you are able to make one-time tip and they display in Tips panel.
  - [ ] Verify tip is reflected in the rewards widget on the NTP.
  - [ ] Verify when you tip an unverified publisher, the one time tip is recorded in the Pending Contributions list.  
- [ ] Verify you are able to make recurring tip and they display in Monthly Contributions panel.
  - [ ] Verify you are able to adjust your recurring tip amount from the BR panel.
  - [ ] Verify recurring tip is reflected in the rewards widget on the NTP.
- [ ] Verify you can tip a verified website.
  - [ ] Verify the website displays in the auto-contribute list after specified amount of time/visits per settings.
- [ ] Verify you can tip a verified YouTube creator.
  - [ ] Verify the YouTube creator displays in the auto-contribute list after specified amount of time/visits per settings.
- [ ] Verify you can tip a verified Vimeo creator.
  - [ ] Verify the Vimeo creator displays in the auto-contribute list after specified amount of time/visits per settings.
- [ ] Verify you can tip a verified Twitch creator.
  - [ ] Verify the Twitch creator displays in the auto-contribute list after specified amount of time/visits per settings.
- [ ] Verify you can tip a verified Twitter user from the panel.
- [ ] Verify you can tip a verified Twitter user via inline tip button.
  - [ ] Verify the in-line tip button is spaced properly.
- [ ] Verify you can tip a verified Github user from the panel.
- [ ] Verify you can tip a verified Github user via inline tip button.
  - [ ] Verify the Github creator displays in the auto-contribute list after specified amount of time/visits per settings.
- [ ] Verify you can tip a verified Reddit user from the panel.
- [ ] Verify you can tip a verified Reddit user via inline tip button.
- [ ] Verify if you disable auto-contribute you are still able to tip creators.
- [ ] Verify if auto-contribute is disabled AC does not occur.
- [ ] Verify if Rewards is disabled AC does not occur.
- [ ] Verify that disabling Rewards and enabling it again does not lose state.
- [ ] Verify that disabling auto-contribute and enabling it again does not lose state.
- [ ] Adjust min visit/time in settings. Visit some sites to verify they are added to the table after the specified settings.
- [ ] Uphold cases
  - [ ] Verify you are able to connect an non-KYC'd Uphold wallet to Rewards. 
    - [ ] Verify if you have Brave controlled funds (ex. UGP grant), you can tip both connected and KYC'd creators. 
    - [ ] Verify Uphold wallet balance is not reflected in Brave. 
    - [ ] Verify if you only have user controlled BAT (BAT in Uphold only), you can not do any tips.
  - [ ] Verify you are able to connect a KYC'd Uphold wallet to Rewards. 
    - [ ] Verify if you have Brave controlled funds (ex. UGP grant), you can tip both connected and KYC'd creators. 
    - [ ] Verify wallet balance in Brave updates when BAT is added to the Brave Browser card. 
    - [ ] Verify if you only have user controlled BAT (BAT in Uphold only), you can only tip KYC'd creators, any tips to non-KYC'd creators go to the Pending Contributions list.
    - [ ] Verify you are able to perform an auto contribute using Uphold BAT.
- [ ] Upgrade Cases
  - [ ] Verify the wallet balance is retained and wallet backup code isn't corrupted.
  - [ ] Verify auto-contribute list is not lost after upgrade.
  - [ ] Verify tips list is not lost after upgrade.
  - [ ] Verify wallet panel transactions list is not lost after upgrade.
  - [ ] Verify KYC'd Uphold wallet is not disconnected on upgrade.

### Ads Upgrade Tests:

- [ ]   Install 0.62.51 and enable Rewards (Ads are not available on this version). Update on `test` channel to 0.xx.xx version. Verify Ads are off by default, should get a BAT logo notification to alert you that Ads are available.
- [ ]   Install 0.64.77 and enable Rewards. Ads are on by default. View an Ad. Update on `test` channel to 0.xx.xx version. Verify Ads are still on after update, Ads panel information was not lost after upgrade, no BAT logo notification.
- [ ]   Install 0.64.77 and enable Rewards. Disable Ads. Update on `test` channel to 0.xx.xx version. Verify Ads are still off after update, no BAT logo notification.
- [ ]   Install 0.xx.xxx and enable Rewards. Ads are on by default. View an ad. Update on `test` channel to 0.xx.xx version. Verify Ads are still on after update, Ads panel information was not lost after upgrade, no BAT logo notification.
- [ ]   install 0.xx.xxx and enable Rewards. Disable Ads. Update on `test` channel to 0.xx.xx version. Verify Ads are still off after update, no BAT logo notification.

### Tor Tabs

- [ ]  Visit https://check.torproject.org in a Tor window, ensure its shows success message for using a Tor exit node
- [ ]  Visit https://check.torproject.org in a Tor window, note down exit node IP address. Do a hard refresh (Ctrl+Shift+R/Cmd+Shift+R), ensure exit IP changes after page reloads
- [ ]  Visit https://protonirockerxow.onion/ in a Tor window, ensure login page is shown
- [ ]  Visit https://browserleaks.com/geo in a Tor window, ensure location isn't shown

### Session storage

- [ ]  Temporarily move away your browser profile and test that a new profile is created when browser is launched 
  - macOS - `~/Library/Application\ Support/BraveSoftware/`
  - Windows - `%userprofile%\appdata\Local\BraveSoftware\` 
  - Linux(Ubuntu) - `~/.config/BraveSoftware/`
- [ ]  Test that windows and tabs restore when closed, including active tab
  - [ ] Ensure that the tabs in the above session are being lazy loaded when the session is restored

## Update tests

- [ ]  Verify visiting `brave://settings/help` triggers update check
- [ ]  Verify once update is downloaded, prompts to `Relaunch` to install update

## Chromium upgrade tests

- [ ]  Verify `brave://gpu` on Brave and `chrome://gpu` on Chrome are similar for the same Chromium version on both browsers

#### Adblock

- [ ]  Verify referrer blocking works properly for TLD+1. Visit `https://technology.slashdot.org/` and verify adblock works properly similar to `https://slashdot.org/`

#### Components
- [ ]   Delete Adblock folder from browser profile and restart browser. Visit `brave://components` and verify `Brave Ad Block Updater` downloads and update the component. Repeat for all Brave components