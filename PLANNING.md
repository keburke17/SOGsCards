# PLANNING
Goal: Proof of Concept - Tx Sequence - Higher or Lower based on RNG  

## Current
[] Study GPT responses for deploying flask/python from MacBook  
[] Study GPT responses for BTC transaction dev process  
[] Review Youtube videos on ESPN/sports APIs
    https://www.youtube.com/results?search_query=espn+player+stat+api
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