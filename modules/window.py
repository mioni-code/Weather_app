from PyQt6.QtWidgets import QMainWindow, QFrame, QGridLayout, QLabel, QPushButton
from modules.app import app 
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QScrollArea 
from PyQt6.QtGui import QMouseEvent, QKeyEvent


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
        self.main_frame.setFixedSize(1024, 800)
        self.main_frame.setStyleSheet("background-color: #5D8AA8")

        self.main_layout = QHBoxLayout(self.main_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        
        self.frame_data_info = QFrame(parent=self.main_frame)
        self.frame_data_info.setStyleSheet("background-color: #FF9966")
        self.frame_data_info.setFixedSize(700, 800)
        self.main_layout.addWidget(self.frame_data_info)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        
        self.frame_data_info_layout = QVBoxLayout(self.frame_data_info)
        self.frame_data_info_layout.setContentsMargins(20, 20, 20, 20)
        self.frame_data_info_layout.setSpacing(10)
        
        self.settings_frame = QFrame(parent=self.frame_data_info)
        self.settings_frame.setStyleSheet("background-color: #003153")
        self.settings_frame.setFixedSize(660, 70)
        self.frame_data_info_layout.addWidget(self.settings_frame, 1)
        
        self.current_weather_frame = QFrame(parent=self.frame_data_info)
        self.current_weather_frame.setStyleSheet("background-color: #003153")
        self.current_weather_frame.setFixedSize(660, 335)
        self.frame_data_info_layout.addWidget(self.current_weather_frame, 1)
        
        self.next_days_weather_frame = QFrame(parent=self.frame_data_info)
        self.next_days_weather_frame.setStyleSheet("background-color: #003153") 
        self.next_days_weather_frame.setFixedSize(660, 335)
        self.frame_data_info_layout.addWidget(self.next_days_weather_frame, 1)

        
        

        
        
        
        
        
        

        
   
    
    

  
           

        

main_window = MainWindow()

