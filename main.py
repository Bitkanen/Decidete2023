import cv2
import mediapipe as mp
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QTimer
import random

# Inicializa MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

class SnakeGameWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.label = QLabel(self)
        self.layout.addWidget(self.label)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(33)  # Actualiza cada 33 ms (aproximadamente 30 FPS)

        self.cap = cv2.VideoCapture(0)

        # Inicializa las variables del juego de Snake
        self.snake = [(5, 5)]
        self.food = self.generate_food()
        self.score = 0

        # Configuración para el rastro de la serpiente
        self.trail_length = 10  # Longitud máxima del rastro
        self.trail = []

    def generate_food(self):
        # Genera una ubicación aleatoria para la comida
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        return (x, y)

    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return

        # Invierte la imagen horizontalmente
        frame = cv2.flip(frame, 1)

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detección de manos
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            # Obtén la posición de la punta del dedo índice de la mano
            landmarks = results.multi_hand_landmarks[0]
            index_finger = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            height, width, _ = frame.shape
            x, y = int(index_finger.x * width), int(index_finger.y * height)

            # Actualiza la posición de la serpiente hacia la posición del dedo índice
            self.snake.insert(0, (x // 50, y // 50))

        # Mueve la serpiente
        new_head = self.snake[0]

        # Verifica colisión con las paredes
        if new_head[0] < 0 or new_head[0] >= 10 or new_head[1] < 0 or new_head[1] >= 10:
            self.snake = [(5, 5)]
            self.score = 0
            self.food = self.generate_food()
        else:
            # Verifica colisión con la comida
            if new_head == self.food:
                self.snake.insert(0, new_head)
                self.food = self.generate_food()
                self.score += 1
            else:
                self.snake.insert(0, new_head)
                if len(self.snake) > self.score + 1:
                    # Reduce la longitud de la serpiente
                    self.snake.pop()

        # Actualiza el rastro de la serpiente
        self.update_snake_trail()

        # Dibuja la serpiente y la comida
        frame = self.draw_snake_and_food(frame_rgb)

        height, width, channel = frame.shape
        bytes_per_line = 3 * width
        q_image = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_image)
        self.label.setPixmap(pixmap)

    def update_snake_trail(self):
        # Actualiza el rastro de la serpiente
        if len(self.snake) >= self.trail_length:
            self.trail.append(self.snake[-self.trail_length:])
        else:
            self.trail.append(self.snake[:])

        if len(self.trail) > self.trail_length:
            self.trail.pop(0)

    def draw_snake_and_food(self, frame):
        # Dibuja el rastro de la serpiente
        for trail_segment in self.trail:
            for segment in trail_segment:
                x, y = segment
                cv2.rectangle(frame, (x * 50, y * 50), (x * 50 + 50, y * 50 + 50), (0, 255, 0), -1)

        # Dibuja la serpiente
        for segment in self.snake:
            x, y = segment
            cv2.rectangle(frame, (x * 50, y * 50), (x * 50 + 50, y * 50 + 50), (0, 255, 0), -1)

        # Dibuja la comida
        x, y = self.food
        cv2.rectangle(frame, (x * 50, y * 50), (x * 50 + 50, y * 50 + 50), (0, 0, 255), -1)

        # Dibuja el marcador
        cv2.putText(frame, f"Score: {self.score}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        return frame


if __name__ == "__main__":
    app = QApplication([])
    window = SnakeGameWindow()
    window.show()
    app.exec_()



