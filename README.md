# REQMAP

ReqMap is a web-based application for managing and visualizing software requirements. It allows users to create, update, and delete requirements, as well as view their relationships in a traceability diagram. You can view the full documentation [here](https://jerameee.github.io/reqmap-docs/).

## Features

- Create, read, update, and delete requirements
- Set priority and status for each requirement
- Track requirement versions
- Visualize requirement relationships with a traceability diagram

## Technology Stack

- Backend: Flask (Python)
- Database: SQLite with SQLAlchemy ORM
- Frontend: HTML, CSS
- Visualization: NetworkX, Matplotlib
- Docs MkDocs

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/reqmap.git
   cd reqmap
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the Flask development server:
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5000`

## Usage

- Add new requirements using the form on the main page
- View existing requirements in the list below the form
- Update or delete requirements by implementing the necessary frontend functionality (not included in the current version)
- Click on "View Traceability Diagram" to see the relationships between requirements

## Testing

Run the unit tests with:
```
python -m unittest test_app.py
```
