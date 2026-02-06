from setuptools import setup

setup(
    name="eve-cli",
    version="0.1.0",
    packages=["scripts"],
    entry_points={
        "console_scripts": [
            "eve-archive = scripts.cli:cli",
            "eve-metrics = scripts.cli:cli",
            "eve-nav = scripts.cli:cli",
        ],
    },
)