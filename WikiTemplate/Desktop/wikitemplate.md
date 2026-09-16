### Installer

- [ ] Check the installer is close to the size of the last release
- [ ]  Check signature: 
  - [ ] If macOS, using `arm64` binary run `spctl --assess --verbose` for the installed version and make sure it returns `accepted` 
  - [ ] If macOS, using `universal` binary run `spctl --assess --verbose` for the installed version and make sure it returns `accepted` 
  - [ ] If Windows right click on the `brave_installer-x64.exe` and go to Properties, go to the Digital Signatures tab and double click on the signature.  Make sure it says "The digital signature is OK" in the popup window

### Adblock lists and filters

 - [ ] Navigate to `brave://adblock` and confirm you are redirected to `brave://settings/shields/filters`
 - [ ] Filter lists
   - [ ] Type "cookie" into the "Filter lists" search box, and verify that the list is filtered down to just the `Easylist-Cookie List - Filter Obtrusive Cookie Notices`
   - [ ] Enable the `Easylist-Cookie List` and refresh the page
   - [ ] Expand the regional filter lists and verify that the cookie list is still enabled
 - [ ] Add custom filter lists
   - [ ] Enter `https://raw.githubusercontent.com/ryanbr/fanboy-adblock/master/fanboy-antifonts.txt` into `Enter filter list URL` and press `Add`
   - [ ] Ensure that the `Custom lists` table appears, with the newly added entry; `Last updated` should be now (e.g. `0 seconds ago`)
   - [ ] Refresh the page after a few seconds and ensure that the `Last updated` time reflects the time that has passed
   - [ ] Use the dropdown next to the entry and verify that all options (`Update now`, `View source`, `Unsubscribe`) are shown
     - [ ] Pressing the `Update now` button should update the timestamp appropriately
     - [ ] `View source` should open the text of the filter list
     - [ ] `Unsubscribe` should delete the entry from the list and hide the table once again
 - [ ] Create custom filters
   - [ ] The `Create custom filters` section should be visible with a text box and `Save changes` button
   - [ ] Adding text to the box, pressing `Save changes`, and refreshing the page should result in the same text appearing in the box after the reload

### Importing

- [ ] Verify that you can import `History`, `Favorites/Bookmarks` and `Extensions` from Google Chrome
- [ ] Verify that you can import `History` and `Bookmarks` from Firefox
- [ ] Verify that you can import `Favorites/Bookmarks` from Microsoft Edge
- [ ] Verify that importing bookmarks using `Bookmark HTML File` retains the folder structure on a clean profile

### Context menus

- [ ] Verify you can block a page element using `Block element via selector` context-menu item
- [ ] Verify selecting `Manage custom filters` opens `brave://adblock` in a NTP
- [ ] Verify removing the rule from `brave://adblock` reflects the change on the website, after reload

### Manifest V2 Extensions

- [ ] Under `brave://settings/extensions/v2` toggle "Enable NoScript" on. Be sure to turn off any other extensions listed here if they are on.
     - [ ] Navigate to https://underpassapp.com/StopTheScript/noscript.html and confirm that the page says "JavaScript is disabled".
     - [ ] Confirm you can open the extension's panel without any errors.
- [ ] Under `brave://settings/extensions/v2` toggle "Enable uBlock Origin" on. Be sure to turn off any other extensions listed here if they are on.
     - [ ] Navigate to a site which contains ads and toggle shields off. Reload the page and confirm ads are still blocked.
     - [ ] Confirm you can open the extension's panel without any errors.
     - [ ] Confirm panel reflects that items are blocked as expected.     
- [ ] Under `brave://settings/extensions/v2` toggle "Enable uMatrix" on. Be sure to turn off any other extensions listed here if they are on.
     - [ ] Navigate to a site which contains ads and toggle shields off. Reload the page and confirm ads are still blocked.
     - [ ] Confirm you can open the extension's panel without any errors.
     - [ ] Confirm panel reflects that items are blocked as expected.     
- [ ] Under `brave://settings/extensions/v2` toggle "Enable AdGuard" on. Be sure to turn off any other extensions listed here if they are on.
     - [ ] Navigate to a site which contains ads and toggle shields off. Reload the page and confirm ads are still blocked.
     - [ ] Confirm you can open the extension's panel without any errors.
     - [ ] Confirm panel reflects that items are blocked as expected.     

### Widevine

- [ ] Verify `Widevine Notification` is shown when you visit Netflix for the first time
- [ ] Test that you can stream on Netflix on a fresh profile after installing Widevine
- [ ] If macOS, run the above Widevine tests for both `arm64` and `universal` builds

### Geolocation

- [ ] Check that https://browserleaks.com/geo works and shows correct location
- [ ] Check that https://html5demos.com/geo/ works but doesn't require an accurate location

### Bravery settings

- [ ] Verify that HTTPS Everywhere works by loading http://https-everywhere.badssl.com/
- [ ] Turning HTTPS Everywhere off and Shields off both disable the redirect to https://https-everywhere.badssl.com/
- [ ] Verify that toggling `Trackers & ads blocked` works as expected
- [ ] Visit https://testsafebrowsing.appspot.com/s/phishing.html, verify that Safe Browsing (via our Proxy) works for all the listed items
- [ ] Visit https://www.blizzard.com and then turn on script blocking, page should not load.
- [ ] Test that 3rd party storage results are blank at https://jsfiddle.net/7ke9r14a/9/ when 3rd party cookies are blocked and not blank when 3rd party cookies are unblocked
- [ ] Test that https://mixed-script.badssl.com/ shows up as grey not red (no mixed content scripts are run)
- [ ] In `brave://settings/security`, choose a DNS provider from the providers listed under Use secure DNS, load `https://browserleaks.com/dns`, and verify your ISP's DNS resolvers aren't detected and shown; only your chosen DoH provider should appear.
- [ ] Open a New Private Window with Tor, load `https://browserleaks.com/dns`, and verify your ISP's DNS resolvers aren't detected and shown.

### Query Filter

- [ ] Visit https://fmarier.github.io/brave-testing/query-filter.html in a Private window and run the tests as directed

### TLS Pinning

- [ ] Visit https://ssl-pinning.someblog.org/ and verify a pinning error is displayed
- [ ] Visit https://pinning-test.badssl.com/ and verify a pinning error is **not** displayed

### Fingerprint Tests

- [ ] Test that https://diafygi.github.io/webrtc-ips/ doesn't leak IP address for each option under `Settings -> Privacy and Security -> WebRTC IP handling policy`

### Brave Ads

- [ ] In rewards-connected state: Verify pages you browse to are being classified in the logs.
- [ ] In rewards-connected state: Verify Notification Ad is served and `view` confirmation is sent. Click the ad and verify `click` confirmation is sent.
- [ ] In rewards-connected state: Verify New Tab Page Ad is served and `view` confirmation is sent. Click the ad and verify `click` confirmation is sent.
- [ ] In rewards-connected state: Verify tokens are redeemed by checking the logs for `Redeem payment tokens` (you can use `--rewards=debug=true` to shorten redemption time).

### Rewards

- [ ] Verify you are able to create a new Rewards profile and are in the unverified state by default
  - [ ] Verify when you visit a creator in this state the panel shows a prompt to connect a custodian and no BAT information (earnings, balance, etc) is displayed
  - [ ] Verify when you visit brave://rewards and/or the panel in this state you are able to scroll to the "Explore" section
- [ ] Verify you are able to connect a custodian or self custody
  - [ ] Verify Rewards balance shows correct BAT value on brave://rewards, panel, and NTP widget after you connect
  - [ ] Verify when you click on the BR panel while on a non-verified creator site, the panel does not display a "Contribute" button
  - [ ] Verify you are able to tip a creator who has the same custodian as you
- [ ] Verify that you are able to reset rewards
  - [ ] Verify that after rewards are reset, you are now in the non-opted in state
  - [ ] Verify you can re-join rewards and the panel, brave://rewards page, and NTP widget are now in the unverified state

### Social-media blocking settings

- [ ] Verify individual `Social media blocking` buttons works as intended when enabled/disabled by visiting https://fmarier.github.io/brave-testing/social-widgets.html
- [ ] ensure that you can log in into https://www.charthop.com while `Allow use of third-party cookies for legacy Google Sign-In` is enabled
- [ ] ensure that once `Allow use of third-party cookies for legacy Google Sign-In` has been disabled, you can't log in into https://www.charthop.com

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
- [ ] With only two devices in chain, verify removing the other device resets the sync on b-c as well

### Tor Tabs

- [ ] Visit https://check.torproject.org in a Tor window, ensure it shows a success message for using a Tor exit node
- [ ] Visit https://check.torproject.org in a Tor window, note down exit node IP address. Do a hard refresh (Ctrl+Shift+R/Cmd+Shift+R), ensure exit IP changes after page reloads
- [ ] Visit https://browserleaks.com/geo in a Tor window, ensure location isn't shown


### Profile Tests

- [ ] Verify that clicking on the "profile avatars" under both Private Browsing and Tor doesn't crash.

### Chromium/Brave GPU

- [ ] Verify that `brave://gpu` (Brave) matches `chrome://gpu` (Chrome) when using the same Chromium version

### Startup & Components

- [ ] Verify that Brave is only contacting `*.brave.com` endpoints on first launch using either `Charles Proxy`, `Fiddler`, `Wireshark` or `LittleSnitch` (or a similar application)
  - [ ] Verify that opening a NTP doesn't trigger any outbound connections related to widgets without user interaction

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
    - [ ] Connection to custodian or self custody is retained
    - [ ] BAT balance is retained
    - [ ] Recurring contributions (if set up) are retained
  - [ ] Ads
    - [ ] `Ads received this month` value is retained
    - [ ] Changes to ads settings are retained
    - [ ] Ensure that ads are not disabled when upgrading to a new version if they were enabled
    - [ ] Ensure that ads are not being enabled when upgrading to a new version if they were disabled
