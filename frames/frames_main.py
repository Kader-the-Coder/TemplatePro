"""Module for configuring and setting the root window."""

from tkinter import ttk
from frames.frames_base import BaseFrame
from frames.frames_left import LeftFrame
from frames.frames_top import TopFrame
from frames.frames_bottom import BottomFrame
from frames.frames_body import BodyFrame
from data import config


class TemplatePro(BaseFrame):
    """Main application class for the Productivity App."""    

    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.default_tab = 0
        self.frames_loaded = False

        self._initialize()
        self._style_widgets()
        self._add_widgets()

    def _initialize(self):
        """Configure the main window."""
        self.root.title(config.WINDOW_TITLE)
        self.root.geometry(f"{config.DEFAULT_WIDTH}x{config.DEFAULT_HEIGHT}")
        self.root.config(bg=config.COLOR_1)
        self.root.wm_attributes('-topmost', 1)
        self.configure_grid()

    def _style_widgets(self):
        """Set up the styles for the application."""
        styles = [
            ("frameTop.TFrame", config.COLOR_2),
            ("frameLeft.TFrame", config.COLOR_2),
            ("frameBody.TFrame", config.COLOR_2),
            ("entry.TEntry", config.COLOR_1),
            ("button.TButton", config.COLOR_1),
        ]
        for style_name, background_color in styles:
            style = ttk.Style()
            style.configure(style_name, background=background_color)

    def _add_widgets(self):
        """Create and place frames and widgets."""
        print("<-----------------HERE----------------->")
        LeftFrame(self.root)
        TopFrame(self.root)
        BottomFrame(self.root)
        BodyFrame(self.root)

    def configure_grid(self):
        """Configure grid row and column weights and minimum sizes."""
        row_config = {
            0: {"minsize": 32}, 1: {"minsize": 32},
            2: {"weight": 1}, 3: {"minsize": 32},
            4: {"minsize": 8}, 5: {"minsize": 32},
            6: {"weight": 1}, 7: {"minsize": 32},
            8: {"minsize": 32}
        }
        for row, config_values in row_config.items():
            self.root.grid_rowconfigure(row, **config_values)

        self.root.grid_columnconfigure(0, minsize=32)
        self.root.grid_columnconfigure(1, weight=1)

    def _set_event_handlers(self, event_number):
        # def on_resize(self, event):
        #     """Debug method to get the current window size."""
        #     width = event.width
        #     height = event.height
        #     print(f"Window resized to: {width}x{height}")

        # def debug_widget(self, event):
        #     """Debug method to get the widget being clicked."""
        #     widget = event.widget  # Get the clicked widget
        #     print(f"Clicked widget: {widget} of type {type(widget).__name__}")
        pass

    def on_reload(self):
        self._add_widgets()
