import discord
from discord.ext import commands

from services import external_lending_requests, external_user_requests

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

