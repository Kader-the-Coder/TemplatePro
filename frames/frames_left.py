"""Module for configuring and setting buttons within a frame."""

from tkinter import ttk
from data import config
from utils import database
from utils.copy import copy
from .frames_base import BaseFrame


class LeftFrame(BaseFrame):
    """
    A frame for holding buttons and other widgets on the left side
    of the application.

    Attributes:
        frame_name (str): The name of the frame.
    """
    def __init__(self, root):
        super().__init__(root, 'left_frame')
        self.frame = self._initialize()
        self._add_widgets()
        self._style_widgets()

    def _initialize(self):
        frame = ttk.Frame(self.root, borderwidth=config.FRAME_BORDER_WIDTH, relief=config.FRAME_RELIEF)
        frame.grid(row=1, column=0, sticky="nsew", padx=config.PADDING, pady=config.PADDING)
        print(f"Initializing {self.root.winfo_name()}.{self.frame_name}")
        return frame

    def _add_widgets(self):
        button_data = database.get_quick_copy_buttons()
        for _, data in enumerate(button_data):
            button = ttk.Button(
                self.frame, text=data[0], width=4, style="button.TButton",
                command=lambda text=data[1]: self._set_event_handlers(1)(text)
                )
            button.text = data[1]
            button.pack(fill="x")

        button_open = ttk.Button(self.frame, text="^", width=4, style="button.TButton",)
        button_open.pack(fill="x", side="bottom")
        print(f"Adding widgets to {self.frame_name}")

    def _style_widgets(self):
        style = ttk.Style()
        style.configure("button.TButton", background=config.COLOR_2)
        print(f"Styling widgets in {self.frame_name}")

    def _set_event_handlers(self, event_number):
        def copy_clicked(text):
            """Copy text of button to clipboard."""
            copy(text)

        if event_number == 1:
            return copy_clicked

        print(f"Setting event handlers for {self.frame_name}")
        return None
