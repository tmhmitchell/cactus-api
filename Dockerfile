FROM python:3.9-buster

WORKDIR /app

# Copy project contents in
COPY cactus cactus
COPY Pipfile.lock .

# Install pipenv
RUN pip3 install pipenv

# Install app dependencies
ENV PIPENV_VENV_IN_PROJECT=1
RUN pipenv install --ignore-pipfile --system

CMD ["pipenv", "run", "gunicorn", "cactus:run()", "--bind",  "0.0.0.0:8000", "--worker-class", "aiohttp.GunicornWebWorker", "--access-logfile", "-"]
