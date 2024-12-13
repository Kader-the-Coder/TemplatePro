from abc import ABC, abstractmethod
import tkinter as tk


class BaseFrame(ABC):
    """
    Base class for frame modules.

    This class provides a basic structure for frame modules, including
    methods for initializing the frame layout, adding widgets,
    styling widgets, and setting event handlers.
    """
    def __init__(self, root_frame):
        self.root_frame = None if isinstance(root_frame, tk.Tk) else root_frame
        self.root = getattr(root_frame, 'root', root_frame)
        self.context = {}

    @abstractmethod
    def _initialize(self):
        """Private method to initialize the frame layout."""

    @abstractmethod
    def _add_widgets(self):
        """Private method to add widgets to the frame."""

    @abstractmethod
    def _style_widgets(self):
        """Private method to style widgets in the frame."""

    @abstractmethod
    def _set_event_handlers(self, event_number):
        """
        Private method to set event handlers for widgets based on the
        given event number.

        Args:
            event_number (int): Identifier for the type of event handler to set.

        Returns:
            function: The event handler function corresponding to the event number.
        """
    def _on_reload(self):
        """Callback method to be implemented by subclasses."""
        self.root_frame.reload_frames()

    def reload_frames(self):
        """Clear and repopulate the window's content."""
        if self.root_frame is None:
            for widget in self.root.winfo_children():
                widget.destroy()
            self._add_widgets()
        else:
            self._on_reload()
