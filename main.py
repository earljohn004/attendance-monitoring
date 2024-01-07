import keyboard
from email_sender import EmailSender
from datetime import datetime

from image_capture import ImageCapture


if __name__ == "__main__":
    new_camera = ImageCapture()
    new_mail = EmailSender()
    new_mail.initialize_system()

    print("To Exit press 'Esc' key...\nTo capture press 'Enter' key...")

    while True:
        if keyboard.is_pressed("Esc"):
            break
        elif keyboard.is_pressed("Enter"):
            print("Capturing image....")
            new_camera.open_camera()

            print("Sending email....")
            now = datetime.now()
            current_time = now.strftime("%d/%m/%Y, %H:%M:%S")
            new_mail.send_message(
                recipient="mpguser004@gmail.com",
                body=f"Hello Parent, Earl John abaquita has arrived in school at {current_time}",
                subject="Attendance notification",
                image_name="captured_image.jpg",
            )
