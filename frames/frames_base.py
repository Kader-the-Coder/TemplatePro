from abc import ABC, abstractmethod

class BaseFrame(ABC):
    """
    Base class for frame modules.

    This class provides a basic structure for frame modules, including
    methods for initializing the frame layout, adding widgets,
    styling widgets, and setting event handlers.
    """
    def __init__(self, root, frame_name):
        self.root = root
        self.frame_name = frame_name

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
