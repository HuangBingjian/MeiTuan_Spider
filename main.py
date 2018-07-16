#-*- coding:utf-8 -*-
import sys
from mt_parse import *


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = show_window()
    sys.exit(app.exec_())