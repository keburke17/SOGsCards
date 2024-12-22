# PLANNING
Current
[] Study GPT responses for deploying flask/python from MacBook
[] Study GPT responses for BTC transaction dev proess 
Next Up
Future

Goal: Proof of Concept - Tx Sequence - Higher or Lower based on RNG

# Game Outline
Player 1 Sets Game Definitions via Web UI, including satoshis pledged
Start Game w Friend - Send Join/Invite Tx - Player 1 invites Player 2
Players draft their teams using Web UI - Simple Folder/Table View; Baseball cards when selecting individual players
Both players agreeing to their draft - Both Sign/Submit Draft Tx
Starts new Game with desired end-time/block heigh
Players can refresh metadata to see live score
At Desired Block Height - Game calculates winner and distributes pot

# Tx Outline
Initiate Game
Accept Game Invite
Start Game/Submit Drafted Teams
- cache player stats
Calculate Winner
- take new snapshot and calculate delta to determine winner
- distribute pot