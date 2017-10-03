class Enumeration:
    """Holds the metadata for a enumeration structure in the MoM Adventure language.

    Attributes:
        name: the name by which this enumeration can be identified. It must be unique in the program.
        values: a dictionary that maps the names of the different values to their respective values
            in this same enumeration.
    """

    def __init__(self, name: str):
        self._name = name
        self._values = {}
        self._counter = 1

    def add_value(self, value: str) -> None:
        """Adds a new value to this enumeration.

        The name of the value must be unique. There is no guarantee of which value it will hold.
        """
        self._values[value] = self._counter
        self._counter += 1

    @property
    def name(self):
        return self._name

    @property
    def values(self):
        return self._values

    __author__ = "Marco A. Peyrot (mpeyrotc)"
    __license__ = "MIT"
    __version__ = "1.0.0"
    __email__ = "macpeyrot@hotmail.com"
    __status__ = "Development"
