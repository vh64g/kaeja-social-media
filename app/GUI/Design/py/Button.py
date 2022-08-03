from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.button import MDIconButton
from kivymd.theming import ThemableBehavior


class HoverIconButton(MDIconButton, ThemableBehavior, HoverBehavior):
    def __int__(self, background_color, hovered_bg_color, icon):
        super().__init__()
        self.background = background_color
        self.hovered_color = hovered_bg_color
        self.icon = icon