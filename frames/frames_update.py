"""Module for configuring and setting up the update window."""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from frames.frames_base import BaseFrame
from utils import database
from data import config


class UpdateFrame(BaseFrame):
    """
    Top frame of the application.

    Attributes:
        frame_name (str): Name of the frame.
    """
    def __init__(self, root_frame):
        super().__init__(root_frame)
        self.new_root = root_frame.context["new_window"]
        self.context = root_frame.context
        self.frame_top, self.frame_bottom = self._initialize()
        self._add_widgets()
        self._style_widgets()

    def _initialize(self):
        # Create a PanedWindow to allow resizing between the top and bottom frames
        paned_window = tk.PanedWindow(self.new_root, orient=tk.VERTICAL, sashwidth=4, sashrelief=tk.RAISED)
        paned_window.grid(row=0, column=0, sticky="nsew")

        # Create the top frame
        frame_top = ttk.Frame(
            paned_window,
            borderwidth=config.FRAME_BORDER_WIDTH,
            relief=config.FRAME_RELIEF
        )
        paned_window.add(frame_top)

        # Configure columns for frame_top
        frame_top.grid_columnconfigure(0, weight=0)
        frame_top.grid_columnconfigure(1, weight=1)
        frame_top.grid_columnconfigure(2, weight=0)

        # Create the bottom frame
        frame_bottom = ttk.Frame(
            paned_window,
            borderwidth=config.FRAME_BORDER_WIDTH,
            relief=config.FRAME_RELIEF
        )
        paned_window.add(frame_bottom)

        # Configure columns for frame_bottom
        frame_bottom.grid_columnconfigure(0, weight=0)
        frame_bottom.grid_columnconfigure(1, weight=1)
        frame_bottom.grid_columnconfigure(2, weight=0)

        # Configure rows and columns of self.root for the PanedWindow
        self.new_root.grid_rowconfigure(0, weight=1)
        self.new_root.grid_columnconfigure(0, weight=1)

        return frame_top, frame_bottom

    def _add_widgets(self):
        configure_top_frame(self.frame_top, self.context, self._set_event_handlers(1))
        configure_bottom_frame(self.frame_bottom, self._set_event_handlers(1))

    def _style_widgets(self):
        pass

    def _set_event_handlers(self, event_number):
        def close_window(frame):
            """Close the new window and show the parent window again."""
            new_width = frame.winfo_width()
            new_height = frame.winfo_height()
            new_x = frame.winfo_x()
            new_y = frame.winfo_y()

            self.root.geometry(f"{new_width}x{new_height}+{new_x}+{new_y}")
            self.new_root.destroy()  # Close the new window
            self.root.deiconify()  # Show the parent window again
            self.reload_frames()

        if event_number == 1:
            return close_window

        return None


def configure_top_frame(frame, context, func):
    """
    Configure the top frame of the update window.

    Creates the widgets in the top frame, which include the category, name, tags, and
    template text fields, as well as buttons for adding, canceling, and deleting templates.

    Parameters:
    frame (tk.Frame): The top frame of the update window.

    Returns:
    tuple: A tuple containing the category, name, tags, template text fields, and the
    add template button.
    """

    # Create top frame widgets
    category_label = tk.Label(frame, text="Category", anchor="e")
    category = tk.Entry(frame)
    name_label = tk.Label(frame, text="Name", anchor="e")
    name = tk.Entry(frame)
    tag_label = tk.Label(frame, text="Tags", anchor="e")
    tags = tk.Entry(frame)
    template_text = tk.Text(frame, height=5, wrap="word", undo=True, autoseparators=True)

    def create_template():
        new_category = category.get()
        if new_category in [c[0] for c in database.get_categories()]:
            new_name = name.get()
            new_tags = [tag.strip() for tag in tags.get().split(",")]
            new_template = template_text.get("1.0", tk.END).strip()
            database.create_template(
                new_name,
                new_template,
                new_category,
                new_tags
                )
            messagebox.showinfo("Info", "Template has been created.")
            func(frame.winfo_toplevel())
            return
        messagebox.showerror("ERROR", "Category does not exist.")

    def update_template():
        new_category = category.get()
        if new_category in [c[0] for c in database.get_categories()]:
            new_name = name.get()
            new_tags = [tag.strip() for tag in tags.get().split(",")]
            new_template = template_text.get("1.0", tk.END).strip()
            # Create a new template
            database.update_template(
                context["template_id"],
                new_category,
                new_name,
                new_tags,
                new_template,
                )
            messagebox.showinfo("Info", "Template has been updated.")
            func(frame.winfo_toplevel())
            return
        messagebox.showerror("ERROR", "Category does not exist.")

    def clear_template():
        category.delete(0, tk.END)
        name.delete(0, tk.END)
        tags.delete(0, tk.END)
        template_text.delete(1.0, tk.END)

    def cancel_template():
        clear_template()
        category.insert(0, context["category"])
        name.insert(0, context["name"])
        tags.insert(0, ", ".join(context["tags"]))
        template_text.insert(1.0, context["template"])

    def delete_template():
        if messagebox.askokcancel("Warning", "Delete template?"):
            database.delete_template(context["template_id"])
            messagebox.showinfo("Info", "Template has been deleted.")
            func(frame.winfo_toplevel())

    # Add widgets to top frame
    add_update_template_button = None
    cancel_clear_template_button = None
    delete_template_button = None
    # If a template has been selected
    if "template_id" in context:
        category.insert(0, context["category"])
        name.insert(0, context["name"])
        tags.insert(0, ", ".join(context["tags"]))
        template_text.insert(1.0, context["template"])
        add_update_template_button = tk.Button(frame, text="Update", command=update_template)
        cancel_clear_template_button = tk.Button(frame, text="Cancel", command=cancel_template)
        delete_template_button = tk.Button(frame, text="Delete", command=delete_template)
        delete_template_button.grid(row=4, column=0, sticky="ew")
    else:
        add_update_template_button = tk.Button(frame, text="Create", command=create_template)
        cancel_clear_template_button = tk.Button(frame, text="Clear", command=clear_template)
    add_update_template_button.grid(row=4, column=2, sticky="ew")
    cancel_clear_template_button.grid(row=4, column=1, sticky="ew")
    category_label.grid(row=0, column=0, sticky="nsew")
    category.grid(row=0, column=1, columnspan=2, sticky="nsew")
    name_label.grid(row=1, column=0, sticky="nsew")
    name.grid(row=1, column=1, columnspan=2, sticky="nsew")
    tag_label.grid(row=2, column=0, sticky="nsew")
    tags.grid(row=2, column=1, columnspan=2, sticky="nsew")
    template_text.grid(row=3, column=0, columnspan=3, sticky="nsew")

    # Configure the grid for the top frame
    frame.grid_rowconfigure(0, weight=0)
    frame.grid_rowconfigure(1, weight=0)
    frame.grid_rowconfigure(2, weight=0)
    frame.grid_rowconfigure(3, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)

def configure_bottom_frame(frame, func):
    """
    Configure the bottom frame by adding a close button.

    Args:
        frame: The Tkinter frame where the button will be added.
        func: A function to be called when the close button is pressed. It 
              should accept the top-level window as its argument.
    """
    close_button = tk.Button(
        frame, text="Close",
        command=lambda: func(frame.winfo_toplevel())
    )
    close_button.grid(column=1, sticky="ew")
