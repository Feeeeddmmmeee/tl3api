# tl3api

A basic, asynchronous wrapper for the API of Traffic Lanes 3 / Intersection Controller written in Python.

## Installation

tl3api was tested on python 3.9, although it should work wither earlier versions too. The recommended and easiest way to install tl3api is (pip)[https://pypi.org/project/pip/]
```sh
pip install tl3api
```

## Quickstart
The Client can be intialized with a context manager or not depending on which option is better for your application.
```py
import tl3api
import aiohttp

async with tl3api.Client(aiohttp.ClientSession()) as ic:
    ### Do stuff
```
With the `ic` instance you can then interact with the API:
```py
import tl3api
import aiohttp

async with tl3api.Client(aiohttp.ClientSession()) as ic:
    # Print the name of the user with the ID of 2452411
    user = await ic.get_details_for_user(user_id=2452411)
    print(user)

    # Print the name of each of the user's maps
    maps = await user.get_user_maps()
    for m in maps:
        print(m)
```

## License
tl3api is provided under the (MIT)[https://opensource.org/licenses/MIT] license. For more details view the LICENSE file.