## Tor Client Updater

- [ ] For development go-update-server. Run brave-browser with `--user-data-dir=component-dev --use-dev-goupdater-url` (These flags are only available in v1.7.x). Once the crx is pushed to production run without these flags.
- [ ] Navigate to `brave://components` and verify `Tor Client Updater (OS)` is updated successfully.
- [ ] Open `New Private Window with Tor` and confirm that it starts without any errors.
	- [ ] Navigate to `check.torproject.org` and verify that tor is working successfully.
	- [ ] Navigate to `brave.com` and `http://brave4u7jddbv7cyviptqjc7jusxh72uik7zt6adtckl5f4nwy2v72qd.onion/` to check if the sites work correctly.
- [ ] Load `brave.com` and `mail.protonmail.com` in a regular Window/Tab and ensure that clicking the `Tor` button in the URL bar correctly launches a Tor window and opens the appropriate `.onion` website.

### Windows
- [ ] Setup Windows SDK by downloading - https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk/
- [ ] Run `"C:\Program Files (x86)\Windows Kits\10\bin\x86\signtool.exe" verify /pa "C:\Users\<user>\AppData\Local\BraveSoftware\Brave-Browser-<channel>\User Data\cpoalefficncklhjfpglfiplenlpccdb\<version>\tor-<version-tor>-win-brave-<version-brave>.exe"` to verify if the signature of the binary is correct.

### MacOS
- [ ] Navigate to `/Users/<user>/Library/Application Support/BraveSoftware/Brave-Browser-<channel>/cldoidikboihgcjfkhdeidbpclkineef/<version>`
- [ ] Run `codesign -vvvv tor-<version-tor>-darwin-brave-<version-brave>` to confirm codesign is valid
- [ ] For MacOS Catalina (10.15+) - Run `spctl -a -vv -t install tor-<version-tor>-darwin-brave-<version-brave>` to verify that the binary is notarized.

### Linux
- [ ] Navigate to `<user-data-dir>/biahpgbdmdkfgndcmfiipgcebobojjkp`
- [ ] Run `ldd tor-<version-tor>-linux-brave-<version-brave>` to confirm tor client is a static binary
