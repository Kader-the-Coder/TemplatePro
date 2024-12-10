import tkinter as tk
from tkinter import ttk
# from data import config
from utils import database


def highlight_frames(frames):
    """Change background color of a widget and its children on hover."""

    def highlight(event, frame_widgets, highlight=True):
        """Apply highlight to a frame and its child widgets."""
        color = "darkgray" if highlight else "SystemButtonFace"
        for widget in frame_widgets:
            widget.config(bg=color)

    for frame in frames:
        # Get all widgets inside the frame
        frame_widgets = [frame] + list(frame.winfo_children())

        # Bind hover events to each widget
        for widget in frame_widgets:
            widget.bind(
                "<Enter>",
                lambda event, fw=frame_widgets: highlight(event, fw, highlight=True),
            )
            widget.bind(
                "<Leave>",
                lambda event, fw=frame_widgets: highlight(event, fw, highlight=False),
            )



def add_widgets_to_tab(canvas, scrollable_frame,
                category=None, name=None, tags=None):
    """
    Add widgets to scrollable frame.

    widget_layout: A function with the following parameters:
        canvas, scrollable_frame, template, row_index
    """
    templates = database.get_templates(category, name, tags)
    for i, template in enumerate(templates):
        widget = ttk.Label(scrollable_frame, name=template, text=template)
        widget.grid()


def add_scrollable_frame(frame):
    """Create a scrollable canvas with a frame inside for content."""
    canvas = tk.Canvas(frame, highlightthickness=0)
    canvas.grid(row=0, column=0, sticky="nsew")

    # Create a vertical scrollbar linked to the canvas
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame that will hold the content inside the canvas
    scrollable_frame = ttk.Frame(canvas)

    # Create a window in the canvas where the scrollable frame is placed
    window_id = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Ensure the scrollable_frame expands to fit the canvas width
    scrollable_frame.grid_columnconfigure(0, weight=1, uniform="equal")

    # Update scroll region on content change
    scrollable_frame.bind("<Configure>", lambda _event: configure_scroll_region(canvas, scrollable_frame))
    
    # Update window width to match canvas width
    canvas.bind("<Configure>", lambda event: resize_canvas(event, canvas, window_id))

    # Make sure the canvas resizes with the grid
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    bind_scroll_events(scrollable_frame, canvas)

    return canvas, scrollable_frame


def on_mouse_wheel(event, canvas):
    """Scroll the canvas with the mouse wheel."""
    scroll_speed = 1
    direction = -scroll_speed if event.delta > 0 else scroll_speed
    canvas.yview_scroll(direction, "units")


def bind_scroll_events_to_all(parent_widget, canvas):
    """
    Recursively bind scroll events to all widgets under a parent widget.

    Only binds scroll events to the canvas directly and ensures propagation.
    """
    parent_widget.bind("<MouseWheel>", lambda e: on_mouse_wheel(e, canvas))
    parent_widget.bind("<Button-4>", lambda e: canvas.yview_scroll(-1, "units"))  # Linux scroll up
    parent_widget.bind("<Button-5>", lambda e: canvas.yview_scroll(1, "units"))   # Linux scroll down

    # Bind scroll events to child widgets that propagate to the canvas
    for child in parent_widget.winfo_children():
        if isinstance(child, tk.Widget):  # Check for tkinter widgets
            child.bind("<MouseWheel>", lambda e: on_mouse_wheel(e, canvas))
            child.bind("<Button-4>", lambda e: canvas.yview_scroll(-1, "units"))
            child.bind("<Button-5>", lambda e: canvas.yview_scroll(1, "units"))
        bind_scroll_events_to_all(child, canvas)



def bind_scroll_events(widget, canvas):
    """Bind mouse wheel events to the given widget for scrolling."""
    widget.bind("<MouseWheel>", lambda e: on_mouse_wheel(e, canvas))  # For Windows and macOS
    widget.bind("<Button-4>", lambda e: canvas.yview_scroll(-1, "units"))  # For Linux scroll up
    widget.bind("<Button-5>", lambda e: canvas.yview_scroll(1, "units"))   # For Linux scroll down


def configure_scroll_region(canvas, scrollable_frame):
    """Configure the scroll region of the canvas based on the scrollable frame."""
    bbox = scrollable_frame.bbox()  # Get the bounding box of the content
    if bbox:  # Check if bbox is valid
        canvas.configure(scrollregion=bbox)  # Set the scroll region based on bbox

        # Adjust the scroll region if content height is smaller than canvas height
        canvas_height = canvas.winfo_height()
        if bbox[3] <= canvas_height:  # bbox[3] is the bottom y-coordinate
            canvas.configure(scrollregion=(0, 0, 0, canvas_height))


def resize_canvas(event, canvas, window_id):
    """Resize the window inside the canvas to match the canvas width."""
    canvas_width = event.width
    canvas.itemconfig(window_id, width=canvas_width)  # Set the width of the scrollable window to match the canvas width


