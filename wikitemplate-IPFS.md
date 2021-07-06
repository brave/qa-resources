## Installation & Setup

  ### `go-updater` node update

  - [ ] Verify going to `brave://ipfs` and clicking on `Install and start` installs and shows `go-ipfs/0.7.0` (or latest released), via the `Version:` section under `Node info`.
  - [ ] Verify, using the above profile, that restarting Brave with `--use-dev-goupdater-url`, and clicking on `Restart` via `brave://ipfs` downloads and installs the latest development candidate.

  ### Config

  - [ ] Verify changing `Maximum IPFS cache size (GB)` on the `brave://settings/ipfs` page (set `Method to resolve IPFS resources` to `Local node` on `brave://settings/ipfs`), the new value is reflected on the diagnostic page (`brave://ipfs`) in the `Repo Stats -> Size` section.

  ### Diagnostic page (`brave://ipfs`)

  - [ ] Verify loading `brave://ipfs` redirects to `brave://ipfs-internals`.
  - [ ] Verify, on a clean profile, visiting `brave://ipfs` will present you with an `Install and start` button, which will install and start an IPFS local node.  Confirm you see `Node is running` under `IPFS node status`, `Stop`, `Restart`, and `My Node` buttons, and a dynamically updating `Connected peers:` count.
  - [ ] Verify that clicking `Stop` resets all statistics, paths, and config information.
  - [ ] Verify that clicking `Start` populates all statistics, paths, and config information, and you see `Stop`, `Restart`, and `My Node` buttons, along with a dynamically updating `Connected peers:` count. 
  - [ ] Verify that clicking `Restart` resets and repopulates all stats, paths, and config information, and you see `Stop`, `Restart`, and `My Node` buttons, along with a dynamically updating `Connected peers:` count.
  - [ ] Verify that clicking on `(details)` to the right of `Connected peers:` takes you to the `PEERS` pane of `127.0.0.1:45002/ipfs/bafy..../#/` and you see a global map with a dynamically updating peer count and listing, below.
  - [ ] Verify that clicking on `Perform a garbage collection sweep` resets and repopulates the `Objects:` and `Size:` stats beneath `Repo Stats`.
  - [ ] Verify that clicking `My Node` takes you to the `Status` pane of the IPFS dashboard, with a URL similar to `127.0.0.1:45002/ipfs/bafy..../#/`, where you see `Connected to IPFS`, MB count of files shared, and dynamically updating peers count, as well as your `PEER ID` and `AGENT`.

## Import:

- [ ] Prerequisites: local node launched and local gateway configured.  On a new profile, loading `ipns://brantly.eth` and clicking `Use a local node` on the interstitial page will set you up.

  ### Importing a page via IPFS

  - [ ] Verify the IPFS item available in the page context menu. Select `Import to IPFS > This page` and import any page content. Make sure the content is downloaded and imported, the import folder is opened when import completed successfully, the page content can be downloaded. The shareable link is copied to the clipboard.

  ### Importing linked content

  - [ ] Verify the IPFS item available in the linked content context menu. Select `Import to IPFS > Linked content` and import any linked content from any page. Make sure the content is downloaded and imported, the import folder is opened when import completed successfully, the file can be downloaded. The shareable link is copied to the clipboard.

  ### Importing selected audio

  - [ ] Verify the IPFS item available in the audio context menu. Select `Import to IPFS > Selected audio` and import any audio from any page. Make sure the audio is downloaded and imported, the import folder is opened when import completed successfully, the file can be downloaded. The shareable link is copied to the clipboard.

  ### Importing selected image

  - [ ] Verify the IPFS item available in the image context menu. Select an image and choose `Import to IPFS > Selected image` and import any image from any page. Make sure the image is downloaded and imported, the import folder is opened when import completed successfully, the file can be downloaded. The shareable link is copied to the clipboard.

  ### Importing selected text

  - [ ] Verify the IPFS item available in the selected text context menu. Select text and choose `Import Selected Text to IPFS`. Make sure the text is wrapped into a file with id like `file_1.txt` and the imported text is available inside the file. The shareable link is copied to the clipboard.

  ### Importing selected video

  - [ ] Verify the IPFS item available in the video context menu. Select a video and choose `Import to IPFS > Selected video`/ Make sure the video is downloaded and imported, the import folder is opened when import completed successfully, the file can be downloaded. The shareable link is copied to the clipboard.

  ### Sharing a local file using IPFS (without keys)

  - [ ] Verify the IPFS item available in the main app menu. Go to `IPFS -> Share Local File Using IPFS` select and import any local file. Make sure the file is imported, the import folder is opened when import completed successfully, the file can be downloaded and the downloaded one is same as original. The shareable link is copied to the clipboard.

  ### Sharing a local folder using IPFS (without keys)

  - [ ] Verify the IPFS item available in the main app menu. Go to `IPFS -> share Local Folder Using IPFS` select and import any local folder. Make sure the whole folder is imported, the import folder is opened when import completed successfully, files can be downloaded and the downloaded one is same as original. The shareable link is copied to the clipboard.

  ### Automatic redirects (needs fleshing out)

  - [ ] Automatic redirection of IPFS resources to IPFS gateway if option enabled on `brave://settings/ipfs` page
  - [ ] Automatic redirect DNSLink to an IPFS version of a website when possible, only if site has header `x-ipfs-path` or DNSLink TXT record if server returned 5xx error
  - [ ] Verify IPFS address bar badge is shown for pages with x-ipfs-header and dnslink TXT record for 5xx error code
  - [ ] Verify by clicking the `IPFS` badge icon in the address bar on IPFS/IPNS pages it shows valid (green) information about the IPFS resource.
  - [ ] Verify, when loading an IPFS/IPNS resources on a new profile (such as `ipns://brantly.eth`), that the interstitial page (`Ask` mode in `brave://settings/ipfs`) gives you two choices: 1) to install a local node (`Use a local node`) or 2) `Use a public gateway` (Android + iOS: public gateway only).

## DNSLink

- [ ] Verify that loading `https://dweb.link/ipfs/QmT5NvUtoM5nWFfrQdVrFtvGfKFmG7AHE8P34isapyhCxX/wiki/Mars.html` redirects you seamlessly to `https://bafybeicgmdpvw4duutrmdxl4a7gc52sxyuk7nz5gby77afwdteh3jc5bqa.ipfs.dweb.link/wiki/Mars.html`, and there's an `Open using IPFS` badge/button in the URL bar.  Confirm that clicking `Open using IPFS` goes to `ipfs://bafybeicgmdpvw4duutrmdxl4a7gc52sxyuk7nz5gby77afwdteh3jc5bqa/wiki/Mars.html`.
- [ ] Verify that loading `https://ipfs.io/ipns/libp2p.io/` shows an `Open using IPFS` button in the URL bar, and clicking it redirects to `ipns://libp2p.io/`.  Confirm it resolves and loads.

## IPFS Companion

- [ ] Verify that toggling `IPFS Companion` to `On` via `brave://settings/ipfs` prompts you to install the extension.  After clicking `Add extension`, confirm you get a notification that IPFS Companion was added to Brave, and are then taken to the `Set your IPFS preference` interstitial page.
- [ ] Verify that clicking on the puzzle-piece icon on the browser toolbar, then `IPFS Companion`, will load a popup.  Click on the gears (settings) icon and confirm it loads the `Companion Preferences` page.

## IPFS URLs

- [ ] Ensure each of the following IPFS URLs load over both `Gateway` and `Local node` modes:
    - [ ] `ipfs://bafybeiemxf5abjwjbikoz4mc3a3dla6ual3jsgpdr4cjr3oz3evfyavhwq/wiki/Vincent_van_Gogh.html`
    - [ ] `ipfs://bafybeigdyrzt5sfp7udm7hu76uh7y26nf3efuylqabf3oclgtqy55fbzdi/`
    - [ ] `ipfs://QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/Tokyo_National_Museum.html`
    - [ ] `ipfs:QmYwAPJzv5CZsnA625s3Xf2nemtYgPpHdWEz79ojWnPbdG/readme`

## IPNS URLs

- [ ] Ensure each of the following IPNS URLs load over both `Gateway` and `Local node` modes:
    - [ ] `ipns://brantly.eth`
    - [ ] `ipns://en.wikipedia-on-ipfs.org`
    - [ ] `ipns://libp2p.io/`
    - [ ] `ipns://ipfs.io`

## Gateway

- [ ] Verify, on a new profile, you can load `brave://settings/ipfs`, click on the `Change` button for `IPFS public gateway address`, enter `https://cloudflare-ipfs.com/` and are presented with an interstitial page after loading `ipns://brantly.eth`.  Click `Use a public gateway` and confirm you're taken to `https://cloudflare-ipfs.com/ipns/brantly.eth/#/`.  (Alternatively, use one from `https://ipfs.github.io/public-gateway-checker/`.)
- [ ] Verify, on a new profile, you can load `https://wikipedia-on-ipfs.org`, switch `Method to resolve IPFS resources` to either `Gateway` or `Local node` in `brave://settings/ipfs`, and then see an `Open using IPFS` badge/icon in the URL bar.
- [ ] Verify clicking on `Open using IPFS` on `https://blog.ipfs.io/24-uncensorable-wikipedia` loads `ipfs://bafybeiaieqdmhtnehaau7kqoj2lmdfqc7juk34cjyb7dxr35vahp22bquu/24-uncensorable-wikipedia/`

  ### Protocol system handler/OS integration

  - [ ] Verify (`Windows`) that pressing `Win+R`, typing `open ipfs://bafkreigcnxudvpojjfwncmauociy5q46zsq46oe66cxbyzie3imabuoege`, and pressing `Enter` opens Brave and loads an HTML page with the word `PASS`.
  - [ ] Verify (`macOS`): opening Terminal, and typing `open ipfs://bafkreigcnxudvpojjfwncmauociy5q46zsq46oe66cxbyzie3imabuoege`, and pressing `Enter` opens Brave and loads an HTML page with the word `PASS`.
  - [ ] Verify (`Linux`) that opening a shell and typing `xdg-open ipfs://bafkreigcnxudvpojjfwncmauociy5q46zsq46oe66cxbyzie3imabuoege` and pressing `Enter` opens Brave and loads an HTML page with the word `PASS`.

## Peers:
- [ ] Prerequisites: local node launched and local gateway configured.

  ### Adding

  - [ ] Verify when you go to `brave://settings/ipfs/peers` and click on the `Add` button, it prompts you to enter a new peer-connection string. Confirm that entering an incorrect string yields `This name is not valid` upon clicking `Submit`. (Acceptable ones are only CIDs or something like `**/p2p/**` format.)
  - [ ] Verify if a peer is added and node is started, it proposes to restart node to apply changes.
  - [ ] Verify the local node is restarted by clicking `Restart` button; happen it shows error message and suggests to see more on diagnostic page.

  ### Removing

  - [ ] Verify a peer can be removed by clicking on Trash icon in the peer line.

## IPNS keys:

- [ ] Prerequisites: local node launched and local gateway configured. Go to `Settings -> IPFS`, there should be an available `Set up your IPNS keys` option, which opens `brave://settings/ipfs/keys`

  ### Sharing a local file using an IPFS key

  - [ ] Verify the IPFS item available in the main app menu. Go to `IPFS -> Share Local File Using IPFS`, select the `self` key via the context menu, under `Publish using IPNS`, and import any local file. Make sure the file is imported, the import folder is opened when import completed successfully, the file can be downloaded and the downloaded one is same as original. The shareable link is copied to the clipboard; verify you see your key before the `?filename=filename.ext` in the copied text, e.g. `https://dweb.link/ipns/k51qzi5uqu5dgxhiv8w8cdvmgdhbvy3t9gn4jwpwwro18fots0xtdabpcxxzwc?filename=Big_Buck_Bunny_4K.webm` (the key is `k51qzi5uqu5dgxhiv8w8cdvmgdhbvy3t9gn4jwpwwro18fots0xtdabpcxxzwc`).

  ### Sharing a local folder using an IPFS key

  - [ ] Verify the IPFS item available in the main app menu. Go to `IPFS -> share Local Folder Using IPFS`,  select the `self` key via the context menu, under `Publish using IPNS`, and import any local folder. Make sure the whole folder is imported, the import folder is opened when import completed successfully, files can be downloaded and the downloaded one is same as original. The shareable link is copied to the clipboard; verify you see your key before the `?filename=Downloads` part, e.g. `https://dweb.link/ipns/k51qzi5uqu5djfh24zd6m4e8fm6d9rju48fyokc13achcfo4hz9fmioev0xln6?filename=Downloads` (`k51qzi5uqu5djfh24zd6m4e8fm6d9rju48fyokc13achcfo4hz9fmioev0xln6` is the key here).

  ### Importing keys

  - [ ] Verify adding a new key by clicking on the `Import` button and choosing an existing key file to import.
  - [ ] Verify imported key is available with entered name; verify entering `self` will yield `This name cannot be used`.
  - [ ] Verify you cannot import the same key twice.

  ### Add/Remove/Rotate keys

  - [ ] Verify when you click `Add`, it prompts for key name and generates a new key.
  - [ ] Verify clicking on `Add` and entering an existing key name shows a `This name cannot be used` error message.
  - [ ] Verify when you click on the Trash icon for a key, it removes the key.