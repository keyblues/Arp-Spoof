# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(411, 437)
        icon = QIcon()
        icon.addFile(u"Ui/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 100, 53, 15))
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setLineWidth(1)
        self.label.setTextFormat(Qt.PlainText)
        self.label.setScaledContents(False)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 20, 53, 15))
        self.label_2.setFont(font)
        self.label_2.setLineWidth(1)
        self.label_2.setTextFormat(Qt.PlainText)
        self.label_2.setScaledContents(False)
        self.lineEdit_gateway = QLineEdit(Form)
        self.lineEdit_gateway.setObjectName(u"lineEdit_gateway")
        self.lineEdit_gateway.setGeometry(QRect(80, 50, 231, 31))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei"])
        font1.setPointSize(13)
        font1.setBold(False)
        font1.setKerning(True)
        self.lineEdit_gateway.setFont(font1)
        self.pushButton_help = QPushButton(Form)
        self.pushButton_help.setObjectName(u"pushButton_help")
        self.pushButton_help.setGeometry(QRect(320, 10, 71, 31))
        self.pushButton_gateway = QPushButton(Form)
        self.pushButton_gateway.setObjectName(u"pushButton_gateway")
        self.pushButton_gateway.setGeometry(QRect(320, 50, 71, 31))
        self.lineEdit_targethost = QLineEdit(Form)
        self.lineEdit_targethost.setObjectName(u"lineEdit_targethost")
        self.lineEdit_targethost.setGeometry(QRect(80, 90, 231, 31))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei"])
        font2.setPointSize(13)
        self.lineEdit_targethost.setFont(font2)
        self.pushButton_targethost = QPushButton(Form)
        self.pushButton_targethost.setObjectName(u"pushButton_targethost")
        self.pushButton_targethost.setGeometry(QRect(320, 90, 71, 31))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 60, 53, 15))
        self.label_3.setFont(font)
        self.label_3.setLineWidth(1)
        self.label_3.setTextFormat(Qt.PlainText)
        self.label_3.setScaledContents(False)
        self.textEdit_log = QTextEdit(Form)
        self.textEdit_log.setObjectName(u"textEdit_log")
        self.textEdit_log.setGeometry(QRect(20, 250, 371, 141))
        font3 = QFont()
        font3.setPointSize(9)
        self.textEdit_log.setFont(font3)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 220, 51, 31))
        self.label_4.setFont(font)
        self.label_4.setLineWidth(1)
        self.label_4.setTextFormat(Qt.PlainText)
        self.label_4.setScaledContents(False)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(300, 410, 91, 16))
        self.label_5.setFont(font)
        self.label_5.setLineWidth(1)
        self.label_5.setTextFormat(Qt.PlainText)
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_quantity = QLabel(Form)
        self.label_quantity.setObjectName(u"label_quantity")
        self.label_quantity.setGeometry(QRect(20, 410, 91, 16))
        self.label_quantity.setFont(font)
        self.label_quantity.setLineWidth(1)
        self.label_quantity.setTextFormat(Qt.PlainText)
        self.label_quantity.setScaledContents(False)
        self.label_quantity.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.radioButton_one = QRadioButton(Form)
        self.radioButton_one.setObjectName(u"radioButton_one")
        self.radioButton_one.setGeometry(QRect(80, 140, 95, 19))
        font4 = QFont()
        font4.setFamilies([u"Microsoft YaHei UI Light"])
        font4.setPointSize(10)
        self.radioButton_one.setFont(font4)
        self.radioButton_one.setChecked(True)
        self.radioButton_tow = QRadioButton(Form)
        self.radioButton_tow.setObjectName(u"radioButton_tow")
        self.radioButton_tow.setGeometry(QRect(240, 140, 88, 20))
        self.radioButton_tow.setFont(font4)
        self.pushButton_start = QPushButton(Form)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setEnabled(True)
        self.pushButton_start.setGeometry(QRect(20, 170, 371, 31))
        self.pushButton_start.setFont(font)
        self.pushButton_stop = QPushButton(Form)
        self.pushButton_stop.setObjectName(u"pushButton_stop")
        self.pushButton_stop.setGeometry(QRect(320, 210, 71, 31))
        self.pushButton_stop.setFont(font)
        self.comboBox_localhost = QComboBox(Form)
        self.comboBox_localhost.setObjectName(u"comboBox_localhost")
        self.comboBox_localhost.setGeometry(QRect(80, 10, 231, 31))
        self.comboBox_localhost.setFont(font2)
        self.comboBox_localhost.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Arp-Spoof", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u76ee\u6807\u5730\u5740", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u672c\u5730\u5730\u5740", None))
        self.lineEdit_gateway.setText("")
        self.pushButton_help.setText(QCoreApplication.translate("Form", u"\u5e2e\u52a9", None))
        self.pushButton_gateway.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u83b7\u53d6", None))
        self.lineEdit_targethost.setText("")
        self.pushButton_targethost.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u83b7\u53d6", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u7f51\u5173\u5730\u5740", None))
        self.textEdit_log.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u65e5\u5fd7", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u5df2\u53d1\u9001\u6570\u636e\u5305", None))
        self.label_quantity.setText(QCoreApplication.translate("Form", u"0", None))
        self.radioButton_one.setText(QCoreApplication.translate("Form", u"\u4e3b\u673a\u578b\u6b3a\u9a97", None))
        self.radioButton_tow.setText(QCoreApplication.translate("Form", u"\u7f51\u5173\u578b\u6b3a\u9a97", None))
        self.pushButton_start.setText(QCoreApplication.translate("Form", u"\u542f\u52a8", None))
        self.pushButton_stop.setText(QCoreApplication.translate("Form", u"\u505c\u6b62", None))
    # retranslateUi

