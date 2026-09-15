import sys
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel
from hardware_control import HardwareController

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        self.controller = HardwareController()
        
        
        self.setWindowTitle("MSI Fan Kontrol Merkezi")
        self.resize(380, 280)
        
        
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1e1e2e;
            }
            QLabel {
                color: #cdd6f4;
                font-size: 15px;
                font-weight: bold;
                padding-bottom: 10px;
            }
            QPushButton {
                background-color: #313244;
                color: #cdd6f4;
                border: 1px solid #45475a;
                border-radius: 8px;
                padding: 12px;
                font-size: 14px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #45475a;
                border: 1px solid #f38ba8; /* MSI Kırmızısı Vurgu çizgisi */
            }
            QPushButton:pressed {
                background-color: #585b70;
            }
        """)

        # Fuck Ai
        main_layout = QVBoxLayout()
        main_layout.setSpacing(12)  # Butonların arasındaki boşluk
        
        
        fan_label = QLabel("⚡ FAN PERFORMANCE PROFİLE")
        main_layout.addWidget(fan_label)
        
        
        btn_silent = QPushButton(" Silent Mode")
        btn_silent.clicked.connect(lambda: self.controller.set_fan_profile("silent"))
        
        btn_auto = QPushButton("Auto Mode")
        btn_auto.clicked.connect(lambda: self.controller.set_fan_profile("auto"))
        
        btn_boost = QPushButton(" Cooler Boost (Uçuşa Geçiyoruz)")
        btn_boost.clicked.connect(lambda: self.controller.set_fan_profile("coolerboost"))
        
        
        main_layout.addWidget(btn_silent)
        main_layout.addWidget(btn_auto)
        main_layout.addWidget(btn_boost)

        
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)
