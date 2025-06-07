from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        
        # 创建主Widget和垂直布局
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        
        # 创建图片显示区域的水平布局
        self.image_layout = QtWidgets.QHBoxLayout()
        
        # 输入图像区域
        self.input = QtWidgets.QLabel()
        self.input.setMinimumSize(600, 400)
        self.input.setStyleSheet("""
            QLabel {
                background: #2D2D2D;
                border: 2px solid #3D3D3D;
                border-radius: 8px;
                padding: 10px;
            }
        """)
        self.input.setAlignment(QtCore.Qt.AlignCenter)
        
        # 输出图像区域
        self.output = QtWidgets.QLabel()
        self.output.setMinimumSize(600, 400)
        self.output.setStyleSheet("""
            QLabel {
                background: #2D2D2D;
                border: 2px solid #3D3D3D;
                border-radius: 8px;
                padding: 10px;
            }
        """)
        self.output.setAlignment(QtCore.Qt.AlignCenter)

        # 添加图片显示区域到布局
        self.image_layout.addWidget(self.input)
        self.image_layout.addWidget(self.output)
        
        # 创建结果显示区域
        self.result_display = QtWidgets.QLabel()
        self.result_display.setStyleSheet("""
            QLabel {
                background: #2D2D2D;
                border: 2px solid #3D3D3D;
                border-radius: 8px;
                padding: 10px;
                color: white;
                font: bold 14px;
            }
        """)
        self.result_display.setAlignment(QtCore.Qt.AlignCenter)
        self.result_display.setText("检测结果将显示在这里")
        
        # 创建按钮区域
        self.button_layout = QtWidgets.QHBoxLayout()
        
        # 图片检测按钮
        self.det_image = QtWidgets.QPushButton()
        self.det_image.setMinimumSize(200, 50)
        self.det_image.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #4CAF50, stop:1 #45a049);
                border-radius: 8px;
                color: white;
                font: bold 14px;
                padding: 10px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #66BB6A, stop:1 #5CB85C);
            }
        """)
        
        # 视频检测按钮
        self.det_video = QtWidgets.QPushButton()
        self.det_video.setMinimumSize(200, 50)
        self.det_video.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #2196F3, stop:1 #1976D2);
                border-radius: 8px;
                color: white;
                font: bold 14px;
                padding: 10px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #42A5F5, stop:1 #1E88E5);
            }
        """)

        # 添加按钮到布局
        self.button_layout.addStretch()
        self.button_layout.addWidget(self.det_image)
        self.button_layout.addSpacing(40)
        self.button_layout.addWidget(self.det_video)
        self.button_layout.addStretch()
        
        # 主布局组合
        self.main_layout.addLayout(self.image_layout, 80)
        self.main_layout.addWidget(self.result_display, 10)
        self.main_layout.addSpacing(30)
        self.main_layout.addLayout(self.button_layout, 20)
        
        # 设置全局样式
        self.centralwidget.setStyleSheet("""
            QMainWindow {
                background: #1E1E1E;
            }
            QLabel[objectName^="input"], QLabel[objectName^="output"] {
                color: #888888;
                font: 14px;
            }
        """)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        # 状态栏样式
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("""
            QStatusBar {
                background: #2D2D2D;
                color: #AAAAAA;
            }
        """)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MCT档杆状态开合识别系统 - 智能检测平台"))
        self.input.setText(_translate("MainWindow", "原始图像显示区域"))
        self.output.setText(_translate("MainWindow", "检测结果输出区域"))
        self.det_image.setText(_translate("MainWindow", "📷 图像检测"))
        self.det_video.setText(_translate("MainWindow", "🎥 视频检测"))