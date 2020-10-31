"""cactus - a REST api for tracking soil moisture levels

Yes, this is overengineered for what it achieves. Pay no attention to that!
"""
import sentry_sdk
import sentry_sdk.integrations.aiohttp

import cactus.config
import cactus.core
import cactus.logging


def run():
    """Configure sentry+logging, return a WSGI application"""
    config = cactus.config.create()

    sentry_sdk.init(
        dsn=config.sentry_dsn,
        integrations=[sentry_sdk.integrations.aiohttp.AioHttpIntegration()],
        environment=config.environment
    )
    cactus.logging.configure()

    return cactus.core.create(config.api_token)
