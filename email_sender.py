import base64
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import time
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError


class EmailSender:
    SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
    CREDENTIALS_JSON = "credentials.json"

    def __init__(self):
        self.flow = None
        self.creds = None
        self.service = None
        assert os.path.exists(
            self.CREDENTIALS_JSON
        ), f"{self.CREDENTIALS_JSON} does not exist. System will shut down"

    def initialize_system(self):
        self.flow = InstalledAppFlow.from_client_secrets_file(
            self.CREDENTIALS_JSON, self.SCOPES
        )
        self.creds = self.flow.run_local_server(port=0)
        self.service = build("gmail", "v1", credentials=self.creds)

    def send_message(self, subject: str, recipient: str, image_name: str, body: str):
        assert recipient is not None, "Unable to send message due to empty recipient"

        with open(image_name, "rb") as f:
            image_part = MIMEImage(f.read())

        message = MIMEMultipart()

        message["Subject"] = subject
        message["To"] = recipient
        html_part = MIMEText(body)
        message.attach(html_part)
        message.attach(image_part)
        create_message = {"raw": base64.urlsafe_b64encode(message.as_bytes()).decode()}

        try:
            message = (
                self.service.users()
                .messages()
                .send(userId="me", body=create_message)
                .execute()
            )
            print(f'sent message to {message} Message Id: {message["id"]}')
        except HTTPError as error:
            print(f"An error occurred: {error}")
            message = None


if __name__ == "__main__":
    new_mail = EmailSender()
    new_mail.initialize_system()
    time.sleep(3)
    new_mail.send_message(
        recipient="mpguser004@gmail.com",
        body="Hello Parent, Earl John abaquita has arrived in school at 07:52am",
        subject="Attendance notification",
        image_name="captured_image.jpg",
    )
