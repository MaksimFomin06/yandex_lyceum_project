import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow
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
        self.lineEdit_latitude.setText("55.768603")
        self.lineEdit_longitude.setText("49.148222")
        self.lineEdit_scale.setText("0.0025")

        self.server_address = 'https://static-maps.yandex.ru/v1?'
        self.api_key = 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'

        self.pushButton_search.clicked.connect(self.maps_api)

    def maps_api(self):
        import requests

        latitude = self.lineEdit_latitude.text()
        longitude = self.lineEdit_longitude.text()
        scale = self.lineEdit_scale.text()
        ll_spn = f'll={longitude},{latitude}&spn={scale},{scale}'
        map_request = f"{self.server_address}{ll_spn}&apikey={self.api_key}"
        response = requests.get(map_request)
        print(map_request)
        if not response.ok:
            print(f"Ошибка выполнения запроса: {response.status_code}")
            return
        pixmap = QPixmap()
        pixmap.loadFromData(response.content)
        self.map_label.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WebProject()
    ex.show()
    sys.exit(app.exec())