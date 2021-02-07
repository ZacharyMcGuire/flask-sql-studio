# FLASK SQL Studio

This repository is built to solve a simple problem: how do I allow SQL Queries to be run against an MS SQL Server instance without granting the user any permissions to the DB or the Network.

This project will provide a Flask web server which can query a provided database & display the results as a table.

Project is setup to use docker to provide a web service and a database service.

## Requirements
* Docker.
* Docker Compose.

## Setup

1. Clone the repository.
2. Run `docker-compose up` in your favourite terminal.