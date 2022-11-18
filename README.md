# Current Task

Simple FastAPI app to display the current task being focused on.

## Inspiration

While developing, I often lose track of what I am focusing on and end up making a bunch of unrelated changes leading to a gnarly commit history. This app was created to keep me focused on the task at hand. It's a simple page with a card that displays the current task and a button allowing me to update what the current focus is via a simple form with a single textarea. The main page will poll for the current task every 5 seconds (this can be adjusted by setting the `INTERVAL` environment variable)

Since this app runs in docker and is available over the local network, I decided to repurpose an old iPod as a small screen to display the current objective that I am working on. This allows me to update the task from my desktop and the iPod will auto update to keep me on task.

## Configuration

Environment variables that can be set:

- `PORT`: Set the port number to access the page (localhost:PORT). Default `8000`.
- `INTERVAL`: Set the polling interval for getting the current task. Default `5s`.
