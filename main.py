import keyboard
from email_sender import EmailSender
from datetime import datetime

from image_capture import ImageCapture
from sheets_database import SheetsDatabase


if __name__ == "__main__":
    new_camera = ImageCapture()
    new_mail = EmailSender()
    db = SheetsDatabase()

    new_mail.initialize_system()
    db.initialize_data()

    print("To Exit press 'Esc' key...\nTo capture press 'Enter' key...")

    while True:
        if keyboard.is_pressed("Esc"):
            break
        elif keyboard.is_pressed("Enter"):
            info = db.find_id_number("3453")

            print("Capturing image....")
            new_camera.open_camera()

            print("Sending email....")
            now = datetime.now()
            current_time = now.strftime("%m/%d/%Y, %H:%M:%S")
            new_mail.send_message(
                recipient=f"{info[1]}",
                body=f"Hello Parent, {info[0]} has arrived in school at {current_time}",
                subject="Attendance notification",
                image_name="captured_image.jpg",
            )
