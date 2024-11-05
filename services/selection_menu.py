from typing import Optional, Callable

import discord
from discord.ext import commands

class SelectionMenu(discord.ui.View):
    def __init__(self, ctx: commands.Context, get_page: Callable, is_request, result_operation: Optional[Callable]):
        self.ctx = ctx
        self.is_request = is_request or False
        self.get_page = get_page
        self.result_operation = result_operation
        self.total_pages: Optional[int] = None
        self.index = 1
        super().__init__(timeout=100)

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user == self.ctx.author:
            return True
        else:
            emb = discord.Embed(
                description=f"Only the author of the command can perform this action.",
                color=16711680
            )
            await interaction.response.send_message(embed=emb, ephemeral=True)
            return False

    async def navigate(self):
        emb, current_card_id, self.total_pages = await self.get_page(self.index)
        if self.total_pages == 1:
            await self.ctx.send(embed=emb)
        elif self.total_pages > 1:
            self.update_buttons()
            await self.ctx.send(embed=emb, view=self)

    async def get_current_card_id(self, interaction: discord.Interaction):
        emb, current_card_id, self.total_pages = await self.get_page(self.index)
        return current_card_id

    async def edit_page(self, interaction: discord.Interaction):
        emb, current_card_id, self.total_pages = await self.get_page(self.index)
        self.update_buttons()
        await interaction.response.edit_message(embed=emb, view=self)

    def update_buttons(self):
        if not self.is_request:
            self.children[0].disabled = True
        if self.index > self.total_pages // 2:
            self.children[3].emoji = "⏮️"
        else:
            self.children[3].emoji = "⏭️"
        self.children[1].disabled = self.index == 1
        self.children[2].disabled = self.index == self.total_pages

    @discord.ui.button(emoji="✅", style=discord.ButtonStyle.blurple)
    async def select(self, interaction: discord.Interaction, button: discord.Button):
        card_id = await self.get_current_card_id(interaction)
        await self.result_operation(card_id)

        emb = discord.Embed(title="Selection Complete", description="Successfully completed request")
        await interaction.response.edit_message(embed=emb, view=self)

    @discord.ui.button(emoji="◀️", style=discord.ButtonStyle.blurple)
    async def previous(self, interaction: discord.Interaction, button: discord.Button):
        self.index -= 1
        await self.edit_page(interaction)

    @discord.ui.button(emoji="▶️", style=discord.ButtonStyle.blurple)
    async def next(self, interaction: discord.Interaction, button: discord.Button):
        self.index += 1
        await self.edit_page(interaction)

    @discord.ui.button(emoji="⏭️", style=discord.ButtonStyle.blurple)
    async def end(self, interaction: discord.Interaction, button: discord.Button):
        if self.index <= self.total_pages//2:
            self.index = self.total_pages
        else:
            self.index = 1
        await self.edit_page(interaction)
