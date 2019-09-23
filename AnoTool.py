# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AnoTool.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import os
import json

class Ui_Form(object):
    def setupUi(self, Form):
        self.form = Form
        self.file_list = os.listdir("Images")
        with open("count") as f:
            self.num = int(f.read())
        self.add_a= True
        self.add_o = False
        self.A_extra = {}
        self.O_extra = {}
        f = open('Attribute')
        self.A_dict = {}
        for line in f.readlines():
            temp = line[:-1].split(':')
            self.A_dict[temp[0]] = temp[1].split(',')
        print(self.A_dict)
        f.close()
        f = open('Object')
        self.O_dict = {}
        for line in f.readlines():
            temp = line[:-1].split(':')
            self.O_dict[temp[0]] = temp[1].split(',')
        f.close()
        print(self.O_dict)
        Form.setObjectName("Form")
        Form.resize(1179, 803)
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(10, 10, 611, 391))
        pixmap = QPixmap("./Images/"+self.file_list[self.num])
        self.label_16.setPixmap(pixmap)
        self.label_16.setScaledContents(True)

        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(510, 403, 111, 31))
        pixmap = QPixmap("logo_iair.png")
        self.label_17.setPixmap(pixmap)
        self.label_17.setScaledContents(True)

        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(300, 403, 201, 31))
        pixmap = QPixmap("xjtu_logo.png")
        self.label_18.setPixmap(pixmap)
        self.label_18.setScaledContents(True)

        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(630, 10, 521, 391))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")

        self.A_comboBox_list = []
        self.A_label_list = []
        for i,key in enumerate(self.A_dict.keys()):
            locals()["A_comboBox" + str(i)] = QtWidgets.QComboBox(self.groupBox)
            if 60*(i+1)+31 <= 391:
                locals()["A_comboBox" + str(i)].setGeometry(QtCore.QRect(10, 60*(i+1), 181, 31))
            else:
                locals()["A_comboBox" + str(i)].setGeometry(QtCore.QRect(10+191, 60*(i+1-6), 181, 31))
            locals()["A_comboBox" + str(i)].setEditable(False)
            locals()["A_comboBox" + str(i)].setObjectName("A_comboBox")
            for val in self.A_dict[key]:
                locals()["A_comboBox" + str(i)].addItem("")
            locals()["A_label" + str(i)] = QtWidgets.QLabel(self.groupBox)
            if 40 + 60 * i <= 391:
                locals()["A_label" + str(i)].setGeometry(QtCore.QRect(10, 40 + 60 * i, 200, 16))
            else:
                locals()["A_label" + str(i)].setGeometry(QtCore.QRect(10 + 191, 40 + 60 * (i - 6), 200, 16))
            font = QtGui.QFont()
            font.setPointSize(18)
            locals()["A_label" + str(i)].setFont(font)
            locals()["A_label" + str(i)].setObjectName("A_label")
            self.A_comboBox_list.append(locals()["A_comboBox" + str(i)])
            self.A_label_list.append(locals()["A_label" + str(i)])
        self.groupBox_5 = QtWidgets.QGroupBox(Form)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 410, 611, 400))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setAutoFillBackground(False)
        self.groupBox_5.setObjectName("groupBox_5")
        self.O_comboBox_list = []
        self.O_label_list = []
        for i, key in enumerate(self.O_dict.keys()):
            locals()["O_comboBox" + str(i)] = QtWidgets.QComboBox(self.groupBox_5)
            if 60 * (i + 1) + 31 < 400:
                locals()["O_comboBox" + str(i)].setGeometry(QtCore.QRect(10, 60 * (i + 1), 181, 31))
            else:
                locals()["O_comboBox" + str(i)].setGeometry(QtCore.QRect(10 + 191, 60 * (i + 1 - 6), 181, 31))
            locals()["O_comboBox" + str(i)].setEditable(False)
            locals()["O_comboBox" + str(i)].setObjectName("O_comboBox")
            for val in self.O_dict[key]:
                locals()["O_comboBox" + str(i)].addItem("")
            locals()["O_label" + str(i)] = QtWidgets.QLabel(self.groupBox_5)
            if 40 + 60 * i < 400:
                locals()["O_label" + str(i)].setGeometry(QtCore.QRect(10, 40 + 60 * i, 200, 16))
            else:
                locals()["O_label" + str(i)].setGeometry(QtCore.QRect(10 + 191, 40 + 60 * (i-6), 200, 16))
            font = QtGui.QFont()
            font.setPointSize(18)
            locals()["O_label" + str(i)].setFont(font)
            locals()["O_label" + str(i)].setObjectName("O_label")
            self.O_comboBox_list.append(locals()["O_comboBox" + str(i)])
            self.O_label_list.append(locals()["O_label" + str(i)])
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(630, 730, 521, 61))
        self.pushButton.clicked.connect(self.btn_save)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 650, 521, 61))
        self.pushButton_2.clicked.connect(self.btn_add_class)
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox_11 = QtWidgets.QComboBox(Form)
        self.comboBox_11.setGeometry(QtCore.QRect(650, 480, 241, 31))
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
        self.lineEdit_2.setGeometry(QtCore.QRect(950, 600, 201, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(630, 540, 521, 61))
        self.pushButton_3.clicked.connect(self.btn_add_val)
        self.pushButton_3.setObjectName("pushButton_3")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(640, 600, 100, 20))
        self.radioButton.setChecked(True)
        self.radioButton.toggled.connect(self.radio_msg)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(730, 600, 100, 20))
        self.radioButton_2.toggled.connect(self.radio_msg)
        self.radioButton_2.setObjectName("radioButton_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(940, 450, 201, 81))
        self.textEdit.setObjectName("textEdit")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(640, 450, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(890, 600, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(880, 450, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(640, 420, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(890, 630, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(950, 630, 201, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(640, 630, 87, 20))
        self.checkBox.setObjectName("checkBox")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(930, 410, 221, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.btn4_back)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Anotation Tool"))
        self.groupBox.setTitle(_translate("Form", "Attribute"))
        for i,key in enumerate(self.A_dict.keys()):
            self.A_label_list[i].setText(_translate("Form", key))
            for j,val in enumerate(self.A_dict[key]):
                self.A_comboBox_list[i].setItemText(j, _translate("Form", val))
        self.groupBox_5.setTitle(_translate("Form", "Object"))
        for i,key in enumerate(self.O_dict.keys()):
            self.O_label_list[i].setText(_translate("Form", key))
            for j,val in enumerate(self.O_dict[key]):
                self.O_comboBox_list[i].setItemText(j, _translate("Form", val))
        for i,key in enumerate(self.A_dict.keys()):
            self.comboBox_11.setItemText(i, _translate("Form", key))
        for i,key in enumerate(self.O_dict.keys()):
            self.comboBox_11.setItemText(i+len(self.A_dict.keys()), _translate("Form", key))
        self.pushButton_3.setText(_translate("Form", "Add Value Complete"))
        self.radioButton.setText(_translate("Form", "Attribute"))
        self.radioButton_2.setText(_translate("Form", "Object"))
        self.label_11.setText(_translate("Form", "Name:"))
        self.label_12.setText(_translate("Form", "Name:"))
        self.label_13.setText(_translate("Form", "Value:"))
        self.label_9.setText(_translate("Form", "Image Name:"+self.file_list[self.num]))
        self.pushButton.setText(_translate("Form", "Anotation Completed"))
        self.pushButton_2.setText(_translate("Form", "Add Class Complete"))
        self.label_15.setText(_translate("Form", "Value:"))
        self.checkBox.setText(_translate("Form", "Update"))
        self.pushButton_4.setText(_translate("Form", "Last Image"))


    def btn_save(self):
        if self.num > len(self.file_list):
            print("Exit!!!")
        self.num += 1
        with open("count","w") as f:
            f.write(str(self.num))
        pixmap = QPixmap("./Images/"+self.file_list[self.num])
        self.label_16.setPixmap(pixmap)
        self.label_16.setScaledContents(True)
        Attribute_ = {}
        Object_ = {}
        for i, key in enumerate(self.A_dict.keys()):
            Val = self.A_comboBox_list[i].currentText()
            if Val != "none":
                Attribute_[key] = Val
        for i,key in enumerate(self.O_dict.keys()):
            Val = self.O_comboBox_list[i].currentText()
            if Val != "none":
                Object_[key] = Val
        Attribute = dict(Attribute_,**self.A_extra)
        Object = dict(Object_,**self.O_extra)
        with open("./Labels/"+self.file_list[self.num-1]+".json",mode="a") as f:
            json.dump(Attribute, f)
            json.dump(Object,f)
        _translate = QtCore.QCoreApplication.translate
        self.label_9.setText(_translate("Form", "Image Name:" + self.file_list[self.num]))
        for comboBox_i in self.A_comboBox_list:
            comboBox_i.setCurrentIndex(0)
        for comboBox_i in self.O_comboBox_list:
            comboBox_i.setCurrentIndex(0)

    def btn_add_val(self):
        my_key = self.comboBox_11.currentText()
        text = self.textEdit.toPlainText()
        text_list = text.split(',')
        _translate = QtCore.QCoreApplication.translate
        for i, key in enumerate(self.A_dict.keys()):
            if key == my_key:
                lines = []
                with open("Attribute") as f:
                    for line in f.readlines():
                        temp = line[:-1].split(':')
                        if temp[0] == my_key:
                            lines.append(line[:-1] +',' +  text+'\n')
                        else:
                            lines.append(line)
                with open("Attribute",'w') as f:
                    s = ''.join(lines)
                    f.write(s)
                for j,txt in enumerate(text_list):
                    self.A_comboBox_list[i].addItem("")
                    self.A_comboBox_list[i].setItemText(self.A_comboBox_list[i].count()-1, _translate("Form", txt))
        for i, key in enumerate(self.O_dict.keys()):
            if key == my_key:
                lines = []
                with open("Object") as f:
                    for line in f.readlines():
                        temp = line[:-1].split(':')
                        if temp[0] == my_key:
                            lines.append(line[:-1] + ','+text+'\n')
                        else:
                            lines.append(line)
                with open("Object",'w') as f:
                    s = ''.join(lines)
                    f.write(s)
                for j,txt in enumerate(text_list):
                    self.O_comboBox_list[i].addItem("")
                    self.O_comboBox_list[i].setItemText(self.O_comboBox_list[i].count()-1, _translate("Form", txt))
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
        _translate = QtCore.QCoreApplication.translate
        if self.add_a:
            self.radioButton.setChecked(True)
            my_key = self.lineEdit_2.text()
            my_val = self.lineEdit_3.text()
            my_val = ['none'] + my_val.split(",")
            if self.checkBox.isChecked():
                if len(my_key) != 0:
                    num_com = len(self.A_comboBox_list)
                    i = num_com
                    self.A_dict[my_key] = my_val
                    locals()["A_comboBox" + str(i)] = QtWidgets.QComboBox(self.groupBox)
                    if 60 * (i + 1) + 31 <= 391:
                        locals()["A_comboBox" + str(i)].setGeometry(QtCore.QRect(10, 60 * (i + 1), 181, 31))
                    else:
                        locals()["A_comboBox" + str(i)].setGeometry(QtCore.QRect(10 + 191, 60 * (i + 1 - 6), 181, 31))
                    locals()["A_comboBox" + str(i)].setEditable(False)
                    locals()["A_comboBox" + str(i)].setObjectName("A_comboBox")
                    for val in my_val:
                        locals()["A_comboBox" + str(i)].addItem("")
                    locals()["A_label" + str(i)] = QtWidgets.QLabel(self.groupBox)
                    if 40 + 60 * i <= 391:
                        locals()["A_label" + str(i)].setGeometry(QtCore.QRect(10, 40 + 60 * i, 200, 16))
                    else:
                        locals()["A_label" + str(i)].setGeometry(QtCore.QRect(10 + 191, 40 + 60 * (i - 6), 200, 16))
                    font = QtGui.QFont()
                    font.setPointSize(18)
                    locals()["A_label" + str(i)].setFont(font)
                    locals()["A_label" + str(i)].setObjectName("A_label")
                    self.A_comboBox_list.append(locals()["A_comboBox" + str(i)])
                    self.A_label_list.append(locals()["A_label" + str(i)])

                    locals()["A_label" + str(i)] .setText(_translate("Form", my_key))
                    for j, val in enumerate(my_val):
                        locals()["A_comboBox" + str(i)].setItemText(j, _translate("Form", val))
                    locals()["A_label" + str(i)].show()
                    locals()["A_comboBox" + str(i)].show()
                    self.comboBox_11.addItem("")
                    self.comboBox_11.setItemText(len(self.A_comboBox_list)+len(self.O_comboBox_list)-1, _translate("Form", my_key))
                    lines = []
                    with open("Attribute") as f:
                        for line in f.readlines():
                            lines.append(line)
                        lines.append("\n" + my_key + ":" + ",".join(my_val))
                    with open("Attribute", 'w') as f:
                        s = ''.join(lines)
                        f.write(s)
            else:
                self.A_extra[my_key] = my_val[1:][0]
        if self.add_o:
            self.add_o = False
            self.radioButton.setChecked(True)
            my_key = self.lineEdit_2.text()
            my_val = self.lineEdit_3.text()
            my_val = ['none'] + my_val.split(",")
            if self.checkBox.isChecked():
                if len(my_key) != 0:
                    num_com = len(self.O_comboBox_list)
                    i = num_com
                    self.O_dict[my_key] = my_val
                    locals()["O_comboBox" + str(i)] = QtWidgets.QComboBox(self.groupBox_5)
                    if 60 * (i + 1) + 31 < 400:
                        locals()["O_comboBox" + str(i)].setGeometry(QtCore.QRect(10, 60 * (i + 1), 181, 31))
                    else:
                        locals()["O_comboBox" + str(i)].setGeometry(QtCore.QRect(10 + 191, 60 * (i + 1 - 6), 181, 31))
                    locals()["O_comboBox" + str(i)].setEditable(False)
                    locals()["O_comboBox" + str(i)].setObjectName("A_comboBox")
                    for val in my_val:
                        locals()["O_comboBox" + str(i)].addItem("")
                    locals()["O_label" + str(i)] = QtWidgets.QLabel(self.groupBox_5)
                    if 40 + 60 * i < 400:
                        locals()["O_label" + str(i)].setGeometry(QtCore.QRect(10, 40 + 60 * i, 200, 16))
                    else:
                        locals()["O_label" + str(i)].setGeometry(QtCore.QRect(10 + 191, 40 + 60 * (i - 6), 200, 16))
                    font = QtGui.QFont()
                    font.setPointSize(18)
                    locals()["O_label" + str(i)].setFont(font)
                    locals()["O_label" + str(i)].setObjectName("O_label")
                    self.O_comboBox_list.append(locals()["O_comboBox" + str(i)])
                    self.O_label_list.append(locals()["O_label" + str(i)])

                    locals()["O_label" + str(i)].setText(_translate("Form", my_key))
                    for j, val in enumerate(my_val):
                        locals()["O_comboBox" + str(i)].setItemText(j, _translate("Form", val))
                    locals()["O_label" + str(i)].show()
                    locals()["O_comboBox" + str(i)].show()
                    self.comboBox_11.addItem("")
                    self.comboBox_11.setItemText(len(self.A_comboBox_list) + len(self.O_comboBox_list)-1,
                                                 _translate("Form", my_key))
                    lines = []
                    with open("Object") as f:
                        for line in f.readlines():
                            lines.append(line)
                        lines.append('\n' + my_key + ":" + ",".join(my_val))
                    with open("Object", 'w') as f:
                        s = ''.join(lines)
                        f.write(s)
            else:
                self.O_extra[my_key] = my_val[1:][0]
        self.radio_flag = False


        self.checkBox.setChecked(False)
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")

    def btn4_back(self):
        if self.num < 1:
            print("Exit!!!")
        self.num = self.num - 1
        with open("count","w") as f:
            f.write(str(self.num))
        pixmap = QPixmap("./Images/"+self.file_list[self.num])
        self.label_16.setPixmap(pixmap)
        self.label_16.setScaledContents(True)
        _translate = QtCore.QCoreApplication.translate
        self.label_9.setText(_translate("Form", "Image Name:" + self.file_list[self.num]))
        for comboBox_i in self.A_comboBox_list:
            comboBox_i.setCurrentIndex(0)
        for comboBox_i in self.O_comboBox_list:
            comboBox_i.setCurrentIndex(0)






if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QWidget()
    ui=Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())