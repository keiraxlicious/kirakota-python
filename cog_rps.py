import enum

import disnake

from BaseView import BaseView


class Buttons(str, enum.Enum):
    PREVIOUS = "<:ArrowLeft:989134685068202024>"
    NEXT = "<:rightArrow:989136803284004874>"
    STOP = "<:dustbin:989150297333043220>"
    LAST = "<:DoubleArrowRight:989134892384256011>"
    FIRST = "<:DoubleArrowLeft:989134953142956152>"


class ClassicPaginator(BaseView):
    def __init__(self, user: disnake.Member, *, timeout: float = 180.0, items: list[disnake.Embed]):
        super().__init__(user, timeout=timeout)
        self.page = 0
        self._items = items
        for n, embed in enumerate(items, start=1):
            embed.set_footer(text=f"Page {n}/{len(items)}", icon_url=self.user.display_avatar)

    async def _update_message(
        self, interaction: disnake.MessageInteraction | disnake.ApplicationCommandInteraction
    ) -> None:
        self._update_state()
        await interaction.response.edit_message(embed=self._items[self.page], view=self)

    def _update_state(self) -> None:
        self.first.disabled = self.previous.disabled = self.page == 0
        self.next.disabled = self.last.disabled = self.page == len(self._items) - 1

    @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=str(Buttons.FIRST.value))
    async