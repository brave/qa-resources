

### Installer

- [ ] Check that installer is close to the size of last release.
- [ ] Check signature: If OS Run `spctl --assess --verbose /Applications/Brave-Browser-Beta.app/` and make sure it returns `accepted`.  If Windows right click on the `brave_installer-x64.exe` and go to Properties, go to the Digital Signatures tab and double click on the signature.  Make sure it says "The digital signature is OK" in the popup window.


### Data

- [ ] Make sure that data from the last version appears in the new version OK
- [ ] With data from the last version, test that
  - [ ] bookmarks on the bookmark toolbar and bookmark folders can be opened
  - [ ] cookies are preserved
  - [ ] installed extensions are retained and work correctly
  - [ ] opened tabs can be reloaded
  - [ ] stored passwords are preserved
  - [ ] unpinned tabs can be pinned

### About pages

- [ ] Test that `brave://` forwards to `chrome://`
- [ ] Test `chrome://adblock` loads adblock page
- [ ] Test `chrome://rewards` loads Brave rewards page 
- [ ] Test `chrome://newtab` loads a new tab
- [ ] Test `chrome://welcome` loads the welcome page 
- [ ] Test `chrome://version` correctly shows Brave version and Chromium version 

### Import

- [ ] Check that you can import bookmarks, cookies, history, passwords and stats from Brave(browser-laptop)
- [ ] Check that you can import bookmarks, cookies, history, passwords from Google Chrome 
- [ ] Check that you can import bookmarks, cookies, history, passwords, autofill and search engines from Firefox
- [ ] Check that you can import bookmarks from Edge

### Context menus

- [ ] Verify `Block element via selector` removes a CSS element from page without reloading
- [ ] Verify `Clear all CSS rules for this sites` removes the blocked element after page reload
- [ ] Verify `Clear all CSS rules for all sites` removes the rule and loads all elements for all pages


## Extensions/Plugins tests

- [ ] Verify one item from Brave Update server is installable (Example: Ad-block DAT file on fresh extension)
- [ ] Verify one item from Google Update server is installable(Example: Extensions from CWS)
- [ ] Verify PDFJS, Torrent viewer extensions are installed automatically on fresh profile and cannot be disabled
- [ ] Test that an old extension gets updated to a new one from an old profile on Google server
- [ ] Test that an old extension gets updated to a new one from an old profile on Brave server
- [ ] Verify magnet links and .torrent files loads Torrent viewer page and able to download torrent

### CWS

- [ ] Verify installing ABP from CWS shows warning message `NOT A RECOMMENDED BRAVE EXTESION!`but still gets installed
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
- [ ] Test that you can stream on Netflix on a fresh profile

### Geolocation

- [ ] Check that https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/Using_geolocation shows correct location
- [ ] Check that https://browserleaks.com/geo works and shows correct location
- [ ] Check that https://html5demos.com/geo/ works but doesn't require an accurate location

### Crash Reporting

- [ ] Check that loading `chrome://crash` causes the new tab to crash
- [ ] Check that `chrome://crashes` lists all the crashes and includes both Crash Report ID & Local Crash ID
- [ ] Verify the crash ID matches the report on brave stats

### Performance test

_Each start should take less than 7 seconds_
- [ ] Enable only sync (new sync group)
- [ ] Enable only sync with a large sync group (many entries)
- [ ] Enable only rewards
- [ ] Only import a large set of bookmarks
- [ ] Combine sync, rewards, and a large set of bookmarks

### Bravery settings

- [ ] Check that HTTPS Everywhere works by loading http://https-everywhere.badssl.com/
- [ ] Turning HTTPS Everywhere off and shields off both disable the redirect to https://https-everywhere.badssl.com/
- [ ] Check that ad replacement works on http://slashdot.org
- [ ] Check that toggling to blocking and allow ads works as expected
- [ ] Test that Google Safe Browsing (via our Proxy) works
- [ ] Visit https://brianbondy.com/ and then turn on script blocking, nothing should load. Allow it from the script blocking UI in the URL bar and it should work
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


### Cookie and Cache

- [ ] Go to http://samy.pl/evercookie/ and set an evercookie. Check that going to prefs, clearing site data and cache, and going back to the Evercookie site does not remember the old evercookie value.

### Session storage

- [ ] Temporarily move away your `~/Library/Application\ Support/BraveSoftware/Brave-Browser/` and test that a new profile is created when browser is launched (`%userprofile%\appdata\Local\BraveSoftware\Brave-Browser\` in Windows, `./config/BraveSoftware/Brave-Browser/` in Ubuntu)
- [ ] Test that windows and tabs restore when closed, including active tab.
  - [ ] Ensure that the tabs in the above session are being lazy loaded when the session is restored

## Chromium upgrade tests

#### Adblock

- [ ] Verify referrer blocking works properly for TLD+1 

#### Components
- Check once `brave/common/brave_switches.cc`
__________

## Yet to implement

- Keyboard Shortcuts
- Ledger/Rewards
  - Ledger Media (To be verified on YouTube and Twitch)
- Sync
- Tor private tabs
- Manual Update tests from older version
  - Test that updating using `BRAVE_UPDATE_VERSION=0.8.3` env variable works correctly.
- Native ledger library, is it still stored in json
- Ensure that hovering over lazy loaded tabs correctly loads the tab without any issues
