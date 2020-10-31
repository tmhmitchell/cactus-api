# cactus-api

How to check the hyrdation of your cactus' soil if over-engineering things is your hobby

----

## Minimal method for running with Docker
```shell
docker build --tag cactus-api .
docker run -e CACTUS_API_TOKEN=<random-value> -e CACTUS_SENTRY_DSN=<sentry-dsn> -e CACTUS_ENVIRONMENT=<dev|prod> cactus-api
```