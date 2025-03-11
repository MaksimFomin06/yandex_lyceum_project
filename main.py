import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt6.QtCore import QEvent, Qt
from PyQt6.QtGui import QPixmap


class WebProject(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("app_design.ui", self)
        self.initUI()
    
    def initUI(self):
        self.map_label = QLabel(self)
        self.map_label.resize(761, 421)
        self.map_label.move(20, 215)
        self.scale_values = (0, 0.0001, 0.0002, 0.0004, 0.0007, 0.002, 0.003, 0.006, 0.02, 0.03, 0.05, 0.09, 0.2, 0.4, 0.7, 2, 3, 6, 12, 22, 40)
        self.scale_v = 5
        self.lineEdit_latitude.setText("55.768603")
        self.lineEdit_longitude.setText("49.148222")
        self.lineEdit_scale.setText(f"{self.scale_values[self.scale_v]}")
        self.server_address = 'https://static-maps.yandex.ru/v1?'
        self.api_key = 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'
        self.maps_api()
        self.pushButton_search.clicked.connect(self.maps_api)

    def keyPressEvent(self, event):
        if event.key() == 16777238:
            if self.scale_v != 20:
                self.scale_v += 1
                self.lineEdit_scale.setText(f"{self.scale_values[self.scale_v]}")
        elif event.key() == 16777239:
            if self.scale_v != 0:
                self.scale_v -= 1
                self.lineEdit_scale.setText(f"{self.scale_values[self.scale_v]}")
        elif event.key() == 16777235:
            self.move_map(0, 1)
        elif event.key() == 16777237:
            self.move_map(0, -1)
        elif event.key() == 16777234:
            self.move_map(-1, 0)
        elif event.key() == 16777236:
            self.move_map(1, 0)
        self.maps_api()

    def move_map(self, dx, dy):
        latitude = float(self.lineEdit_latitude.text())
        longitude = float(self.lineEdit_longitude.text())
        scale = float(self.lineEdit_scale.text())
        delta_lat = scale * dy
        delta_lon = scale * dx
        new_latitude = latitude + delta_lat
        new_longitude = longitude + delta_lon
        if -90 <= new_latitude <= 90 and -180 <= new_longitude <= 180:
            self.lineEdit_latitude.setText(f"{new_latitude}")
            self.lineEdit_longitude.setText(f"{new_longitude}")

    def maps_api(self):
        import requests

        latitude = self.lineEdit_latitude.text()
        longitude = self.lineEdit_longitude.text()
        scale = self.lineEdit_scale.text()
        ll_spn = f'll={longitude},{latitude}&spn={scale},{scale}'
        map_request = f"{self.server_address}{ll_spn}&apikey={self.api_key}"
        response = requests.get(map_request)
        if not response.ok:
            print(f"Ошибка выполнения запроса: {response.status_code}")
            return
        pixmap = QPixmap()
        pixmap.loadFromData(response.content)
        self.map_label.setPixmap(pixmap)
        self.map_label.setFocus()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WebProject()
    ex.show()
    sys.exit(app.exec())