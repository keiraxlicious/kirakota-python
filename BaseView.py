__all__: tuple[str, ...] = ("BaseView",)
# pyright: reportUnknownVariableType=false


class BaseView(discord.ui.View):
    interaction: discord.MessageInteraction

    def __init__(self, user: discord.Member | discord.User, *, timeout: float = 180.0):
        super().__init__(timeout=timeout)
        self.user = user

    async def on_timeout(self) -> None:
        self._disable()
        try:
            await self.interaction.response.edit_message(view=self)
        except (discord.HTTPException, discord.InteractionResponded):
            await self.interaction.edit_original_response(view=self)

    async def interaction_check(self, interaction: discord.MessageInteraction) -> bool:
        if interaction.user.id == self.user.id:
            await interaction.response.defer()
            self.interaction = interaction
            return True
        await interaction.send("You are not allowed to use this view.", ephemeral=True)
        return False

    def _disable(self) -> None:
        for child in self.children:
            if isinstance(child, discord.ui.Button):
                child.disabled = True
            elif isinstance(child, discord.ui.Select):
                child.disabled = True

    async def on_error(
        self, error: Exception, item: discord.ui.Item[discord.ui.View], interaction: discord.MessageInteraction
    ) -> None:
        await interaction.edit_original_response(
            content=None,
            embed=discord.Embed(
                description="An error occurred while processing your request.", color=discord.Color.red()
            ),
            view=None,
            attachments=[],
        )
        # await interaction.client.on_error("view_error", ViewException(error, item, interaction))

#Keira Version.
# ------- x-------

import enum

import discord

from .. import BaseView


class Buttons(str, enum.Enum):
    PREVIOUS = "<:ArrowLeft:989134685068202024>"
    NEXT = "<:rightArrow:989136803284004874>"
    STOP = "<:dustbin:989150297333043220>"
    LAST = "<:DoubleArrowRight:989134892384256011>"
    FIRST = "<:DoubleArrowLeft:989134953142956152>"


class ClassicPaginator(BaseView):
    def __init__(self, ctx, user: discord.Member, *, timeout: float = 180.0, items: list[discord.Embed]):
        super().__init__(user, timeout=timeout)
        self._items = ctx.guild  
        self.page = 0        
        self._items = items
        for n, embed in enumerate(items, start=1):
            embed.set_footer(text=f"Page {n}/{len(items)}", icon_url=self.user.display_avatar)

    async def _update_message(
        self, interaction: discord.MessageInteraction | discord.ApplicationCommandInteraction
    ) -> None:
        self._update_state()
        await interaction.response.edit_message(embed=self._items[self.page], view=self)

    def _update_state(self) -> None:
        self.first.disabled = self.previous.disabled = self.page == 0
        self.next.disabled = self.last.disabled = self.page == len(self._items) - 1

    @discord.ui.button(style=discord.ButtonStyle.blurple, emoji=str(Buttons.FIRST.value))
    async def first(self, _button: discord.ui.Button[discord.ui.View], interaction: discord.MessageInteraction) -> None:
        self.page = 0
        await self._update_message(interaction)

    @discord.ui.button(style=discord.ButtonStyle.blurple, emoji=str(Buttons.PREVIOUS.value))
    async def previous(
        self, _button: discord.ui.Button[discord.ui.View], interaction: discord.MessageInteraction
    ) -> None:
        self.page -= 1
        await self._update_message(interaction)

    @discord.ui.button(style=discord.ButtonStyle.blurple, emoji=str(Buttons.STOP.value))
    async def finish(
        self, _button: discord.ui.Button[discord.ui.View], interaction: discord.MessageInteraction
    ) -> None:
        await interaction.delete_original_response()

    @discord.ui.button(style=discord.ButtonStyle.blurple, emoji=str(Buttons.NEXT.value))
    async def next(self, _button: discord.ui.Button[discord.ui.View], interaction: discord.MessageInteraction) -> None:
        self.page += 1
        await self._update_message(interaction)

    @discord.ui.button(style=discord.ButtonStyle.blurple, emoji=str(Buttons.LAST.value))
    async def last(self, _button: discord.ui.Button[discord.ui.View], interaction: discord.MessageInteraction) -> None:
        self.page = len(self._items) - 1
        await self._update_message(interaction)

    @classmethod
    async def start(
        cls,
        inter: discord.ApplicationCommandInteraction,
        *,
        timeout: float = 180.0,
        items: list[discord.Embed],
    ) -> "ClassicPaginator":
        assert isinstance(inter.author, discord.Member)
        assert isinstance(items, list)
        paginator = cls(inter.author, timeout=timeout, items=items)
        await paginator._update_message(inter)
        return paginator