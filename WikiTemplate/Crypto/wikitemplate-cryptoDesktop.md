
## Onboarding

- [ ] Verify loading `brave://wallet` on a clean profile shows onboarding flow
- [ ] Verify you are able to complete the onboarding flow to Ethereum create wallet by default
- [ ] Verify you are able to complete the backup seed phrase during onboarding itself
- [ ] Verify you can skip the onboarding from backup wallet screen and still create a wallet
- [ ] Verify when a Dapp interacts without creating wallet opens a new tab and shows onboarding

## Importing Wallet

- [ ] Verify with MetaMask extension installed and wallet created, visiting `brave://wallet/crypto/onboarding/import-or-restore` shows option to import account from MetaMask during onboarding
- [ ] Verify error message is shown when trying to use same password as MetaMask and it doesn't meet Brave Wallet's password criteria
- [ ] Verify able to successfully import MetaMask wallet into Brave Wallet
- [ ] Verify with Crypto Wallet Extension installed and wallet created, visiting `brave://wallet/crypto/onboarding/import-or-restore` shows option to import account from old Crypto Wallet Extension
- [ ] Verify error message is shown when trying to use same password as Crypto Wallet Extension and it doesn't meet Brave Wallet's password criteria
- [ ] Verify able to successfully import Crypto Wallet Extension with 12-seed into Brave Wallet
- [ ] Verify able to successfully import Crypto Wallet Extension with 24-seed word into Brave Wallet

## Panel

- [ ] Verify when wallet is not created opening the wallet panel shows `Learn More` message. Clicking on it opens `brave://wallet` in a new tab
- [ ] Verify when wallet is created, opening the panel shows default account and selected network and account balance
- [ ] Verify Buy/Send/Swap buttons are available and loads corresponding screens to perform action
- [ ] Verify transaction history button is shown and lists recent transactions for selected network when clicked
- [ ] Verify changing network in panel updates the corresponding account in panel and in portfolio page
- [ ] Verify changing account in panel updates the corresponding network in panel and in portfolio page
- [ ] Verify when a Dapp is connected to wallet account, panel shows a `Connected` state notification
- [ ] Verify when a Dapp connection is revoked, panel shows a `Disconnected` state notification
- [ ] Verify selecting `Connected Sites` from panel menu loads `brave://settings/content/<Network>` for Ethereum/Solana based on selected account
- [ ] Verify selecting `View on Block explorer` from panel loads the corresponding account's details on the network block explorer
- [ ] Verify selecting `Help Center` opens a new tab and loads `https://support.brave.com/hc/en-us/articles/4415497656461-Brave-Walllet-FAQ`
- [ ] Verify you are able to lock the wallet from panel menu
- [ ] Verify clicking on the expand button on the top-left of panel loads the wallet page in a new tab

## Portfolio & Accounts

- [ ] Verify after creating a wallet it loads portfolio screen by default
- [ ] Verify portfolio page shows balance of all accounts
- [ ] Verify able to show/hide balance on portfolio screen
- [ ] Verify able to search for token in portfolio screen
- [ ] Verify able to filter assets list by specific network via the network dropdown
- [ ] Verify able to sort NFT's and Assets list by balance amount
- [ ] Verify able to add or remove assets from view via `Visible assets` button
- [ ] Verify able to add a new custom asset for specific network
- [ ] Verify able to add hide/remove custom asset via `Visible assets` list
- [ ] Verify able to create a new primary account for Ethereum/Solana/Filecoin via `Create Account` in accounts tab
- [ ] Verify able to import Ethereum/Solana/Filecoin accounts via `Import` option
- [ ] Verify imported accounts are listed under `Secondary Accounts`
- [ ] Verify able to import Ethereum/Solana/Filecoin accounts via `Import from hardware wallet`
- [ ] Verify imported hardware wallet accounts are listed under `Secondary Accounts`
- [ ] Verify Wallet backup message is shown on both portfolio and accounts tab if skipped during onboarding
- [ ] Verify Brave Wallet is not default message is shown when MetaMask is installed and `Brave Wallet (Prefer extensions)` is set as default wallet provider

## Ethereum

- [ ] Verify when a new wallet is created Ethereum Account is created but not set as default
- [ ] Verify for a newly created Ethereum wallet, `ETH` and `BAT` tokens are added by default on portfolio screen
- [ ] Verify the account address is same for Ethereum Mainnet and other EVM's
- [ ] Verify able to add a new Ethereum account via the Accounts tab
- [ ] Verify able to import an Ethereum account via `Private Key` or `JSON file` under the import section
- [ ] Verify able to import Ethereum account via hardware keys
- [ ] Verify able to resolve UD/ENS Domains on `Send To` tab

## Solana

- [ ] Verify when a new wallet is created Solana Account is created and set as default
- [ ] Verify when `Solana Mainnet Beta` is selected in network dropdown in panel or in widget, it prompts to create a new Solana account
- [ ] Verify selecting `Yes` in the create Solana account modal creates a new Solana account
- [ ] Verify selecting `No` in the create Solana account doesn't create a new Solana account
- [ ] Verify able to add a new Solana account via the Accounts tab
- [ ] Verify able to import an Solana account via `Private Key`  under the import section
- [ ] Verify able to import Solana account via hardware keys

## Filecoin

- [ ] Verify when a new wallet is created there is no Filecoin account created by default
- [ ] Verify when `Filecoin` is selected in network dropdown in panel or in widget, it prompts to create a new Filecoin account
- [ ] Verify selecting `Yes` in the create Filecoin account modal creates a new Filecoin account
- [ ] Verify selecting `No` in the create Filecoin account modal doesn't create a new Filecoin account 
- [ ] Verify able to add a new Filecoin account via the Accounts tab
- [ ] Verify able to import an Filecoin account via `Private Key` under the import section
- [ ] Verify able to import Filecoin account via hardware keys

## Hardware

- [ ] Verify able to connect Ledger and import Ethereum accounts
- [ ] Verify able to connect Ledger and import Solana accounts
- [ ] Verify able to connect Ledger and import Filecoin accounts
- [ ] Verify able to connect Trezor and import Ethereum accounts

## Custom Tokens

- [ ] Verify able to manually add a ERC721 token
- [ ] Verify able to manually add a custom token for Ethereum/EVM network 
- [ ] Verify able to manually add a custom token for Solana network
- [ ] Verify able to add a custom token via webpage (Coingecko/Coinmarketcap)

## Wallet Settings

- [ ] Verify Default Ethereum Wallet dropdown is set to `Brave Wallet` as default
- [ ] Verify Default Solana Wallet dropdown is set to `Brave Wallet (prefer extensions)` as default
- [ ] Verify Default Ethereum/Solana Wallet allows to set Brave Wallet as default
- [ ] Verify Default Ethereum/Solana Wallet allows to set it to None
- [ ] Verify with Crypto Wallets Extension flag enabled `Crypto Wallet (deprecated)` is only shown for Default Ethereum Wallet
- [ ] Verify able to change default base currency (USD -> Other)
- [ ] Verify able to change default base cryptocurrency from BTC to other (ETH/LTC/BCH etc)
- [ ] Verify able to update default wallet lock time and works as expected
- [ ] Verify able to clear wallet transaction & nonce information
- [ ] Verify able to add custom network 
- [ ] Verify able to set a network as active network from settings
- [ ] Verify able to delete added custom network
- [ ] Verify able to edit pre-loaded default networks
- [ ] Verify able to enable/disable test networks
- [ ] Verify able to reset default networks when edited

## Dapp Support (Ethereum & Solana)

- [ ] Verify able to connect to an Ethereum Dapp 
- [ ] Verify after connecting to an Ethereum Dapp the connected state is saved in `brave://settings/content/ethereum`
- [ ] Verify able to connect to an Solana Dapp 
- [ ] Verify after connecting to an Solana Dapp the connected state is saved in `brave://settings/content/ethereum`
- [ ] Verify able to connect multiple accounts to Dapp (Both Ethereum & Solana)
- [ ] Verify able to submit transactions when wallet is connected to Dapp (Both Ethereum & Solana)
- [ ] Verify able to add a custom token from Dapp
- [ ] Verify able to Sign Transactions for both Ethereum & Solana accounts
- [ ] Verify able to add a custom network via Dapp
- [ ] Verify network switch prompt is shown when adding a new network or changing network in Dapp

## Restore & Reset

- [ ] Verify able to restore a wallet using seed words from the onboarding screen (No wallet created)
- [ ] Verify able to restore a wallet using seed words from wallet lock screen (Wallet created & Locked)
- [ ] Verify when a wallet is restored, there is no "Backup wallet" message is shown
- [ ] Verify when a wallet is restored, all the accounts that have a transaction are restored
- [ ] Verify when a wallet is restored it restores all Ethereum & Solana accounts that have a send transaction
- [ ] Verify able to reset wallet from `brave://settings/wallet`
- [ ] Verify wallet tab is reloaded when wallet is reset from settings

## Transactions

- [ ] Verify Buy ETH works with different on-ramp providers
- [ ] Verify Buy Solana works with different on-ramp providers
- [ ] Verify Buy Filecoin works 
- [ ] Verify able to submit Send ETH transaction
- [ ] Verify able to submit Send SOL transaction
- [ ] Verify able to submit Send FIL transaction
- [ ] Verify able to perform Swap ETH transaction
- [ ] Verify able to perform Swap SOL transaction
- [ ] Verify able to perform Swap on different pre-loaded EVM chains 
- [ ] Verify transaction notification is shown for confirmed/error/rejected transactions
- [ ] Verify clicking on the transaction notification opens a new tab and loads the token details to view the current transaction
- [ ] Verify able to submit and approve Ethereum transactions via imported Ethereum account on Ledger
- [ ] Verify able to submit and approve Solana transactions via imported Solana account on Ledger
- [ ] Verify able to submit and approve Filecoin transactions via imported Filecoin account on Ledger
- [ ] Verify able to submit and approve transactions via imported Ethereum account on Trezor
