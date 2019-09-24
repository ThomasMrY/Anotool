# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AnoTool.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QListWidget, QStackedWidget
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtCore import QSize, Qt
import os
import json

class Ui_Form(object):
    def setupUi(self, Form):
        self.form = Form
        self.O_answer = {}
        self.A_answer = {}
        self.file_list = os.listdir("Images")
        with open("count") as f:
            self.num = int(f.read())
        self.add_a= True
        self.add_o = False
        self.A_extra = {}
        self.O_extra = {}
        f = open('Attribute', encoding='utf-8-sig')
        self.A_dict = {}
        for line in f.readlines():
            temp = line[:-1].split('：')
            self.A_dict[temp[0]] = temp[1].split('，')
        print(self.A_dict)
        f.close()
        f = open('Object', encoding='utf-8-sig')
        self.O_dict = {}
        for line in f.readlines():
            temp = line[:-1].split('：')
            self.O_dict[temp[0]] = temp[1].split('，')
        f.close()
        print(self.O_dict)
        Form.setObjectName("Form")
        Form.resize(1179, 803)
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(30, 40, 441, 331))
        pixmap = QPixmap("./Images/"+self.file_list[self.num])
        self.label_16.setPixmap(pixmap)
        self.label_16.setScaledContents(True)

        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(610, 720, 111, 31))
        pixmap = QPixmap("logo_iair.png")
        self.label_17.setPixmap(pixmap)
        self.label_17.setScaledContents(True)

        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(400, 720, 201, 31))
        pixmap = QPixmap("xjtu_logo.png")
        self.label_18.setPixmap(pixmap)
        self.label_18.setScaledContents(True)

        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(490, 10, 351, 411))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")

        self.A_comboBox_list = []
        self.A_label_list = []
        with open('QListWidgetQSS.qss', 'r') as f:  # 导入QListWidget的qss样式
            self.list_style = f.read()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.left_widget = QListWidget(self.groupBox)  # 左侧选项列表
        self.left_widget.setGeometry(QtCore.QRect(40, 40, 181, 360))
        self.left_widget.setStyleSheet(self.list_style)
        self.right_widget = QStackedWidget(self.groupBox)
        self.right_widget.setGeometry(QtCore.QRect(190, 40, 181, 360))

        with open('oQListWigetQSS.qss', 'r') as f:  # 导入QListWidget的qss样式
            self.olist_style = f.read()

        self.groupBox_5 = QtWidgets.QGroupBox(Form)
        self.groupBox_5.setGeometry(QtCore.QRect(850, 10, 291, 361))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.oleft_widget = QListWidget(self.groupBox_5)  # 左侧选项列表
        self.oleft_widget.setGeometry(QtCore.QRect(10, 40, 181, 300))
        self.oleft_widget.setStyleSheet(self.olist_style)
        self.oright_widget = QStackedWidget(self.groupBox_5)
        self.oright_widget.setGeometry(QtCore.QRect(150, 40, 181, 300))

        font = QtGui.QFont()
        font.setPointSize(18)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setAutoFillBackground(False)
        self.groupBox_5.setObjectName("groupBox_5")
        self.O_comboBox_list = []
        self.O_label_list = []
        self.pushButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setGeometry(QtCore.QRect(570, 610, 551, 61))
        self.pushButton.clicked.connect(self.btn_save)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setGeometry(QtCore.QRect(570, 530, 551, 61))
        self.pushButton_2.clicked.connect(self.btn_add_class)
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox_11 = QtWidgets.QComboBox(Form)
        self.comboBox_11.setGeometry(QtCore.QRect(40, 440, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.comboBox_11.setFont(font)
        self.comboBox_11.setEditable(False)
        self.comboBox_11.setObjectName("comboBox_11")
        for i,key in enumerate(self.A_dict.keys()):
            self.comboBox_11.addItem("")
        for i,key in enumerate(self.O_dict.keys()):
            self.comboBox_11.addItem("")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(930, 460, 201, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 530, 461, 61))
        self.pushButton_3.clicked.connect(self.btn_add_val)
        self.pushButton_3.setObjectName("pushButton_3")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(580, 470, 100, 20))
        self.radioButton.setChecked(True)
        self.radioButton.toggled.connect(self.radio_msg)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(670, 470, 100, 20))
        self.radioButton_2.toggled.connect(self.radio_msg)
        self.radioButton_2.setObjectName("radioButton_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(300, 440, 201, 81))
        self.textEdit.setObjectName("textEdit")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(40, 410, 60, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(850, 460, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(300, 410, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(30, 380, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(860, 490, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(930, 490, 201, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(580, 490, 87, 20))
        self.checkBox.setObjectName("checkBox")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setGeometry(QtCore.QRect(930, 380, 211, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.btn4_back)
        self.QTextEdit = QtWidgets.QTextEdit(Form)
        self.QTextEdit.setGeometry(QtCore.QRect(40, 610, 461, 91))
        self.QTextEdit.setObjectName("QTextEdit")
        self.label_left = QtWidgets.QLabel(Form)
        self.label_left.setGeometry(QtCore.QRect(800, 700, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_left.setFont(font)
        self.label_left.setObjectName("label_left")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        '''加载界面ui'''

        self.left_widget.currentRowChanged.connect(self.right_widget.setCurrentIndex)  # list和右侧窗口的index对应绑定
        self.oleft_widget.currentRowChanged.connect(self.oright_widget.setCurrentIndex)  # list和右侧窗口的index对应绑定


        # self.left_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 隐藏滚动条
        self.left_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)


        for i,att_cl in enumerate(self.A_dict.keys()):
            self.item = QListWidgetItem(att_cl, self.left_widget)  # 左侧选项的添加
            font = QtGui.QFont()
            font.setPointSize(15)
            self.item.setFont(font)
            self.item.setSizeHint(QSize(15, 25))
            self.item.setTextAlignment(Qt.AlignCenter)  # 居中显示

            locals()['stack' + str(i)] = QListWidget()  # 左侧选项列表
            locals()['stack' + str(i)].setGeometry(QtCore.QRect(0, 0, 181, 360))
            locals()['stack' + str(i)].setStyleSheet(self.list_style)
            for att_v in self.A_dict[att_cl]:
                self.ritem = QListWidgetItem(att_v, locals()['stack' + str(i)])  # 左侧选项的添加
                font = QtGui.QFont()
                font.setPointSize(15)
                self.ritem.setFont(font)
                self.ritem.setSizeHint(QSize(15, 25))
                self.ritem.setTextAlignment(Qt.AlignCenter)  # 居中显示
            self.right_widget.addWidget(locals()['stack' + str(i)])
            self.A_comboBox_list.append(locals()["stack" + str(i)])
            locals()['stack'+str(i)].currentRowChanged.connect(self.row_change)

        for i,obj_cl in enumerate(self.O_dict.keys()):
            self.oitem = QListWidgetItem(obj_cl, self.oleft_widget)  # 左侧选项的添加
            font = QtGui.QFont()
            font.setPointSize(15)
            self.oitem.setFont(font)
            self.oitem.setSizeHint(QSize(15, 25))
            self.oitem.setTextAlignment(Qt.AlignCenter)  # 居中显示

            locals()['ostack' + str(i)] = QListWidget()  # 左侧选项列表
            locals()['ostack' + str(i)].setGeometry(QtCore.QRect(0, 0, 181, 360))
            locals()['ostack' + str(i)].setStyleSheet(self.olist_style)
            for obj_v in self.O_dict[obj_cl]:
                self.oritem = QListWidgetItem(obj_v, locals()['ostack' + str(i)])  # 左侧选项的添加
                font = QtGui.QFont()
                font.setPointSize(15)
                self.oritem.setFont(font)
                self.oritem.setSizeHint(QSize(15, 25))
                self.oritem.setTextAlignment(Qt.AlignCenter)  # 居中显示
            self.oright_widget.addWidget(locals()['ostack' + str(i)])
            self.O_comboBox_list.append(locals()["ostack" + str(i)])
            locals()['ostack' + str(i)].currentRowChanged.connect(self.orow_change)


        _translate = QtCore.QCoreApplication.translate
        for i, key in enumerate(self.A_dict.keys()):
            self.comboBox_11.setItemText(i, _translate("Form", key))
        for i, key in enumerate(self.O_dict.keys()):
            self.comboBox_11.setItemText(i + len(self.A_dict.keys()), _translate("Form", key))
        Form.setWindowTitle(_translate("Form", "Anotation Tool"))
        self.groupBox.setTitle(_translate("Form", "属性"))
        self.groupBox_5.setTitle(_translate("Form", "对象"))
        self.pushButton_3.setText(_translate("Form", "完成添加"))
        self.radioButton.setText(_translate("Form", "属性"))
        self.radioButton_2.setText(_translate("Form", "对象"))
        self.label_11.setText(_translate("Form", "名称："))
        self.label_12.setText(_translate("Form", "名称："))
        self.label_13.setText(_translate("Form", "值:"))
        self.label_9.setText(_translate("Form", "文件名称:"+self.file_list[self.num]))
        self.label_left.setText(_translate("Form", "图片已标注:" + str(len(os.listdir("Labels/"))) + "，还剩:" + str(len(self.file_list)-len(os.listdir("Labels/")))))
        self.pushButton.setText(_translate("Form", "注释图片"))
        self.pushButton_2.setText(_translate("Form", "属性/对象完成添加"))
        self.label_15.setText(_translate("Form", "值:"))
        self.checkBox.setText(_translate("Form", "更新到图表"))
        self.pushButton_4.setText(_translate("Form", "上一张图片"))
    def row_change(self):
        cv = self.left_widget.currentIndex().data()
        i = self.left_widget.currentIndex().row()
        j = self.A_comboBox_list[i].currentIndex().row()
        vv = self.A_comboBox_list[i].currentIndex().data()
        self.A_answer[cv] = vv
        self.QTextEdit.setPlainText(str("对象:\n")+str(self.O_answer)+"\n"+str("属性:\n")+str(self.A_answer)+"\n")
    def orow_change(self):
        cv = self.oleft_widget.currentIndex().data()
        i = self.oleft_widget.currentIndex().row()
        j = self.O_comboBox_list[i].currentIndex().row()
        vv = self.O_comboBox_list[i].currentIndex().data()
        self.O_answer[cv] = vv
        self.QTextEdit.setPlainText(str("对象:\n") + str(self.O_answer) + "\n" + str("属性:\n") + str(self.A_answer) + "\n")
    def btn_save(self):
        self.num += 1
        with open("count","w") as f:
            f.write(str(self.num))
        text = self.QTextEdit.toPlainText()
        O_an = eval(text.split('\n')[1])
        A_an = eval(text.split('\n')[3])
        if os.path.exists("./Labels/" + self.file_list[self.num - 1] + ".json"):
            os.remove("./Labels/" + self.file_list[self.num - 1] + ".json")
        with open("./Labels/" + self.file_list[self.num - 1] + ".json", mode="a") as f:
            json.dump(A_an, f,ensure_ascii=False)
            json.dump(O_an, f,ensure_ascii=False)
        if self.num > len(self.file_list) - 1:
            sys.exit(0)
        pixmap = QPixmap("./Images/"+self.file_list[self.num])
        self.label_16.setPixmap(pixmap)
        self.label_16.setScaledContents(True)
        self.left_widget.reset()
        self.oleft_widget.reset()
        _translate = QtCore.QCoreApplication.translate
        self.label_9.setText(_translate("Form", "Image Name:" + self.file_list[self.num]))
        self.label_left.setText(_translate("Form", "图片已标注:" + str(len(os.listdir("Labels/"))) + "，还剩:" + str(
            len(self.file_list) - len(os.listdir("Labels/")))))
        for comboBox_i in self.A_comboBox_list:
            comboBox_i.reset()
        for comboBox_i in self.O_comboBox_list:
            comboBox_i.reset()
        self.QTextEdit.clear()

    def btn_add_val(self):
        my_key = self.comboBox_11.currentText()
        text = self.textEdit.toPlainText()
        text_list = text.split('，')
        _translate = QtCore.QCoreApplication.translate
        for i, key in enumerate(self.A_dict.keys()):
            if key == my_key:
                lines = []
                with open("Attribute", encoding='utf-8-sig') as f:
                    for line in f.readlines():
                        temp = line[:-1].split('：')
                        if temp[0] == my_key:
                            lines.append(line[:-1] +'，' +  text+'\n')
                        else:
                            lines.append(line)
                with open("Attribute",'w',encoding='utf-8') as f:
                    s = ''.join(lines)
                    f.write(str(s))
                for txt in text_list:
                    self.item = QListWidgetItem(txt, self.A_comboBox_list[i])  # 左侧选项的添加
                    font = QtGui.QFont()
                    font.setPointSize(15)
                    self.item.setFont(font)
                    self.item.setSizeHint(QSize(15, 25))
                    self.item.setTextAlignment(Qt.AlignCenter)  # 居中显示
                self.A_dict[key] += text_list
        for i, key in enumerate(self.O_dict.keys()):
            if key == my_key:
                lines = []
                with open("Object",encoding="utf-8-sig") as f:
                    for line in f.readlines():
                        temp = line[:-1].split('：')
                        if temp[0] == my_key:
                            lines.append(line[:-1] + '，'+text+'\n')
                        else:
                            lines.append(line)
                with open("Object",'w',encoding='utf-8') as f:
                    s = ''.join(lines)
                    f.write(str(s))
                for txt in text_list:
                    self.oitem = QListWidgetItem(txt,self.O_comboBox_list[i])  # 左侧选项的添加
                    font = QtGui.QFont()
                    font.setPointSize(15)
                    self.oitem.setFont(font)
                    self.oitem.setSizeHint(QSize(15, 25))
                    self.oitem.setTextAlignment(Qt.AlignCenter)  # 居中显示
                self.O_dict[key] += text_list
        print([my_key,text])

        self.textEdit.setText("")

    def radio_msg(self):
        if self.radioButton.isChecked():
            self.add_a = True
            self.add_o = False
        if self.radioButton_2.isChecked():
            self.add_o = True
            self.add_a = False
    def btn_add_class(self):
        if self.add_a:
            self.radioButton.setChecked(True)
            my_key = self.lineEdit_2.text()
            my_val = self.lineEdit_3.text()
            my_val = my_val.split("，")
            if self.checkBox.isChecked():
                if len(my_key) != 0:
                    i = len(self.A_comboBox_list)
                    self.item = QListWidgetItem(my_key, self.left_widget)  # 左侧选项的添加
                    font = QtGui.QFont()
                    font.setPointSize(15)
                    self.item.setFont(font)
                    self.item.setSizeHint(QSize(15, 25))
                    self.item.setTextAlignment(Qt.AlignCenter)  # 居中显示

                    locals()['stack' + str(i)] = QListWidget()  # 左侧选项列表
                    locals()['stack' + str(i)].setGeometry(QtCore.QRect(0, 0, 181, 360))
                    locals()['stack' + str(i)].setStyleSheet(self.list_style)
                    for att_v in my_val:
                        self.ritem = QListWidgetItem(att_v, locals()['stack' + str(i)])  # 左侧选项的添加
                        font = QtGui.QFont()
                        font.setPointSize(15)
                        self.ritem.setFont(font)
                        self.ritem.setSizeHint(QSize(15, 25))
                        self.ritem.setTextAlignment(Qt.AlignCenter)  # 居中显示
                    self.right_widget.addWidget(locals()['stack' + str(i)])
                    self.A_comboBox_list.append(locals()["stack" + str(i)])
                    locals()['stack' + str(i)].currentRowChanged.connect(self.row_change)
                    self.A_dict[my_key] = my_val
                    lines = []
                    with open("Attribute", encoding="utf-8-sig") as f:
                        for line in f.readlines():
                            lines.append(line)
                        lines.append('\n' + my_key + "：" + "，".join(my_val))
                    with open("Attribute", 'w', encoding="utf-8") as f:
                        s = ''.join(lines)
                        f.write(str(s))
            else:
                text = self.QTextEdit.toPlainText()
                if len(text)!= 0:
                    self.A_answer = eval(text.split('\n')[3])
                    self.O_answer = eval(text.split('\n')[1])
                else:
                    self.A_answer = {}
                    self.O_answer = {}
                # print(A_an)
                self.A_answer[my_key] = my_val[0]
                self.QTextEdit.setPlainText(
                    str("对象:\n") + str(self.O_answer) + "\n" + str("属性:\n") + str(self.A_answer) + "\n")
        if self.add_o:
            self.add_o = False
            self.radioButton.setChecked(True)
            my_key = self.lineEdit_2.text()
            my_val = self.lineEdit_3.text()
            my_val = my_val.split("，")
            if self.checkBox.isChecked():
                if len(my_key) != 0:
                    i = len(self.O_comboBox_list)
                    self.oitem = QListWidgetItem(my_key, self.oleft_widget)  # 左侧选项的添加
                    font = QtGui.QFont()
                    font.setPointSize(15)
                    self.oitem.setFont(font)
                    self.oitem.setSizeHint(QSize(15, 25))
                    self.oitem.setSizeHint(QSize(15, 20))
                    self.oitem.setTextAlignment(Qt.AlignCenter)  # 居中显示

                    locals()['ostack' + str(i)] = QListWidget()  # 左侧选项列表
                    locals()['ostack' + str(i)].setGeometry(QtCore.QRect(0, 0, 181, 360))
                    locals()['ostack' + str(i)].setStyleSheet(self.olist_style)
                    for obj_v in my_val:
                        self.oritem = QListWidgetItem(obj_v, locals()['ostack' + str(i)])  # 左侧选项的添加
                        font = QtGui.QFont()
                        font.setPointSize(15)
                        self.oritem.setFont(font)
                        self.oritem.setSizeHint(QSize(15, 25))
                        self.oritem.setTextAlignment(Qt.AlignCenter)  # 居中显示
                    self.oright_widget.addWidget(locals()['ostack' + str(i)])
                    self.O_comboBox_list.append(locals()["ostack" + str(i)])
                    locals()['ostack' + str(i)].currentRowChanged.connect(self.orow_change)
                    self.O_dict[my_key] = my_val
                    lines = []
                    with open("Object",encoding="utf-8-sig") as f:
                        for line in f.readlines():
                            lines.append(line)
                        lines.append('\n' + my_key + "：" + "，".join(my_val))
                    with open("Object", 'w',encoding="utf-8") as f:
                        s = ''.join(lines)
                        f.write(str(s))
            else:
                text = self.QTextEdit.toPlainText()
                if len(text) != 0:
                    self.A_answer = eval(text.split('\n')[3])
                    self.O_answer = eval(text.split('\n')[1])
                else:
                    self.A_answer = {}
                    self.O_answer = {}
                self.O_answer[my_key] = my_val[0]
                self.QTextEdit.setPlainText(
                    str("对象:\n") + str(self.O_answer) + "\n" + str("属性:\n") + str(self.A_answer) + "\n")
        self.radio_flag = False


        self.checkBox.setChecked(False)
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")

    def btn4_back(self):
        if self.num < 1:
            sys.exit(0)
        self.num = self.num - 1
        with open("count","w") as f:
            f.write(str(self.num))
        pixmap = QPixmap("./Images/"+self.file_list[self.num])
        self.label_16.setPixmap(pixmap)
        self.label_16.setScaledContents(True)
        _translate = QtCore.QCoreApplication.translate
        self.label_9.setText(_translate("Form", "Image Name:" + self.file_list[self.num]))
        for comboBox_i in self.A_comboBox_list:
            comboBox_i.reset()
        for comboBox_i in self.O_comboBox_list:
            comboBox_i.reset()
        self.QTextEdit.clear()







if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QWidget()
    ui=Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())