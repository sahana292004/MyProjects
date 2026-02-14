
# SQL Query Generator

A simple SQL Query Generator built with FastAPI that generates SQL queries based on user prompts. This application leverages a template-based approach for generating SQL queries and integrates a chat engine for handling the generation logic.

## Features

- **Dynamic SQL Query Generation**: Generate SQL queries from user input prompts.
- **User-Friendly Interface**: Rendered using Jinja2 templates for an interactive experience.
- **Logging**: Comprehensive logging of requests and errors for better debugging and monitoring.
- **Health Check Endpoint**: Simple endpoint to verify the application's health.
- **Error Handling**: Robust error handling for a smoother user experience.

## Technologies Used

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+.
- **Jinja2**: A templating engine for Python to render HTML templates.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **Uvicorn**: A lightning-fast ASGI server for running FastAPI applications.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/sql-query-generator.git
   cd sql-query-generator
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Start the application**:

   ```bash
   uvicorn main:app --host 127.0.0.1 --port 8000
   ```

5. **Access the application**:
   Open your web browser and navigate to `http://127.0.0.1:8000`.

## Usage

1. **Navigate to the root page**:
   - You will see a form to enter your SQL query prompt.

2. **Input your SQL request**:
   - Enter your SQL query prompt (e.g., "Select all records from the hotels table where the city is 'Paris'.").

3. **Submit the form**:
   - The application will generate the SQL query based on your input.

4. **View the generated SQL query**:
   - The application will display the generated SQL query on the page.

## API Endpoints

### GET `/`

- Renders the main HTML page.

### POST `/generate`

- Generates an SQL query based on the user prompt.
- **Request Body**: 
  ```json
  {
    "user_prompt": "Your SQL prompt here."
  }
  ```
- **Response**:
  ```json
  {
    "sql_query": "Generated SQL query here."
  }
  ```

### GET `/healthcheck`

- Returns a health status of the application.
- **Response**:
  ```json
  {
    "status": "healthy"
  }
  ```

