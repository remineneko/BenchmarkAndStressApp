# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\remin\PycharmProjects\BenchmarkAndStressApp\AppResources\ShuffleDomains.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ShuffleChoice(object):
    def setupUi(self, ShuffleChoice):
        ShuffleChoice.setObjectName("ShuffleChoice")
        ShuffleChoice.setFixedSize(281, 230)
        self.shuffleValid = QtWidgets.QPushButton(ShuffleChoice)
        self.shuffleValid.setGeometry(QtCore.QRect(10, 20, 261, 51))
        self.shuffleValid.setObjectName("shuffleValid")
        self.shuffleRandom = QtWidgets.QPushButton(ShuffleChoice)
        self.shuffleRandom.setGeometry(QtCore.QRect(10, 90, 261, 51))
        self.shuffleRandom.setObjectName("shuffleRandom")
        self.shuffleBlocked = QtWidgets.QPushButton(ShuffleChoice)
        self.shuffleBlocked.setGeometry(QtCore.QRect(10, 160, 261, 51))
        self.shuffleBlocked.setObjectName("shuffleBlocked")

        self.retranslateUi(ShuffleChoice)
        QtCore.QMetaObject.connectSlotsByName(ShuffleChoice)

    def retranslateUi(self, ShuffleChoice):
        _translate = QtCore.QCoreApplication.translate
        ShuffleChoice.setWindowTitle(_translate("ShuffleChoice", "Dialog"))
        self.shuffleValid.setText(_translate("ShuffleChoice", "Shuffle Valid Domains"))
        self.shuffleRandom.setText(_translate("ShuffleChoice", "Shuffle Random Domains"))
        self.shuffleBlocked.setText(_translate("ShuffleChoice", "Shuffle Blocked Domains"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ShuffleChoice = QtWidgets.QDialog()
    ui = Ui_ShuffleChoice()
    ui.setupUi(ShuffleChoice)
    ShuffleChoice.show()
    sys.exit(app.exec_())
