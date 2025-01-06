# PLANNING
Goal: Proof of Concept - Tx Sequence - Higher or Lower based on RNG  

## Current
[x] Study GPT responses for deploying flask/python from MacBook
[] Fix GPT-designed flask deployment
[] Study GPT responses for BTC transaction dev process  
[] Determine Vault/Wallet multi-sig approach
* Have two initiate a wallet itself via web app; wallet holds the wager UTXO and settings/teams UTXO
* Determine bot as 3rd party multi-sig participant; holds wallet and checks wallet for block height to initiate score tx?
[] scoring tx strategy - 
* SOGs Card inscribes (posts) game schedule to drive website UI list; includes expected result block height
* players initiat wager with child tx by selecting game and sending inscription to invitee wallet
* invitee selects wager UTXO and sends a copy back to intiating player? 

* After X block height - SOGs Cards inscribe scores as child tx; will also score each wager UTXO that was also a child of the orig schedule inscription
that will on chain at block height X;
 have that be child to orig tx? then parent triggers 'settle wager' tx at x+1?

 * web UI - schedule page and result page
    * schedule posts 'Upcoming Games' and result shows 'Scored Games'
    * Clicking the Upcoming Game will initiate wager workflow; Clicking Scored Games will list Scored UTXOs and winners!
    ms wallet holding in-progress UTXOs

## Next Up
## Future

# Game Outline
1. Player 1 Sets Game Definitions via Web UI, including satoshis pledged  
2. Start Game w Friend - Send Join/Invite Tx - Player 1 invites Player 2  
3. Players draft their teams using Web UI - Simple Folder/Table View; Baseball cards when selecting individual players  
4. oth players agreeing to their draft - Both Sign/Submit Draft Tx  
5. Starts new Game with desired end-time/block heigh  
6. Players can refresh metadata to see live score  
7. At Desired Block Height - Game calculates winner and distributes pot  


# Tx Outline
* Initiate Game
    * Accept Game Invite
* Start Game/Submit Drafted Teams
    * cache player stats
* Calculate Winner
    * take new snapshot and calculate delta to determine winner
    * distribute pot


# POC Requirements
* Initiate multisig Tx to confirm settings/wager
    * Web App to inititate Tx; One wallet invites the other and waits for confirmation; initiating wallet chooses the settings
        * Settings include Wager and Block Height to complete
        * Question - can wallet show custom text to communicate the game settings?
    * Upon Confirmation - 
        * Backend - Inscribe - Draft 5 players and track 1 Stat; hardcode example 'PlayerDataDraft' and hardcode example 'PlayerDataResult' with example results to show delta in player stats
* Initiate Tx to score game in X Block Height
    * Backend - calculates winning wallet based on 'PlayerDataDelta'; which team has a combined higher point total
    * Inscribe winner inscription and distribute wager to winning wallet
    * Question - can you initiate a future tx to be sent at X block height?
    * Question - can the initial Tx 'take the UTXOs' from the initiated chat? OR is held by a 3rd/independent wallet/vault?


# POC v2 Requirements
* Add API Usage for Live/Random Players
    * API randomizes player selection and caches Player Points and/or Game Results
* Add API usage for Scoring Rounds
    * API caches new Player Points and/or Game Results
* Add Manual Draft
    * Subsequent multisig Tx - Child Tx - both teams are drafted manually via player review/selection feature