
# Open Questions
## BTC Questions
* Is it possible to ‘send tx’ in multi-sig? i.e. wallet shows pop-up? Pop-up if in app waiting room?
* can you create a Tx and hold it to a block height? 
* Pizza Pets - are the pets calling anything; or is meta data just updated each block? are they only 'meta alive/dead'?
* How do you see/relate a parent to a child inscription? how is that handled with collections?


# Tools/Utilities/Components
* Hiro - has ord index APIs
    * sounds like its to supplement/compliment ord itself
    * Indexer to follow/post new parents to the web UI.
    * indexer to track open wages; grabbed when scoring results to 'trigger pot' release to winner.
    * easy link for API key
* OrdinalsBot - inscribe API

# Ordinal Theory
* Runes vs inscriptions
    * Runes are fungible tokens
        * The process of creating a Bitcoin rune is called “etching”. This involves creating a “genesis” UTXO including the details of the rune’s name, symbol, decimals, and total supply
        * Runes stores all data, including etching, minting, and transfer messages in OP_RETURN.
    * Ordinals are non-fungible tokens
        * Stores data in the witness part of a transaction
    * Both should be native and taproot compatiable; and lightning compatible

# Areas of Focus
Basic Tx
Ordinal Tx
Adv Ordinals
Setup multi sig
Sports APIs
ESPN APIs - https://gist.github.com/akeaswaran/b48b02f1c94f873c6655e7129910fc3b
