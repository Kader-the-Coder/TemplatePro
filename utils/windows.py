import tkinter as tk

def open_new_window(root_frame, new_frame=None):
    """Create a new window that overlaps the main window and hides the parent."""
    def on_child_close(root, new_window):
        """Closes the main window when the child is closed."""
        new_window.destroy()
        root.destroy()

    root = root_frame.root.winfo_toplevel()
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

    new_window.protocol(
        "WM_DELETE_WINDOW",
        lambda root=root, new_window=new_window: on_child_close(root, new_window)
        )
    root_frame.context["new_window"] = new_window
    new_frame(root_frame)
