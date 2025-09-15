FROM python:3.13-alpine

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
    if [ "$INCLUDE_DEV" = "true" ]; then \
        poetry install --no-root --with test; \
    else \
        poetry install --no-root --without test --extras supervisord --extras cloudcli; \
    fi
