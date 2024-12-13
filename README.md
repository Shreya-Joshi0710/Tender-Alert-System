# Tender Alert System

The **Tender Alert System** is a Python-based application that automates the process of fetching tender details from a database and notifying recipients via email. The project leverages modular coding practices and tools like Streamlit for the UI, and SMTP for email communication.

## Project Structure

```plaintext
TenderAlertSystem/
│
├── database/
│   ├── connection.py           # Handles SQL Server connection logic
│   ├── crud_operations.py      # Contains functions to fetch data from the database
│
├── email_sender/
│   ├── email_sender.py         # Handles email sending logic
│
├── ui/
│   ├── streamlit_ui.py         # Streamlit-based user interface
│
├── utils/
│   ├── environment.py          # Loads environment variables from .env file
│
├── main.py                     # Entry point to start the application
├── requirements.txt            # Python dependencies
└── .env                        # Environment variables
```

--------------------------------------------------------------------------------------------------------------------------

## Features

### Database
- **Connection Management**: Establishes a connection to the SQL Server database using credentials from the `.env` file.
- **CRUD Operations**: Fetches tender data filtered by date range.

### Email Sending
- Converts tender data to an HTML table and sends it via email to the recipient.
- Attaches a CSV file containing the tender details.

### User Interface
- Developed with **Streamlit** to allow users to:
  - Select date ranges for fetching tender data.
  - Specify the recipient email.
  - Preview fetched data before sending it.

### Environment Management
- Loads configurations like database credentials and email settings securely from the `.env` file.

--------------------------------------------------------------------------------------------------------------------------

## Setup Instructions

### Prerequisites
1. Install Python (version 3.8 or above).
2. Ensure SQL Server is configured and accessible.
3. Set up a Gmail account with an app-specific password for sending emails.

### Installation
1. Clone the repository:
   ```bash
   git clone "https://github.com/yourusername/TenderAlertSystem.git"
   cd TenderAlertSystem
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the `.env` file with your configurations:
   ```plaintext
   DB_SERVER=YOUR_SERVER_NAME
   DB_NAME=YOUR_DATABASE_NAME
   DB_DRIVER={ODBC Driver 17 for SQL Server}
   DB_TRUSTED_CONNECTION=yes

   EMAIL_SENDER=your_email@example.com
   EMAIL_PASSWORD=your_app_specific_password
   EMAIL_SMTP_SERVER=smtp.gmail.com
   EMAIL_SMTP_PORT=587
   ```

---

## Usage

1. Run the application:
   ```bash
   python main.py
   ```
2. Access the Streamlit UI in your web browser (usually at `http://localhost:8501`).
3. Follow these steps in the UI:
   - Select a date range.
   - Enter the recipient email address.
   - Fetch tenders and preview the results.
   - Send the email with the tender details.

--------------------------------------------------------------------------------------------------------------------------

## Code Overview

### Database Module (`database/`)
- **`connection.py`**:
  - Establishes connection to the SQL Server using the `pyodbc` library.
  - Connection details are securely loaded from the `.env` file.

- **`crud_operations.py`**:
  - Contains a function `fetch_filtered_records` to retrieve tender details for a given date range.

### Email Sending Module (`email_sender/`)
- **`email_sender.py`**:
  - Formats tender details as an HTML table and a CSV file.
  - Sends the email using `smtplib`.

### User Interface (`ui/`)
- **`streamlit_ui.py`**:
  - Provides an interactive interface for selecting date ranges, entering recipient details, fetching data, and sending emails.

### Utilities (`utils/`)
- **`environment.py`**:
  - Loads and manages environment variables.

### Entry Point (`main.py`)
- Initializes the environment and starts the Streamlit application.

--------------------------------------------------------------------------------------------------------------------------

## Dependencies

Listed in `requirements.txt`:
```plaintext
streamlit
pyodbc
pandas
smtplib
python-dotenv
```
Install dependencies with:
```bash
pip install -r requirements.txt
```

--------------------------------------------------------------------------------------------------------------------------

## Sample `.env` File

```plaintext
DB_SERVER=<your_database_server>
DB_NAME=<your_database_name>
DB_DRIVER={ODBC Driver 17 for SQL Server}
DB_TRUSTED_CONNECTION=Yes

EMAIL_SENDER=22BT04D150@gsfcuniversity.ac.in
EMAIL_PASSWORD=kefoizojabbboxek
EMAIL_SMTP_SERVER=smtp.gmail.com
EMAIL_SMTP_PORT=587
```

--------------------------------------------------------------------------------------------------------------------------

## License

This project is licensed under the MIT License. See the LICENSE file for details.

--------------------------------------------------------------------------------------------------------------------------

## Acknowledgments

- **Streamlit** for the user-friendly UI framework.
- **Python Dotenv** for managing environment variables.
- **Pandas** for efficient data manipulation.

--------------------------------------------------------------------------------------------------------------------------

## Contact
For any issues or feature requests, please contact
[Shreya Joshi](mailto:shreya.joshi2025@gmail.com) / [Devanshi Dhabalia](mailto:dhabaliadevanshi@gmail.com).

--------------------------------------------------------------------------------------------------------------------------