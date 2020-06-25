## Process

- [ ] Request approval by reviewers for the go-update PR
- [ ] Once approved, create an issue in [`devops repository`](https://github.com/brave/devops/issues) to request deployment of the approved branch to dev environment
- [ ] Request sign-off from @qa-team by testing the changes in dev environment. To use the dev environment, you can use `--use-dev-goupdater-url` with Brave Browser.
- [ ] Merge the changes in go-update to `master`
- [ ] Create an issue in devops to request deployment of the master branch to production environment.
- [ ] Run through the test plan in the PR, once deployed in production.

## Test Plan

Running these tests in addition to the test plan specified for the issue ensures that `go-update` is working correctly.

- [ ] Open a clean brave-browser profile and verify the following components are updated correctly:
  - Brave Local Data Updater
  - Brave Ad Block Update
  - Brave Tor Client Updater (Mac/Win/Linux)
  - NTP Sponsored Images (Locale)
  - CRLSet
  - Brave SpeedReader Updater
  - Brave HTTPS Everywhere Updater

- Using little snitch/fiddler confirm that there are no direct connections to non-brave/bravesoftware domains. 
  - We don't proxy request for tor download on development server. So you'll see one request to `amazonaws.com`

- [ ] **Brave-Local-Data:** 
  - Navigate to `https://chrome.google.com/webstore/detail/1password-extension-deskt/aomjjhallfgjeglblehebfpbcfeobpgk` and confirm that the extension not verified warning is not displayed.

  ![local-data-updater](https://jumde.github.io/img/local-data-updater.png)

- [ ] **Brave Ad-Block Update:**
  - Navigate to cnn.com - and verify you are able to see ads and trackers blocked

  ![ad-block](https://jumde.github.io/img/ad-block.png)

- [ ] **Brave Tor Client Updater:**
  - Open `Private Window with Tor`
  - Navigate to `check.torproject.org` and verify tor works.

- [ ] **NTP Sponsored Images (Locale):**
  - Open 4 new-tab pages
  - Verify one of them has the sponsored image

- [ ] **CRLSet:**
  - Navigate to `https://revoked.badssl.com/` and confirm SSL warnings are displayed

- [ ] **Brave HTTPS Everywhere Updater:**
  - Navigate to `http://https-everywhere.badssl.com/` - and verify the shield count for HTTPS Everywhere is updated.
  
  ![https-everywhere](https://jumde.github.io/img/https-everywhere.png)

- [ ] **Widevine Content Decryption Module:**
  - Navigate to `https://bitmovin.com/demos/drm` - Verify that the modal to install Widevine is displayed.
  - Install Widevine
  - Navigate to brave://components and verify the component is successfully installed
  - Verify that videos play successfully


