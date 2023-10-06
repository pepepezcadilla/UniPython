import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit, QMainWindow, QStackedWidget, QMessageBox
from PyQt5.QtGui import QPixmap
from PIL import Image
from io import BytesIO

# Función para hacer una llamada a la API de NASA y devolver la respuesta JSON
def call_nasa_api(endpoint, params={}):
    base_url = "https://api.nasa.gov"
    api_key = "Ra7HdCODBCYjowtlzE2YfXwbYsqZvyJnkUFKiXBD"  # Reemplaza con tu API Key de la NASA
    params["api_key"] = api_key
    response = requests.get(f"{base_url}/{endpoint}", params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error al llamar a la API de la NASA.")
        return None

# Función para obtener la imagen del día y mostrarla
def get_and_show_nasa_image(image_label):
    date_data = call_nasa_api("planetary/apod")
    if date_data:
        image_url = date_data['url']
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            image_bytes = BytesIO(image_response.content)
            image = Image.open(image_bytes)
            pixmap = QPixmap()
            pixmap.loadFromData(image_bytes.getvalue())
            image_label.setPixmap(pixmap)
        else:
            print("Error al descargar la imagen de la NASA.")

class NASAInfoApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("NASA Info App")
        self.setGeometry(100, 100, 600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.stacked_widget = QStackedWidget()
        central_layout = QVBoxLayout()
        central_layout.addWidget(self.stacked_widget)
        central_widget.setLayout(central_layout)

        self.initUI()

    def initUI(self):
        # Botones de navegación
        self.nav_buttons = []

        # Pantalla de inicio
        self.home_widget = QWidget()
        self.stacked_widget.addWidget(self.home_widget)
        self.stacked_widget.setCurrentWidget(self.home_widget)

        layout_home = QVBoxLayout()

        self.menu_label = QLabel("Selecciona una opción:")
        layout_home.addWidget(self.menu_label)

        asteroid_button = QPushButton("1. Asteroids - NeoWs (Lista de asteroides)")
        asteroid_button.clicked.connect(self.show_asteroids)
        layout_home.addWidget(asteroid_button)
        self.nav_buttons.append(asteroid_button)

        mars_rover_button = QPushButton("2. Mars Rover (Curiosity)")
        mars_rover_button.clicked.connect(self.show_mars_rover)
        layout_home.addWidget(mars_rover_button)
        self.nav_buttons.append(mars_rover_button)

        image_of_the_day_button = QPushButton("3. Imagen del día")
        image_of_the_day_button.clicked.connect(self.show_image_of_the_day)
        layout_home.addWidget(image_of_the_day_button)
        self.nav_buttons.append(image_of_the_day_button)

        exit_button = QPushButton("4. Salir")
        exit_button.clicked.connect(self.close_app)
        layout_home.addWidget(exit_button)
        self.nav_buttons.append(exit_button)

        self.home_widget.setLayout(layout_home)

        # Pantalla de asteroides
        self.asteroid_widget = QWidget()
        self.stacked_widget.addWidget(self.asteroid_widget)

        layout_asteroids = QVBoxLayout()

        self.asteroid_result = QTextEdit(self)
        layout_asteroids.addWidget(self.asteroid_result)

        self.back_button_asteroids = QPushButton("Volver")
        self.back_button_asteroids.clicked.connect(self.show_home)
        layout_asteroids.addWidget(self.back_button_asteroids)

        self.asteroid_widget.setLayout(layout_asteroids)

        # Pantalla de Mars Rover
        self.mars_rover_widget = QWidget()
        self.stacked_widget.addWidget(self.mars_rover_widget)

        layout_mars_rover = QVBoxLayout()

        self.mars_rover_result = QTextEdit(self)
        layout_mars_rover.addWidget(self.mars_rover_result)

        self.back_button_mars_rover = QPushButton("Volver")
        self.back_button_mars_rover.clicked.connect(self.show_home)
        layout_mars_rover.addWidget(self.back_button_mars_rover)

        self.mars_rover_widget.setLayout(layout_mars_rover)

        # Pantalla de Imagen del Día
        self.image_of_the_day_widget = QWidget()
        self.stacked_widget.addWidget(self.image_of_the_day_widget)

        layout_image_of_the_day = QVBoxLayout()

        self.image_label = QLabel(self)
        layout_image_of_the_day.addWidget(self.image_label)

        self.back_button_image_of_the_day = QPushButton("Volver")
        self.back_button_image_of_the_day.clicked.connect(self.show_home)
        layout_image_of_the_day.addWidget(self.back_button_image_of_the_day)

        self.image_of_the_day_widget.setLayout(layout_image_of_the_day)

        self.show()

    def show_asteroids(self):
        asteroid_data = call_nasa_api("neo/rest/v1/neo/browse")
        if asteroid_data:
            asteroid_list = "\n".join([f"Nombre: {asteroid['name']}, Diámetro: {asteroid['estimated_diameter']['meters']['estimated_diameter_max']} metros" for asteroid in asteroid_data['near_earth_objects']])
            self.asteroid_result.setPlainText(asteroid_list)
            self.stacked_widget.setCurrentWidget(self.asteroid_widget)

    def show_mars_rover(self):
        rover_data = call_nasa_api("mars-photos/api/v1/rovers/curiosity", params={"sol": 1000})
        if rover_data:
            rover_info = f"Nombre: {rover_data['rover']['name']}\n" \
                         f"Fecha de aterrizaje: {rover_data['rover']['landing_date']}\n" \
                         f"Status: {rover_data['rover']['status']}"
            self.mars_rover_result.setPlainText(rover_info)
            self.stacked_widget.setCurrentWidget(self.mars_rover_widget)

    def show_image_of_the_day(self):
        get_and_show_nasa_image(self.image_label)
        self.stacked_widget.setCurrentWidget(self.image_of_the_day_widget)

    def show_home(self):
        self.stacked_widget.setCurrentWidget(self.home_widget)

    def close_app(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = NASAInfoApp()

    while True:
        # Mostrar el programa continuamente hasta que el usuario decida salir
        app.exec_()
        reply = QMessageBox.question(window, 'Salir', '¿Quieres salir de la aplicación?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            break  # Salir del bucle si el usuario elige salir

    sys.exit()