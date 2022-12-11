from typing import TYPE_CHECKING, Literal, Optional, List
from tl3api.base import ICObjectBase

if TYPE_CHECKING:
    from tl3api.user import User
    from tl3api.high_score import HighScore
    from tl3api.comment import Comment

class Map(ICObjectBase):
    """A :class: representing an Intersection Controller :class:`.Map`.

    =================================== ================================================
    Attribute                           Description
    =================================== ================================================
    name                                The name of the :class:`.Map`.
    desc                                The description of the :class:`.Map`.
    game_mode_group                     1 => Simulation, 2 => Traffic Controller, 3 => 
                                        Miscellaneous
    file_name                           ?
    file_ext                            ?
    author                              The ID of the :class:`.Map` author.
    created                             Timestamp of the :class:`.Map`'s creation date.
    updated                             Timestamp of the last update.
    game_version                        ?
    votes_up                            How many upvotes the :class:`.Map` has received.
    votes_down                          How many downvotes the :class:`.Map` has received.
    high_score                          The highest score on the :class:`.Map`.
    high_score_user                     ID of the :class:`.User` responsible for the high 
                                        score.
    fully_uploaded                      Whether the :class:`.Map` has been fully uploaded 
                                        or not.
    map_version                         Version of the :class:`.Map`.
    target_score                        The target score of the :class:`.Map`.
    favorties                           How many :class:`.Users` favorited the 
                                        :class:`.Map`.
    deleted                             ?
    object_id                           ID of the :class:`.Map`.
    author_name                         Name of the :class:`.Map` author.
    """
    name: str
    """The name of the :class:`.Map`."""
    desc: str
    """The description of the :class:`.Map`."""
    game_mode_group: Literal[1, 2, 3]
    """1 => Simulation, 2 => Traffic Controller, 3 => Miscellaneous"""
    file_name: str
    file_ext: str
    author: int
    """The ID of the :class:`.Map` author."""
    created: int
    """Timestamp of the :class:`.Map`'s creation date."""
    updated: int
    """Timestamp of the last update."""
    game_version: int
    votes_up: int
    """How many upvotes the :class:`.Map` has received."""
    votes_down: int
    """How many downvotes the :class:`.Map` has received."""
    high_score: int
    """The highest score on the :class:`.Map`."""
    high_score_user: int
    """ID of the :class:`.User` responsible for the high score."""
    fully_uploaded: bool
    """Whether the :class:`.Map` has been fully uploaded or not."""
    map_version: int
    """Version of the :class:`.Map`."""
    target_score: int
    """The target score of the :class:`.Map`."""
    favorites: int
    """How many :class:`.Users` favorited the :class:`.Map`."""
    deleted: bool
    object_id: int
    """ID of the :class:`.Map`."""
    author_name: str
    """Name of the :class:`.Map` author."""

    def __str__(self) -> str:
        return self.name

    async def get_author(self) -> "User":
        """Return the author :class:`.User` object."""
        return await self._client.get_details_for_user(user_id=self.author)

    async def get_high_score_user(self) -> Optional["User"]:
        """Return the high score :class:`.User`."""
        try:
            return await self._client.get_details_for_user(user_id=self.high_score_user)
        except:
            None

    def get_thumbnail_url(self) -> str:
        """Return the :class:`.Map`'s thumbnail url."""
        return self._client.get_map_thumbnail_url(map_id=self.object_id)

    async def get_comments(
        self, 
        limit: int, 
        before: Optional[int] = None
    ) -> List["Comment"]:
        """Return :class:`.Comment`s under this :class:`.Map`."""
        return await self._client.list_comments_on_map(map_id=self.object_id, limit=limit, before=before)

    async def get_high_scores(
        self, 
        count: int
    ) -> List["HighScore"]:
        """Return :class:`.HighScore`s under this :class:`.Map`"""
        return await self._client.list_high_scores_on_map(map_id=self.object_id, count=count)