# List commands
default:
    @just --list

# Pre-commit check
check:
    pipenv run pre-commit run --all-files

# Start development server
dev: dump-req
    docker-compose -f docker-compose.yml down -v || true
    docker-compose -f docker-compose.yml up -d --build

# Dump installed packages into requirements.txt
dump-req:
    pipenv requirements > requirements.txt

# Set --set-upstream value and push
push:
    @git push --set-upstream origin `git rev-parse --abbrev-ref HEAD`

# Setup dev enviroment
setup:
    #! /usr/bin/bash
    mkdir -p .venv
    echo "Define a task" > app/task.txt
    npm install
    pipenv install --dev
    pipenv run pre-commit install

# Run Tailwindcss
tw:
    npx tailwindcss -i style.css -o ./app/static/css/style.css --watch
