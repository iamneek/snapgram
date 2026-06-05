# SnapGram

A simple Instagram-like social media web app built with Django. Users can sign up, share photo posts, like and comment on posts, and manage their profiles.

**Live Demo:** [snapgram-k2zw.onrender.com](https://snapgram-k2zw.onrender.com/)

## Screenshots

<!-- Add screenshot of the feed here -->

&nbsp;

<!-- Add screenshot of a user profile here -->

&nbsp;

<!-- Add screenshot of the post detail / comments here -->

&nbsp;

## Features

- User registration, login, and logout
- Custom user profiles with bio and avatar
- Create, view, and delete photo posts
- Like and unlike posts
- Comment on posts and delete your own comments
- Paginated feed of recent posts
- User search
- HTMX-powered interactions (likes, comments, pagination) without full page reloads

## Tech Stack

- **Backend:** Django 6, Python 3.13
- **Database:** PostgreSQL
- **Storage:** Cloudinary (for post images and avatars)
- **Frontend:** Django templates, Tailwind CSS, DaisyUI, HTMX
- **Server:** Gunicorn + WhiteNoise
- **Deployment:** Docker on Render

## Local Setup

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd SnapGram
   ```

2. Create a virtual environment and install dependencies (using `uv`):
   ```bash
   uv sync
   ```

3. Copy the environment example file and fill in your values:
   ```bash
   cp .env.example .env
   ```
   You will need a PostgreSQL database and a Cloudinary account.

4. Run migrations and start the dev server:
   ```bash
   uv run python manage.py migrate
   uv run python manage.py runserver
   ```

## Deployment

The app is deployed on [Render](https://render.com/) using the included `Dockerfile`.

### Keeping It Awake

Render's free plan puts services to sleep after 15 minutes of inactivity, which causes a noticeable cold-start delay on the first request after a quiet period. To work around this, the deployed instance is monitored by [UptimeRobot](https://uptimerobot.com/), which pings the app every few minutes so it stays warm.

- **Uptime status:** [stats.uptimerobot.com/RwVnflyrPU](https://stats.uptimerobot.com/RwVnflyrPU)

## Project Structure

```
apps/
  posts/      # Post, Comment, Like models and feed/detail views
  users/      # Custom User and Profile models, auth and profile views
snapgram/     # Django project (settings, urls, wsgi)
templates/    # Django templates (base, feed, posts, users)
Dockerfile    # Container build for Render
```