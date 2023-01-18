"""Primary Home App which allows switching into a number of other apps.

Also includes media control and settings management.
"""

try:
    from typing import Any, Dict, Optional
except ImportError:
    pass

from apps.func import FuncKeysApp

from apps.window import WindowManagementApp
from apps.chrome import ChromeApp
from apps.spotify import SpotifyApp
from apps.code import CodeApp
from apps.firefox import FirefoxApp
from apps.git import GitApp
from apps.term import TermApp
from apps.teams import TeamsApp
from apps.vs import VsApp
from apps.sharex import ShareXApp

from utils.app_pad import AppPad
from utils.apps.key import Key, KeyApp

from utils.commands import (
    ConsumerControlCode,
    Media,
    SwitchAppCommand,
)
from utils.constants import (
    COLOR_FUNC,
    COLOR_CHROME,
    COLOR_CODE,
    COLOR_FILES,
    COLOR_NOTION,
    COLOR_SLACK,
    COLOR_SPOTIFY,
    COLOR_SUBLIME_MERGE,
    COLOR_TERMINAL,
    COLOR_WINMAN,
)


class HomeApp(KeyApp):
    """
    Main menu app that displays when starting the Macropad. Includes media
    controls, a selector for the host OS, and buttons to switch to various
    the other defined apps.
    """

    name = "Home"

    encoder_button = Media(ConsumerControlCode.MUTE)

    encoder_increase = Media(ConsumerControlCode.VOLUME_INCREMENT)
    encoder_decrease = Media(ConsumerControlCode.VOLUME_DECREMENT)

    def __init__(self, app_pad: AppPad, settings: Optional[Dict[str, Any]] = None):
        self.initialize_settings_dependent_keys(app_pad, settings)
        super().__init__(app_pad, settings=settings)

    @classmethod
    def initialize_settings_dependent_keys(
        cls, app_pad: AppPad, settings: Optional[Dict[str, Any]] = None
    ):

        window_manager_app = WindowManagementApp(app_pad, settings)
        cls.key_0 = Key(
            text="WinGen",
            color=COLOR_WINMAN,
            command=SwitchAppCommand(window_manager_app),
        )

        chrome_app = ChromeApp(app_pad, settings)
        cls.key_1 = Key(
            text="Chrome", color=COLOR_CHROME, command=SwitchAppCommand(chrome_app)
        )

        firefox_app = FirefoxApp(app_pad, settings)
        cls.key_2= Key(
            text="FF", color=COLOR_FILES, command=SwitchAppCommand(firefox_app)
        )

        code_app = CodeApp(app_pad, settings)
        cls.key_3 = Key(
            text="VS Code", color=COLOR_CODE, command=SwitchAppCommand(code_app)
        )

        vs_app = VsApp(app_pad, settings)
        cls.key_5 = Key(
            text="Vis Studio", color=COLOR_SUBLIME_MERGE, command=SwitchAppCommand(vs_app)
        )

        git_app = GitApp(app_pad, settings)
        cls.key_6 = Key(
            text="Git", color=COLOR_NOTION, command=SwitchAppCommand(git_app)
        )

        term_app = TermApp(app_pad, settings)
        cls.key_7 = Key(
            text="Term", color=COLOR_TERMINAL, command=SwitchAppCommand(term_app)
        )

        func_keys_app = FuncKeysApp(app_pad, settings)
        cls.key_8 = Key(
            text="Func", color=COLOR_FUNC, command=SwitchAppCommand(func_keys_app)
        )

        teams_app = TeamsApp(app_pad, settings)
        cls.key_9 = Key(
           text="Teams", color=COLOR_SLACK, command=SwitchAppCommand(teams_app)
        )

        sharex_app = ShareXApp(app_pad, settings)
        cls.key_10 = Key(
            text="ShareX", color=COLOR_WINMAN, command=SwitchAppCommand(sharex_app)
        )

        spotify_app = SpotifyApp(app_pad, settings)
        cls.key_11 = Key(
            text="Music", color=COLOR_SPOTIFY, command=SwitchAppCommand(spotify_app)
        )
