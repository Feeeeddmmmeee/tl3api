from typing import TYPE_CHECKING, Optional, Dict, Any

import re

if TYPE_CHECKING:
    from wrapper import Client

class ICObjectBase:
    """Superclass for all Intersection Controller classes."""
    _client: "Client"
    object_id: int

    def __init__(
        self, 
        client: "Client", 
        _data: Optional[Dict[str, Any]]
    ):
        """Initialize an :class:`.ICObjectBase` instance.
        
        :param client: An instance of :class:`.Client`.

        """
        self._client = client
        if _data:
            for attribute, value in _data.items():
                setattr(self, self._convert(attribute), value)

    def __eq__(self, other: "ICObjectBase") -> bool:
        return self.object_id == other.object_id

    def __ne__(self, other: "ICObjectBase") -> bool:
        return not self == other

    def _convert(self, string: str) -> str:
        s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", string)
        return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()