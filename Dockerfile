FROM python:3.13-alpine

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_CACHE_DIR="/.cache" \
    POETRY_CACHE_DIR="/.poetry-cache" \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    PATH="/opt/poetry/bin:$PATH" \
    COLLECT_ANALYTICS=0

RUN apk add --no-cache build-base gfortran linux-headers libgomp openblas-dev lapack-dev

ADD https://install.python-poetry.org /tmp/install-poetry.py
RUN python /tmp/install-poetry.py

WORKDIR /label-studio-enterprise
ENV VENV_PATH="/label-studio-enterprise/.venv"
ENV PATH="$VENV_PATH/bin:$PATH"

COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN --mount=type=cache,target=/.poetry-cache,id=poetry-cache-alpine,sharing=locked \
    poetry check --lock && \
    poetry install --no-root -vvvv
