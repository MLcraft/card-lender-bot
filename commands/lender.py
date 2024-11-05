from typing import Optional, Callable

import discord
from discord.ext import commands

from services import external_lending_requests, external_user_requests, external_card_info_requests, selection_menu


class Lender(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # use regular text command with params user to lend and card to search
    # keep track of user and give menu for card search results
    # then let user pick the card they want with scroll buttons then click confirm button to lend
    @commands.command()
    async def lendCard(self, ctx, borrower: discord.Member, count, *, args: Optional[str]):
        owner_id = external_user_requests.getUserIdFromAPI(ctx.author.id)
        borrower_id = external_user_requests.getUserIdFromAPI(borrower.id)
        async def performLendOperation(cardId):
            external_lending_requests.postLendCardFromOwnerToUser(owner_id, borrower_id, cardId, count)
            return

        await self.searchScryfallCards(ctx, performLendOperation, args)

    # use regular text command with params user to return card to and card to search
    # keep track of user and give menu for card search results
    # then let user pick the card they want with scroll buttons then click confirm button to return
    @commands.command()
    async def returnCard(self, ctx, owner: discord.Member, count, *, args: Optional[str]):
        owner_id = external_user_requests.getUserIdFromAPI(owner.id)
        borrower_id = external_user_requests.getUserIdFromAPI(ctx.author.id)

        async def performReturnOperation(cardId):
            external_lending_requests.postReturnCardFromUserToOwner(owner_id, borrower_id, cardId, count)
            return

        await self.searchScryfallCards(ctx, performReturnOperation, args)

    # use regular text command with params user to check lending list
    # default current user if none provided
    @commands.command()
    async def listLentCards(self, ctx, lender: discord.Member):
        userID = external_user_requests.getUserIdFromAPI(lender.id)
        external_lending_requests.getListCardsLentByOwner(userID)
        return

    # use regular text command with params user to check borrowing list
    # default current user if none provided
    @commands.command()
    async def listBorrowedCards(self, ctx, borrower: discord.Member):
        userID = external_user_requests.getUserIdFromAPI(borrower.id)
        external_lending_requests.getListCardsBorrowedByUser(userID)
        return

    async def searchScryfallCards(self, ctx, resultOperation: Callable, searchString: Optional[str]):
        cardSearchResults = []
        if searchString is None:
            cardSearchResults = external_card_info_requests.postCardInfoSearch(None, None, None,)
        else:
            passed_args = [None, None, None]
            arguments = searchString.split(",")
            current_arg = 0
            while current_arg < len(arguments):
                passed_args[current_arg] = arguments[current_arg]
                current_arg += 1
            cardSearchResults = external_card_info_requests.postCardInfoSearch(passed_args[0], passed_args[1], passed_args[2])

        if len(cardSearchResults) == 0:
            return

        async def get_page(page: int):
            currentResult = cardSearchResults[page - 1]
            emb = discord.Embed(title="Search Results for Query", description=searchString)
            emb.add_field(name=currentResult["name"], value=currentResult["set_code"].upper() + " " + currentResult["collector_number"], inline=False)
            emb.set_image(
                url=currentResult["card_image_url"])
            emb.set_author(name=f"Requested by {ctx.author}")
            emb.set_footer(text=f"Result {page} of {len(cardSearchResults)}")
            return emb, currentResult["id"], len(cardSearchResults)

        await selection_menu.SelectionMenu(ctx, get_page, resultOperation).navigate()