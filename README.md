
# SnapGram

&nbsp;


<p align="center"><img src="https://socialify.git.ci/iamneek/snapgram/image?custom_language=Django&amp;font=Inter&amp;language=1&amp;name=1&amp;pattern=Circuit+Board&amp;&amp;&amp;theme=Light" alt="project-image"></p> <p align="center"><img src="https://img.shields.io/badge/Django-092E20?logo=django&amp;logoColor=white&amp;style=for-the-badge" alt="shields"><img src="https://img.shields.io/badge/Python-3776AB?logo=python&amp;logoColor=white&amp;style=for-the-badge" alt="shields"></p> <p id="description">A note-taking application built with Django.</p>

&nbsp;


A simple Instagram-like social media web app built with Django. Users can sign up, share photo posts, like and comment on posts, and manage their profiles.

**Live Demo:** [snapgram-k2zw.onrender.com](https://snapgram-k2zw.onrender.com/)

## Screenshots

<img width="1347" height="689" alt="image" src="https://github.com/user-attachments/assets/fcfe0745-1776-4a4c-b259-b9e657a80342" />


&nbsp;

<img width="1333" height="678" alt="image" src="https://github.com/user-attachments/assets/159a51fd-b497-4ecc-96d0-a0c880f85318" />


&nbsp;

<img width="1340" height="674" alt="image" src="https://github.com/user-attachments/assets/30f0aa59-52fc-4e79-865b-4c4a6d31b42b" />


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
   git clone https://github.com/iamneek/snapgram.git
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

### Keeping It Awake ( MISSION FAILED :( )

Render's free plan puts services to sleep after 15 minutes of inactivity, which causes a noticeable cold-start delay on the first request after a quiet period. To work around this, the deployed instance is monitored by [UptimeRobot](https://uptimerobot.com/), which pings the app every few minutes so it stays warm. (Didn't work for me)

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
