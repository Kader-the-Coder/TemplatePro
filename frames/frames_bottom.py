"""Module for configuring and setting an update button within a frame."""

import tkinter as tk
from tkinter import ttk
from data import config
from frames import frames_update
from frames.frames_base import BaseFrame
from frames.frames_update import UpdateFrame
from utils.windows import open_new_window


class BottomFrame(BaseFrame):
    """
    Top frame of the application.

    Attributes:
        frame_name (str): Name of the frame.
    """
    def __init__(self, root):
        super().__init__(root, 'bottom_frame')
        self.frame = self._initialize()
        self._add_widgets()
        self._style_widgets()

    def _initialize(self):
        frame = ttk.Frame(self.root, borderwidth=config.FRAME_BORDER_WIDTH, relief=config.FRAME_RELIEF)
        frame.grid(row=3, column=0, columnspan=2, sticky="ew", padx=config.PADDING, pady=config.PADDING)
        # Adjust row and column weights to make the frame responsive
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=0)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_columnconfigure(2, weight=0)
        print(f"Initializing {self.root.winfo_name()}.{self.frame_name}")
        return frame

    def _add_widgets(self):
        button_load = ttk.Button(
            self.frame, text="UPDATE", style="button.TButton",
            command=self._set_event_handlers(1)
            )
        button_load.grid(row=0, column=1, padx=config.PADDING, pady=config.PADDING, sticky="ew")
        print(f"Adding widgets to {self.frame_name}")

    def _style_widgets(self):
        style = ttk.Style()
        style.configure("button.TButton", background=config.COLOR_1)
        print(f"Styling widgets in {self.frame_name}")

    def _set_event_handlers(self, event_number):
        def open_frames_update_window():
            open_new_window(self.frame, UpdateFrame, 'update_frame')

        if event_number == 1:
            return open_frames_update_window

        print(f"Setting event handlers for {self.frame_name}")
        return None
