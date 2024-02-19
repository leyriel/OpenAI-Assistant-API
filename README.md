# OpenAI Python Assistant

This project is a Python implementation that facilitates communication with an OpenAI-based virtual assistant. It aims to provide a simplified api interface for interacting with OpenAI's advanced language models.

## Technologies

- Python 3.x
- OpenAI API

## Features

- Real-time interaction with the OpenAI assistant.
- Ability to send text queries and receive responses.
- Simple and intuitive user interface.

## How to Use

To use this project, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies (`pip install -r requirements.txt`).
3. Set up your OpenAI API keys in a `.env` file.
4. Run the main script to start the assistant.

## Contributions
Contributions are always welcome! If you have any improvements or corrections, feel free to open an issue or a pull request.

### Create Database Migration
To create a new database migration, run the following command:
`alembic revision --autogenerate -m "Migration title`

### Push Database Migration
To apply the latest migration to your database, use:
`alembic upgrade head`

### Start Application
To start the application, execute:
`uvicorn app.main:app --reload`

### .env File Content
Create a `.env` file in the root directory of your project and include the following content:
`OPENAI_KEY="your_openai_key"
OPENAI_ASSISTANT_ID="your_openai_assistant_id"
DB_USERNAME="root"
DB_PASSWORD="root"
DB_SERVER="localhost"
DB_PORT="3306"
DB_NAME="your_database_name"
`
Ensure you have created and configured the `.env` file with your specific settings before starting the application.
