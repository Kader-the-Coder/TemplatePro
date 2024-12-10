"""Module for configuring and setting widgets within a frame."""

from tkinter import ttk
from data import config
from .frames_base import BaseFrame


class TopFrame(BaseFrame):
    """
    Top frame of the application.

    Attributes:
        frame_name (str): Name of the frame.
    """
    def __init__(self, root):
        super().__init__(root, 'top_frame')
        self.frame = self._initialize()
        self._add_widgets()
        self._style_widgets()

    def _initialize(self):
        frame = ttk.Frame(self.root, borderwidth=config.FRAME_BORDER_WIDTH, relief=config.FRAME_RELIEF)
        frame.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=config.PADDING, pady=config.PADDING)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        print(f"Initializing {self.root.winfo_name()}.{self.frame_name}")
        return frame

    def _add_widgets(self):
        entry = ttk.Entry(self.frame, style="entry.TEntry")
        entry.grid(row=0, column=0, padx=config.PADDING, pady=config.PADDING,
                sticky="nsew")
        entry = ttk.Entry(self.frame, style="entry.TEntry")
        entry.grid(row=0, column=1, padx=config.PADDING, pady=config.PADDING,
                sticky="nsew")

        button_load = ttk.Button(self.frame, text="LOAD", width=8, style="button.TButton")
        button_load.grid(row=0, column=2, padx=config.PADDING, pady=config.PADDING)
        print(f"Adding widgets to {self.frame_name}")

    def _style_widgets(self):
        style = ttk.Style()
        style.configure("entry.TEntry", background=config.COLOR_2)
        style.configure("button.TButton", background=config.COLOR_2)
        print(f"Styling widgets in {self.frame_name}")

    def _set_event_handlers(self, event_number):
        # def copy_clicked(text):
        #     """Copy text of button to clipboard."""
        #     copy(text)

        # if event_number == 1:
        #     return copy_clicked

        print(f"Setting event handlers for {self.frame_name}")
        return None
