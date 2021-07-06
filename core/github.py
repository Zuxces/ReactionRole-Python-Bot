import aiohttp


async def get_latest():
    # Get latest version string from GitHub
    async with aiohttp.ClientSession() as cs:
        async with cs.get(
            "https://raw.githubusercontent.com/Zuxces/ReactionRole-Python-Bot"
        ) as r:
            latest = await r.text()

    return latest.rstrip("\n").rstrip("\r")


async def check_for_updates(version):
    # Get latest version from GitHub repo and checks it against the current one
    latest = await get_latest()
    if latest > version:
        return latest

    return False


async def latest_changelog():
    # Get the changes for the latest version
    async with aiohttp.ClientSession() as cs:
        async with cs.get(
            "https://raw.githubusercontent.com/Zuxces/ReactionRole-Python-Bot"
        ) as r:
            changelog = await r.text()

    changelog = changelog.split("###")[1].rstrip(
        "\n"
    )  # Only get the latest version changes
    changelog = changelog[
        changelog.index("-") :
    ]  # Remove every character up to the first bullet point
    changelog += "\n\n[View more](https://github.com/Zuxces/)"

    return changelog
