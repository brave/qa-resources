# IPFS on Desktop


## Installation & Setup

   ### `IPFS installation`

   - [ ] Verify going to `brave://ipfs` and clicking on `Install and start` installs and shows the latest [`go-ipfs` release](https://github.com/ipfs/go-ipfs/blob/master/CHANGELOG.md), via the `Version:` section under `Node info`.

   ### `Seed profile`

  - [ ] Load `ipns://en.wikipedia-on-ipfs.org`.
  - [ ] Choose `Use a local node`.
  - [ ] Run the `IPNS Keys` (add/rotate) section.
  - [ ] Run the `Import and Sharing` (page, image, text, video) section.

   ### `go-updater node update`

  - [ ] Verify, using the above profile, that restarting Brave with `--use-dev-goupdater-url`, and clicking on `Restart` via `brave://ipfs` downloads and installs the latest in-development (release) candidate.
  - [ ] Confirm that `Method to resolve IPFS resources` is `Local node` in `brave://settings/ipfs`.
  - [ ] Confirm that keys and imports are intact, post-migration.
  - [ ] Confirm that `brave://ipfs-internals` shows `Node is not running` under `IPFS node status`, with a `Start` button.
  - [ ] Click on `Start`.
  - [ ] Confirm the node starts, and paths and version info are correct.

   ### `Config`

  - [ ] Verify changing `Maximum IPFS cache size (GB)` on the `brave://settings/ipfs` page (set `Method to resolve IPFS resources` to `Local node` on `brave://settings/ipfs`), the new value is reflected on the diagnostic page (`brave://ipfs`) in the `Repo Stats -> Size` section.

## Diagnostic page (`brave://ipfs`)

- [ ] Verify loading `brave://ipfs` redirects to `brave://ipfs-internals`.
- [ ] Verify, on a clean profile, visiting `brave://ipfs` will present you with an `Install and start` button, which will install and start an IPFS local node.  Confirm you see `Node is running` under `IPFS node status`, `Stop`, `Restart`, and `My Node` buttons, and a dynamically updating `Connected peers:` count.
- [ ] Verify that clicking `Stop` temporarily clears all statistics, paths, and config information.
- [ ] Verify that clicking `Start` populates all statistics, paths, and config information, and you see `Stop`, `Restart`, and `My Node` buttons, along with a dynamically updating `Connected peers:` count.
- [ ] Verify that clicking `Restart` clears and then repopulates all stats, paths, and config information, and you see `Stop`, `Restart`, and `My Node` buttons, along with a dynamically updating `Connected peers:` count.
- [ ] Verify that clicking on `(details)` to the right of `Connected peers:` takes you to the `PEERS` pane of `127.0.0.1:45002/ipfs/bafy..../#/` and you see a global map with a dynamically updating peer count and listing, below.
- [ ] Verify that clicking on `Perform a garbage collection sweep` resets and repopulates the `Objects:` and `Size:` stats beneath `Repo Stats`.
- [ ] Verify that clicking `My Node` takes you to the `Status` pane of the IPFS dashboard, with a URL similar to `127.0.0.1:45002/ipfs/bafy..../#/`, where you see `Connected to IPFS`, MB count of files shared, and dynamically updating peers count, as well as your `PEER ID` and `AGENT`.

## Import and Sharing

- [ ] Prerequisites: local node launched and local gateway configured.  On a new profile, loading `ipns://en.wikipedia-on-ipfs.org` and clicking `Use a local node` on the interstitial page will set you up.

   ### `Importing a page via IPFS`

   - [ ] Load `wikipedia.org`. Context-click the page and select `Import to IPFS > This page`.
   - [ ] Verify the content is downloaded and imported successfully.
   - [ ] Verify the import folder is opened upon successful import.
   - [ ] Verify the shareable link is copied to the clipboard and opens when pasting it into a new tab.

   ### `Importing linked content`

   - [ ] Load `https://search.brave.com/search?q=hiddenmickeys&source=desktop`.  Context-click the first link there and select `Import to IPFS > Linked content`.
   - [ ] Verify the content is downloaded and imported successfully.
   - [ ] Verify the import folder is opened upon successful import.
   - [ ] Verify the shareable link is copied to the clipboard and opens when pasting it into a new tab.

   ### `Importing selected audio`

   - [ ] Load `https://samplelib.com/sample-mp3.html`.  Context-click any audio file and select `Import to IPFS > Selected audio`.
   - [ ] Verify the audio is downloaded and imported successfully.
   - [ ] Verify the import folder opens upon successful import.
   - [ ] Verify the shareable link is copied to the clipboard and opens when pasting it into a new tab.

   ### `Importing selected image`

   - [ ] Verify you are able to import an image by visiting `search.brave.com`, right-clicking on the logo, and choosing `Import to IPFS > Selected image.`
   - [ ] Verify the image is downloaded and imported successfully.
   - [ ] Verify the import folder opens upon successful import.
   - [ ] Verify the shareable link is copied to the clipboard, and pasting the link in a new tab opens it.

   ### `Importing selected text`

   - [ ] Load `https://lipsum.com/` and make a text selection.  Context-click and choose `Import Selected Text to IPFS`.
   - [ ] Verify the text is wrapped into a file with id like `file_1` and the imported text is readable inside the file.
   - [ ] Verify the import folder opens upon successful import.
   - [ ] Verify the shareable link is copied to the clipboard and opens when pasting it into a new tab.

   ### `Importing selected video`

   - [ ] Load the [Big Buck Bunny test file](https://upload.wikimedia.org/wikipedia/commons/c/c0/Big_Buck_Bunny_4K.webm). Verify you are able to import the video via context menu `Import to IPFS > Selected video`.
   - [ ] Verify the video is downloaded and imported successfully.
   - [ ] Verify the import folder opens upon successful import.
   - [ ] Verify the shareable link is copied to the clipboard and opens when pasting in a new tab.

   Note: For the other types, downloading from the IPFS webui (My Node) and ensuring they still play in a media player, is enough.

   ### `Sharing a local file using IPFS (without IPNS keys)`

   - [ ] Verify the IPFS item is available in the main app menu. Go to `IPFS -> Share Local File Using IPFS` select and import any local file.
   - [ ] Verify the file is downloaded and imported successfully,
   - [ ] Verify the import folder is opened upon successful completion.
   - [ ] Verify the shareable link starting with `https://dweb.link/ipfs/` is copied to the clipboard, and opens when pasting into a new tab.
   - [ ] Share the following filetypes:
       - [ ] .avi
       - [ ] .txt
       - [ ] .json
       - [ ] .mpeg
       - [ ] .mp3
       - [ ] .mp4
       - [ ] .ogg
       - [ ] .wav
       - [ ] .webm

   ### `Sharing a local folder using IPFS (without IPNS keys)`

   - [ ] Go to `IPFS -> share Local Folder Using IPFS`, and select and import any local folder.
   - [ ] Verify the whole folder is downloaded and imported successfully.
   - [ ] Verify the import folder opens upon successful import.
   - [ ] Verify the shareable link is copied to the clipboard, and opens when pasting into a new tab.

## Address bar

### Badge shown only when IPFS support is enabled

- [ ] Verify, on a new profile, you can load `https://en.wikipedia-on-ipfs.org`, switch `Method to resolve IPFS resources` to either `Gateway` or `Local node` in `brave://settings/ipfs`, and then see an `Open using IPFS` badge/icon in the URL bar.


### Badge on a public gateway

- [ ] Verify that loading `https://dweb.link/ipfs/QmT5NvUtoM5nWFfrQdVrFtvGfKFmG7AHE8P34isapyhCxX/wiki/Mars.html` redirects you seamlessly to `https://bafybeicgmdpvw4duutrmdxl4a7gc52sxyuk7nz5gby77afwdteh3jc5bqa.ipfs.dweb.link/wiki/Mars.html`, and there's an `Open using IPFS` badge/button in the URL bar.  Confirm that clicking `Open using IPFS` goes to `ipfs://bafybeicgmdpvw4duutrmdxl4a7gc52sxyuk7nz5gby77afwdteh3jc5bqa/wiki/Mars.html`.
- [ ] Verify that loading `https://ipfs.io/ipns/libp2p.io/` shows an `Open using IPFS` button in the URL bar, and clicking it redirects to `ipns://libp2p.io/`.  Confirm it resolves and loads.

### Badge on DNSlink websites

- [ ] Verify clicking on `Open using IPFS` on `https://en.wikipedia-on-ipfs.org/wiki/Asia/#Economy` loads `ipns://en.wikipedia-on-ipfs.org/wiki/Asia/#Economy` in a new tab.
- [ ] Verify clicking on `Open using IPFS` on `https://blog.ipfs.io/24-uncensorable-wikipedia` loads `ipns://blog.ipfs.io/24-uncensorable-wikipedia/` in a new tab.

### Protocol info popup

- [ ] Load `ipns://brantly.eth` while using `Local node` for the resolver, and confirm there's a clickable info badge "IPFS" to the left of the URL, with on click pop-up that says `This content was loaded over the IPFS protocol.`

## Automatic redirects to IPFS

- [ ] Via `brave://settings/ipfs`, set `Redirect IPFS resources to the configured IPFS gateway` to `On`.
  - [ ] Load `https://ipfs.io/ipfs/QmbWqxBEKC3P8tqsKc98xmWNzrzDtRLMiMPL8wBuTGsMnR` and confirm it redirects to `ipfs://bafybeigdyrzt5sfp7udm7hu76uh7y26nf3efuylqabf3oclgtqy55fbzdi`.
  - [ ] Load  `https://en.wikipedia-on-ipfs.org/wiki/` and confirm it redirects to `ipns://en.wikipedia-on-ipfs.org/wiki/`.


## IPFS Companion

- [ ] Verify that toggling `IPFS Companion` to `On` via `brave://settings/ipfs` prompts you to install the extension.  After clicking `Add extension`, confirm you get a notification that IPFS Companion was added to Brave, and are then taken to the `Set your IPFS preference` interstitial page.
- [ ] Verify that clicking on the puzzle-piece icon on the browser toolbar, then `IPFS Companion`, will load a popup.
  - [ ] Click on the gears (settings) icon and confirm it loads the `Companion Preferences` page.
  - [ ] Click on `My Node` and confirm it opens the same ipfs-webui interface as `My Node` at `brave://ipfs-internals`

## IPFS URLs

- [ ] Ensure each of the following IPFS URLs load over both `Gateway` and `Local node` modes:
    - [ ] `ipfs://bafybeiemxf5abjwjbikoz4mc3a3dla6ual3jsgpdr4cjr3oz3evfyavhwq/wiki/Vincent_van_Gogh.html#Life`
    - [ ] `ipfs://bafybeigdyrzt5sfp7udm7hu76uh7y26nf3efuylqabf3oclgtqy55fbzdi/`
    - [ ] `ipfs://QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/Tokyo_National_Museum.html`
    - [ ] `ipfs:QmYwAPJzv5CZsnA625s3Xf2nemtYgPpHdWEz79ojWnPbdG/readme`

## IPNS URLs

- [ ] Ensure each of the following IPNS URLs load over both `Gateway` and `Local node` modes:
   - [ ] `ipns://en.wikipedia-on-ipfs.org`
   - [ ] `ipns://en.wikipedia-on-ipfs.org/wiki/Tokyo#Islands`
   - [ ] `ipns://docs.ipfs.io`
   - [ ] `ipns://brantly.eth` (ENS)
   - [ ] `ipns://brave.crypto` (Unstoppable Domains)

## Gateway choice

## The interstitial page

- [ ] Confirm a fresh profile has `Method to resolve IPFS resources` set to `Ask` in `brave://settings/ipfs`.
  - [ ] Verify visiting `ipfs://bafybeigdyrzt5sfp7udm7hu76uh7y26nf3efuylqabf3oclgtqy55fbzdi` loads the interstitial page.
  - [ ] Verify visiting `ipns://en.wikipedia-on-ipfs.org` in a new tab loads the same interstitial page.
    - [ ] Verify selecting `Use a public gateway` loads `https://cf-ipfs.com/ipns/en.wikipedia-on-ipfs.org/wiki/` which then redirect to unique Origin at `https://en-wikipedia--on--ipfs-org.ipns.cf-ipfs.com/wiki/`.
    - [ ] Verify selecting `Use local node` loads `ipns://en.wikipedia-on-ipfs.org/wiki/`.

### Public Path gateway

- [ ] Verify, on a new profile, you can't change the IPFS public gateway address to `https://cloudflare-ipfs.com/` via `Settings -> IPFS -> IPFS public gateway address -> Change`.
- [ ] An error stating `Only a valid IPFS gateway with Origin isolation enabled can be used in Brave` is displayed ([example](https://github.com/brave/brave-browser/issues/18212#issuecomment-923632150)).

### Public Subdomain Gateway

- [ ] Verify, on a new profile, you can change the IPFS public gateway address to `https://cf-ipfs.com/` via `Settings -> IPFS -> IPFS public gateway address
 -> Change`.
- [ ] Verify opening `ipns://en.wikipedia-on-ipfs.org/wiki/` and selecting `Use a public gateway` loads `https://cf-ipfs.com/ipns/en.wikipedia-on-ipfs.org/wiki/` which then redirect to unique Origin at `https://en-wikipedia--on--ipfs-org.ipns.cf-ipfs.com/wiki/` Verify  loads `https://cf-ipfs.com/ipns/en.wikipedia-on-ipfs.org/wiki/` which then redirect to unique Origin at `https://en-wikipedia--on--ipfs-org.ipns.cf-ipfs.com/wiki/`.

### Protocol system handler/OS integration

#### ipfs://

- [ ] Verify (`Windows`) that pressing `Win+R`, typing `open ipfs://bafkreigcnxudvpojjfwncmauociy5q46zsq46oe66cxbyzie3imabuoege`, and pressing `Enter` opens Brave and loads an HTML page with the word `PASS`.
- [ ] Verify (`macOS`): opening Terminal, and typing `open ipfs://bafkreigcnxudvpojjfwncmauociy5q46zsq46oe66cxbyzie3imabuoege`, and pressing `Enter` opens Brave and loads an HTML page with the word `PASS`.
- [ ] Verify (`Linux`) that opening a shell and typing `xdg-open ipfs://bafkreigcnxudvpojjfwncmauociy5q46zsq46oe66cxbyzie3imabuoege` and pressing `Enter` opens Brave and loads an HTML page with the word `PASS`.

#### ipns://

- [ ] Verify (`Windows`) that pressing `Win+R`, typing `open ipns://en.wikipedia-on-ipfs.org/wiki/Tokyo#Islands`, and pressing `Enter` opens Brave and loads an HTML page scrolled to the header `Islands`.
- [ ] Verify (`macOS`): opening Terminal, and typing `open ipns://en.wikipedia-on-ipfs.org/wiki/Tokyo#Islands`, and pressing `Enter` opens Brave and loads an HTML page scrolled to the header `Islands`.
- [ ] Verify (`Linux`) that opening a shell and typing `xdg-open ipns://en.wikipedia-on-ipfs.org/wiki/Tokyo#Islands`, and pressing `Enter` opens Brave and loads an HTML page scrolled to the header `Islands`.


## Peers

- [ ] Prerequisites: local node launched and local gateway configured on two machines, locally networked (LAN, can be over Wi-Fi).

   ### `Adding`; see [issue 15567](https://github.com/brave/brave-browser/issues/15567#issuecomment-867983572) for full setup steps

   - [ ] Verify when you go to `brave://settings/ipfs/peers` and click on the `Add` button, it prompts you to enter a new peer-connection string. Confirm that entering an incorrect string yields `This name is not valid` upon clicking `Submit`. (Acceptable ones are only CIDs or something like `**/p2p/**` format.)
   - [ ] Verify if a peer is added and node is started, it proposes to restart node to apply changes.
   - [ ] Verify the local node is restarted by clicking `Restart` button; happen it shows error message and suggests to see more on diagnostic page.
   - [ ] Verify that `Peering.Peers` section of IPFS node config file got updated (either via `My Node → Settings → IPFS Config` or by manually inspecting `brave_ipfs/config` file).

   ### `Removing`

   - [ ] Verify a peer can be removed by clicking on the Trash icon in the peer line.

## IPNS Keys

- [ ] Prerequisites: local node launched and local gateway configured. Go to `Settings -> IPFS`, there should be an available `Set up your IPNS keys` option, which opens `brave://settings/ipfs/keys`

   ### `Publishing a local file using an IPNS key`

   - [ ] (after [brave/brave-browser#16998](https://github.com/brave/brave-browser/issues/16998) lands) Verify you're able to share a local file via `IPFS -> Share local file using IPNS -> self`.
   - [ ] Verify once the file is imported, the import folder is opened and the file can be downloaded.
   - [ ] Once the import is successful, verify a shareable link starting with `https://dweb.link/ipns/` is copied to the clipboard by opening a new tab and pasting from the context menu or `CTRL+V`.
   - [ ] Verify you see the IPNS key (e.g. `k51q...`) before the `?filename=filename.ext` from the copied text.

   ### `Publishing a local folder using an IPNS key`

   - [ ] (after [brave/brave-browser#16998](https://github.com/brave/brave-browser/issues/16998) lands) Verify you're able to share a local file via `IPFS > Share local folder using IPNS -> self`.
   - [ ] Verify once the file is imported, the import folder is opened and the file can be downloaded.
   - [ ] Once the import is successful, verify a shareable link starting with `https://dweb.link/ipns/` is copied to clipboard by opening a new tab and pasting from context menu or `CTRL+V`.
   - [ ] Verify you see the IPNS key (e.g. `k51q...`) before the `?filename=filename.ext` from the copied text.

   ### `Importing keys`

   - [ ] Verify adding a new key by clicking on the `Import` button and choosing an existing key file to import.
   - [ ] Verify imported key is available with entered name; verify entering `self` will yield `This name cannot be used`.
   - [ ] Verify you cannot import keys with the same name; each key name must be unique.

   ### `Publishing content with IPNS key`

   - [ ] Verify keys are available in all import menus in order to pin content by selected key; the import link should contain the selected key.

   ### `Add/Remove/Rotate keys`

   - [ ] Verify when you click `Add`, it prompts for a key name and generates a new key.
   - [ ] Verify clicking on `Add` and entering an existing key name shows a `This name cannot be used` error message.
   - [ ] Verify clicking on the Rotate key icon for the `self` key prompts for a key name.  Enter a valid, unique name and click `Rotate`.  Confirm the key is created with your entered name, original hash, and a new `self` key (with a new hash value) is generated.
   - [ ] Verify clicking on the 3-dots menu to the right of a key gives you two options: `Export key` and `Remove key`.  Choose `Export key` and confirm you get prompted to save the key.  Click `Save` and ensure the key is saved to disk. Delete the key from `brave://settings/ipfs/keys` and now click `Add` to confirm the same key as the original is added from disk.
   - [ ] Verify clicking on the 3-dots menu and choosing `Remove key` removes the key from the UI.

***

# IPFS on Android

### `Public Gateway Setting`

- [ ] Verify `IPFS Gateway` option is available under `Brave Shields & Privacy`.
- [ ] Verify the setting is enabled by default.
- [ ] Verify disable/enable setting is retained between browser launch/restarts.
- [ ] Verify setting state is retained during upgrade.
- [ ] Verify you can't change the IPFS public gateway address to `https://cloudflare-ipfs.com/` (An error `Only a valid IPFS gateway with Origin isolation enabled can be used in Brave` is displayed – [example](https://github.com/brave/brave-browser/issues/18212#issuecomment-923632150)).
- [ ] Verify you can change the IPFS public gateway address to `https://cf-ipfs.com/`  (passes the Origin isolation test).

### `IPFS/IPNS URI`

- [ ] Verify visiting `ipfs://bafybeiemxf5abjwjbikoz4mc3a3dla6ual3jsgpdr4cjr3oz3evfyavhwq/wiki/Vincent_van_Gogh.html` for the first time triggers IPFS interstitial page to select public gateway to load the URI.
  - [ ] Verify selecting `Use a public gateway` loads `https://bafybeiemxf5abjwjbikoz4mc3a3dla6ual3jsgpdr4cjr3oz3evfyavhwq.ipfs.dweb.link/wiki/Vincent_van_Gogh.html` via public gateway.
- [ ] Verify visiting `ipns://brave.crypto` brings up IPFS interstitial page.
   - [ ] Verify selecting `Use a public gate` loads `https://brave-crypto.ipns.dweb.link` via public gateway.
- [ ] Verify when setting is disabled, loading an `ipfs://` URI or `ipns://` URI doesn't show any interstitial page.
- [ ] Verify `ipfs://` URI or `ipns://` URI doesn't load on a private tab even when the setting is enabled.
