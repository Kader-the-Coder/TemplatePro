"""Scrollable frame implementation with interactive widgets using Tkinter."""

import tkinter as tk
from tkinter import ttk
from data import config
from utils import database
from utils.widgets import (highlight_frames, add_scrollable_frame, bind_scroll_events_to_all)
from utils.copy import copy
from .frames_base import BaseFrame


class BodyFrame(BaseFrame):
    """
    Represents the body frame of the application.

    Attributes:
        frame_name (str): The name of the frame.
    """
    def __init__(self, root):
        super().__init__(root, 'body_frame')
        self.frame = self._initialize()
        self._add_widgets()
        self._style_widgets()

    def _initialize(self):
        frame = ttk.Frame(self.root, borderwidth=config.FRAME_BORDER_WIDTH, relief=config.FRAME_RELIEF)
        frame.grid(row=1, column=1, columnspan=2, sticky="nsew", padx=config.PADDING, pady=config.PADDING)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        print(f"Initializing {self.root.winfo_name()}.{self.frame_name}")
        return frame

    def _add_widgets(self):
        # def on_tab_change(event):
        #     """Store selected tab in instance class when reloading widgets."""
        #     notebook = event.widget
        #     selected_tab_id = notebook.select()
        #     instance.default_tab = notebook.index(selected_tab_id)

        # Create a notebook to hold the tabs for each category
        notebook = ttk.Notebook(self.frame, style='TNotebook')

        # Create and add tabs for each category in the database
        categories = database.get_categories()
        tags = []
        for _, category in enumerate(categories):
            tab_frame = ttk.Frame(notebook)
            if tags:
                name = tags[0] if len(tags) == 1 else None
            else:
                name = None
            tab_label = (
                f"({len(database.get_templates(category[0], name, tags))}) "
                f"{category[0][:4]}..."
                )
            notebook.add(tab_frame, text=tab_label)

            # Make tab scrollable and add widgets to tab.
            canvas, scrollable_frame = add_scrollable_frame(tab_frame)
            templates = database.get_templates(category[0], name, tags)
            frames = []  # To hold the widget references for highlighting
            for i, template in enumerate(templates):
                # Create frame to hold sub-widgets
                frame = tk.Frame(scrollable_frame, borderwidth=config.FRAME_BORDER_WIDTH, relief=config.FRAME_RELIEF)
                frame.grid(row=i, column=0, sticky="ew", padx=config.PADDING, pady=config.PADDING)

                # Configure the columns in the frame to expand
                frame.grid_columnconfigure(0, weight=0)  # Checkbox column
                frame.grid_columnconfigure(1, weight=1, uniform="equal")  # Label column
                frame.grid_columnconfigure(2, weight=0)  # Button column

                # Add widgets
                # NOTE:Using a tk.Label instead of ttk.Label for direct background manipulation
                # Add copy buttons to frame
                button = tk.Button(frame, text="📋", width=2, border=2, bg="SystemButtonFace", command=lambda text = template[2]: self._set_event_handlers(1)(text))
                button.grid(row=0, column=0, sticky="w")

                # Add options to frame
                widget = tk.Label(frame, text=template[1], anchor="w", bg="SystemButtonFace")
                widget.grid(row=0, column=1, sticky="we")

                # Add "edit" button to frame
                button = tk.Button(frame, text="Edit", width=4, command=lambda: self._set_event_handlers(2))
                button.grid(row=0, column=2, sticky="e")

                frames.append(frame)
            
            bind_scroll_events_to_all(scrollable_frame, canvas)
            highlight_frames(frames)

            
        notebook.grid(row=0, column=0, sticky="nsew")
        print(f"Adding widgets to {self.frame_name}")

    def _style_widgets(self):
        style = ttk.Style()
        style.configure("Custom.TNotebook.Tab", foreground="black")
        style.map("TNotebook.Tab",
            foreground=[('selected', 'black'), ('!selected', '#665956')],
            )
        print(f"Styling widgets in {self.frame_name}")

    def _set_event_handlers(self, event_number):
        # def open_new_window(frame, default:int = None):
        #     """Create a new window that overlaps the main window and hides the parent."""
        #     root = self.frame.winfo_toplevel()
        #     root.withdraw()  # Hide the parent window

        #     new_window = tk.Toplevel(root)
        #     new_window.title("Templates")
        #     new_window.wm_attributes('-topmost', 1)

        #     # Ensure new window overlaps old window.
        #     root_width = root.winfo_width()
        #     root_height = root.winfo_height()
        #     root_x = root.winfo_x()
        #     root_y = root.winfo_y()
        #     new_window.geometry(f"{root_width}x{root_height}+{root_x}+{root_y}")

        #     frames_update.set_widgets(root, new_window, default)

        def copy_clicked(text):
            """Copy text of button to clipboard."""
            copy(text)

        if event_number == 1:
            return copy_clicked

        print(f"Setting event handlers for {self.frame_name}")
        return None
