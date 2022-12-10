from setuptools import setup, find_packages

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Operating System :: Microsoft :: Windows :: Windows 10",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3"
]

setup(
    name="tl3api",
    version="1.0.0",
    license="MIT",
    author="Feeeeddmmmeee",
    packages=find_packages(exclude="tests"),
    url="https://github.com/Feeeeddmmmeee/tl3api",
    classifiers=classifiers,
    description="An asynchronous API wrapper for the Traffic Lanes 3 / Intersection Controller API.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    keywords="api, ic, tl3, wrapper, async",
    requires=["aiohttp"]
)