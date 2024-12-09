"""Module for configuring and setting an update button within a frame."""

import tkinter as tk
from tkinter import ttk
from data import config
from frames import frames_update
from .frames_base import BaseFrame


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
        frame.grid(row=3, column=0, sticky="ew", padx=config.PADDING, pady=config.PADDING)
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
            command=lambda frame=self.frame: self._set_event_handlers(1)(frame)
            )
        button_load.grid(row=0, column=1, padx=config.PADDING, pady=config.PADDING, sticky="ew")
        print(f"Adding widgets to {self.frame_name}")

    def _style_widgets(self):
        style = ttk.Style()
        style.configure("button.TButton", background=config.COLOR_1)
        print(f"Styling widgets in {self.frame_name}")

    def _set_event_handlers(self, event_number):
        def open_new_window(frame, default:int = None):
            """Create a new window that overlaps the main window and hides the parent."""
            root = self.frame.winfo_toplevel()
            root.withdraw()  # Hide the parent window

            new_window = tk.Toplevel(root)
            new_window.title("Templates")
            new_window.wm_attributes('-topmost', 1)

            # Ensure new window overlaps old window.
            root_width = root.winfo_width()
            root_height = root.winfo_height()
            root_x = root.winfo_x()
            root_y = root.winfo_y()
            new_window.geometry(f"{root_width}x{root_height}+{root_x}+{root_y}")

            frames_update.set_widgets(root, new_window, default)

            def on_child_close(root, new_window):
                """Closes the main window when the child is closed."""
                new_window.destroy()
                root.destroy()

            new_window.protocol(
                "WM_DELETE_WINDOW",
                lambda root=root, new_window=new_window: on_child_close(root, new_window)
                )

        if event_number == 1:
            return open_new_window

        print(f"Setting event handlers for {self.frame_name}")
        return None
