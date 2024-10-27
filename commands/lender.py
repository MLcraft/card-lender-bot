from typing import Optional

import discord
from discord.ext import commands

from services import external_lending_requests, external_user_requests, external_card_info_requests

class Lender(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # use regular text command with params user to lend and card to search
    # keep track of user and give menu for card search results
    # then let user pick the card they want with scroll buttons then click confirm button to lend
    @commands.command()
    async def lendCard(self, ctx, borrower: discord.Member, ):
        pass
    # use regular text command with params user to return card to and card to search
    # keep track of user and give menu for card search results
    # then let user pick the card they want with scroll buttons then click confirm button to return
    @commands.command()
    async def returnCard(self, ctx, borrower: discord.Member, ):
        pass

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

    @commands.command()
    async def searchScryfallCards(self, ctx, *, args: Optional[str]):
        if args is None:
            print(external_card_info_requests.postCardInfoSearch(None, None, None,))
            return
        else:
            passed_args = [None, None, None]
            arguments = args.split(",")
            current_arg = 0
            while current_arg < len(arguments):
                passed_args[current_arg] = arguments[current_arg]
                current_arg += 1
            print(external_card_info_requests.postCardInfoSearch(passed_args[0], passed_args[1], passed_args[2]))
            return