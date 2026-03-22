# Mini Event Parser

A lightweight Flask-based API that extracts basic event information from text input and returns structured JSON output.

## Project Overview

This project is a simple backend demo for event parsing. It accepts raw event-related text through a REST API and identifies key fields such as:

- event name
- date
- time
- location

It is designed as a small prototype to demonstrate:

- backend API development with Flask
- basic rule-based text parsing
- JSON request/response handling
- Docker containerization
- automated testing with pytest
- CI workflow with GitHub Actions

## Features

- Health check endpoint: `/`
- Event parsing endpoint: `/parse`
- Extracts basic fields from input text
- Returns structured JSON output
- Dockerized for easy deployment
- Automated testing with pytest
- CI pipeline with GitHub Actions

## Project Structure

```text
mini-event-parser/
├── src/
│   └── app.py
├── tests/
│   └── test_app.py
├── .github/
│   └── workflows/
│       └── python-ci.yml
├── requirements.txt
├── Dockerfile
└── README.md