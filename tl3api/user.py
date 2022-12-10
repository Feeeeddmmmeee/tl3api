from typing import TYPE_CHECKING, List
from tl3api.base import ICObjectBase

if TYPE_CHECKING:
    from tl3api.map import Map

class User(ICObjectBase):
    """A :class: representing an Intersection Controller :class:`.User`.
    
    =================================== ================================================
    Attribute                           Description
    =================================== ================================================
    ``object_id``                       The ID of the :class:`.User`.
    ``game_version``                    ?
    ``last_login``                      Timestamp of the :class:`.User`'s last login to
                                        the game.
    ``maps``                            Amount of :class:`.Map`s the :class:`.User` has 
                                        uploaded.
    ``name``                            The :class:`.User`'s name.
    ``followers``                       Amount of followers the :class:`.User` has.
    """
    object_id: int
    """The ID of the :class:`.User`."""
    game_version: int
    last_login: int
    """Timestamp of the :class:`.User`'s last login to the game."""
    maps: int
    """Amount of :class:`.Map`s the :class:`.User` has uploaded."""
    name: str
    """The :class:`.User`'s name."""
    followers: int
    """ Amount of followers the :class:`.User` has."""

    def __str__(self) -> str:
        return self.name

    async def get_user_maps(
        self, 
        max_version: int = 999, 
        result: int = 50, 
        page: int = 0
    ) -> List["Map"]:
        """Return a :class:`List` of :class:`.Map`'s made by the :class:`.User`.
        
        :param max_version: The requester's game version, so if you have version 10 of the app you will not get :class:`.Map`s that were made using 20 and might not be possible to play. 
        :param result: Amount of :class:`.Map`s to return on each page.
        :param page: Which page to return.
        """
        return await self._client.list_maps_by_user(user_id=self.object_id, max_version=max_version, result=result, page=page)