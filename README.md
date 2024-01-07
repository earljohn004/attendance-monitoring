# Attendance Monitoring System

## Requirements

- Install [python 3.11](https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe)
- Optional: [Install VSCode](https://code.visualstudio.com/) for code modifications
- Prepare Gmail API credentials and Developer tokens

## Prepare the environment

1. Clone or Download this repository
   ![image](https://github.com/earljohn004/attendance-monitoring/assets/11734022/724e9893-6afe-4f18-bb31-85e0458a9d92)

2. Extract File and Open command prompt using the command `cmd` in the File Explorer
   ![image](https://github.com/earljohn004/attendance-monitoring/assets/11734022/12744904-754b-41d4-8d01-a8dbd60d4a5b)

3. Run the command `py -m venv .venv` to create a virtual environment
   ![image](https://github.com/earljohn004/attendance-monitoring/assets/11734022/f1f65c6f-6dad-4d03-9edb-ffbfb05b754e)

4. Run the command `.venv\Scripts\activate.bat`
   ![image](https://github.com/earljohn004/attendance-monitoring/assets/11734022/ccc8a53a-11ef-4b41-9510-afa764c30934)

5. Run the command `pip install -r requirements.txt` 
   ![image](https://github.com/earljohn004/attendance-monitoring/assets/11734022/78388e30-2b9e-4875-ada6-63fd8db9cb6c)

### How to use the software

6. Run the system using the command `python main.py`
   ![image](https://github.com/earljohn004/attendance-monitoring/assets/11734022/98ba704d-2900-4e6c-bc58-ca5573fa4722)

Arduino Software Serial read is not yet working. Demo software using `main.py`

## Google API credentials steps

### Enable Gmail API:

- Go to the Google Cloud Console.
- Create a new project or select an existing project.
- In the left navigation pane, click on "APIs & Services" -> "Library."
- Search for "Gmail API" and enable it for your project.

### Create Credentials:

- After enabling the Gmail API, go to "APIs & Services" -> "Credentials."
- Click on "Create Credentials" and choose "OAuth client ID."
- Select "Desktop app" as the application type.
- Download the credentials file (JSON format) and save it as credentials.json.
