"""core - route definitions and WSGI app creation"""
import logging

from aiohttp import web

_HYDRATION_KEY = 'hydration'
_API_TOKEN_KEY = 'api-token'
_API_TOKEN_HEADER = 'X-Cactus-Auth'

logger = logging.getLogger(__name__)


async def set_hydration(request: web.Request) -> web.Response:
    """Validate request authorisation, then retrieve the hydration value
    sent and store it in the application context for later use.

    A hydration value must be between 0 and 1 (inclusively).
    """
    # Confirm presence and validity of auth token
    if request.headers.get(_API_TOKEN_HEADER) is None:
        logger.warning('Request is missing %s header', _API_TOKEN_HEADER)
        return web.json_response(data={}, status=401)

    # NOTE: Not constant time, but this is a toy, so it doesn't matter
    if request.headers[_API_TOKEN_HEADER] != request.app[_API_TOKEN_KEY]:
        logger.warning('Received token did not match configured token')
        return web.json_response(data={}, status=401)

    # Retrieve, validate and store hyrdation data
    data = await request.json()

    if _HYDRATION_KEY not in data:
        logger.info('No hydration key in request json')
        return web.json_response(data={}, status=400)

    if not 0 <= data[_HYDRATION_KEY] <= 1:
        logger.info(
            'Hydration value is out of bounds - (%.1f)', data[_HYDRATION_KEY])
        return web.json_response(data={}, status=400)

    request.app[_HYDRATION_KEY] = data[_HYDRATION_KEY]
    logger.info('Set hydration to %s', data[_HYDRATION_KEY])

    return web.json_response(data={}, status=200)


async def get_hydration(request: web.Request) -> web.Response:
    """Retrieve a hydration value from app context return it to the client"""
    hydration = request.app.get(_HYDRATION_KEY)

    if hydration is None:
        logger.warning('Hydration was requested before being set')

    return web.json_response(data={'hydration': hydration}, status=200)


def create(api_token: str) -> web.Application:
    """Create a WSGI application"""
    app = web.Application()
    app.add_routes(
        [
            web.get('/1/hydration', get_hydration),
            web.post('/1/hydration', set_hydration)
        ]
    )
    app[_API_TOKEN_KEY] = api_token
    return app
