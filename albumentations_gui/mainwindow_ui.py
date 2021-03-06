# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1305, 1020)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.line_edit_image_path = QtWidgets.QLineEdit(self.centralWidget)
        self.line_edit_image_path.setReadOnly(True)
        self.line_edit_image_path.setObjectName("line_edit_image_path")
        self.horizontalLayout.addWidget(self.line_edit_image_path)
        self.button_open_image = QtWidgets.QPushButton(self.centralWidget)
        self.button_open_image.setObjectName("button_open_image")
        self.horizontalLayout.addWidget(self.button_open_image)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_code = QtWidgets.QWidget()
        self.tab_code.setObjectName("tab_code")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab_code)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.text_edit_code = QtWidgets.QTextEdit(self.tab_code)
        self.text_edit_code.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.text_edit_code.setObjectName("text_edit_code")
        self.horizontalLayout_6.addWidget(self.text_edit_code)
        self.tabWidget.addTab(self.tab_code, "")
        self.tab_dosctring = QtWidgets.QWidget()
        self.tab_dosctring.setObjectName("tab_dosctring")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_dosctring)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.text_edit_docstring = QtWidgets.QTextBrowser(self.tab_dosctring)
        self.text_edit_docstring.setMinimumSize(QtCore.QSize(320, 0))
        self.text_edit_docstring.setReadOnly(True)
        self.text_edit_docstring.setObjectName("text_edit_docstring")
        self.verticalLayout_3.addWidget(self.text_edit_docstring)
        self.tabWidget.addTab(self.tab_dosctring, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.textBrowser_json = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_json.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textBrowser_json.setObjectName("textBrowser_json")
        self.horizontalLayout_7.addWidget(self.textBrowser_json)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.textBrowser_yaml = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_yaml.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textBrowser_yaml.setObjectName("textBrowser_yaml")
        self.horizontalLayout_8.addWidget(self.textBrowser_yaml)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.transforms_tree = QtWidgets.QTreeView(self.centralWidget)
        self.transforms_tree.setObjectName("transforms_tree")
        self.horizontalLayout_5.addWidget(self.transforms_tree)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.button_clear = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_clear.sizePolicy().hasHeightForWidth())
        self.button_clear.setSizePolicy(sizePolicy)
        self.button_clear.setObjectName("button_clear")
        self.horizontalLayout_4.addWidget(self.button_clear)
        self.button_update_image = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_update_image.sizePolicy().hasHeightForWidth())
        self.button_update_image.setSizePolicy(sizePolicy)
        self.button_update_image.setObjectName("button_update_image")
        self.horizontalLayout_4.addWidget(self.button_update_image)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.list_widget_selected_transforms = QtWidgets.QListWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_widget_selected_transforms.sizePolicy().hasHeightForWidth())
        self.list_widget_selected_transforms.setSizePolicy(sizePolicy)
        self.list_widget_selected_transforms.setMaximumSize(QtCore.QSize(200, 16777215))
        self.list_widget_selected_transforms.setObjectName("list_widget_selected_transforms")
        self.verticalLayout_4.addWidget(self.list_widget_selected_transforms)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.scrollArea = QtWidgets.QScrollArea(self.centralWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 809, 965))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_image = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_image.setObjectName("label_image")
        self.horizontalLayout_3.addWidget(self.label_image)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        self.horizontalLayout_2.setStretch(1, 4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_open_image.setText(_translate("MainWindow", "Open"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_code), _translate("MainWindow", "Code"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_dosctring), _translate("MainWindow", "Docstring"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "JSON"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "YAML"))
        self.label.setText(_translate("MainWindow", "Selected transforms"))
        self.button_clear.setText(_translate("MainWindow", "Clear"))
        self.button_update_image.setText(_translate("MainWindow", "Update image"))
        self.label_image.setText(_translate("MainWindow", "Empty Image"))

