from datetime import datetime
from arduino_receiver import ArduinoReceiver
from email_sender import EmailSender
from image_capture import ImageCapture
from sheets_database import SheetsDatabase


if __name__ == "__main__":
    new_camera = ImageCapture()
    new_mail = EmailSender()
    db = SheetsDatabase()
    arduino = ArduinoReceiver(port="COM3")

    new_mail.initialize_system()
    db.initialize_data()

    def execute_system(id_number):
        print(f"Finding {id_number} in database..")
        info = db.find_id_number(id_number)

        if info[0] == "" or info[1] == "":
            print("RFID is not registered")
            return

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
    
    # TODO: For debugging and testing
    # execute_system(id_number="EBF64222")
    # arduino.debug_func_call(func=execute_system)

    arduino.read_serial(func=execute_system)
