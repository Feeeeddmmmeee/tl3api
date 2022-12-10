from typing import TYPE_CHECKING, Optional
from tl3api.base import ICObjectBase

if TYPE_CHECKING:
    from tl3api.user import User
    from tl3api.map import Map

class Comment(ICObjectBase):
    """A :class: representing an Intersection Controller :class:`.Map` :class:`.Comment`.
    
    =================================== ================================================
    Attribute                           Description
    =================================== ================================================
    user                                ID of the :class:`.Comment` author.
    map                                 ID of the :class:`.Map` on which the :class:`.Comment` was posted.
    comment                             The content of the :class:`.Comment`.
    flag                                ?
    date_posted                         Timestamp of when the :class:`.Comment` was posted.
    rtl                                 ?
    reply_to_user_id                    ID of the :class:`.User` who the :class:`.Comment` author replied to.
    object_id                           ID of the :class:`.Comment`.
    username                            Name of the :class:`.Comment` author.
    reply_username                      Name of the :class:`.User` who the :class:`.Comment` author replied to.
    """
    user: int
    """ID of the :class:`.Comment` author."""
    map: int
    """ID of the :class:`.Map` on which the :class:`.Comment` was posted."""
    comment: str
    """The content of the :class:`.Comment`."""
    flag: int
    date_posted: int
    """Timestamp of when the :class:`.Comment` was posted."""
    rtl: bool
    reply_to_user_id: int
    """ID of the :class:`.User` who the :class:`.Comment` author replied to."""
    object_id: int
    """ID of the :class:`.Comment`."""
    username: str
    """Name of the :class:`.Comment` author."""
    reply_username: str
    """Name of the :class:`.User` who the :class:`.Comment` author replied to."""

    def __str__(self) -> str:
        return self.comment

    async def get_author(self) -> "User":
        """Return the :class:`.Comment`'s author."""
        return await self._client.get_details_for_user(user_id=self.user)

    async def get_reply_user(self) -> Optional["User"]:
        """Return the :class:`.User`'s who the author replied to."""
        try:
            return await self._client.get_details_for_user(user_id=self.reply_to_user_id)
        except:
            return None

    async def get_map(self) -> "Map":
        """Return the :class:`.Map` on which the :class:`.Comment` was posted."""
        return await self._client.get_map_details(map_id=self.map)