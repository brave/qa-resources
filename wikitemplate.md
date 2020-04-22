### Installer

- [ ] Check that installer is close to the size of last release
- [ ] Check signature: If OS Run `spctl --assess --verbose /Applications/Brave-Browser-Beta.app/` and make sure it returns `accepted`.  If Windows right click on the `brave_installer-x64.exe` and go to Properties, go to the Digital Signatures tab and double click on the signature.  Make sure it says "The digital signature is OK" in the popup window


### Data(Upgrade from previous release)

- [ ] Make sure that data from the last version appears in the new version OK
- [ ] With data from the last version, verify that
  - [ ] Bookmarks on the bookmark toolbar and bookmark folders can be opened
  - [ ] Cookies are preserved
  - [ ] Installed extensions are retained and work correctly
  - [ ] Opened tabs can be reloaded
  - [ ] Stored passwords are preserved
  - [ ] Unpinned tabs can be pinned
  - [ ] Sync chain created in previous version is retained 
  - [ ] Social media blocking buttons changes are retained

### About pages

- [ ] Verify that `chrome://` forwards to `brave://`
- [ ] Verify `brave://adblock` loads adblock page
- [ ] Verify `brave://newtab` loads a new tab
- [ ] Verify `brave://rewards` loads Brave rewards page 
- [ ] Verify `brave://settings` loads Brave settings page 
- [ ] Verify `brave://version` correctly shows Brave version and Chromium version 
- [ ] Verify `brave://welcome` loads the welcome page 

### Import tests

- [ ] Verify that you can import `History`, `Favorites/Bookmarks` and `Passwords` from Google Chrome 
- [ ] Verify that you can import `History`, `Favorites/Bookmarks`, `Passwords`, `Search Engines` and `Autofill` from Firefox
- [ ] Verify that you can import `Favorites/Bookmarks` from Mirosoft Edge
- [ ] Verify that importing bookmarks using `Bookmark HTML File` retains the folder structure on a clean profile

### Context menus

- [ ] Verify `Block element via selector` removes a CSS element from page without reloading
- [ ] Verify `Clear all CSS rules for this sites` removes the blocked element after page reload
- [ ] Verify `Clear all CSS rules for all sites` removes the rule and loads all elements for all pages

## Extensions/Plugins tests

- [ ] Verify one item from Brave Update server is installable (Example: Ad-block DAT file on fresh extension)
- [ ] Verify one item from Google Update server is installable (Example: Extensions from CWS)
- [ ] Verify PDFJS, Torrent viewer extensions are installed automatically on fresh profile and cannot be disabled
- [ ] Verify older version of an extension gets updated to new version via Google server
- [ ] Verify older version of an extension gets updated to new version via Brave server 
- [ ] Verify magnet links and .torrent files loads Torrent viewer page and able to download torrent
- [ ] Use an old profile to verify extension updates work correctly.

### CWS

- [ ] Verify installing ABP from CWS shows warning message `NOT A RECOMMENDED BRAVE EXTENSION!`but still allows to install the extension
- [ ] Verify installing LastPass from CWS doesn't show any warning message 
- [ ] Verify installing an extension that is not vetted by Brave gets blocked

### Flash tests

- [ ] Test that Flash gets blocked by default when installed
- [ ] Test that once you allow Flash, it turns into a click to play area, and loads flash when allowed

### PDF

- [ ] Test that you can print a PDF
- [ ] Test that PDF is loaded over HTTPS at https://basicattentiontoken.org/BasicAttentionTokenWhitePaper-4.pdf
- [ ] Test that PDF is loaded over HTTP at http://www.pdf995.com/samples/pdf.pdf

### Widevine

- [ ] Verify `Widevine Notification` is shown when you visit Netflix for the first time
- [ ] Test that you can stream on Netflix on a fresh profile after installing Widevine 

### Geolocation

- [ ] Check that https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/Using_geolocation shows correct location
- [ ] Check that https://browserleaks.com/geo works and shows correct location
- [ ] Check that https://html5demos.com/geo/ works but doesn't require an accurate location

### Crash Reporting

- [ ] Check that loading `brave://crash` causes the new tab to crash
- [ ] Check that `brave://crashes` lists all the crashes and includes both Crash Report ID & Local Crash ID
- [ ] Verify the crash ID matches the report on brave stats

### Performance test

_Each start should take less than 7 seconds_
- [ ] Enable only rewards
- [ ] Only import a large set of bookmarks
- [ ] Combine rewards, and a large set of bookmarks

### Bravery settings

- [ ] Verify that HTTPS Everywhere works by loading http://https-everywhere.badssl.com/
- [ ] Turning HTTPS Everywhere off and shields off both disable the redirect to https://https-everywhere.badssl.com/
- [ ] Verify that toggling `Ads and trackers blocked` works as expected
- [ ] Visit https://testsafebrowsing.appspot.com/s/phishing.html, verify that Safe Browsing (via our Proxy) works for all the listed items
- [ ] Visit https://brianbondy.com/ and then turn on script blocking, page should not load. Allow it from the script blocking UI in the URL bar and it should load the page correctly
- [ ] Test that 3rd party storage results are blank at https://jsfiddle.net/7ke9r14a/9/ when 3rd party cookies are blocked and not blank when 3rd party cookies are unblocked

### Fingerprint Tests

- [ ] Visit https://jsfiddle.net/bkf50r8v/13/, ensure 3 blocked items are listed in shields. Result window should show `got canvas fingerprint 0`  and  `got webgl fingerprint 00`
- [ ] Test that audio fingerprint is blocked at https://audiofingerprint.openwpm.com/ only when `Block all fingerprinting protection` is on
- [ ] Test that Brave browser isn't detected on https://extensions.inrialpes.fr/brave/
- [ ] Test that https://diafygi.github.io/webrtc-ips/ doesn't leak IP address when `Block all fingerprinting protection` is on

### Content tests

- [ ] Open a page with an input control and type some misspellings on a textbox, make sure they are underlined
- [ ] Make sure that right clicking on a word with suggestions gives a suggestion and that clicking on the suggestion replaces the text
- [ ] Test that https://mixed-script.badssl.com/ shows up as grey not red (no mixed content scripts are run)

### Brave Ads

- [ ] Verify when you enable Rewards from panel or brave://rewards, Ads are enabled by default
- [ ] Verify Ads UI (panel, settings, etc) shows when in a region with Ads support
- [ ] Verify Ads UI (panel, settings, etc) does not show when in a region without Ads support. Verify the Ads panel does show the 'Sorry! Ads are not yet available in your region.' message.
- [ ] Verify when the system language is English, the Browser language is French, and you are in one of the supported regions, Ad notifications are still served to you.
- [ ] Verify you are served Ad notifications when Ads are enabled
  - [ ] Verify ad earnings are reflected in the rewards widget on the NTP.
- [ ] Verify when Ads are toggled off, there are no Ad messages in the logs
- [ ] Verify when Rewards are toggled off (but Ads were not explicitly toggled off), there are no Ads logs recorded
- [ ] Verify view/click/dismiss/landed ad notifications show in confirmations.json
- [ ] Verify pages you browse to are being classified in the logs
- [ ] Verify tokens are redeemed by viewing the logs (you can use --rewards=debug=true to shorten redemption time) 
- [ ] Verify Ad is not shown if a tab is playing media and is only shown after it stops playing
- [ ] Upgrade Cases
  - [ ] Verify when updating from the previous version Ads info in the panel is not lost
  - [ ] Update to latest version from 0.62.51 (or a version without Ads available). Verify you are notified to try ads via a BAT logo notification but Ads are not automatically turned on for you.
  - [ ] Update to latest version from previous version. Verify Ads status (check both on and off) is the same as it was prior to update.

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

### Social-media blocking settings

- [ ] Verify individual `Social media blocking` buttons works as intended when enabled/disabled by visiting https://fmarier.github.io/brave-testing/social-widgets.html

### Sync

- [ ] Verify you are able to create a sync chain and add a mobile/computer to the chain
- [ ] Verify you are able to join an existing sync chain using code words
- [ ] Verify the device name is shown properly when sync chain is created
- [ ] Verify you are able to add a new mobile device to the chain via QR code/code words
- [ ] Verify newly created bookmarks get sync'd to all devices on the sync chain
- [ ] Verify existing bookmarks on current profile gets sync'd to all devices on the sync chain
- [ ] Verify folder structure is retained after sync completes
- [ ] Verify bookmarks don't duplicate when sync'd from other devices
- [ ] Verify removing bookmark from device gets sync'd to all devices on the sync chain
- [ ] Verify adding/removing a bookmark in offline mode gets sync'd to all devices on the sync chain when device comes online
- [ ] With only two device in chain, verify removing the other device resets the sync on b-c as well

### Tor Tabs

- [ ] Visit https://check.torproject.org in a Tor window, ensure its shows success message for using a Tor exit node
- [ ] Visit https://check.torproject.org in a Tor window, note down exit node IP address. Do a hard refresh (Ctrl+Shift+R/Cmd+Shift+R), ensure exit IP changes after page reloads
- [ ] Visit https://check.torproject.org in a Tor window, note down exit node IP address. Click `New Tor Identity for this site` in app menu, ensure the exit node IP address changes after page is reloaded
- [ ] Visit https://protonirockerxow.onion/ in a Tor window, ensure login page is shown
- [ ] Visit http://pdf995.com in a Tor window, should warn about connecting to HTTP site
- [ ] Visit https://browserleaks.com/geo in a Tor window, ensure location isn't shown
- [ ] Visit https://diafygi.github.io/webrtc-ips/ in a Tor window with block all fingerprinting, ensure WebRTC is blocked and no IP is shown
- [ ] Visit https://diafygi.github.io/webrtc-ips/ in a Tor window, disable shields, ensure WebRTC is blocked and no IP is shown
- [ ] Verify Flash doesn't work on Tor window even if it is enabled in `brave://settings/content/flash`
- [ ] Verify Torrent viewer doesn't load in a Tor window and warns when trying to load a torrent/magnet link in a Tor window
- [ ] Verify Google Widevine doesn't load in Tor window and doesn't prompt Google Windevine notification in URL bar
- [ ] Ensure you are able to download a file in Tor window. Verify all Download/Cancel, Download/Retry and Download works in Tor window
- [ ] Disconnect network and open a Tor window, should show modal to retry connection or relaunch Tor window to connect 

### Cookie and Cache

- [ ] Go to http://samy.pl/evercookie/ and set an evercookie. Check that going to prefs, clearing site data and cache, and going back to the evercookie site does not remember the old evercookie value

### Session storage

- [ ] Temporarily move away your browser profile and test that a new profile is created when browser is launched 
  - macOS - `~/Library/Application\ Support/BraveSoftware/`
  - Windows - `%userprofile%\appdata\Local\BraveSoftware\` 
  - Linux(Ubuntu) - `~/.config/BraveSoftware/`
- [ ] Test that windows and tabs restore when closed, including active tab
  - [ ] Ensure that the tabs in the above session are being lazy loaded when the session is restored

## Update tests

- [ ] Verify visiting `brave://settings/help` triggers update check
- [ ] Verify once update is downloaded, prompts to `Relaunch` to install update


## Chromium upgrade tests

- [ ] Verify `brave://gpu` on Brave and `chrome://gpu` on Chrome are similar for the same Chromium version on both browsers

#### Adblock

- [ ] Verify referrer blocking works properly for TLD+1. Visit `https://technology.slashdot.org/` and verify adblock works properly similar to `https://slashdot.org/`

#### Components
- [ ]  Delete Adblock folder from browser profile and restart browser. Visit `brave://components` and verify `Brave Ad Block Updater` downloads and update the component. Repeat for all Brave components
- [ ] Restart the browser, load brave://components, wait for 8 mins and verify that no component shows any errors
- [ ] Verify Brave Local Data Updater, Brave Ad Block Updater, Brave Tor Client Updater (Mac), PDF Viewer (PDF.js), Brave HTTPS Everywhere Updater have non-zero version numbers

### Keyboard Shortcuts (WIP)



#### Rewards Media (To be verified on YouTube and Twitch) (WIP)

