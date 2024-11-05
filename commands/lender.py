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
        user_id = external_user_requests.getUserIdFromAPI(lender.id)
        lending_results = external_lending_requests.getListCardsLentByOwner(user_id)

        if len(lending_results) == 0:
            return

        async def get_page(page: int):
            current_result = lending_results[page - 1]
            emb = discord.Embed(title="List of Cards Lent Out", description=f"<@{current_result["owner_id"]}>")
            emb.add_field(name="Borrowed By", value=f"<@{current_result["borrower_id"]}>")
            emb.add_field(name=current_result["card_name"], value=current_result["card_set_code"].upper() + " " + current_result["card_number"], inline=False)
            emb.add_field(name="Number of Copies", value=current_result["count"], inline=False)
            emb.set_image(
                url=current_result["card_image_url"])
            emb.set_author(name=f"Requested by {ctx.author}")
            emb.set_footer(text=f"Result {page} of {len(lending_results)}")
            return emb, current_result["id"], len(lending_results)

        await selection_menu.SelectionMenu(ctx, get_page, False, None).navigate()

        return

    # use regular text command with params user to check borrowing list
    # default current user if none provided
    @commands.command()
    async def listBorrowedCards(self, ctx, borrower: discord.Member):
        user_id = external_user_requests.getUserIdFromAPI(borrower.id)
        borrowing_results = external_lending_requests.getListCardsBorrowedByUser(user_id)

        if len(borrowing_results) == 0:
            return

        async def get_page(page: int):
            current_result = borrowing_results[page - 1]
            emb = discord.Embed(title="List of Cards Borrowed", description=f"<@{current_result["borrower_id"]}>")
            emb.add_field(name="Borrowed From", value=f"<@{current_result["owner_id"]}>")
            emb.add_field(name=current_result["card_name"], value=current_result["card_set_code"].upper() + " " + current_result["card_number"], inline=False)
            emb.add_field(name="Number of Copies", value=current_result["count"], inline=False)
            emb.set_image(
                url=current_result["card_image_url"])
            emb.set_author(name=f"Requested by {ctx.author}")
            emb.set_footer(text=f"Result {page} of {len(borrowing_results)}")
            return emb, current_result["id"], len(borrowing_results)

        await selection_menu.SelectionMenu(ctx, get_page, False, None).navigate()
        return

    async def searchScryfallCards(self, ctx, result_operation: Callable, search_string: Optional[str]):
        card_search_results = []
        if search_string is None:
            card_search_results = external_card_info_requests.postCardInfoSearch(None, None, None,)
        else:
            passed_args = [None, None, None]
            arguments = search_string.split(",")
            current_arg = 0
            while current_arg < len(arguments):
                passed_args[current_arg] = arguments[current_arg]
                current_arg += 1
            card_search_results = external_card_info_requests.postCardInfoSearch(passed_args[0], passed_args[1], passed_args[2])

        if len(card_search_results) == 0:
            return

        async def get_page(page: int):
            current_result = card_search_results[page - 1]
            emb = discord.Embed(title="Search Results for Query", description=search_string)
            emb.add_field(name=current_result["name"], value=current_result["set_code"].upper() + " " + current_result["collector_number"], inline=False)
            emb.set_image(
                url=current_result["card_image_url"])
            emb.set_author(name=f"Requested by {ctx.author}")
            emb.set_footer(text=f"Result {page} of {len(card_search_results)}")
            return emb, current_result["id"], len(card_search_results)

        await selection_menu.SelectionMenu(ctx, get_page, True, result_operation).navigate()