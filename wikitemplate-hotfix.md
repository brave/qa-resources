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

- [ ]  Verify wallet is auto created after enabling rewards
- [ ]  Verify account balance shows correct BAT and USD value
- [ ]  Verify you are able to restore a wallet
- [ ]  Verify wallet address matches the QR code that is generated under `Add funds`
- [ ]  Verify actions taken (claiming grant, tipping, auto-contribute) display in wallet panel
- [ ]  Verify adding funds via any of the currencies flows into wallet after specified amount of time
- [ ]  Verify adding funds to an existing wallet with amount, adjusts the BAT value appropriately
- [ ]  Verify monthly budget shows correct BAT and USD value
- [ ]  Verify you are able to exclude a publisher from the auto-contribute table by clicking on the `x` in auto-contribute table and popup list of sites
- [ ]  Verify you are able to exclude a publisher by using the toggle on the Rewards Panel
- [ ]  Verify when you click on the BR panel while on a site, the panel displays site specific information (site favicon, domain, attention %)
- [ ]  Verify when you click on `Send a tip`, the custom tip banner displays
- [ ]  Verify you are able to make one-time tip and they display in tips panel
- [ ]  Verify you are able to make recurring tip and they display in tips panel
- [ ]  Verify you can tip a verified publisher
- [ ]  Verify you can tip a verified YouTube creator
- [ ]  Verify tip panel shows a verified checkmark for a verified publisher/verified YouTube creator
- [ ]  Verify tip panel shows a message about unverified publisher
- [ ]  Verify BR panel shows message about an unverified publisher
- [ ]  Verify you are able to perform a contribution
- [ ]  Verify if you disable auto-contribute you are still able to tip regular sites and YouTube creators
- [ ]  Verify that disabling Rewards and enabling it again does not lose state
- [ ]  Verify that disabling auto-contribute and enabling it again does not lose state
- [ ]  Adjust min visit/time in settings. Visit some sites and YouTube channels to verify they are added to the table after the specified settings
- [ ]  Upgrade from older version
  - [ ]  Verify the wallet balance is retained and wallet backup code isn't corrupted
  - [ ]  Verify auto-contribute list is not lost after upgrade
  - [ ]  Verify tips list is not lost after upgrade
  - [ ]  Verify wallet panel transactions list is not lost after upgrade

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