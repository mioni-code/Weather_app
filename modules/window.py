from PyQt6.QtWidgets import QMainWindow, QFrame, QGridLayout, QLabel, QPushButton
from modules.app import app 
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QScrollArea, QWidget
from PyQt6.QtGui import QMouseEvent, QKeyEvent



    
class CityCards(QFrame):
    def __init__(self, city_name, time, description, temperature, max_temp, min_temp, parent=None):
        super().__init__(parent =parent)
                
                
        self.setFixedHeight(90)
        self.setStyleSheet("background-color: #003153; border-radius: 10px; color: white;")
        row =QHBoxLayout(self)
        left = QVBoxLayout()
        left.addWidget(QLabel(city_name))
        left.addWidget(QLabel(time))
        left.addWidget(QLabel(description))
                
        right = QVBoxLayout()
        temperature_label = QLabel(temperature)
        temperature_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        minmax_label = QLabel(f"Max: {max_temp}°C, Min: {min_temp}°C")
        minmax_label.setAlignment(Qt.AlignmentFlag.AlignRight)
                
        right.addWidget(temperature_label)
        right.addWidget(minmax_label)
                
        row.addLayout(left)
        row.addLayout(right)
                
class CityList(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        
        self.setFixedSize(324, 800)
        self.setStyleSheet("background-color: #5D8AA8; border: none")
        self.dark_icon = True

        layout = QVBoxLayout(self)
        top = QHBoxLayout()
        self.theme_button = QPushButton("🌙")
        self.theme_button.setFixedSize(40, 28)
        self.theme_button.clicked.connect(self.change_icon)
        top.addWidget(self.theme_button)
        top.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout.addLayout(top)
        
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        
        content = QWidget()
        cards_layout = QVBoxLayout(content)
        
        cities = [
            ("Дніпро", "15:24", "Sunny", "25°C", "30°C", "20°C"),
            ("Київ", "15:24", "Cloudy", "18°C", "22°C", "15°C"),
            ("Львів", "15:24", "Rainy", "20°C", "25°C", "18°C"),
            ("Чернівці", "15:24", "Windy", "22°C", "28°C", "19°C"),
            ("Чернігів", "15:24", "Sunny", "24°C", "29°C", "21°C"),
            ("Одеса", "15:24", "Cloudy", "19°C", "23°C", "16°C"),
            ("Харків", "15:24", "Snowy", "-5°C", "-2°C", "-10°C"),
            ("Полтава", "15:24", "Sunny", "30°C", "35°C", "25°C"),
            ("Житомир", "15:24", "Windy", "20°C", "25°C", "15°C"),
            ("Вінниця", "15:24", "Rainy", "22°C", "27°C", "18°C"),
            
        ]        
        
        for city in cities:
            city_card = CityCards(*city)
            cards_layout.addWidget(city_card)

        scroll_area.setWidget(content)
        layout.addWidget(scroll_area)

    def change_icon(self):
        if self.dark_icon == True:
            self.theme_button.setText("☀️")
            self.dark_icon = False
        else:
            self.theme_button.setText("🌙")
            self.dark_icon = True


        

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.WIDTH_WINDOW = 1024
        self.HEIGHT_WINDOW  = 800
        
        primary_screen = app.primaryScreen()
        screen_size = primary_screen.size()
        width_screen = screen_size.width()
        height_screen = screen_size.height()

        self.setGeometry(
            (width_screen // 2) - (self.WIDTH_WINDOW // 2), 
            (height_screen // 2) - (self.HEIGHT_WINDOW // 2), 
            self.WIDTH_WINDOW, 
            self.HEIGHT_WINDOW
        )
        
        self.setStyleSheet("background-color: #5D8AA8")

        
        self.main_frame = QFrame(parent=self)
        self.main_frame.setFixedSize( self.WIDTH_WINDOW, self.HEIGHT_WINDOW)
        self.main_frame.setStyleSheet("background-color: #5D8AA8")

        self.main_layout = QHBoxLayout(self.main_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        

        self.frame_cities = CityList(parent = self.main_frame)
        self.frame_cities.setStyleSheet("background-color: gray")
        self.frame_cities.setFixedSize(324, 800)
        self.main_layout.addWidget(self.frame_cities)
        
        self.frame_data_info = QFrame(parent=self.main_frame)
        self.frame_data_info.setStyleSheet("background-color: #FF9966")
        self.frame_data_info.setFixedSize(700, 800)
        self.main_layout.addWidget(self.frame_data_info)
        
        self.frame_data_info_layout = QVBoxLayout(self.frame_data_info)
        self.frame_data_info_layout.setContentsMargins(20, 20, 20, 20)
        self.frame_data_info_layout.setSpacing(10)
        
        self.settings_frame = QFrame(parent=self.frame_data_info)
        self.settings_frame.setStyleSheet("background-color: #003153")
        self.settings_frame.setFixedSize(660, 50)
        self.frame_data_info_layout.addWidget(self.settings_frame)
        
        self.current_weather_frame = QFrame(parent=self.frame_data_info)
        self.current_weather_frame.setStyleSheet("background-color: #003153")
        self.current_weather_frame.setFixedSize(660, 340)
        self.frame_data_info_layout.addWidget(self.current_weather_frame)
        
        self.next_days_weather_frame = QFrame(parent=self.frame_data_info)
        self.next_days_weather_frame.setStyleSheet("background-color: #003153") 
        self.next_days_weather_frame.setFixedSize(660, 330)
        self.frame_data_info_layout.addWidget(self.next_days_weather_frame)
        

        
        
main_window = MainWindow()

 

