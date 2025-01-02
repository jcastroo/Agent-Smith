# Agent Smith

**Agent Smith** is a Python application designed to monitor website statuses and send email alerts using the Gmail API if any website becomes unavailable.

## Features

- Monitors the status of user-configured websites every 12 hours (43200 seconds).
- Sends email alerts via Gmail API when a website encounters an error or goes offline.
- Configurable check intervals.

## Requirements

- Python 3.7 or higher
- Gmail API credentials
- Python dependencies (installed automatically)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/jcastroo/agent-smith.git
cd agent-smith
```

### 2. Requirements

```bash
pip install -r requirements.txt
```
### 3. Install the package

```bash
pip install .
```

### 4. Configure Gmail API credentials

   1. Go to the Google Cloud Console.
   2. Create a project and enable the Gmail API.
   3. Download the credentials.json file and place it in the project directory.

### 5. Authenticate the user

The first time you run the script, it will open a Google authentication window for you to grant access to the API.

### 6. Usage

Run the monitor directly from the terminal:

```bash
agent-smith
```
### 7. Configuration

Edit the main.py file to customize:

    Website List: Add or remove websites in the Websites variable.
    Check Interval: Adjust the check_interval value to set the time (in seconds) between checks.
    Email Recipient: Update the email_receiver value with the recipient's email address for alerts.

### 8. Dependencies

    requests
    google-auth
    google-auth-oauthlib
    google-api-python-client

These dependencies are installed automatically during the setup process.

### 9. License

This project is licensed under the MIT License.


### 10. Notes:
- Replace `https://github.com/jcastroo/Agent-Smith` with the actual repository URL, if applicable.
- Feel free to modify the content to better suit your specific needs or preferences.

### Created by João Castro.
