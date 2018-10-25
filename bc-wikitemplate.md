

### Installer

- [ ] Check that installer is close to the size of last release
- [ ] Check signature: If OS Run `spctl --assess --verbose /Applications/Brave-Browser-Beta.app/` and make sure it returns `accepted`.  If Windows right click on the `brave_installer-x64.exe` and go to Properties, go to the Digital Signatures tab and double click on the signature.  Make sure it says "The digital signature is OK" in the popup window


### Data

- [ ] Make sure that data from the last version appears in the new version OK
- [ ] With data from the last version, verify that
  - [ ] bookmarks on the bookmark toolbar and bookmark folders can be opened
  - [ ] cookies are preserved
  - [ ] installed extensions are retained and work correctly
  - [ ] opened tabs can be reloaded
  - [ ] stored passwords are preserved
  - [ ] unpinned tabs can be pinned

### About pages

- [ ] Verify that `chrome://` forwards to `brave://`
- [ ] Verify `brave://adblock` loads adblock page
- [ ] Verify `brave://rewards` loads Brave rewards page 
- [ ] Verify `brave://newtab` loads a new tab
- [ ] Verify `brave://welcome` loads the welcome page 
- [ ] Verify `brave://version` correctly shows Brave version and Chromium version 

### Import tests

- [ ] Verify that you can import bookmarks, cookies, history, passwords and stats from Brave(browser-laptop)
- [ ] Verify that you can import bookmarks, cookies, history, passwords from Google Chrome 
- [ ] Verify that you can import bookmarks, cookies, history, passwords, autofill and search engines from Firefox
- [ ] Verify that you can import bookmarks from Edge
- [ ] Verify importing `Bookmark HTML` file retains the folder structure on a clean profile

### Context menus

- [ ] Verify `Block element via selector` removes a CSS element from page without reloading
- [ ] Verify `Clear all CSS rules for this sites` removes the blocked element after page reload
- [ ] Verify `Clear all CSS rules for all sites` removes the rule and loads all elements for all pages

### Keyboard Shortcuts (WIP)


## Extensions/Plugins tests

- [ ] Verify one item from Brave Update server is installable (Example: Ad-block DAT file on fresh extension)
- [ ] Verify one item from Google Update server is installable(Example: Extensions from CWS)
- [ ] Verify PDFJS, Torrent viewer extensions are installed automatically on fresh profile and cannot be disabled
- [ ] Verify older version of an extension gets updated to new version via Google server
- [ ] Verify older version of an extension gets updated to new version via Brave server 
- [ ] Verify magnet links and .torrent files loads Torrent viewer page and able to download torrent

### CWS

- [ ] Verify installing ABP from CWS shows warning message `NOT A RECOMMENDED BRAVE EXTESION!`but still allows to install the extension
- [ ] Verify installing LastPass from CWS doesn't show any warning message 
- [ ] Verify installing an extesion that is not vetted by Brave gets blocked

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
- [ ] Enable only sync (new sync group)
- [ ] Enable only sync with a large sync group (many entries)
- [ ] Enable only rewards
- [ ] Only import a large set of bookmarks
- [ ] Combine sync, rewards, and a large set of bookmarks
- [ ] Ensure that hovering over lazy loaded tabs correctly loads the tab without any issues 

### Bravery settings

- [ ] Verify that HTTPS Everywhere works by loading http://https-everywhere.badssl.com/
- [ ] Turning HTTPS Everywhere off and shields off both disable the redirect to https://https-everywhere.badssl.com/
- [ ] Verify that toggling `Ad Control` works as expected
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

### Sync (WIP)

### Rewards (WIP)

####Rewards Media (To be verified on YouTube and Twitch) (WIP)

### Cookie and Cache

- [ ] Go to http://samy.pl/evercookie/ and set an evercookie. Check that going to prefs, clearing site data and cache, and going back to the Evercookie site does not remember the old evercookie value

### Session storage

- [ ] Temporarily move away your browser profile and test that a new profile is created when browser is launched 
  - macOS - `~/Library/Application\ Support/BraveSoftware/Brave-Browser-Beta/`
  - Windows - `%userprofile%\appdata\Local\BraveSoftware\Brave-Browser-Beta\` 
  - Linux(Ubuntu) -  `./config/BraveSoftware/Brave-Browser-Beta/`
- [ ] Test that windows and tabs restore when closed, including active tab
  - [ ] Ensure that the tabs in the above session are being lazy loaded when the session is restored

## Update tests

- [ ] Verify visiting `brave://settings/help` triggers update check
- [ ] Verify once update is downloaded, prompts to `Relaunch` to install update


## Chromium upgrade tests

#### Adblock

- [ ] Verify referrer blocking works properly for TLD+1 

#### Components
- [ ]  Delete Adblock folder from browser profile and restart browser. Visit `brave://components` and verify `Brave Ad Block Updater` downloads and update the component. Repeat for all Brave components

