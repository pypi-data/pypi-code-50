import aiohttp


async def validate(session: aiohttp.ClientSession, url, validator):
    async with session.get(url) as response:
        return await validator(response)


async def validate_status_ok(response: aiohttp.ClientResponse):
    # Bug with ssl https://github.com/aio-libs/aiohttp/issues/3535
    # Need to read the buffer.
    await response.read()
    return response.status == 200


async def validate_pypi(session, package_name):
    url = f'https://pypi.org/pypi/{package_name}/json'
    return not await validate(
        session, url, validate_status_ok
    )


async def validate_npm(session, package_name):
    url = f'https://api.npms.io/v2/package/{package_name}'
    return not await validate(
        session, url, validate_status_ok
    )
