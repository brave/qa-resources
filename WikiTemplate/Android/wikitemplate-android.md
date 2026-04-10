
## Installer

- [ ] Verify that the installer's file size is approximately the same as the most recent release.
- [ ] Verify that the Brave version displayed in the `About` section matches precisely what is anticipated.

## Startup

- [ ] Verify that, upon its initial startup, Brave exclusively communicates with `*.brave.com` endpoints by monitoring network traffic through a tool such as Charles Proxy, Fiddler, Wireshark, or a comparable application.
  - [ ] Verify that opening a New Tab Page (NTP) does not initiate any outbound connections related to widgets in the absence of user interaction.

## Visual look

- [ ] Verify that after each merge:
  - [ ] No Chrome/Chromium references appear on `brave://version`.
  - [ ] No Chrome/Chromium references appear in normal or private tabs.
  - [ ] No Chrome/Chromium references appear in site permission settings for `Location`, `Camera`, `Microphone`, or `Augmented Reality`.
  - [ ] No Chrome/Chromium icons are displayed in normal or private tabs.

## Custom tabs

- [ ] Verify that Brave correctly handles links opened from Gmail, Slack or another messaging app.
- [ ] Verify that custom tabs function properly regardless of whether sync is enabled or disabled.

## Tabs and Tab Groups

- [ ] Verify that `Automatically open tab groups from other devices` is disabled by default.
  - [ ] Verify that the setting does not reset to its default value after being modified and the browser is restarted.
- [ ] Verify that `Only open links in current tab group` is disabled by default.
  - [ ] Verify that the setting does not reset to its default value after being modified and the browser is restarted.

## Developer Tools

- [ ] Verify that sub-links can be inspected using developer tools.

## Clear Data

- [ ] Verify that the `Clear data on exit` feature functions correctly as expected.

## Appearance Settings

- [ ] Verify that the `hamburger menu` and `share menu` contain no unexpected or unwanted items.
- [ ] Verify that modified default settings are saved correctly and do not result in any browser crashes.
- [ ] Verify that the `top address bar` + `bottom navigation bar` are enabled by default.
  - [ ] Verify that the `bottom address bar` can be enabled.
  - [ ] Verify that the `bottom navigation bar` buttons function properly.
- [ ] Verify that the `toolbar shortcut` is turned off by default and that it can be switched on.
  - [ ] Verify that modifying `toolbar shortcut` settings and relaunching the browser does not alter it.

## Unstoppable Domains, ENS and SNS

- [ ] Verify that the configuration options for `Unstoppable Domains`, `ENS`, and `SNS` are visible in the settings and that any modifications made to them remain saved after restarting the browser.

## Downloads

- [ ] Verify that file downloads function correctly and that all actions on the download item work as expected.
  - [ ] Verify that the audio file from https://pixabay.com/music/ is successfully downloaded.
  - [ ] Verify that the image from https://unsplash.com/ is successfully downloaded.
- [ ] Verify that a PDF is successfully downloaded over HTTPS at `https://basicattentiontoken.org/BasicAttentionTokenWhitePaper-4.pdf`.
- [ ] Verify that a PDF is successfully downloaded over HTTP at `http://www.pdf995.com/samples/pdf.pdf`.

## Bravery settings

- [ ] Verify that HTTPS Everywhere is functioning correctly by navigating to `http://https-everywhere.badssl.com/`.
- [ ] Verify that disabling both HTTPS Everywhere and Shields prevents the automatic redirect to `https://https-everywhere.badssl.com/`.
- [ ] Verify that toggling between blocking and allowing ads behaves as expected.
- [ ] Verify that it is possible to proceed past a certificate error on `https://badssl.com/`.
- [ ] Verify that Safe Browsing protection is active by visiting `https://testsafebrowsing.appspot.com`.
- [ ] Verify that enabling script blocking in the settings prevents content from loading on `https://x.com/`, and that disabling `Block scripts` through `Brave Shields` restores full functionality.
- [ ] Verify that default Bravery settings are applied on pages without custom site settings.
- [ ] Verify that third-party storage values are empty at `https://jsfiddle.net/7ke9r14a/7/` when third-party cookies are blocked.
- [ ] Verify that your ISP's DNS resolvers are neither detected nor displayed; only your selected `DoH` provider should appear. To test this, choose a DNS provider under `Settings → Brave Shields & privacy → Use secure DNS` and visit `https://browserleaks.com/dns`.
- [ ] Verify that results match expectations for all six test configurations by running them on `https://dev-pages.brave.software/storage/ephemeral-storage.html`.

### Fingerprint Tests

- [ ] Verify that 2 blocked items are listed in `Brave Shields` by visiting `https://browserleaks.com/webrtc`.
- [ ] Verify that `https://diafygi.github.io/webrtc-ips/` does not expose the user's IP address for any option listed under `Settings → Brave Shields & privacy → WebRTC IP handling policy`.

### Query Filter

- [ ] Verify that the results match expectations for each test by visiting `https://fmarier.github.io/brave-testing/query-filter.html` in a `Private tab` and following the provided test instructions.

## Content Tests

- [ ] Verify that context menus function correctly in the new X (Twitter) tab by navigating to `https://brianbondy.com/` and tapping the Twitter icon at the bottom of the page.
- [ ] Verify that passwords can be saved by visiting `https://feedly.com` or `https://todoist.com` and signing in to your account. Confirm that the saved password is automatically populated on subsequent visits to the site when signed out.
- [ ] Verify that `https://mixed-script.badssl.com/` displays as grey rather than red, confirming that no mixed content scripts are executed.

## Brave Rewards

- [ ] Verify that no reward-related endpoints are called when a user visits a media platform (such as YouTube, Reddit, or X) without having joined Rewards.
  - [ ] Verify that none of the following domains are contacted: `rewards.brave.com`, `pcdn.brave.com`, `grant.rewards.brave.com`, or `api.rewards.brave.com`.
- [ ] Verify that a new Rewards profile can be created successfully and that it begins in an unverified state by default.
  - [ ] Verify that when visiting a creator in this state, the Rewards UI prompts the user to connect a custodian and does not display any BAT-related data (such as earnings or balance).
  - [ ] Verify that navigating to the Rewards UI in this state allows the user to scroll down to the `Explore` section.
  - [ ] Verify that cards are displayed correctly in the Rewards UI through the `Explore` section.
  - [ ] Verify that ad type toggles can be enabled and disabled from the `Ads Settings` panel in the Rewards UI.
- [ ] Verify that users can successfully link a custodian or opt for self-custody.
  - [ ] Verify that the Rewards balance reflects the correct BAT amount after connecting a custodian.
  - [ ] Verify that tapping the Rewards icon on a verified creator's site displays a `Contribute` button.
  - [ ] Verify that tapping the Rewards icon on a non-verified creator's site does not display a `Contribute` button.
  - [ ] Verify that tipping is available when the creator shares the same custodian as the user.
  - [ ] Verify that no `Disconnect` option is available once a custodian has been connected.
- [ ] Verify that the Rewards profile can be reset successfully.
  - [ ] Verify that after resetting, the profile returns to a non-opted-in state.
  - [ ] Verify that rejoining Rewards returns the Rewards UI to an unverified state.

## Brave Ads

- [ ] Verify that ads are automatically activated once Rewards are turned on in eligible regions.
- [ ] Verify that by default ads are displayed only when the app is in use.
- [ ] Verify that ad notifications are displayed according to the configured ads per hour frequency.
- [ ] Verify that multiple ad notifications accumulate in the notification tray.
- [ ] Verify that swiping left or right on an ad notification dismisses it and removes it from the notification tray.
- [ ] Verify that tapping an ad notification opens its corresponding landing page.
- [ ] Verify that the `view`, `clicked`, `landed`, and `dismiss` states are properly recorded based on user interaction.

## Sync

- [ ] Verify that joining the Sync chain by scanning the QR code works as expected.
- [ ] Verify that joining the Sync chain using code words works as expected.
- [ ] Verify that it is possible to create a Sync chain with only one device.
- [ ] Verify that you can set up a Sync chain on the device and connect additional devices using either a QR code or code words.
- [ ] Verify that once the Sync chain is set up, only `Bookmarks` and `Passwords` are enabled by default under `Sync Options`.
- [ ] Verify that toggling `Sync everything` on will activate all other switches.
- [ ] Verify that bookmarks created before joining the Sync chain are also synchronized across all connected devices.
- [ ] Verify that `Autofill` data is synchronized to all devices when the option is turned on.
- [ ] Verify that `History` is synchronized across all devices and that tabs from other devices are displayed there.
- [ ] Verify that `Open tabs` data synchronizes properly and that tabs currently open on other devices appear in `Recent tabs` under the name of their respective device.
- [ ] Verify that `Password` data is synchronized across all devices.
- [ ] Verify that `Settings` successfully syncs site settings across all devices.
- [ ] Verify that a bookmark added from a `custom tab` gets synchronized across all devices in the chain.
- [ ] Verify that selecting `Remove this device` triggers a confirmation prompt before removing the device from the sync chain.

## Top sites view

- [ ] Verify that tapping and holding a Top site brings up a context menu containing a removal option. Keep in mind that removing a site is permanent and will stop it from showing up in Top sites — only remove sites you don't need.
- [ ] Verify that Top sites can be pinned and rearranged.

## Session storage

- [ ] Verify that tabs are recovered after being closed, including the currently active tab.

## Upgrade from previous version

Examples of pre-requisites before upgrading from the previous version to the build being tested:

 * visit several websites so `Top Tiles` under New Tab Page gets updated/populated
 * add several websites to the Android home screen via `Add to Home screen` (from the hamburger/setting menu)
 * add several bookmarks including folders
 * change/update several settings (Example: default search engine, adding a custom home page, changing site settings, changing several privacy settings, etc..)
 * create/enable a Brave Wallet (or restore if an individual who's going through the upgrade has one available)
 * enable Brave News and add/remove several sources
 * change the default shield settings on various websites (Example: enable script blocking/change FP/Ad blocking to strict, disable shields)
 * Login into several websites and leave them opened
 * Login into several websites and close the tabs so they're not opened when upgrading
 * Login into a website and leave it as the active tab while upgrading
 * enable/create a sync chain with several devices

 **`Upgrade Cases`**

- [ ] Verify that `brave://version` shows the right Brave and Chromium versions.
- [ ] Verify that bookmarks and folders from the prior release are intact and accessible.
- [ ] Verify that previously open tabs are preserved and load correctly when accessed.
  - [ ] Verify that the correct website appears as the active tab after upgrading.
  - [ ] Verify that websites you were logged into while upgrading remain authenticated (cookies should be intact).
  - [ ] Verify that websites you were logged into but had closed before upgrading still retain your login when reopened.
  - [ ] Verify that websites you were previously logged into open in a logged-out state after an upgrade, if `Shred site's data` was enabled.
- [ ] Verify that per-site Shields settings from the previous version are still in place after upgrading.
- [ ] Verify that saved passwords appear under `Settings` -> `Brave Password Manager` and autofill works properly.
- [ ] Verify that the Sync chain is intact and continues to sync across all connected devices.
  - [ ] Verify that sending links/tabs via `Send to devices` functions as expected.
  - [ ] Verify that any new bookmarks added after the upgrade are synced across all devices in the chain.
- [ ] Verify that Brave News remains enabled and any source customizations from before are preserved.
- [ ] Verify that configuration changes made in `Settings` have carried over (e.g., script blocking, fingerprinting/ad blocking set to strict, disabled shields).
  - [ ] Verify that Unstoppable Domains, ENS, and SNS settings are unchanged from the previous version.
- [ ] Verify that browsing `History` has been retained.
- [ ] Verify that website shortcuts added via `Add to Home screen` are still visible on the Android home screen and open the correct pages.
- [ ] Verify that Brave widgets remain on the Android home screen and function correctly.
- [ ] Verify that the `Tabs and tab groups` setting remains unchanged after the upgrade.
- [ ] Verify that the `Appearance` settings have not changed following the upgrade:
  - [ ] `Customize menu` retains the same configuration it had prior to upgrading.
  - [ ] `Toolbar shortcut` is still enabled and the previously selected shortcut remains the same.
  - [ ] `Address bar` position is the same as it was before the upgrade.
  - [ ] `Only open links in current tab group` status has not been toggled from its previous state.
- [ ] Verify that the `Clear data on exit` preference is preserved.
- [ ] Rewards:
  - [ ] Verify that Custodian or self-custody connection is maintained.
  - [ ] Verify that BAT balance remains intact.
  - [ ] Verify that any recurring contributions that were set up are still active.
- [ ] Ads:
  - [ ] Verify that the `Ads received this month` count is retained after the upgrade.
  - [ ] Verify that any modifications to ads settings are preserved after the upgrade.
  - [ ] Verify if ads were enabled before upgrading remain enabled after the upgrade.
  - [ ] Verify if ads were disabled before upgrading remain disabled after the upgrade.
