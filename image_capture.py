import time
import cv2


class ImageCapture:
    IMAGE_CAPTURE_DELAY = 3

    def __init__(self):
        self.camera_index = 0
        self.save_path = "captured_image.jpg"
        self.cap = None
        pass

    def _intialize_system(self):
        self.cap = cv2.VideoCapture(self.camera_index)

        if not self.cap.isOpened():
            print("Error: Could not open camera.")
            return

        cv2.namedWindow("Camera Preview", cv2.WINDOW_NORMAL)

    def open_camera(self):
        self._intialize_system()
        while True:
            ret, frame = self.cap.read()

            if not ret:
                print("Error: Could not capture frame.")
                break

            cv2.imshow("Camera Preview", frame)

            for index in range(self.IMAGE_CAPTURE_DELAY, 0, -1):
                print(f"Capturing image in {index} seconds...")
                cv2.waitKey(1)

            cv2.imwrite(self.save_path, frame)
            print(f"Image captured and saved to {self.save_path}")
            break

    def __del__(self):
        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    new_camera = ImageCapture()
    new_camera.open_camera()
