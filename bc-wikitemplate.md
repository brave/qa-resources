
## Installer

- [ ] Check that installer is close to the size of last release.
- [ ] Check signature: If OS Run `spctl --assess --verbose /Applications/Brave-Browser.app/` and make sure it returns `accepted`.  If Windows right click on the installer exe and go to Properties, go to the Digital Signatures tab and double click on the signature.  Make sure it says "The digital signature is OK" in the popup window.
- [ ] Check Brave and Chromium version in chrome://about

## Data

- [ ] Make sure that data from the last version appears in the new version OK
- [ ] With data from the last version, test that
  - [ ] cookies are preserved
  - [ ] pinned tabs can be opened
  - [ ] pinned tabs can be unpinned
  - [ ] unpinned tabs can be re-pinned
  - [ ] opened tabs can be reloaded
  - [ ] bookmarks on the bookmark toolbar can be opened
  - [ ] bookmarks in the bookmark folder toolbar can be opened

## About pages

- [ ] Test that brave:// forwards to chrome://
- [ ] chrome://adblock
- [ ] chrome://payments
- [ ] chrome://newtab
- [ ] chrome://welcome
- [ ] chrome://version

## Import

- [ ] Check that you can import from browser-laptop
- [ ] Check that you can import from Google Chrome (We implemented all ourselves)
- [ ] Check that you can import from Firefox (Cookies is all we implemented ourselves)
- [ ] Check that you can import from Edge (No custom code we implemented ourselves)

## Context menus

- [ ] Block this element option

## Keyboard Shortcuts

- [ ] TODO: Custom ones we define for functionality not in Chrome but in brave-core

## Printing PDF

- [ ] Test that you can print a PDF

## Extensions/Plugins tests

- [ ] At least one thing on Brave Update server is installable (Example: Ad-block DAT file on fresh extension)
- [ ] At least one thing on Google Update server is installable
- [ ] PDFJS extension gets instaslled automatically on fresh profile
- [ ] Test that an old extension gets updated to a new one from an old profile on Google server
- [ ] Test that an old extension gets updated to a new one from an old profile on Brave server

### Widevine
- [ ] Test that you can log into Netflix and start a show from a fresh profile

### Flash tests
- [ ] Test that Flash gets blocked by default when installed
- [ ] Test that once you allow Flash, it turns into a click to play area, and can play when clicked.

## Geolocation

- [ ] Check that https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/Using_geolocation is blocked due to cross-origin iframes
- [ ] Check that https://browserleaks.com/geo works and shows correct location
- [ ] Check that https://html5demos.com/geo/ works but doesn't require an accurate location

## Crash Reporting

- [ ] Check that loading `chrome://crash` causes the new tab to crash
- [ ] Check that `chrome://crashes` lists all the crashes and includes both Crash Report ID & Local Crash ID
- [ ] Verify the crash ID matches the report on brave stats

## Performance test

_Each start should take less than 7 seconds_
- [ ] Enable only sync (new sync group).
- [ ] Enable only sync with a large sync group (many entries).
- [ ] Enable only payments.
- [ ] Only import a large set of bookmarks.
- [ ] Combine sync, payments, and a large set of bookmarks.

## Bravery settings

- [ ] Check that HTTPS Everywhere works by loading http://https-everywhere.badssl.com/
- [ ] Turning HTTPS Everywhere off and shields off both disable the redirect to https://https-everywhere.badssl.com/
- [ ] Check that ad replacement works on http://slashdot.org
- [ ] Check that toggling to blocking and allow ads works as expected
- [ ] Test that Google Safe Browsing (via our Proxy) works
- [ ] Visit https://brianbondy.com/ and then turn on script blocking, nothing should load. Allow it from the script blocking UI in the URL bar and it should work
- [ ] Test that 3rd party storage results are blank at https://jsfiddle.net/7ke9r14a/9/ when 3rd party cookies are blocked and not blank when 3rd party cookies are unblocked

## Fingerprint Tests

- [ ] Visit https://jsfiddle.net/bkf50r8v/13/, ensure 3 blocked items are listed in shields. Result window should show `got canvas fingerprint 0`  and  `got webgl fingerprint 00`
- [ ] Test that audio fingerprint is blocked at https://audiofingerprint.openwpm.com/ only when `Block all fingerprinting protection` is on
- [ ] Test that Brave browser isn't detected on https://extensions.inrialpes.fr/brave/
- [ ] Test that https://diafygi.github.io/webrtc-ips/ doesn't leak IP address when `Block all fingerprinting protection` is on

## PDF
- [ ] Test that PDF is loaded over https at https://basicattentiontoken.org/BasicAttentionTokenWhitePaper-4.pdf
- [ ] Test that PDF is loaded over http at http://www.pdf995.com/samples/pdf.pdf

## Content tests

- [ ] Spellcheck, open a page with an input control and type some misspellings on a textbox, make sure they are underlined.
- [ ] Make sure that right clicking on a word with suggestions gives a suggestion and that clicking on the suggestion replaces the text
- [ ] Test that https://mixed-script.badssl.com/ shows up as grey not red (no mixed content scripts are run).

## TODO: Ledger

- [ ] Verify wallet is auto created after enabling payments
- [ ] Verify monthly budget and account balance shows correct BAT and USD value
- [ ] Click on `add funds` and click on each currency and verify it shows wallet address and QR Code
- [ ] Verify that Brave BAT wallet address can be copied
- [ ] Verify adding funds via any of the currencies flows into BAT Wallet after specified amount of time
- [ ] Verify adding funds to an existing wallet with amount, adjusts the BAT value appropriately
- [ ] Change min visit and min time in advance setting and verify if the publisher list gets updated based on new setting
- [ ] Visit nytimes.com for a few seconds and make sure it shows up in the Payments table
- [ ] Check that disabling payments and enabling them again does not lose state
- [ ] Generate 500 ledger table entries using `npm run add-simulated-synopsis-visits 500`
  - [ ] ensure that disabling/enabling Brave Payments several times doesn't cause any issues
  - [ ] visit `about:preferences` and switch through all the available preference pages including Payments and ensure they're loading without issues
  - [ ] ensure that loading/viewing `about:preferences#payments` doesn't cause the CPU to reach 100% of usage and cause performance issues
  - [ ] ensure that both `Minimum page time` & `Minimum visits` work correctly with the large list of ledger entries
  - [ ] ensure that you can sort the ledger table using `Site`, `Include`, `Views`, `Time Spent` and `%`
- [ ] Upgrade from older version
  - [ ] Verify the wallet isn't corrupted upon upgrade (balance is retained and wallet backup code isn't corrupted)
  - [ ] Verify publishers list is not lost after upgrade

### TODO: Ledger Media (To be verified on YouTube and Twitch)

  - [ ] Visit any YouTube/Twitch video in a normal/session tab and ensure the video publisher name is listed in ledger table
  - [ ] Visit any YouTube/Twitch video in a private tab and ensure the video publisher name is not listed in ledger table
  - [ ] Visit any live YouTube/Twitch video and ensure the time spent is shown under ledger table
  - [ ] Visit any embeded YouTube/Twitch video and ensure the video publisher name is listed in ledger table
  - [ ] Ensure total time spent is correctly calculated for each publisher video
  - [ ] Ensure total time spent is correctly calculated when switching to YouTube/Twitch video from an embeded video
  - [ ] Ensure YouTube/Twitch publishers are not listed when `Allow contributions to video` is disabled in adavanced settings
  - [ ] Ensure existing YouTube/Twitch publishers are not lost when `Allow contributions to video` is disabled in adavanced settings
  - [ ] Ensure YouTube/Twitch publishers is listed but not included when `auto-include` is disabled
  - [ ] Update Advanced settings to different time/visit value and ensure YouTube/Twitch videos are added to ledger table once criteria is met
  - [ ] Perform a contribution while YouTube/Twitch channels are included on the ledger. Ensure the channels are listed on the contribution statement
  - [ ] Verify that you are able to delete YouTube/Twitch publishers from ledger table
  - [ ] Verify that you are able to re-add YouTube/Twitch publishers to ledger table
  - [ ] Verify if you minimize a Twitch video (Stream/VOD) and navigate around the site, the video is counted in ledger

## Sync

- [ ] Verify you are able to sync two devices using the secret code
- [ ] Visit a site on device 1 and change shield setting, ensure that the saved site preference is synced to device 2
- [ ] Enable Browsing history sync on device 1, ensure the history is shown on device 2
- [ ] Clear browsing history on device 1, ensure the history is sync back on device 1 from device 2
- [ ] Import/Add bookmarks on device 1, ensure it is synced on device 2
- [ ] Ensure imported bookmark folder structure is maintained on device 2
- [ ] Ensure bookmark favicons are shown after sync

## Cookie and Cache

- [ ] Go to http://samy.pl/evercookie/ and set an evercookie. Check that going to prefs, clearing site data and cache, and going back to the Evercookie site does not remember the old evercookie value. (No custom code in Brave for this yet)

## Update tests

- [ ] TODO: Test that updating using `BRAVE_UPDATE_VERSION=0.8.3` env variable works correctly.

## Things to check once:

- Native ledger library, is it still stored in json
- Migrate snaps to QA from devops
- Can QA get production server copy for ledger back-end?
- Can QA get more control to restart ledger services, when things go wrong.
- Check one time that these exceptions work: `brave/common/shield_exceptions.cc`
- Check one referrer blocking works properly with TLD+1
- Evercookie works correctly?
- Find a good channel (maybe youtube) to see upcoming Chrome issues that we should be concerned about.
- Release notes should mention big things we are getting for free.
- Check once `brave/common/brave_switches.cc`
- What happens if you install uBlock or ABP?
- What happens with automatically installed extensions? 
