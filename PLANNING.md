# PLANNING
Goal: Proof of Concept - Tx Sequence - Higher or Lower based on RNG  

## Current
[x] Study GPT responses for deploying flask/python from MacBook
[] Fix GPT-designed flask deployment
[] Study GPT responses for BTC transaction dev process  
[] Determine Vault/Wallet multi-sig approach
* Have two initiate a wallet itself via web app; wallet holds the wager UTXO and settings/teams UTXO
[] Determine bot as 3rd party multi-sig participant; holds wallet and checks wallet for block height to initiate score tx?

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

# Game Settings

# Draft Logic/flow
* Complete Random - X players
* Fill Roster Positions 