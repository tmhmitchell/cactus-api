FROM python:3.9-buster

WORKDIR /app

# Copy project files in
COPY cactus cactus
COPY Pipfile .
COPY Pipfile.lock .

RUN pip3 install pipenv

# Install app dependencies
RUN pipenv install --deploy --system

CMD ["pipenv", "run", "gunicorn", "cactus:run()", "--bind",  "0.0.0.0:8000", "--worker-class", "aiohttp.GunicornWebWorker", "--access-logfile", "-"]
