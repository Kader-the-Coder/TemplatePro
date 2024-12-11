"""Module for configuring and setting the root window."""

import tkinter as tk
from tkinter import ttk
from frames.frames_left import LeftFrame
from frames.frames_top import TopFrame
from frames.frames_bottom import BottomFrame
from frames.frames_body import BodyFrame
from data import config


class TemplatePro():
    """Main application class for the Productivity App."""    

    def __init__(self, root):
        """Initialize the application."""
        self.root = root
        self.default_tab = 0
        self.configure_root_window(root)
        # self.configure_styles()
        self.create_frames(root)
        self.configure_grid(root)
        
        

    def configure_root_window(self, root):
        """Configure the main window."""
        root.title(config.WINDOW_TITLE)
        root.geometry(f"{config.DEFAULT_WIDTH}x{config.DEFAULT_HEIGHT}")
        root.config(bg=config.COLOR_1)
        root.wm_attributes('-topmost', 1)

    # def configure_styles(self):
    #     """Set up the styles for the application."""
    #     styles = [
    #         ("frameTop.TFrame", config.COLOR_2),
    #         ("frameLeft.TFrame", config.COLOR_2),
    #         ("frameBody.TFrame", config.COLOR_2),
    #         ("entry.TEntry", config.COLOR_1),
    #         ("button.TButton", config.COLOR_1),
    #     ]
    #     for style_name, background_color in styles:
    #         style = ttk.Style()
    #         style.configure(style_name, background=background_color)

    def create_frames(self, root):
        """Create and place frames and widgets."""
        left_frame = LeftFrame(root)
        top_frame = TopFrame(root)
        bottom_frame = BottomFrame(root)
        body_frame = BodyFrame(root)
        return left_frame, top_frame, bottom_frame, body_frame

    def configure_grid(self, root):
        """Configure grid row and column weights and minimum sizes."""
        row_config = {
            0: {"minsize": 32}, 1: {"minsize": 32},
            2: {"weight": 1}, 3: {"minsize": 32},
            4: {"minsize": 8}, 5: {"minsize": 32},
            6: {"weight": 1}, 7: {"minsize": 32},
            8: {"minsize": 32}
        }
        for row, config_values in row_config.items():
            root.grid_rowconfigure(row, **config_values)

        root.grid_columnconfigure(0, minsize=32)
        root.grid_columnconfigure(1, weight=1)

    # def on_resize(self, event):
    #     """Debug method to get the current window size."""
    #     width = event.width
    #     height = event.height
    #     print(f"Window resized to: {width}x{height}")

    # def debug_widget(self, event):
    #     """Debug method to get the widget being clicked."""
    #     widget = event.widget  # Get the clicked widget
    #     print(f"Clicked widget: {widget} of type {type(widget).__name__}")

    # def reload_window(self):
    #     """Clear and repopulate the window's content."""
    #     for widget in self.root.winfo_children():
    #         widget.destroy()

    #     # Recreate the frames and widgets
    #     self.create_frames(self.root)
