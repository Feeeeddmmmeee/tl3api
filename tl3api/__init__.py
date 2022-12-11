"""
Traffic Lanes 3 / Intersection Controller API Wrapper
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A basic async wrapper for the IC API

:copyright: (c) 2022-present Feeeeddmmmeee
:license: MIT, see LICENSE for more details
"""
from tl3api.comment import Comment
from tl3api.high_score import HighScore
from tl3api.map import Map 
from tl3api.user import User
from tl3api.wrapper import Client

__version__ = "1.2.0"

__all__ = ["Comment", "HighScore", "Map", "User", "Client"]