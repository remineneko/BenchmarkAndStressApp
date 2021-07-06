# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\remin\PycharmProjects\BenchmarkAndStressApp\AppResources\NewDomainUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from src.UI import AddDomains, SetDomain, RemoveDifferentDomains, AddDifferentDomains, random_add
from src.main.MainComponents.LocalStorage import LocalStorage
from src.main.MainComponents.DomainRandomizer import domain_random


class Ui_MainWindow(object):
    def __init__(self, storage: LocalStorage):
        self.storage = storage
        self.valid_data = self.storage.get_valid_domains()
        self.random_data = self.storage.get_random_domains()
        self.blocked_data = self.storage.get_blocked_domains()

        self.valid_data = self.filter(self.valid_data)
        self.random_data =self.filter(self.random_data)
        self.blocked_data = self.filter(self.blocked_data)

    def filter(self, data_list):
        '''
        filters out the duplicate in the given list.
        :return:
        '''
        return list(dict.fromkeys(data_list))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(870, 613)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ValidList = QtWidgets.QListWidget(self.centralwidget)
        self.ValidList.setGeometry(QtCore.QRect(20, 50, 231, 521))
        self.ValidList.setObjectName("ValidList")

        if len(self.valid_data) != 0:
            self.ValidList.addItems(self.valid_data)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(730, 50, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(730, 110, 121, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(730, 170, 121, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(730, 230, 121, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.RandomList = QtWidgets.QListWidget(self.centralwidget)
        self.RandomList.setGeometry(QtCore.QRect(250, 50, 231, 521))
        self.RandomList.setObjectName("RandomList")

        if len(self.random_data) != 0:
            self.RandomList.addItems(self.random_data)

        self.BlockList = QtWidgets.QListWidget(self.centralwidget)
        self.BlockList.setGeometry(QtCore.QRect(480, 50, 231, 521))
        self.BlockList.setObjectName("BlockList")

        if len(self.blocked_data) != 0:
            self.BlockList.addItems(self.blocked_data)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 20, 131, 21))
        self.label.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 20, 141, 21))
        self.label_4.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(520, 20, 131, 21))
        self.label_2.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Domains"))
        self.pushButton.setText(_translate("MainWindow", "Add Domains"))
        self.pushButton.clicked.connect(self.addChoices)
        self.pushButton_5.setText(_translate("MainWindow", "Modify"))
        self.pushButton_5.clicked.connect(self.openDialog)
        self.pushButton_2.setText(_translate("MainWindow", "Remove"))
        self.pushButton_2.clicked.connect(self.removeItem)
        self.pushButton_3.setText(_translate("MainWindow", "Remove All"))
        self.pushButton_3.clicked.connect(self.removeAll)
        self.label.setText(_translate("MainWindow", "Valid Domains"))
        self.label_4.setText(_translate("MainWindow", "Random Domains"))
        self.label_2.setText(_translate("MainWindow", "Blocked Domains"))

    def _get_cur_selected(self):
        return {'valid': self.ValidList.selectedItems(), 'random': self.RandomList.selectedItems(),
                    'blocked': self.BlockList.selectedItems()}

    def addChoices(self):
        self.choice_ = QtWidgets.QDialog()
        self.choice_ui = AddDifferentDomains.Ui_Dialog()
        self.choice_ui.setupUi(self.choice_)
        self.choice_.show()
        self.choice_ui.pushButton.clicked.connect(lambda: self.openWindow('valid'))
        self.choice_ui.pushButton_2.clicked.connect(self.openRandom)
        self.choice_ui.pushButton_3.clicked.connect(lambda: self.openWindow('blocked'))

    def openWindow(self, chosen_section):
        self.window = QtWidgets.QMainWindow()
        self.ui = AddDomains.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.pushButton.clicked.connect(lambda: self.addContent(self.ui.lineEdit.text(), chosen_section))

    def openRandom(self):
        self.r_dialog = QtWidgets.QDialog()
        self.r_ui = random_add.Ui_Dialog()
        self.r_ui.setupUi(self.r_dialog)
        self.r_dialog.show()
        self.r_ui.buttonBox.accepted.connect(lambda: self.addRandom(self.r_ui.lineEdit.text() ,self.r_dialog))

    def addRandom(self, text, dialog):
        dialog.close()
        if len(text) == 0 or not text.isdigit():
            self.error_dialog = QtWidgets.QErrorMessage()
            self.error_dialog.setWindowTitle('Warning')
            self.error_dialog.showMessage('Please type a number')
            self.error_dialog.exec_()
        else:
            random_gen = domain_random(int(text))
            self.RandomList.addItems(random_gen)
            self.storage.add_domains(random_gen, 'random')

    def openDialog(self):
        selected = self._get_cur_selected()
        total_selected = sum([len(sel) for sel in selected.values()])
        sole_selected = {k:v for k,v in selected.items() if len(v) == 1}
        if total_selected == 0:
            self.error_dialog = QtWidgets.QErrorMessage()
            self.error_dialog.setWindowTitle('Warning')
            self.error_dialog.showMessage('Please choose a domain to be edited.')
            self.error_dialog.exec_()
        elif total_selected > 1:
            self.error_dialog = QtWidgets.QErrorMessage()
            self.error_dialog.setWindowTitle('Warning')
            self.error_dialog.showMessage('Please choose only one domain to be edited.')
            self.error_dialog.exec_()
        else:
            self.dialog = QtWidgets.QDialog()
            self.ui = SetDomain.Ui_Dialog()
            self.ui.setupUi(self.dialog)
            self.dialog.show()
            self.ui.lineEdit.setText(sole_selected[list(sole_selected.keys())[0]][0].text())
            self.ui.buttonBox.accepted.connect(lambda: self.modifyContent(self.dialog, self.ui.lineEdit.text(), sole_selected))

    def addContent(self, content, section):
        content_list = content.split(";")
        for c in content_list:
            stripped_content = c.strip()
            if len(stripped_content) != 0:
                cur_data = self.storage.get_domain_by_section(section)
                if stripped_content not in cur_data:
                    if section == 'valid':
                        self.ValidList.addItem(stripped_content)
                    elif section == 'random':
                        self.RandomList.addItem(stripped_content)
                    else:
                        self.BlockList.addItem(stripped_content)
                    self.storage.add_domain(stripped_content, section)
        self.window.close()

    def modifyContent(self, dialog, content, select_dict):
        dialog.close()
        content = content.replace(" ", "")
        key_to_change, val_to_change = list(select_dict.items())[0]
        self.storage.modify_domain(key_to_change,val_to_change[0].text(), content)
        self.refresh(key_to_change)

    def refresh(self, key):
        if key == 'valid':
            self.ValidList.clear()
            self.valid_data = self.storage.get_valid_domains()
            self.ValidList.addItems(self.valid_data)
        elif key == 'random':
            self.RandomList.clear()
            self.random_data = self.storage.get_random_domains()
            self.RandomList.addItems(self.random_data)
        else:
            self.BlockList.clear()
            self.blocked_data = self.storage.get_blocked_domains()
            self.BlockList.addItems(self.blocked_data)


    def removeItem(self):
        selected = self._get_cur_selected()
        total_selected = sum([len(sel) for sel in selected.items()])
        if total_selected == 0:
            self.error_dialog = QtWidgets.QErrorMessage()
            self.error_dialog.setWindowTitle('Warning')
            self.error_dialog.showMessage('Please choose a domain to be removed.')
            self.error_dialog.exec_()
        for key in selected:
            if key == 'valid':
                for entry in selected[key]:
                    self.ValidList.takeItem(self.ValidList.row(entry))
                    self.storage.remove_domains(entry.text(),key)
            elif key == 'random':
                for entry in selected[key]:
                    self.RandomList.takeItem(self.RandomList.row(entry))
                    self.storage.remove_domains(entry.text(),key)
            else:
                for entry in selected[key]:
                    self.BlockList.takeItem(self.BlockList.row(entry))
                    self.storage.remove_domains(entry.text(),key)

    def removeAll(self):
        self.remove_dialog = QtWidgets.QDialog()
        self.remove_obj = RemoveDifferentDomains.Ui_Dialog()

        self.remove_obj.setupUi(self.remove_dialog)
        self.remove_dialog.show()
        self.remove_obj.pushButton.clicked.connect(lambda: self.remove_valid(self.remove_dialog))
        self.remove_obj.pushButton_2.clicked.connect(lambda: self.remove_random(self.remove_dialog))
        self.remove_obj.pushButton_3.clicked.connect(lambda: self.remove_blocked(self.remove_dialog))

    def remove_valid(self, mw):
        self.ValidList.clear()
        self.storage.remove_all_domains('valid')
        mw.close()

    def remove_random(self, mw):
        self.RandomList.clear()
        self.storage.remove_all_domains('random')
        mw.close()

    def remove_blocked(self, mw):
        self.BlockList.clear()
        self.storage.remove_all_domains('blocked')
        mw.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
