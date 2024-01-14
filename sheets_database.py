import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class SheetsDatabase:
    SCOPES = [
        "https://www.googleapis.com/auth/gmail.send",
        "https://www.googleapis.com/auth/spreadsheets.readonly",
    ]

    def __init__(self) -> None:
        self.creds = None
        self.spreadsheet_id = "1oOI7Srf2lyqvMmtumRY0e9N7A-k3wBe6a8RMXtyfjCo"
        self.spreadsheet_range = "Sheet1!A2:C15"
        self._authorize_access()

    def _authorize_access(self):
        if os.path.exists("token.json"):
            self.creds = Credentials.from_authorized_user_file(
                "token.json", self.SCOPES
            )
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", self.SCOPES
                )
                self.creds = flow.run_local_server(port=0)
            with open("token.json", "w") as token:
                token.write(self.creds.to_json())

    def initialize_data(self):
        try:
            service = build("sheets", "v4", credentials=self.creds)

            sheet = service.spreadsheets()
            result = (
                sheet.values()
                .get(
                    spreadsheetId=self.spreadsheet_id,
                    range=self.spreadsheet_range,
                )
                .execute()
            )
            self.values = result.get("values", [])
        except HttpError as err:
            print(err)

    def find_id_number(self, search_id: str):
        if not self.values:
            return ("", "")

        for row in self.values:
            if row[0] == search_id:
                print(f"{row[0]}, {row[1]}, {row[2]}")
                return (row[1], row[2])


if __name__ == "__main__":
    db = SheetsDatabase()
    db.initialize_data()
