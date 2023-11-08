import cv2
import mediapipe as mp
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QTimer

# Inicializa MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

class HandTrackingWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.label = QLabel(self)
        self.layout.addWidget(self.label)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(10)  # Actualiza cada 10 ms

        self.cap = cv2.VideoCapture(0)

    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Inv
        frame_rgb = cv2.flip(frame_rgb, 1)

        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                for point, landmark in enumerate(landmarks.landmark):
                    height, width, _ = frame.shape
                    cx, cy = int(landmark.x * width), int(landmark.y * height)
                    cv2.circle(frame, (cx, cy), 5, (255, 0, 0), -1)

                    # Calc
                    middle_x = width // 3
                    middle_y = height // 3

                    if cx < middle_x - 50 and cy < middle_y - 50:
                        # izquierda
                        print("Arriba Izquierda")
                    elif cx < middle_x - 50 and cy > middle_y + 50:
                        #  abajo izquierda
                        print("Abajo Izquierda")
                    elif cx > middle_x + 50 and cy < middle_y - 50:
                        #  arriba derecha
                        print("Arriba Derecha")
                    elif cx > middle_x + 50 and cy > middle_y + 50:
                        # abajo derecha
                        print("Abajo Derecha")

        height, width, channel = frame.shape
        bytes_per_line = 3 * width
        q_image = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_image)
        self.label.setPixmap(pixmap)


if __name__ == "__main__":
    app = QApplication([])
    window = HandTrackingWindow()
    window.show()
    app.exec_()