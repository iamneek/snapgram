FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen

COPY . .

ENV DJANGO_SETTINGS_MODULE=snapgram.settings.prod

ARG DJANGO_SECRET_KEY=dummy-secret-key-for-build

ENV DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY

RUN uv run python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["uv", "run", "gunicorn", "snapgram.wsgi:application", "--bind", "0.0.0.0:8000"]