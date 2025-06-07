import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QTimer, Qt
from main_window import Ui_MainWindow
import torch
import cv2
import datetime
import logging

# 设置日志
logging.basicConfig(
    filename='detection_log.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def convert2QImage(img):
    height, width, channel = img.shape
    return QImage(img, width, height, width*channel, QImage.Format_RGB888)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.model = torch.hub.load('', 
                          'custom', 
                          path="runs/train/exp/weights/best.pt", 
                          source='local',
                          autoshape=True)  # 启用自动shape处理
        self.timer = QTimer()
        self.timer.setInterval(1)
        self.video = None
        self.bind_slots()

    def image_pred(self, file_path):
        img = cv2.imread(file_path)  # 读取为BGR格式
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转为RGB格式
    
        results = self.model(img)  # 传入图像数组而非路径
        image = results.render()[0].copy()
        
        # 获取检测结果
        detections = results.pandas().xyxy[0]
        result_text = ""
        for _, detection in detections.iterrows():
            label = detection['name']
            confidence = detection['confidence']
            result_text += f"状态: {label}, 置信度: {confidence:.2f}\n"
            # 记录日志
            logging.info(f"检测结果: 状态: {label}, 置信度: {confidence:.2f}")
        
        # 更新结果显示标签
        self.result_display.setText(result_text)
        
        return convert2QImage(image)

    def video_pred(self):
        ret, frame = self.video.read()
        if not ret:
            self.timer.stop()
        else:
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            self.input.setPixmap(QPixmap.fromImage(convert2QImage(frame)))
            results = self.model(frame)
            image = results.render()[0]
            
            # 获取检测结果
            detections = results.pandas().xyxy[0]
            result_text = ""
            for _, detection in detections.iterrows():
                label = detection['name']
                confidence = detection['confidence']
                result_text += f"状态: {label}, 置信度: {confidence:.2f}\n"
                # 记录日志
                logging.info(f"检测结果: 状态: {label}, 置信度: {confidence:.2f}")
            
            # 更新结果显示标签
            self.result_display.setText(result_text)
            
            self.output.setPixmap(QPixmap.fromImage(convert2QImage(image)))

    def open_image(self):
        print("点击了检测图片")
        self.timer.stop()
        file_path = QFileDialog.getOpenFileName(
            self, 
            directory='./data/datasets/images/train', 
            filter='*.jpg;*.png;*.jpeg'
        )
        if file_path[0]:
            input_pixmap = QPixmap(file_path[0]).scaled(
                self.input.size(), 
                Qt.KeepAspectRatio,  
                Qt.SmoothTransformation
            )
            self.input.setPixmap(input_pixmap)
    
            qimage = self.image_pred(file_path[0])
            output_pixmap = QPixmap.fromImage(qimage).scaled(
                self.output.size(),
                Qt.KeepAspectRatio,  
                Qt.SmoothTransformation
            )
            self.output.setPixmap(output_pixmap)

    def open_video(self):
        print("点击了检测视频")
        file_path = QFileDialog.getOpenFileName(self, directory='./data/datasets',
                                                filter='*.mp4')
        if file_path[0]:
            file_path = file_path[0]
            self.video = cv2.VideoCapture(file_path)
            self.timer.start()

    def bind_slots(self):
        self.det_image.clicked.connect(self.open_image)
        self.det_video.clicked.connect(self.open_video)
        self.timer.timeout.connect(self.video_pred)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()