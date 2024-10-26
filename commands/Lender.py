import discord
from discord.ext import commands


class Lender(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # use regular text command with params user to lend and card to search
    # keep track of user and give menu for card search results
    # then let user pick the card they want with scroll buttons then click confirm button to lend
    @commands.command()
    async def lendCard(self, interaction: discord.Interaction, borrower: discord.Member, ):
        pass
    # use regular text command with params user to return card to and card to search
    # keep track of user and give menu for card search results
    # then let user pick the card they want with scroll buttons then click confirm button to return
    @commands.command()
    async def returnCard(self, interaction: discord.Interaction, borrower: discord.Member, ):
        pass

    # use regular text command with params user to check lending list
    # default current user if none provided
    @commands.command()
    async def listLentCards(self, interaction: discord.Interaction, borrower: discord.Member):
        pass

    # use regular text command with params user to check borrowing list
    # default current user if none provided
    @commands.command()
    async def listBorrowedCards(self, interaction: discord.Interaction, borrower: discord.Member):
        pass

