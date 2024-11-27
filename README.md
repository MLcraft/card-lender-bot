# MTGLoanBot

---
### A Discord bot to keep track of card loans between friends for the Magic: The Gathering trading card game

## Add the bot to your server: [<img src="https://gist.github.com/cxmeel/0dbc95191f239b631c3874f4ccf114e2/raw/discord-icon.svg" alt="Invite the bot to your server!" height="24" />](https://discord.com/oauth2/authorize?client_id=1287629937578213429&permissions=1689917160151104&scope=bot)

---
## Build and Run Instructions
Make sure the backend API is running on `localhost:8080` 

Instructions for the backend can be found in this repo: [card-collection](https://github.com/MLcraft/card-collection)

Add `BACKEND_API_URL` and `DISCORD_BOT_TOKEN` to your environment variables (can use .env)

Run `pip install -r requirements.txt` to resolve packages

Once configured, run `python3 bot.py` to activate the bot

---

## Commands

### Card search parameters - `cardName`,`cardSetCode`,`cardNumber`
Comma separated list of search parameters for finding specific cards. Set code and Card number are optional but can help if there's a specific printing the user is looking for. Parameters are not case sensitive but must be properly typed, there is no fuzzy search functionality.

Example: `the one ring,ltr,741`

### Lend cards - `$lendCard`
**Parameters**: `userToLendTo` `count` `card search parameters`

Lends a specific card from the user who uses the command to the provided user (either user ID or discord mention) in the provided count.

Example: `$lendCard @user1 2 unlicensed hearse`
### Return cards - `$returnCard`
**Parameters**: `userToLendTo` `count` `card search parameters`

Returns a specific card from the user who uses the command to the provided user (either user ID or discord mention) in the provided count. If the count is greater than the amount of copies being borrowed, clears all the borrowed copies.

Example: `$returnCard @user2 2 unlicensed hearse,snc`
### List cards lent out by user - `$listLentCards`
**Parameters**: `userToLookUp`

Lists all cards lent out by the provided user (either user ID or discord mention)

Example: `$listLentCards @user2`
### List cards borrowed by user - `$listBorrowedCards`
**Parameters**: `userToLookUp`

Lists all cards borrowed by the provided user (either user ID or discord mention)

Example: `$listBorrowedCards @user1`
