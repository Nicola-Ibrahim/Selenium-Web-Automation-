# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/nicola/AppData/Local/Temp/Facebook_UIAVWsby.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 750)
        MainWindow.setMinimumSize(QtCore.QSize(900, 750))
        MainWindow.setMaximumSize(QtCore.QSize(900, 750))
        MainWindow.setStyleSheet("/*\n"
"Aqua Style Sheet for QT Applications\n"
"Author: Jaime A. Quiroga P.\n"
"Company: GTRONICK\n"
"Last updated: 22/01/2019, 07:55.\n"
"Available at: https://github.com/GTRONICK/QSS/blob/master/Aqua.qss\n"
"*/\n"
"\n"
"\n"
"\n"
"QMainWindow {\n"
"\n"
"    \n"
"    \n"
"    \n"
"}\n"
"\n"
"QMessageBox {\n"
"    background-color: rgb(100, 100, 100);\n"
"    color: rgb(255,255,255);\n"
"}\n"
"\n"
"QMessageBox QLabel {\n"
"    color: rgb(255,255,255);\n"
"}\n"
"\n"
"QMessageBox QPushButton {\n"
"    color: rgb(255,255,255);\n"
"    \n"
"    background-color: rgb(47, 113, 255);\n"
"}\n"
"\n"
"QTableView{\n"
"    \n"
"    alternate-background-color : rgb(220, 220, 220); \n"
"    selection-background-color :     rgb(174, 174, 174);     \n"
"\n"
"\n"
"    gridline-color: rgb(0, 31, 98);\n"
"\n"
"    font: 16pt \"Arial\";\n"
"    \n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-radius:4px;\n"
"\n"
"    border-color: rgb(244, 154, 32);\n"
"\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: rgb(0, 31, 98) ;\n"
"    color: white;\n"
"    padding-left: 0px;\n"
"    border: 4px solid #6c6c6c;\n"
"    font: 75 18pt \"Arial\";\n"
"\n"
"    border-style: none;\n"
"    border-bottom: 1px solid #fffff8;\n"
"    border-right: 1px solid #fffff8;\n"
"    border-radius:4px;\n"
"\n"
"\n"
"}\n"
"\n"
"QHeaderView::section:checked\n"
"{\n"
"    background-color: rgb(255, 170, 0);\n"
"    border-radius:4px;\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border-top: 1px solid #fffff8;\n"
"    border-radius:4px;\n"
"}\n"
"\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border-left: 1px solid #fffff8;\n"
"    border-radius:4px;\n"
"}\n"
"\n"
"\n"
"QTableView QTableCornerButton::section {\n"
"    background:  rgb(244, 154, 32);\n"
"    border: 2px outset red;\n"
"    image:url(:/icons/icons/checkmark.svg)\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QTreeView {\n"
"    show-decoration-selected:1;\n"
"    \n"
"    font: 16pt \"Times New Roman\";\n"
"}\n"
"\n"
"QTreeView::item {\n"
"     border: 1px solid #d9d9d9;\n"
"    border-top-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"}\n"
"\n"
"QTreeView::item:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e7effd, stop: 1 #cbdaf1);\n"
"    border: 1px solid #bfcde4;\n"
"}\n"
"\n"
"QTreeView::item:selected {\n"
"    border: 1px solid #567dbc;\n"
"}\n"
"\n"
"QTreeView::item:selected:active{\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6ea1f1, stop: 1 #567dbc);\n"
"}\n"
"\n"
"QTreeView::item:selected:!active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6b9be8, stop: 1 #577fbf);\n"
"}\n"
"\n"
"\n"
"QTreeView::branch:has-siblings:!adjoins-item {\n"
"    border-image:url(:/icons/icons/vline.png) 0;\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:adjoins-item {\n"
"    border-image: url(:/icons/icons/branch-more.png)  0;\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
"    border-image: url(:/icons/icons/branch-end.png) 0;\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"        border-image: none;\n"
"        image:url(:/icons/icons/branch-closed.png);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  {\n"
"        border-image: none;\n"
"        image: url(:/icons/icons/branch-open.png);\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox{\n"
"    \n"
"    font-size:25px;\n"
"}\n"
"\n"
"QGroupBox{\n"
"    font-size: 14px;\n"
"    font-family: Arial, Helvetica, sans-serif;\n"
"    font-weight: bold;\n"
"    color: rgb(95, 95, 95);\n"
"    border: 1px solid gray;\n"
"      padding:  1em 1em;\n"
"      border-radius: 16px;\n"
" }\n"
"\n"
"QTextEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QPlainTextEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QToolButton {\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"QToolButton:hover{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(197, 197, 197), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(197, 197, 197));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"QToolButton:pressed{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border-width: 4px; \n"
"    border-radius: 8px;\n"
"    border-style: solid;\n"
"    border-color: rgb(150,150,150);\n"
"    font-size: 25px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border-width: 4px; \n"
"    border-radius: 8px;\n"
"    border-style: solid;\n"
"    border-color: rgb(244, 154, 32);\n"
"    font-size: 25px;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character: 9679;\n"
"}\n"
"\n"
"QLabel {\n"
"    color:rgb(150,150,150);\n"
"    font-size: 25px;\n"
"\n"
"}\n"
"QSpinBox {\n"
"    padding-right: 10px; /* make room for the arrows */\n"
"    border-width: 6;\n"
"}\n"
"QSpinBox::up-arrow {\n"
"    width: 7px;\n"
"    height: 7px;\n"
"}\n"
"\n"
"QToolTip {\n"
"    font: 12pt \"Times New Roman\";\n"
"    border: 2px solid rgb(174,174,174);\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    \n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QRadioButton {\n"
"    color: 000000;\n"
"    padding: 1px;\n"
"    font-size:25px;\n"
"\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"      width:25px;\n"
"    height: 25px;\n"
"\n"
"    border-style:solid;\n"
"    border-radius:14px;\n"
"    border-width: 2px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"    color: #a9b7c6;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"      width:25px;\n"
"    height: 25px;\n"
"\n"
"    border-style:solid;\n"
"    border-radius:14px;\n"
"    border-width: 2px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"    color: #a9b7c6;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"    font-size: 25px;\n"
"\n"
"    border-style: solid;\n"
"    border-width: 0px;\n"
"    border-radius: 5px;\n"
"    padding: 3px;\n"
"    color: rgb(255,255,255);\n"
"    \n"
"    background-color: rgb(244, 154, 32);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-style:  solid;\n"
"    border-width: 0px;\n"
"    border-radius: 5px;\n"
"    padding: 3px;\n"
"\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(150,150,150);\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style:  solid;\n"
"    \n"
"    border-width: 0px;\n"
"    border-radius: 5px;\n"
"    padding: 3px;\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(174,174,174);\n"
"}\n"
"\n"
"\n"
"QLCDNumber {\n"
"    color: rgb(0, 113, 255, 255);\n"
"}\n"
"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(240, 240, 240);\n"
"    border-width: 1px; \n"
"    border-radius: 10px;\n"
"    border-color: rgb(230, 230, 230);\n"
"    border-style: solid;\n"
"    background-color:rgb(207,207,207);\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"    border-radius: 10px;\n"
"}\n"
"QMenuBar {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(207, 209, 207, 255), stop:1 rgba(230, 229, 230, 255));\n"
"}\n"
"QMenuBar::item {\n"
"    color: #000000;\n"
"      spacing: 3px;\n"
"      padding: 1px 4px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(207, 209, 207, 255), stop:1 rgba(230, 229, 230, 255));\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"      background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"    color: #FFFFFF;\n"
"}\n"
"QMenu::item:selected {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"    border-bottom-color: transparent;\n"
"    border-left-width: 2px;\n"
"    color: #000000;\n"
"    padding-left:15px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"}\n"
"QMenu::item {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-bottom-width: 1px;\n"
"    color: #000000;\n"
"    padding-left:17px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"}\n"
"QTabWidget {\n"
"    color:rgb(0,0,0);\n"
"    \n"
"    background-color: rgb(224, 224, 224);\n"
"    \n"
"    \n"
"}\n"
"QTabWidget::pane {\n"
"        border-color: rgb(223,223,223);\n"
"        background-color:rgb(226,226,226);\n"
"        border-style: solid;\n"
"        border-width: 2px;\n"
"        border-radius: 6px;\n"
"}\n"
"QTabBar::tab:first {\n"
"    border-style: solid;\n"
"    border-left-width:1px;\n"
"    border-right-width:0px;\n"
"    border-top-width:1px;\n"
"    border-bottom-width:1px;\n"
"    border-top-color: rgb(209,209,209);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-bottom-color: rgb(229,229,229);\n"
"    border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    color: #000000;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab:last {\n"
"    border-style: solid;\n"
"    border-width:1px;\n"
"    border-top-color: rgb(209,209,209);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-bottom-color: rgb(229,229,229);\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    color: #000000;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab {\n"
"    border-style: solid;\n"
"    border-top-width:1px;\n"
"    border-bottom-width:1px;\n"
"    border-left-width:1px;\n"
"    border-top-color: rgb(209,209,209);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-bottom-color: rgb(229,229,229);\n"
"    color: #000000;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"      border-style: solid;\n"
"      border-left-width:1px;\n"
"    border-right-color: transparent;\n"
"    border-top-color: rgb(209,209,209);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-bottom-color: rgb(229,229,229);\n"
"    color: #FFFFFF;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:first:selected, QTabBar::tab:hover {\n"
"      border-style: solid;\n"
"      border-left-width:1px;\n"
"      border-bottom-width:1px;\n"
"      border-top-width:1px;\n"
"    border-right-color: transparent;\n"
"    border-top-color: rgb(209,209,209);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-bottom-color: rgb(229,229,229);\n"
"    color: #FFFFFF;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"\n"
"\n"
"QStatusBar {\n"
"    color:#027f7f;\n"
"}\n"
"QSpinBox {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDoubleSpinBox {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QTimeEdit {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDateTimeEdit {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDateEdit {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"\n"
"QToolBox {\n"
"    color: #a9b7c6;\n"
"    background-color:#000000;\n"
"}\n"
"QToolBox::tab {\n"
"    color: #a9b7c6;\n"
"    background-color:#000000;\n"
"}\n"
"QToolBox::tab:selected {\n"
"    color: #FFFFFF;\n"
"    background-color:#000000;\n"
"}\n"
"QScrollArea {\n"
"    color: #FFFFFF;\n"
"    background-color:#000000;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    width: 12px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    height: 12px;\n"
"    margin: 0 -5px;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: rgb(181,181,181);\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: rgb(181,181,181);\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"    background-color: qlineargradient(spread:pad, y1:0.5, x1:1, y2:0.5, x2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QScrollBar:horizontal {\n"
"    max-height: 20px;\n"
"    border: 1px transparent grey;\n"
"    margin: 0px 20px 0px 20px;\n"
"}\n"
"QScrollBar:vertical {\n"
"    max-width: 20px;\n"
"    border: 1px transparent grey;\n"
"    margin: 20px 0px 20px 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    border-radius: 7px;\n"
"    min-width: 25px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(147, 200, 200);\n"
"    border-radius: 7px;\n"
"    min-width: 25px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    border-radius: 7px;\n"
"    min-height: 25px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(147, 200, 200);\n"
"    border-radius: 7px;\n"
"    min-height: 25px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"   border: 2px transparent grey;\n"
"   border-top-right-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   width: 20px;\n"
"   subcontrol-position: right;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-right-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   width: 20px;\n"
"   subcontrol-position: right;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"   border: 2px transparent grey;\n"
"   border-bottom-left-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-bottom-left-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-bottom-left-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   width: 20px;\n"
"   subcontrol-position: left;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-bottom-left-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   width: 20px;\n"
"   subcontrol-position: left;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-top-right-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   height: 20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-top-right-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   height: 20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::left-arrow:horizontal {\n"
"   border: 1px transparent grey;\n"
"   border-top-left-radius: 3px;\n"
"   border-bottom-left-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::right-arrow:horizontal {\n"
"   border: 1px transparent grey;\n"
"   border-top-right-radius: 3px;\n"
"   border-bottom-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::up-arrow:vertical {\n"
"   border: 1px transparent grey;\n"
"   border-top-left-radius: 3px;\n"
"   border-top-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::down-arrow:vertical {\n"
"   border: 1px transparent grey;\n"
"   border-bottom-left-radius: 3px;\n"
"   border-bottom-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"   background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"   background: none;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.social_media_stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.social_media_stackedWidget.setObjectName("social_media_stackedWidget")
        self.facebook_frame = QtWidgets.QWidget()
        self.facebook_frame.setObjectName("facebook_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.facebook_frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.facebook_frame)
        self.stackedWidget.setMinimumSize(QtCore.QSize(100, 0))
        self.stackedWidget.setObjectName("stackedWidget")
        self.comments_frame = QtWidgets.QWidget()
        self.comments_frame.setObjectName("comments_frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.comments_frame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_15 = QtWidgets.QLabel(self.comments_frame)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_6.addWidget(self.label_15)
        self.post_url_txt1 = QtWidgets.QLineEdit(self.comments_frame)
        self.post_url_txt1.setMinimumSize(QtCore.QSize(500, 50))
        self.post_url_txt1.setObjectName("post_url_txt1")
        self.verticalLayout_6.addWidget(self.post_url_txt1)
        self.frame_25 = QtWidgets.QFrame(self.comments_frame)
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.frame_25)
        self.horizontalLayout_21.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_21.setSpacing(7)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_2 = QtWidgets.QLabel(self.frame_25)
        self.label_2.setMinimumSize(QtCore.QSize(200, 50))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_21.addWidget(self.label_2)
        self.accounts_file_txt1 = QtWidgets.QLineEdit(self.frame_25)
        self.accounts_file_txt1.setMinimumSize(QtCore.QSize(300, 50))
        self.accounts_file_txt1.setDragEnabled(True)
        self.accounts_file_txt1.setReadOnly(True)
        self.accounts_file_txt1.setObjectName("accounts_file_txt1")
        self.horizontalLayout_21.addWidget(self.accounts_file_txt1)
        self.load_accounts_file_btn1 = QtWidgets.QPushButton(self.frame_25)
        self.load_accounts_file_btn1.setMinimumSize(QtCore.QSize(70, 50))
        self.load_accounts_file_btn1.setObjectName("load_accounts_file_btn1")
        self.horizontalLayout_21.addWidget(self.load_accounts_file_btn1)
        self.verticalLayout_6.addWidget(self.frame_25)
        self.frame_27 = QtWidgets.QFrame(self.comments_frame)
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.frame_27)
        self.horizontalLayout_24.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_24.setSpacing(7)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_23 = QtWidgets.QLabel(self.frame_27)
        self.label_23.setMinimumSize(QtCore.QSize(200, 50))
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_24.addWidget(self.label_23)
        self.comments_file_txt1 = QtWidgets.QLineEdit(self.frame_27)
        self.comments_file_txt1.setMinimumSize(QtCore.QSize(300, 50))
        self.comments_file_txt1.setReadOnly(True)
        self.comments_file_txt1.setObjectName("comments_file_txt1")
        self.horizontalLayout_24.addWidget(self.comments_file_txt1)
        self.load_commetns_file_btn1 = QtWidgets.QPushButton(self.frame_27)
        self.load_commetns_file_btn1.setMinimumSize(QtCore.QSize(70, 50))
        self.load_commetns_file_btn1.setObjectName("load_commetns_file_btn1")
        self.horizontalLayout_24.addWidget(self.load_commetns_file_btn1)
        self.verticalLayout_6.addWidget(self.frame_27)
        self.frame_7 = QtWidgets.QFrame(self.comments_frame)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setContentsMargins(0, 11, 0, 11)
        self.horizontalLayout_6.setSpacing(7)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.frame_7)
        self.label_4.setMinimumSize(QtCore.QSize(200, 50))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.start_acc_range_txt1 = QtWidgets.QLineEdit(self.frame_7)
        self.start_acc_range_txt1.setMinimumSize(QtCore.QSize(90, 50))
        self.start_acc_range_txt1.setMaximumSize(QtCore.QSize(90, 16777215))
        self.start_acc_range_txt1.setObjectName("start_acc_range_txt1")
        self.horizontalLayout_6.addWidget(self.start_acc_range_txt1)
        self.label_3 = QtWidgets.QLabel(self.frame_7)
        self.label_3.setMinimumSize(QtCore.QSize(80, 50))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.end_acc_range_txt1 = QtWidgets.QLineEdit(self.frame_7)
        self.end_acc_range_txt1.setMinimumSize(QtCore.QSize(90, 50))
        self.end_acc_range_txt1.setMaximumSize(QtCore.QSize(90, 16777215))
        self.end_acc_range_txt1.setObjectName("end_acc_range_txt1")
        self.horizontalLayout_6.addWidget(self.end_acc_range_txt1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_6.addWidget(self.frame_7)
        self.frame_12 = QtWidgets.QFrame(self.comments_frame)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_10.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.run_error_lbl1 = QtWidgets.QLabel(self.frame_12)
        self.run_error_lbl1.setMinimumSize(QtCore.QSize(0, 50))
        self.run_error_lbl1.setText("")
        self.run_error_lbl1.setObjectName("run_error_lbl1")
        self.horizontalLayout_10.addWidget(self.run_error_lbl1)
        self.verticalLayout_6.addWidget(self.frame_12)
        self.frame_14 = QtWidgets.QFrame(self.comments_frame)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_17.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_17.setSpacing(7)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_20 = QtWidgets.QLabel(self.frame_14)
        self.label_20.setMinimumSize(QtCore.QSize(200, 50))
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_17.addWidget(self.label_20)
        self.num_of_workers_txt1 = QtWidgets.QLineEdit(self.frame_14)
        self.num_of_workers_txt1.setMinimumSize(QtCore.QSize(90, 50))
        self.num_of_workers_txt1.setMaximumSize(QtCore.QSize(90, 16777215))
        self.num_of_workers_txt1.setObjectName("num_of_workers_txt1")
        self.horizontalLayout_17.addWidget(self.num_of_workers_txt1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem1)
        self.verticalLayout_6.addWidget(self.frame_14)
        self.frame_10 = QtWidgets.QFrame(self.comments_frame)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setContentsMargins(0, 11, 0, 11)
        self.horizontalLayout_8.setSpacing(7)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.frame_10)
        self.label_5.setMinimumSize(QtCore.QSize(200, 50))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.comments_type_comboBox1 = QtWidgets.QComboBox(self.frame_10)
        self.comments_type_comboBox1.setMinimumSize(QtCore.QSize(250, 50))
        self.comments_type_comboBox1.setMaximumSize(QtCore.QSize(250, 16777215))
        self.comments_type_comboBox1.setObjectName("comments_type_comboBox1")
        self.horizontalLayout_8.addWidget(self.comments_type_comboBox1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.verticalLayout_6.addWidget(self.frame_10)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.frame_2 = QtWidgets.QFrame(self.comments_frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(364, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.run_btn1 = QtWidgets.QPushButton(self.frame_2)
        self.run_btn1.setMinimumSize(QtCore.QSize(200, 40))
        self.run_btn1.setObjectName("run_btn1")
        self.horizontalLayout_2.addWidget(self.run_btn1)
        self.verticalLayout_6.addWidget(self.frame_2)
        self.stackedWidget.addWidget(self.comments_frame)
        self.likes_frame = QtWidgets.QWidget()
        self.likes_frame.setObjectName("likes_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.likes_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_16 = QtWidgets.QLabel(self.likes_frame)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_3.addWidget(self.label_16)
        self.post_url_txt2 = QtWidgets.QLineEdit(self.likes_frame)
        self.post_url_txt2.setMinimumSize(QtCore.QSize(500, 50))
        self.post_url_txt2.setObjectName("post_url_txt2")
        self.verticalLayout_3.addWidget(self.post_url_txt2)
        self.frame_24 = QtWidgets.QFrame(self.likes_frame)
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.frame_24)
        self.horizontalLayout_20.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label = QtWidgets.QLabel(self.frame_24)
        self.label.setMinimumSize(QtCore.QSize(200, 50))
        self.label.setObjectName("label")
        self.horizontalLayout_20.addWidget(self.label)
        self.accounts_file_txt2 = QtWidgets.QLineEdit(self.frame_24)
        self.accounts_file_txt2.setMinimumSize(QtCore.QSize(300, 50))
        self.accounts_file_txt2.setReadOnly(True)
        self.accounts_file_txt2.setObjectName("accounts_file_txt2")
        self.horizontalLayout_20.addWidget(self.accounts_file_txt2)
        self.load_accounts_file_btn2 = QtWidgets.QPushButton(self.frame_24)
        self.load_accounts_file_btn2.setMinimumSize(QtCore.QSize(70, 50))
        self.load_accounts_file_btn2.setObjectName("load_accounts_file_btn2")
        self.horizontalLayout_20.addWidget(self.load_accounts_file_btn2)
        self.verticalLayout_3.addWidget(self.frame_24)
        self.frame_17 = QtWidgets.QFrame(self.likes_frame)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_13.setContentsMargins(0, 11, 0, 11)
        self.horizontalLayout_13.setSpacing(7)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_9 = QtWidgets.QLabel(self.frame_17)
        self.label_9.setMinimumSize(QtCore.QSize(200, 50))
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_13.addWidget(self.label_9)
        self.start_acc_range_txt2 = QtWidgets.QLineEdit(self.frame_17)
        self.start_acc_range_txt2.setMinimumSize(QtCore.QSize(90, 50))
        self.start_acc_range_txt2.setMaximumSize(QtCore.QSize(90, 16777215))
        self.start_acc_range_txt2.setObjectName("start_acc_range_txt2")
        self.horizontalLayout_13.addWidget(self.start_acc_range_txt2)
        self.label_11 = QtWidgets.QLabel(self.frame_17)
        self.label_11.setMinimumSize(QtCore.QSize(80, 50))
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_13.addWidget(self.label_11)
        self.end_acc_range_txt2 = QtWidgets.QLineEdit(self.frame_17)
        self.end_acc_range_txt2.setMinimumSize(QtCore.QSize(90, 50))
        self.end_acc_range_txt2.setMaximumSize(QtCore.QSize(90, 16777215))
        self.end_acc_range_txt2.setObjectName("end_acc_range_txt2")
        self.horizontalLayout_13.addWidget(self.end_acc_range_txt2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem5)
        self.verticalLayout_3.addWidget(self.frame_17)
        self.frame_16 = QtWidgets.QFrame(self.likes_frame)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_14.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.run_error_lbl2 = QtWidgets.QLabel(self.frame_16)
        self.run_error_lbl2.setMinimumSize(QtCore.QSize(0, 50))
        self.run_error_lbl2.setText("")
        self.run_error_lbl2.setObjectName("run_error_lbl2")
        self.horizontalLayout_14.addWidget(self.run_error_lbl2)
        self.verticalLayout_3.addWidget(self.frame_16)
        self.frame_5 = QtWidgets.QFrame(self.likes_frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_19 = QtWidgets.QLabel(self.frame_5)
        self.label_19.setMinimumSize(QtCore.QSize(200, 50))
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_5.addWidget(self.label_19)
        self.num_of_workers_txt2 = QtWidgets.QLineEdit(self.frame_5)
        self.num_of_workers_txt2.setMinimumSize(QtCore.QSize(90, 50))
        self.num_of_workers_txt2.setMaximumSize(QtCore.QSize(90, 16777215))
        self.num_of_workers_txt2.setObjectName("num_of_workers_txt2")
        self.horizontalLayout_5.addWidget(self.num_of_workers_txt2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.verticalLayout_3.addWidget(self.frame_5)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.frame_15 = QtWidgets.QFrame(self.likes_frame)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem8 = QtWidgets.QSpacerItem(364, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem8)
        self.run_btn2 = QtWidgets.QPushButton(self.frame_15)
        self.run_btn2.setMinimumSize(QtCore.QSize(200, 40))
        self.run_btn2.setObjectName("run_btn2")
        self.horizontalLayout_12.addWidget(self.run_btn2)
        self.verticalLayout_3.addWidget(self.frame_15)
        self.stackedWidget.addWidget(self.likes_frame)
        self.comments_likes_frame = QtWidgets.QWidget()
        self.comments_likes_frame.setObjectName("comments_likes_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.comments_likes_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_17 = QtWidgets.QLabel(self.comments_likes_frame)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_4.addWidget(self.label_17)
        self.post_url_txt3 = QtWidgets.QLineEdit(self.comments_likes_frame)
        self.post_url_txt3.setMinimumSize(QtCore.QSize(500, 50))
        self.post_url_txt3.setObjectName("post_url_txt3")
        self.verticalLayout_4.addWidget(self.post_url_txt3)
        self.frame_29 = QtWidgets.QFrame(self.comments_likes_frame)
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.frame_29)
        self.horizontalLayout_26.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_25 = QtWidgets.QLabel(self.frame_29)
        self.label_25.setMinimumSize(QtCore.QSize(200, 50))
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_26.addWidget(self.label_25)
        self.accounts_file_txt3 = QtWidgets.QLineEdit(self.frame_29)
        self.accounts_file_txt3.setMinimumSize(QtCore.QSize(300, 50))
        self.accounts_file_txt3.setReadOnly(True)
        self.accounts_file_txt3.setObjectName("accounts_file_txt3")
        self.horizontalLayout_26.addWidget(self.accounts_file_txt3)
        self.load_accounts_file_btn3 = QtWidgets.QPushButton(self.frame_29)
        self.load_accounts_file_btn3.setMinimumSize(QtCore.QSize(70, 50))
        self.load_accounts_file_btn3.setObjectName("load_accounts_file_btn3")
        self.horizontalLayout_26.addWidget(self.load_accounts_file_btn3)
        self.verticalLayout_4.addWidget(self.frame_29)
        self.frame_28 = QtWidgets.QFrame(self.comments_likes_frame)
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.frame_28)
        self.horizontalLayout_25.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_24 = QtWidgets.QLabel(self.frame_28)
        self.label_24.setMinimumSize(QtCore.QSize(200, 50))
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_25.addWidget(self.label_24)
        self.comments_file_txt3 = QtWidgets.QLineEdit(self.frame_28)
        self.comments_file_txt3.setMinimumSize(QtCore.QSize(300, 50))
        self.comments_file_txt3.setReadOnly(True)
        self.comments_file_txt3.setObjectName("comments_file_txt3")
        self.horizontalLayout_25.addWidget(self.comments_file_txt3)
        self.load_commetns_file_btn3 = QtWidgets.QPushButton(self.frame_28)
        self.load_commetns_file_btn3.setMinimumSize(QtCore.QSize(70, 50))
        self.load_commetns_file_btn3.setObjectName("load_commetns_file_btn3")
        self.horizontalLayout_25.addWidget(self.load_commetns_file_btn3)
        self.verticalLayout_4.addWidget(self.frame_28)
        self.frame_11 = QtWidgets.QFrame(self.comments_likes_frame)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_6 = QtWidgets.QLabel(self.frame_11)
        self.label_6.setMinimumSize(QtCore.QSize(200, 50))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_9.addWidget(self.label_6)
        self.start_acc_range_txt3 = QtWidgets.QLineEdit(self.frame_11)
        self.start_acc_range_txt3.setMinimumSize(QtCore.QSize(90, 50))
        self.start_acc_range_txt3.setMaximumSize(QtCore.QSize(90, 16777215))
        self.start_acc_range_txt3.setObjectName("start_acc_range_txt3")
        self.horizontalLayout_9.addWidget(self.start_acc_range_txt3)
        self.label_7 = QtWidgets.QLabel(self.frame_11)
        self.label_7.setMinimumSize(QtCore.QSize(80, 50))
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.end_acc_range_txt3 = QtWidgets.QLineEdit(self.frame_11)
        self.end_acc_range_txt3.setMinimumSize(QtCore.QSize(90, 50))
        self.end_acc_range_txt3.setMaximumSize(QtCore.QSize(90, 16777215))
        self.end_acc_range_txt3.setObjectName("end_acc_range_txt3")
        self.horizontalLayout_9.addWidget(self.end_acc_range_txt3)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem9)
        self.verticalLayout_4.addWidget(self.frame_11)
        self.frame_18 = QtWidgets.QFrame(self.comments_likes_frame)
        self.frame_18.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_16.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.run_error_lbl3 = QtWidgets.QLabel(self.frame_18)
        self.run_error_lbl3.setText("")
        self.run_error_lbl3.setObjectName("run_error_lbl3")
        self.horizontalLayout_16.addWidget(self.run_error_lbl3)
        self.verticalLayout_4.addWidget(self.frame_18)
        self.frame_22 = QtWidgets.QFrame(self.comments_likes_frame)
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_22)
        self.horizontalLayout_18.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_21 = QtWidgets.QLabel(self.frame_22)
        self.label_21.setMinimumSize(QtCore.QSize(200, 50))
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_18.addWidget(self.label_21)
        self.num_of_workers_txt3 = QtWidgets.QLineEdit(self.frame_22)
        self.num_of_workers_txt3.setMinimumSize(QtCore.QSize(90, 50))
        self.num_of_workers_txt3.setMaximumSize(QtCore.QSize(90, 16777215))
        self.num_of_workers_txt3.setObjectName("num_of_workers_txt3")
        self.horizontalLayout_18.addWidget(self.num_of_workers_txt3)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem10)
        self.verticalLayout_4.addWidget(self.frame_22)
        self.frame_13 = QtWidgets.QFrame(self.comments_likes_frame)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_8 = QtWidgets.QLabel(self.frame_13)
        self.label_8.setMinimumSize(QtCore.QSize(200, 50))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_11.addWidget(self.label_8)
        self.comments_type_comboBox2 = QtWidgets.QComboBox(self.frame_13)
        self.comments_type_comboBox2.setMinimumSize(QtCore.QSize(250, 50))
        self.comments_type_comboBox2.setObjectName("comments_type_comboBox2")
        self.horizontalLayout_11.addWidget(self.comments_type_comboBox2)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem11)
        self.verticalLayout_4.addWidget(self.frame_13)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem12)
        self.frame_4 = QtWidgets.QFrame(self.comments_likes_frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem13 = QtWidgets.QSpacerItem(364, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem13)
        self.run_btn3 = QtWidgets.QPushButton(self.frame_4)
        self.run_btn3.setMinimumSize(QtCore.QSize(200, 40))
        self.run_btn3.setObjectName("run_btn3")
        self.horizontalLayout_4.addWidget(self.run_btn3)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.stackedWidget.addWidget(self.comments_likes_frame)
        self.page_following_frame = QtWidgets.QWidget()
        self.page_following_frame.setObjectName("page_following_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_following_frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_18 = QtWidgets.QLabel(self.page_following_frame)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_5.addWidget(self.label_18)
        self.page_url_txt4 = QtWidgets.QLineEdit(self.page_following_frame)
        self.page_url_txt4.setMinimumSize(QtCore.QSize(500, 50))
        self.page_url_txt4.setObjectName("page_url_txt4")
        self.verticalLayout_5.addWidget(self.page_url_txt4)
        self.frame_26 = QtWidgets.QFrame(self.page_following_frame)
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.frame_26)
        self.horizontalLayout_22.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_10 = QtWidgets.QLabel(self.frame_26)
        self.label_10.setMinimumSize(QtCore.QSize(200, 50))
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_22.addWidget(self.label_10)
        self.accounts_file_txt4 = QtWidgets.QLineEdit(self.frame_26)
        self.accounts_file_txt4.setMinimumSize(QtCore.QSize(300, 50))
        self.accounts_file_txt4.setReadOnly(True)
        self.accounts_file_txt4.setObjectName("accounts_file_txt4")
        self.horizontalLayout_22.addWidget(self.accounts_file_txt4)
        self.load_accounts_file_btn4 = QtWidgets.QPushButton(self.frame_26)
        self.load_accounts_file_btn4.setMinimumSize(QtCore.QSize(70, 50))
        self.load_accounts_file_btn4.setObjectName("load_accounts_file_btn4")
        self.horizontalLayout_22.addWidget(self.load_accounts_file_btn4)
        self.verticalLayout_5.addWidget(self.frame_26)
        self.frame_20 = QtWidgets.QFrame(self.page_following_frame)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_15.setContentsMargins(0, 11, 0, 11)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_12 = QtWidgets.QLabel(self.frame_20)
        self.label_12.setMinimumSize(QtCore.QSize(200, 50))
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_15.addWidget(self.label_12)
        self.start_acc_range_txt4 = QtWidgets.QLineEdit(self.frame_20)
        self.start_acc_range_txt4.setMinimumSize(QtCore.QSize(90, 50))
        self.start_acc_range_txt4.setMaximumSize(QtCore.QSize(90, 16777215))
        self.start_acc_range_txt4.setObjectName("start_acc_range_txt4")
        self.horizontalLayout_15.addWidget(self.start_acc_range_txt4)
        self.label_14 = QtWidgets.QLabel(self.frame_20)
        self.label_14.setMinimumSize(QtCore.QSize(80, 50))
        self.label_14.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_15.addWidget(self.label_14)
        self.end_acc_range_txt4 = QtWidgets.QLineEdit(self.frame_20)
        self.end_acc_range_txt4.setMinimumSize(QtCore.QSize(90, 50))
        self.end_acc_range_txt4.setMaximumSize(QtCore.QSize(90, 16777215))
        self.end_acc_range_txt4.setObjectName("end_acc_range_txt4")
        self.horizontalLayout_15.addWidget(self.end_acc_range_txt4)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem14)
        self.verticalLayout_5.addWidget(self.frame_20)
        self.frame_19 = QtWidgets.QFrame(self.page_following_frame)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout_23.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.run_error_lbl4 = QtWidgets.QLabel(self.frame_19)
        self.run_error_lbl4.setMinimumSize(QtCore.QSize(0, 50))
        self.run_error_lbl4.setText("")
        self.run_error_lbl4.setObjectName("run_error_lbl4")
        self.horizontalLayout_23.addWidget(self.run_error_lbl4)
        self.verticalLayout_5.addWidget(self.frame_19)
        self.frame_23 = QtWidgets.QFrame(self.page_following_frame)
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_23)
        self.horizontalLayout_19.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_22 = QtWidgets.QLabel(self.frame_23)
        self.label_22.setMinimumSize(QtCore.QSize(200, 50))
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_19.addWidget(self.label_22)
        self.num_of_workers_txt4 = QtWidgets.QLineEdit(self.frame_23)
        self.num_of_workers_txt4.setMinimumSize(QtCore.QSize(90, 50))
        self.num_of_workers_txt4.setMaximumSize(QtCore.QSize(90, 16777215))
        self.num_of_workers_txt4.setObjectName("num_of_workers_txt4")
        self.horizontalLayout_19.addWidget(self.num_of_workers_txt4)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem15)
        self.verticalLayout_5.addWidget(self.frame_23)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem16)
        self.frame_3 = QtWidgets.QFrame(self.page_following_frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem17 = QtWidgets.QSpacerItem(364, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem17)
        self.run_btn4 = QtWidgets.QPushButton(self.frame_3)
        self.run_btn4.setMinimumSize(QtCore.QSize(200, 40))
        self.run_btn4.setObjectName("run_btn4")
        self.horizontalLayout_3.addWidget(self.run_btn4)
        self.verticalLayout_5.addWidget(self.frame_3)
        self.stackedWidget.addWidget(self.page_following_frame)
        self.accounts_groups_frame = QtWidgets.QWidget()
        self.accounts_groups_frame.setObjectName("accounts_groups_frame")
        self.stackedWidget.addWidget(self.accounts_groups_frame)
        self.gridLayout_2.addWidget(self.stackedWidget, 0, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.facebook_frame)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comments_btn = QtWidgets.QPushButton(self.frame)
        self.comments_btn.setMinimumSize(QtCore.QSize(200, 50))
        self.comments_btn.setObjectName("comments_btn")
        self.verticalLayout.addWidget(self.comments_btn)
        self.Likes_btn = QtWidgets.QPushButton(self.frame)
        self.Likes_btn.setMinimumSize(QtCore.QSize(200, 50))
        self.Likes_btn.setObjectName("Likes_btn")
        self.verticalLayout.addWidget(self.Likes_btn)
        self.comm_likes_btn = QtWidgets.QPushButton(self.frame)
        self.comm_likes_btn.setMinimumSize(QtCore.QSize(200, 50))
        self.comm_likes_btn.setObjectName("comm_likes_btn")
        self.verticalLayout.addWidget(self.comm_likes_btn)
        self.page_following_btn = QtWidgets.QPushButton(self.frame)
        self.page_following_btn.setMinimumSize(QtCore.QSize(200, 50))
        self.page_following_btn.setObjectName("page_following_btn")
        self.verticalLayout.addWidget(self.page_following_btn)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem18)
        self.return_btn1 = QtWidgets.QPushButton(self.frame)
        self.return_btn1.setMinimumSize(QtCore.QSize(200, 30))
        self.return_btn1.setMaximumSize(QtCore.QSize(150, 16777215))
        self.return_btn1.setStyleSheet("")
        self.return_btn1.setObjectName("return_btn1")
        self.verticalLayout.addWidget(self.return_btn1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.social_media_stackedWidget.addWidget(self.facebook_frame)
        self.Instagram_frame = QtWidgets.QWidget()
        self.Instagram_frame.setObjectName("Instagram_frame")
        self.social_media_stackedWidget.addWidget(self.Instagram_frame)
        self.Main_frame = QtWidgets.QWidget()
        self.Main_frame.setObjectName("Main_frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Main_frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_8 = QtWidgets.QFrame(self.Main_frame)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.frame_8)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem19)
        self.instagram_btn = QtWidgets.QPushButton(self.frame_6)
        self.instagram_btn.setMinimumSize(QtCore.QSize(200, 100))
        self.instagram_btn.setObjectName("instagram_btn")
        self.horizontalLayout.addWidget(self.instagram_btn)
        self.facebook_btn = QtWidgets.QPushButton(self.frame_6)
        self.facebook_btn.setMinimumSize(QtCore.QSize(200, 100))
        self.facebook_btn.setObjectName("facebook_btn")
        self.horizontalLayout.addWidget(self.facebook_btn)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem20)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setSpacing(30)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem21)
        self.label_13 = QtWidgets.QLabel(self.frame_9)
        self.label_13.setMinimumSize(QtCore.QSize(200, 50))
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_7.addWidget(self.label_13)
        self.driver_type_comboBox = QtWidgets.QComboBox(self.frame_9)
        self.driver_type_comboBox.setMinimumSize(QtCore.QSize(200, 50))
        self.driver_type_comboBox.setObjectName("driver_type_comboBox")
        self.driver_type_comboBox.addItem("")
        self.driver_type_comboBox.addItem("")
        self.horizontalLayout_7.addWidget(self.driver_type_comboBox)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem22)
        self.verticalLayout_2.addWidget(self.frame_9)
        self.gridLayout_3.addWidget(self.frame_8, 1, 0, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem23, 2, 0, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem24, 0, 0, 1, 1)
        self.social_media_stackedWidget.addWidget(self.Main_frame)
        self.gridLayout.addWidget(self.social_media_stackedWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.social_media_stackedWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_15.setText(_translate("MainWindow", "ADD COMMENTS"))
        self.post_url_txt1.setPlaceholderText(_translate("MainWindow", "Enter post url"))
        self.label_2.setText(_translate("MainWindow", "Accounts file"))
        self.load_accounts_file_btn1.setText(_translate("MainWindow", "load"))
        self.label_23.setText(_translate("MainWindow", "comments file"))
        self.load_commetns_file_btn1.setText(_translate("MainWindow", "load"))
        self.label_4.setText(_translate("MainWindow", "Accounts range"))
        self.start_acc_range_txt1.setPlaceholderText(_translate("MainWindow", "from"))
        self.label_3.setText(_translate("MainWindow", ">"))
        self.end_acc_range_txt1.setPlaceholderText(_translate("MainWindow", "to"))
        self.label_20.setText(_translate("MainWindow", "# of worker"))
        self.label_5.setText(_translate("MainWindow", "Comments Type"))
        self.run_btn1.setText(_translate("MainWindow", "Run"))
        self.label_16.setText(_translate("MainWindow", "ADD LIKES"))
        self.post_url_txt2.setPlaceholderText(_translate("MainWindow", "Enter post url"))
        self.label.setText(_translate("MainWindow", "Accounts file"))
        self.load_accounts_file_btn2.setText(_translate("MainWindow", "load"))
        self.label_9.setText(_translate("MainWindow", "Accounts range"))
        self.start_acc_range_txt2.setPlaceholderText(_translate("MainWindow", "from"))
        self.label_11.setText(_translate("MainWindow", ">"))
        self.end_acc_range_txt2.setPlaceholderText(_translate("MainWindow", "to"))
        self.label_19.setText(_translate("MainWindow", "# of worker"))
        self.run_btn2.setText(_translate("MainWindow", "Run"))
        self.label_17.setText(_translate("MainWindow", "ADD COMMENTS and LIKES"))
        self.post_url_txt3.setPlaceholderText(_translate("MainWindow", "Enter post url"))
        self.label_25.setText(_translate("MainWindow", "Accounts file"))
        self.load_accounts_file_btn3.setText(_translate("MainWindow", "load"))
        self.label_24.setText(_translate("MainWindow", "Comments file"))
        self.load_commetns_file_btn3.setText(_translate("MainWindow", "load"))
        self.label_6.setText(_translate("MainWindow", "Accounts range"))
        self.start_acc_range_txt3.setPlaceholderText(_translate("MainWindow", "from"))
        self.label_7.setText(_translate("MainWindow", ">"))
        self.end_acc_range_txt3.setPlaceholderText(_translate("MainWindow", "to"))
        self.label_21.setText(_translate("MainWindow", "# of worker"))
        self.label_8.setText(_translate("MainWindow", "Comments Type"))
        self.run_btn3.setText(_translate("MainWindow", "Run"))
        self.label_18.setText(_translate("MainWindow", "ADD PAGE FOLLOWING"))
        self.page_url_txt4.setPlaceholderText(_translate("MainWindow", "Enter page url"))
        self.label_10.setText(_translate("MainWindow", "Accounts file"))
        self.load_accounts_file_btn4.setText(_translate("MainWindow", "load"))
        self.label_12.setText(_translate("MainWindow", "Accounts range"))
        self.start_acc_range_txt4.setPlaceholderText(_translate("MainWindow", "from"))
        self.label_14.setText(_translate("MainWindow", ">"))
        self.end_acc_range_txt4.setPlaceholderText(_translate("MainWindow", "to"))
        self.label_22.setText(_translate("MainWindow", "# of worker"))
        self.run_btn4.setText(_translate("MainWindow", "Run"))
        self.comments_btn.setText(_translate("MainWindow", "comments"))
        self.Likes_btn.setText(_translate("MainWindow", "Likes"))
        self.comm_likes_btn.setText(_translate("MainWindow", "Comments\n"
"and\n"
"Likes"))
        self.page_following_btn.setText(_translate("MainWindow", "page following"))
        self.pushButton.setText(_translate("MainWindow", "Group"))
        self.return_btn1.setText(_translate("MainWindow", "Reutrn"))
        self.instagram_btn.setText(_translate("MainWindow", "Instagram"))
        self.facebook_btn.setText(_translate("MainWindow", "Facebook"))
        self.label_13.setText(_translate("MainWindow", "Select driver type"))
        self.driver_type_comboBox.setItemText(0, _translate("MainWindow", "Chrome"))
        self.driver_type_comboBox.setItemText(1, _translate("MainWindow", "Firefox"))

