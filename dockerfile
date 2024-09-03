FROM python:3.11.9-slim AS base

# Confgure poetry
ENV POETRY_NO_INTERACTION=1 \
    # Make poetry create virtual env in the project's root
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache \
    POETRY_VERSION=1.8.3

ENV VIRTUAL_ENV=/app/.venv 
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

# Install poetry
RUN pip install poetry==${POETRY_VERSION}

# Install dependencies
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.in-project true && poetry install --no-dev

FROM base AS runtime

# Copy app files from your server into the container
COPY . .

# Informs Docker that the container listens on the Streamlit's default port
EXPOSE 8501

# Instructs Docker to test that container is still working
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Executes streamlit run command line 
ENTRYPOINT ["python", "-m", "streamlit", "run", "app.py", "--server.port=8501"]


