import serial
import time


class ArduinoReceiver:
    def __init__(self, port="COM1", baud_rate=9600):
        self.arduino_port = port
        self.baud_rate = baud_rate
        self.timeout = 10
        self.delay_start = 5
        self.serial = serial.Serial(
            self.arduino_port, self.baud_rate, timeout=self.timeout
        )
    
    def configure_port(self, port):
        self.arduino_port = port

    def read_serial(self):
        time.sleep(self.delay_start)
        try:
            while True:
                if self.serial.in_waiting > 0:
                    data = self.serial.readline().decode("utf-8").strip()
                    print(f"Received from Arduino: {data}")
                    # TODO: Kani diri na part kay need ta ug code na mutrigger ra sa capture sa arduino

        except serial.SerialException as e:
            print(f"Error: {e}")

        finally:
            if self.serial.is_open:
                self.serial.close()


if __name__ == "__main__":
    arduino = ArduinoReceiver()
    arduino.read_serial()
