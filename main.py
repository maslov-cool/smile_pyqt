import io
import sys
from PIL import Image

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QPoint

my_widget_design = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1000</width>
    <height>1000</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>1000</width>
    <height>1000</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>1000</width>
    <height>1000</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Рост хорошего настроения</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QSlider" name="slider">
    <property name="geometry">
     <rect>
      <x>970</x>
      <y>40</y>
      <width>20</width>
      <height>500</height>
     </rect>
    </property>
    <property name="orientation">
     <enum>Qt::Vertical</enum>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class GoodMoodRising(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(my_widget_design)
        uic.loadUi(f, self)

        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(50)
        self.slider.valueChanged.connect(self.update)

    def paintEvent(self, event):
        size = self.slider.value()
        qp = QPainter()
        qp.begin(self)
        qp.setPen(QColor(255, 0, 0))
        qp.drawEllipse(0, 0, 10 * size, 10 * size)
        qp.drawEllipse(2 * size, 2 * size, 2 * size, 2 * size)
        qp.drawEllipse(6 * size, 2 * size, 2 * size, 2 * size)
        qp.drawArc(2 * size, 6 * size, 6 * size, 2 * size, -480, -1920)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GoodMoodRising()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())


