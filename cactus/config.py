"""config - handle application config"""
import dataclasses
import os

_ENV_API_TOKEN = 'CACTUS_API_TOKEN'
_ENV_SENTRY_DSN = 'CACTUS_SENTRY_DSN'
_ENV_ENVIRONMENT = 'CACTUS_ENVIRONMENT'


@dataclasses.dataclass
class CactusAPIConfig:
    """Container for API config"""
    api_token: str
    sentry_dsn: str
    environment: str


def validate_environment(env_name):
    """Ensure the "environment" we want to run as is either prod or dev"""
    if env_name not in ('prod', 'dev'):
        raise ValueError(f'Expected either "prod" or "dev", got "{env_name}"')


def read_from_environ(var_name) -> str:
    """Attempt to read a variable from the environment"""
    try:
        return os.environ[var_name]
    except KeyError as exc:
        raise KeyError(
            f'Environment variable "{var_name}" is not set') from exc


def create() -> CactusAPIConfig:
    """Read the environment and create a configuration object"""
    return CactusAPIConfig(
        read_from_environ(_ENV_API_TOKEN),
        read_from_environ(_ENV_SENTRY_DSN),
        read_from_environ(_ENV_ENVIRONMENT)
    )
