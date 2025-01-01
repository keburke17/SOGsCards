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

* Game Features
* Add Roster spots