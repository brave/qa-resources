### Installer

- [ ] Check the installer is close to the size of the last release
- [ ]  Check signature: 
  - [ ] If macOS, using x64 binary run `spctl --assess --verbose` for the installed version and make sure it returns `accepted` 
  - [ ] If macOS, using universal binary run `spctl --assess --verbose` for the installed version and make sure it returns `accepted` 
  - [ ] If Windows right click on the `brave_installer-x64.exe` and go to Properties, go to the Digital Signatures tab and double click on the signature.  Make sure it says "The digital signature is OK" in the popup window

### About pages

- [ ] Verify that both `chrome://` and `about://` forward to `brave://` (run through several internal pages)

### Importing

- [ ] Verify that you can import `History`, `Favorites/Bookmarks` and `Passwords` from Google Chrome
- [ ] Verify that you can import `History`, `Favorites/Bookmarks`, `Passwords`, `Search Engines` and `Autofill` from Firefox
- [ ] Verify that you can import `Favorites/Bookmarks` from Microsoft Edge
- [ ] Verify that importing bookmarks using `Bookmark HTML File` retains the folder structure on a clean profile

### Context menus

- [ ] Verify you can block a page element using `Block element via selector` context-menu item
- [ ] Verify selecting `Manage custom filters` opens `brave://adblock` in a NTP
- [ ] Verify removing the rule from `brave://adblock` reflects the change on the website, after reload

### Extensions/Plugins

- [ ] Verify pdfium, Torrent viewer extensions are installed automatically on fresh profile and cannot be disabled (they don't show up in `brave://extensions`)
- [ ] Verify older version of an extension gets updated to new version via Google server
- [ ] Verify older version of an extension gets updated to new version via Brave server
- [ ] Verify that `magnet` links and `.torrent` files correctly open WebTorrent and you're able to download the file(s)
  - **Tip:** Free torrents available via https://webtorrent.io/free-torrents

### Chrome Web Store (CWS)

- [ ] Verify that installing https://chrome.google.com/webstore/detail/adblock-plus-free-ad-bloc/cfhdojbkjhnklbpkdaibdccddilifddb from CWS displays the `Brave has not reviewed the extension.` warning via the "Add Extension" modal
- [ ] Verify that installing https://chrome.google.com/webstore/detail/lastpass-free-password-ma/hdokiejnpimakedhajhdlcegeplioahd from CWS doesn't display the `Brave has not reviewed the extension.` warning via the "Add Extension" modal

### PDF

- [ ] Test that you can print a PDF
- [ ] Test that PDF is loaded over HTTPS at https://basicattentiontoken.org/BasicAttentionTokenWhitePaper-4.pdf
- [ ] Test that PDF is loaded over HTTP at http://www.pdf995.com/samples/pdf.pdf
- [ ] Test that https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.105.6357&rep=rep1&type=pdf opens without issues

### Widevine

- [ ] Verify `Widevine Notification` is shown when you visit Netflix for the first time
- [ ] Test that you can stream on Netflix on a fresh profile after installing Widevine
- [ ] Verify `Widevine Notification` is shown when you visit HBO Max for the first time
- [ ] Test that you can stream on HBO Max on a fresh profile after installing Widevine
- [ ] If macOS, run the above Widevine tests for both `x64` and `universal` builds

### Geolocation

- [ ] Check that https://browserleaks.com/geo works and shows correct location
- [ ] Check that https://html5demos.com/geo/ works but doesn't require an accurate location

### Crash Reporting

- [ ] Check that loading `brave://crash` & `brave://gpucrash` causes the new tab to crash
- [ ] Check that `brave://crashes` lists the `Uploaded Crash Report ID` once the report has been submitted
- [ ] Verify the crash ID matches the report on Backtrace using `_rxid equal [ value ]`

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

### TLS Pinning

- [ ] Visit https://ssl-pinning.someblog.org/ and verify a pinning error is displayed

### Fingerprint Tests

- [ ] Visit https://jsfiddle.net/bkf50r8v/13/, ensure 3 blocked items are listed in Shields. Result window should show `got canvas fingerprint 0` and `got webgl fingerprint 00`
- [ ] Test that audio fingerprint is blocked at https://audiofingerprint.openwpm.com/ only when `Block all fingerprinting protection` is on
- [ ] Test that Brave browser isn't detected via user-agent, on https://www.whatismybrowser.com.  The site **will** say "Looks like Brave on [Windows/Linux/macOS]", and yet, "But it's announcing that it's Chrome [version] on [platform]"
- [ ] Test that https://diafygi.github.io/webrtc-ips/ doesn't leak IP address for each option under `Settings -> Privacy and Security -> WebRTC IP handling policy`

### Brave Ads

- [ ] Verify when you enable Rewards from panel or `brave://rewards`, Ads are enabled by default
- [ ] Verify Ads UI (panel, settings, etc) shows when in a region with Ads support
- [ ] Verify Ads UI (panel, settings, etc) does not show when in a region without Ads support. Verify the Ads panel does show the 'Sorry! Ads are not yet available in your region.' message.
- [ ] Verify when the system language is English, the Browser language is French, and you are in one of the supported regions, Ad notifications are still served to you.
- [ ] Verify you are served Ad notifications when Ads are enabled
  - [ ] Verify ad earnings are reflected in the rewards widget on the NTP.
- [ ] Verify when Ads are toggled off, there are no Ad messages in the logs
- [ ] Verify when Rewards are toggled off (but Ads were not explicitly toggled off), there are no Ads logs recorded
- [ ] Verify view/click/dismiss/landed ad notifications show in `confirmations.json`
- [ ] Verify pages you browse to are being classified in the logs
- [ ] Verify tokens are redeemed by viewing the logs (you can use `--rewards=debug=true` to shorten redemption time)
- [ ] Verify Ad is not shown if a tab is playing media and is only shown after it stops playing

### Rewards

- [ ] Verify that none of the reward endpoints are being contacted when a user visits a media publisher (`youtube.com`, `reddit.com`, `twitter.com`, `github.com`) and hasn't interacted with rewards
  - [ ] Verify that `rewards.brave.com`, `pcdn.brave.com`, `grant.rewards.brave.com` or `api.rewards.brave.com` are not being contacted
- [ ] Verify you are able to create a new Rewards profile.
- [ ] Verify you are able to restore an old Rewards profile.
- [ ] Verify Rewards balance shows correct BAT and USD value.
- [ ] Verify actions taken (claiming grant, tipping, auto-contribute) display in panel transactions list.
- [ ] Verify AC monthly budget shows correct BAT and USD value.
- [ ] Verify you are able to exclude a publisher from the auto-contribute table and popup list of sites.
- [ ] Verify you are able to exclude a publisher by using the toggle on the Rewards Panel.
- [ ] Verify you are able to perform an auto contribution.
  - [ ] Verify auto contribution is reflected in the rewards widget on the new-tab page (NTP).
- [ ] Verify monthly statement shows expected data.
- [ ] Verify when you click on the BR panel while on a site, the panel displays site-specific information (site favicon, domain, attention %).
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
- [ ] Verify you can tip a verified GitHub user from the panel.
- [ ] Verify you can tip a verified GitHub user via inline tip button.
  - [ ] Verify the GitHub creator displays in the auto-contribute list after specified amount of time/visits per settings.
- [ ] Verify you can tip a verified Reddit user from the panel.
- [ ] Verify you can tip a verified Reddit user via inline tip button.
- [ ] Verify if you disable auto-contribute you are still able to tip creators.
- [ ] Verify if auto-contribute is disabled AC does not occur.
- [ ] Verify if Rewards is disabled AC does not occur.
- [ ] Verify that disabling Rewards and enabling it again does not lose state.
- [ ] Adjust min visit/time in settings. Visit some sites to verify they are added to the table after the specified settings.
- [ ] Uphold cases
  - [ ] Verify you are able to connect a KYC'd Uphold account to Rewards.  
  - [ ] Verify balance in Brave updates when BAT is added to the Brave Browser card.
  - [ ] Verify if you only have user-controlled BAT (BAT in Uphold only), you can only tip KYC'd creators, any tips to non-KYC'd creators go to the Pending Contributions list.
  - [ ] Verify connected (verified but not KYC'd) publishers display messaging on panel and tip banner.
  - [ ] Verify you are able to perform an auto contribute using Uphold BAT.

### Social-media blocking settings

- [ ] Verify individual `Social media blocking` buttons works as intended when enabled/disabled by visiting https://fmarier.github.io/brave-testing/social-widgets.html
- [ ] visit `brave://settings/privacy` -> `Site and Shields Settings` -> `Cookies and site data` and ensure that
  - [ ] both `https://[*.]firebaseapp.com` & `https://accounts.google.com` are added into `Sites that can always use cookies` when `Allow Google login buttons on third party sites` is enabled
  - [ ] both `https://[*.]firebaseapp.com` & `https://accounts.google.com` are removed from `Sites that can always use cookies` when `Allow Google login buttons on third party sites` is disabled
- [ ] ensure that you can log in into https://www.expensify.com while `Allow Google login buttons on third party sites` is enabled
- [ ] ensure that once `Allow Google login buttons on third party sites` has been disabled, you can't log in into https://www.expensify.com

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
- [ ] Visit https://check.torproject.org in a Tor window, note down exit node IP address. Click `New Tor connection for this site` in app menu, ensure the exit node IP address changes after page is reloaded
- [ ] Visit https://protonmailrmez3lotccipshtkleegetolb73fuirgj7r4o4vfu7ozyd.onion, https://brave4u7jddbv7cyviptqjc7jusxh72uik7zt6adtckl5f4nwy2v72qd.onion/, and https://search.brave4u7jddbv7cyviptqjc7jusxh72uik7zt6adtckl5f4nwy2v72qd.onion/ in a Tor window and ensure all pages resolve
- [ ] Visit https://browserleaks.com/geo in a Tor window, ensure location isn't shown
- [ ] Verify Torrent viewer doesn't load in a Tor window
- [ ] Ensure you are able to download a file in a Tor window. Verify all Download/Cancel, Download/Retry and Download works in Tor window

### Cookie and Cache

- [ ] Go to http://samy.pl/evercookie/ and set an evercookie. Check that going to prefs, clearing site data and cache, and going back to the evercookie site does not remember the old evercookie value

### Chromium/Brave GPU

- [ ] Verify that `brave://gpu` (Brave) matches `chrome://gpu` (Chrome) when using the same Chromium version

### Startup & Components

- [ ] Verify that Brave is only contacting `*.brave.com` endpoints on first launch using either `Charles Proxy`, `Fiddler`, `Wireshark` or `LittleSnitch` (or a similar application)
  - [ ] Verify that opening a NTP doesn't trigger any outbound connections related to widgets without user interaction
- [ ] Remove the following component folders and ensure that they're being re-downloaded after restarting the browser:
  - [ ] `afalakplffnnnlkncjhbmahjfjhmlkal`: `AutoplayWhitelist.dat`, `ExtensionWhitelist.dat`, `ReferrerWhitelist.json` and `Greaselion.json`
  - [ ] `CertificateRevocation`
  - [ ] `cffkpbalmllkdoenhmdmpbkajipdjfam`: `rs-ABPFilterParserData.dat` & `regional_catalog.json` (AdBlock)
  - [ ] `gccbbckogglekeggclmmekihdgdpdgoe`: (Sponsored New Tab Images)
  - [ ] `jicbkmdloagakknpihibphagfckhjdih`: `speedreader-updater.dat`
  - [ ] `oofiananboodjbbmdelgdommihjbkfag`: HTTPSE
  - [ ] `Safe Browsing`
- [ ] Restart the browser, load `brave://components`, wait for 8 mins and verify that no component shows any errors

**Note:** Always double check `brave://components` to make sure there's no errors/missing version numbers

### Session storage

- [ ] Temporarily move away your browser profile and test that a new profile is created on browser relaunch
  - macOS - `~/Library/Application\ Support/BraveSoftware/`
  - Windows - `%userprofile%\appdata\Local\BraveSoftware\`
  - Linux(Ubuntu) - `~/.config/BraveSoftware/`
- [ ] Test that both windows and tabs are being restored, including the current active tab
- [ ] Ensure that tabs are being lazy loaded when a previous session is being restored

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

## Hardware Wallet Test (To be checked on each major CR bump)

- [ ] Verify you can link hardware wallet using Trezor and unlock the wallet
- [ ] Verify you can link hardware wallet using Ledger Nano and unlock the wallet
- [ ] Verify you can perform a transaction with hardware wallet using Ledger Nano or Trezor
