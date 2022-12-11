from typing import Optional, List, Literal

import aiohttp

from tl3api.user import User
from tl3api.map import Map
from tl3api.comment import Comment
from tl3api.high_score import HighScore

class Client:
    """A :class: for handling API requests."""

    def __init__(self, session: aiohttp.ClientSession):
        """Initialize a :class:`.Client` class instance.
        
        :param session: An aiohttp client session.

        """
        self._session = session

    async def __aenter__(self) -> "Client":
        return self

    async def __aexit__(self, *args):
        await self.close()

    async def close(self):
        """Close the aiohttp :class:`ClientSession`."""
        await self._session.close()

    async def get_details_for_user(self, user_id: int) -> Optional[User]:
        """Create a :class:`.User` instance from its ID.
        
        :param user_id: The :class:`.User`'s ID.
        """
        async with self._session.get("https://tl3.shadowtree-software.se/TL3BackEnd/rest/user2/public/info/" + str(user_id), verify_ssl=False) as response:
            try:
                user =  User(self, await response.json())
            except:
                user = None

        return user

    async def search_for_users(
        self, 
        query: str, 
        result: int, 
        page: int = 0
    ) -> List[User]:
        """Create a list of :class:`.User`s with names similar to the specified query.
        
        :param query: Name to search for.
        :param result: Amount of :class:`.User`s to return on each page.
        :param page: Which page to return.
        """
        async with self._session.get(f"https://tl3.shadowtree-software.se/TL3BackEnd/rest/user2/public/search?result={result}&page={page}&query={query}", verify_ssl=False) as response:
            users = await response.json()

        users = [await self.get_details_for_user(User(self, user).object_id) for user in users]
        return users

    def get_map_thumbnail_url(self, map_id: int) -> str:
        """Returns the thumbnail url for a :class:`.Map`."""
        return f"https://tl3.shadowtree-software.se/TL3BackEnd/rest/map/public/{map_id}/thumb"

    async def get_map_details(self, map_id: int) -> Optional[Map]:
        """Create a :class:`.Map` instance from its ID.
        
        :param map_id: The :class:`.Map`'s ID.
        """
        async with self._session.get(f"https://tl3.shadowtree-software.se/TL3BackEnd/rest/map/public/{map_id}/meta", verify_ssl=False) as response:
            try:
                _map = Map(self, await response.json())
            except:
                _map = None

        return _map

    async def list_maps_by_user(
        self, 
        user_id: int, 
        max_version: int = 999, 
        result: int = 50, 
        page: int = 0
    ) -> List[Map]:
        """Return a :class:`List` of :class:`.Map`'s made by the :class:`.User`.
        
        :param user_id: ID of the :class:`.User`.
        :param max_version: The requester's game version, so if you have version 10 of the app you will not get :class:`.Map`s that were made using 20 and might not be possible to play. 
        :param result: Amount of :class:`.Map`s to return on each page.
        :param page: Which page to return.
        """
        async with self._session.get(f"https://tl3.shadowtree-software.se/TL3BackEnd/rest/map/public/user/{user_id}?maxversion={max_version}&result={result}&page={page}", verify_ssl=False) as response:
            maps = await response.json()

        maps = [Map(self, _map) for _map in maps]
        return maps

    async def search_for_maps(
        self, 
        query: str, 
        game_mode: Literal[1, 2, 3], 
        result: int, 
        page: int = 0, 
        max_version: int = 999
    ) -> List[Map]:
        """Create a list of :class:`.Map`s with names similar to the specified query.
        
        :param query: Name to search for.
        :param game_mode: 1 => Simulation, 2 => Traffic Controller, 3 => Miscellaneous.
        :param result: Amount of :class:`.Map`s to return on each page.
        :param page: Which page to return.
        :param max_version: The requester's game version, so if you have version 10 of the app you will not get :class:`.Map`s that were made using 20 and might not be possible to play. 
        """
        async with self._session.get(f"https://tl3.shadowtree-software.se/TL3BackEnd/rest/map/public/top/{game_mode}/search?maxversion={max_version}&result={result}&page={page}&query={query}", verify_ssl=False) as response:
            maps = await response.json()

        maps = [Map(self, _map) for _map in maps]
        return maps

    async def list_new_maps(
        self, 
        game_mode: Literal[1, 2, 3], 
        result: int, 
        page: int = 0, 
        max_version: int = 999
    ) -> List[Map]:
        """Create a list of :class:`.Map`s that were recently uploaded.
        
        :param game_mode: 1 => Simulation, 2 => Traffic Controller, 3 => Miscellaneous.
        :param result: Amount of :class:`.Map`s to return on each page.
        :param page: Which page to return.
        :param max_version: The requester's game version, so if you have version 10 of the app you will not get :class:`.Map`s that were made using 20 and might not be possible to play. 
        """
        async with self._session.get(f"https://tl3.shadowtree-software.se/TL3BackEnd/rest/map/public/new/{game_mode}?maxversion={max_version}&result={result}&page={page}", verify_ssl=False) as response:
            maps = await response.json()

        maps = [Map(self, _map) for _map in maps]
        return maps

    async def find_top_maps(
        self, 
        game_mode: Literal[1, 2, 3], 
        time: Literal["alltime", "month", "week", "day"], 
        result: int, 
        max_version: int = 999, 
        page: int = 0, 
        offset: int = 0, 
        trendsystem: Literal[0, 1] = 1
    ) -> List[Map]:
        """Create a list of :class:`.Map` that currently are in one of the top categories.
        
        :param game_mode: 1 => Simulation, 2 => Traffic Controller, 3 => Miscellaneous.
        :param time: Which trending category to use.
        :param result: Amount of :class:`.Map`s to return on each page.
        :param max_version: The requester's game version, so if you have version 10 of the app you will not get :class:`.Map`s that were made using 20 and might not be possible to play. 
        :param page: Which page to return.
        :param offset: How many weeks / months / days from today to give results for, negative to go back in time, positive will give future and thus usually an empty list.
        :param trendsystem: Should always be set to 1 as that is the current version used ingame. 
        """

        async with self._session.get(f"https://tl3.shadowtree-software.se/TL3BackEnd/rest/map/public/top/{game_mode}/{time}?maxversion={max_version}&result={result}&page={page}&trendsystem={trendsystem}&offset={offset}", verify_ssl=False) as response:
            maps = await response.json()

        maps = [Map(self, _map) for _map in maps]
        return maps

    async def list_comments_on_map(
        self, 
        map_id: int, 
        limit: int, 
        before: Optional[int] = None
    ) -> List[Comment]:
        """Create a list of :class:`.Comment`s under a certain :class:`.Map`.
        
        :param map_id: ID of the :class:`.Map`.
        :param limit: Amount of :class:`.Comment`s to return.
        :param before: ID of :class:`.Comment` to fetch results after, in order to not get duplicates.
        """

        if before: before = f"&before={before}"
        else: before = ""

        async with self._session.get(f"https://tl3.shadowtree-software.se/TL3BackEnd/rest/comment/public/{map_id}?limit={limit}{before}", verify_ssl=False) as response:
            comments = await response.json()
        
        comments = [Comment(self, comment) for comment in comments]
        return comments

    async def list_high_scores_on_map(
        self, 
        map_id: int, 
        count: int
    ) -> List[HighScore]:
        """Return :class:`.HighScore`s from a certain :class:`.Map`.
        
        :param map_id: ID of the :class:`.Map`.
        :param count: Amount of :class:`.HighScore`s to get.
        """

        async with self._session.get(f"https://tl3.shadowtree-software.se/TL3BackEnd/rest/highscore/public/{map_id}?count={count}", verify_ssl=False) as response:
            high_scores = await response.json()

        high_scores = [HighScore(self, high_score) for high_score in high_scores]
        return high_scores