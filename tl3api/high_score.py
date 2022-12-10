from typing import TYPE_CHECKING
from tl3api.base import ICObjectBase

if TYPE_CHECKING:
    from tl3api.user import User
    from tl3api.map import Map

class HighScore(ICObjectBase):
    """A :class: represneting an Intersection Controller :class:`.HighScore`.
    
    =================================== ================================================
    Attribute                           Description
    =================================== ================================================
    user_id                             ID of the author.
    map_id                              ID of the :class:`.Map`.
    score                               The score.
    map_version                         Version of the :class:`.Map`
    date_made                           Timestamp of when the :class:`.HighScore` was made.
    object_id                           ID of the :class:`.HighScore`.
    username                            Name of the author.
    """
    user_id: int
    """ID of the author."""
    map_id: int
    """ID of the :class:`.Map`."""
    score: int
    """The score."""
    map_version: int
    """Version of the :class:`.Map`"""
    date_made: int
    """Timestamp of when the :class:`.HighScore` was made."""
    object_id: int
    """ID of the :class:`.HighScore`."""
    username: int
    """Name of the author."""

    async def get_author(self) -> "User":
        """Return the :class:`.HighScore` author."""
        return await self._client.get_details_for_user(user_id=self.user_id)

    async def get_map(self) -> "Map":
        """Return the :class:`.Map` on which the :class:`.HighScore` was made."""
        return await self._client.get_map_details(map_id=self.map_id)