from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject, QSize, QTime, Qt)
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QCheckBox, QDateEdit, QFrame, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QListWidget,
                               QProgressBar, QPushButton,QSizePolicy, QTabWidget, QWidget, QFileDialog, QMessageBox)
from emitter import *
import var
import threading
from time import sleep
from parser import name as nm
from reader import get_coberturas


class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(600, 400)
        Widget.setWindowIcon(QIcon('dados/ícone.ico'))

        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabs = QTabWidget(Widget)
        self.tabs.setObjectName(u"tabs")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy)
        self.tabs.setTabShape(QTabWidget.Rounded)
        self.tabs.setDocumentMode(False)
        self.tabs.setMovable(False)
        self.multiple_tab = QWidget()
        self.multiple_tab.setObjectName(u"multiple_tab")
        self.gridLayout_3 = QGridLayout(self.multiple_tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.output_multiple_layout = QHBoxLayout()
        self.output_multiple_layout.setObjectName(u"output_multiple_layout")
        self.output_multiple_button = QPushButton(self.multiple_tab)
        self.output_multiple_button.setObjectName(u"output_multiple_button")
        self.output_multiple_button.setMinimumSize(QSize(160, 30))

        self.output_multiple_layout.addWidget(self.output_multiple_button)

        self.output_header_multiple_label = QLabel(self.multiple_tab)
        self.output_header_multiple_label.setObjectName(u"output_header_multiple_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.output_header_multiple_label.sizePolicy().hasHeightForWidth())
        self.output_header_multiple_label.setSizePolicy(sizePolicy1)

        self.output_multiple_layout.addWidget(self.output_header_multiple_label)

        self.output_multiple_label = QLabel(self.multiple_tab)
        self.output_multiple_label.setObjectName(u"output_multiple_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.output_multiple_label.sizePolicy().hasHeightForWidth())
        self.output_multiple_label.setSizePolicy(sizePolicy2)
        self.output_multiple_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.output_multiple_layout.addWidget(self.output_multiple_label)


        self.gridLayout_3.addLayout(self.output_multiple_layout, 1, 0, 1, 1)

        self.line = QFrame(self.multiple_tab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 4, 0, 1, 1)

        self.emission_layout = QHBoxLayout()
        self.emission_layout.setObjectName(u"emission_layout")
        self.labels_grid_layout = QGridLayout()
        self.labels_grid_layout.setObjectName(u"labels_grid_layout")
        self.speed_label = QLabel(self.multiple_tab)
        self.speed_label.setObjectName(u"speed_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.speed_label.sizePolicy().hasHeightForWidth())
        self.speed_label.setSizePolicy(sizePolicy3)

        self.labels_grid_layout.addWidget(self.speed_label, 0, 1, 1, 1)

        self.speed_header_label = QLabel(self.multiple_tab)
        self.speed_header_label.setObjectName(u"speed_header_label")
        sizePolicy1.setHeightForWidth(self.speed_header_label.sizePolicy().hasHeightForWidth())
        self.speed_header_label.setSizePolicy(sizePolicy1)

        self.labels_grid_layout.addWidget(self.speed_header_label, 0, 0, 1, 1)

        self.time_header_label = QLabel(self.multiple_tab)
        self.time_header_label.setObjectName(u"time_header_label")
        sizePolicy1.setHeightForWidth(self.time_header_label.sizePolicy().hasHeightForWidth())
        self.time_header_label.setSizePolicy(sizePolicy1)

        self.labels_grid_layout.addWidget(self.time_header_label, 1, 0, 1, 1)

        self.time_label = QLabel(self.multiple_tab)
        self.time_label.setObjectName(u"time_label")
        sizePolicy3.setHeightForWidth(self.time_label.sizePolicy().hasHeightForWidth())
        self.time_label.setSizePolicy(sizePolicy3)

        self.labels_grid_layout.addWidget(self.time_label, 1, 1, 1, 1)


        self.emission_layout.addLayout(self.labels_grid_layout)

        self.emission_button = QPushButton(self.multiple_tab)
        self.emission_button.setObjectName(u"emission_button")
        self.emission_button.setMinimumSize(QSize(0, 30))

        self.emission_layout.addWidget(self.emission_button)


        self.gridLayout_3.addLayout(self.emission_layout, 6, 0, 1, 1)

        self.progressBar = QProgressBar(self.multiple_tab)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.gridLayout_3.addWidget(self.progressBar, 5, 0, 1, 1)

        self.date_layout = QHBoxLayout()
        self.date_layout.setObjectName(u"date_layout")
        self.start_date_layout = QHBoxLayout()
        self.start_date_layout.setObjectName(u"start_date_layout")
        self.start_date_label = QLabel(self.multiple_tab)
        self.start_date_label.setObjectName(u"start_date_label")
        sizePolicy1.setHeightForWidth(self.start_date_label.sizePolicy().hasHeightForWidth())
        self.start_date_label.setSizePolicy(sizePolicy1)

        self.start_date_layout.addWidget(self.start_date_label)

        self.start_date_multiple_dateedit = QDateEdit(self.multiple_tab)
        self.start_date_multiple_dateedit.setObjectName(u"start_date_multiple_dateedit")
        self.start_date_multiple_dateedit.setDateTime(QDateTime(QDate(2023, 1, 13), QTime(0, 0, 0)))
        self.start_date_multiple_dateedit.setTime(QTime(0, 0, 0))
        self.start_date_multiple_dateedit.setMaximumDate(QDate(2023, 12, 31))
        self.start_date_multiple_dateedit.setMinimumDate(QDate(2023, 1, 13))
        self.start_date_multiple_dateedit.setCalendarPopup(True)

        self.start_date_layout.addWidget(self.start_date_multiple_dateedit)


        self.date_layout.addLayout(self.start_date_layout)

        self.end_date_layout = QHBoxLayout()
        self.end_date_layout.setObjectName(u"end_date_layout")
        self.end_date_label = QLabel(self.multiple_tab)
        self.end_date_label.setObjectName(u"end_date_label")
        sizePolicy1.setHeightForWidth(self.end_date_label.sizePolicy().hasHeightForWidth())
        self.end_date_label.setSizePolicy(sizePolicy1)

        self.end_date_layout.addWidget(self.end_date_label)

        self.end_date_multiple_dateedit = QDateEdit(self.multiple_tab)
        self.end_date_multiple_dateedit.setObjectName(u"end_date_multiple_dateedit")
        self.end_date_multiple_dateedit.setDateTime(QDateTime(QDate(2023, 1, 13), QTime(0, 0, 0)))
        self.end_date_multiple_dateedit.setTime(QTime(0, 0, 0))
        self.end_date_multiple_dateedit.setMaximumDate(QDate(2023, 12, 31))
        self.end_date_multiple_dateedit.setMinimumDate(QDate(2023, 1, 13))
        self.end_date_multiple_dateedit.setCalendarPopup(True)

        self.end_date_layout.addWidget(self.end_date_multiple_dateedit)


        self.date_layout.addLayout(self.end_date_layout)


        self.gridLayout_3.addLayout(self.date_layout, 2, 0, 1, 1)

        self.input_layout = QHBoxLayout()
        self.input_layout.setObjectName(u"input_layout")
        self.input_button = QPushButton(self.multiple_tab)
        self.input_button.setObjectName(u"input_button")
        self.input_button.setMinimumSize(QSize(160, 30))

        self.input_layout.addWidget(self.input_button)

        self.input_header_label = QLabel(self.multiple_tab)
        self.input_header_label.setObjectName(u"input_header_label")
        sizePolicy1.setHeightForWidth(self.input_header_label.sizePolicy().hasHeightForWidth())
        self.input_header_label.setSizePolicy(sizePolicy1)

        self.input_layout.addWidget(self.input_header_label)

        self.input_label = QLabel(self.multiple_tab)
        self.input_label.setObjectName(u"input_label")
        sizePolicy2.setHeightForWidth(self.input_label.sizePolicy().hasHeightForWidth())
        self.input_label.setSizePolicy(sizePolicy2)
        self.input_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.input_layout.addWidget(self.input_label)


        self.gridLayout_3.addLayout(self.input_layout, 0, 0, 1, 1)

        self.apolice_checkbox = QCheckBox(self.multiple_tab)
        self.apolice_checkbox.setObjectName(u"apolice_checkbox")

        self.gridLayout_3.addWidget(self.apolice_checkbox, 3, 0, 1, 1)

        self.tabs.addTab(self.multiple_tab, "")
        self.singular_tab = QWidget()
        self.singular_tab.setObjectName(u"singular_tab")
        self.gridLayout_2 = QGridLayout(self.singular_tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.output_header_label = QLabel(self.singular_tab)
        self.output_header_label.setObjectName(u"output_header_label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.output_header_label.sizePolicy().hasHeightForWidth())
        self.output_header_label.setSizePolicy(sizePolicy4)

        self.gridLayout_2.addWidget(self.output_header_label, 0, 1, 1, 1)

        self.output_button = QPushButton(self.singular_tab)
        self.output_button.setObjectName(u"output_button")
        sizePolicy4.setHeightForWidth(self.output_button.sizePolicy().hasHeightForWidth())
        self.output_button.setSizePolicy(sizePolicy4)
        self.output_button.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.output_button, 0, 0, 1, 1)

        self.name_layout = QHBoxLayout()
        self.name_layout.setObjectName(u"name_layout")
        self.name_label = QLabel(self.singular_tab)
        self.name_label.setObjectName(u"name_label")
        sizePolicy4.setHeightForWidth(self.name_label.sizePolicy().hasHeightForWidth())
        self.name_label.setSizePolicy(sizePolicy4)
        self.name_label.setMinimumSize(QSize(60, 0))

        self.name_layout.addWidget(self.name_label)

        self.name_lineedit = QLineEdit(self.singular_tab)
        self.name_lineedit.setObjectName(u"name_lineedit")
        self.name_lineedit.setMaximumSize(QSize(16777215, 16777215))
        self.name_lineedit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.name_layout.addWidget(self.name_lineedit)


        self.gridLayout_2.addLayout(self.name_layout, 2, 3, 1, 3)

        self.matricula_layout = QHBoxLayout()
        self.matricula_layout.setObjectName(u"matricula_layout")
        self.matricula_label = QLabel(self.singular_tab)
        self.matricula_label.setObjectName(u"matricula_label")
        sizePolicy4.setHeightForWidth(self.matricula_label.sizePolicy().hasHeightForWidth())
        self.matricula_label.setSizePolicy(sizePolicy4)
        self.matricula_label.setMinimumSize(QSize(60, 0))

        self.matricula_layout.addWidget(self.matricula_label)

        self.matricula_lineedit = QLineEdit(self.singular_tab)
        self.matricula_lineedit.setObjectName(u"matricula_lineedit")
        self.matricula_lineedit.setMaximumSize(QSize(16777215, 16777215))
        self.matricula_lineedit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.matricula_layout.addWidget(self.matricula_lineedit)


        self.gridLayout_2.addLayout(self.matricula_layout, 5, 3, 1, 3)

        self.end_date_layout_multiple = QHBoxLayout()
        self.end_date_layout_multiple.setObjectName(u"end_date_layout_multiple")
        self.end_date_singular_label = QLabel(self.singular_tab)
        self.end_date_singular_label.setObjectName(u"end_date_singular_label")
        sizePolicy4.setHeightForWidth(self.end_date_singular_label.sizePolicy().hasHeightForWidth())
        self.end_date_singular_label.setSizePolicy(sizePolicy4)
        self.end_date_singular_label.setMinimumSize(QSize(90, 0))

        self.end_date_layout_multiple.addWidget(self.end_date_singular_label)

        self.end_date_singular_dateedit = QDateEdit(self.singular_tab)
        self.end_date_singular_dateedit.setObjectName(u"end_date_singular_dateedit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.end_date_singular_dateedit.sizePolicy().hasHeightForWidth())
        self.end_date_singular_dateedit.setSizePolicy(sizePolicy5)
        self.end_date_singular_dateedit.setDateTime(QDateTime(QDate(2023, 1, 1), QTime(0, 0, 0)))
        self.end_date_singular_dateedit.setTime(QTime(0, 0, 0))
        self.end_date_singular_dateedit.setMaximumDate(QDate(2032, 12, 31))
        self.end_date_singular_dateedit.setMinimumDate(QDate(2023, 1, 1))
        self.end_date_singular_dateedit.setCalendarPopup(True)

        self.end_date_layout_multiple.addWidget(self.end_date_singular_dateedit)


        self.gridLayout_2.addLayout(self.end_date_layout_multiple, 7, 3, 1, 3)

        self.cpf_layout = QHBoxLayout()
        self.cpf_layout.setObjectName(u"cpf_layout")
        self.cpf_label = QLabel(self.singular_tab)
        self.cpf_label.setObjectName(u"cpf_label")
        sizePolicy4.setHeightForWidth(self.cpf_label.sizePolicy().hasHeightForWidth())
        self.cpf_label.setSizePolicy(sizePolicy4)
        self.cpf_label.setMinimumSize(QSize(60, 0))

        self.cpf_layout.addWidget(self.cpf_label)

        self.cpf_lineedit = QLineEdit(self.singular_tab)
        self.cpf_lineedit.setObjectName(u"cpf_lineedit")
        self.cpf_lineedit.setMaximumSize(QSize(16777215, 16777215))
        self.cpf_lineedit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.cpf_layout.addWidget(self.cpf_lineedit)


        self.gridLayout_2.addLayout(self.cpf_layout, 3, 3, 1, 3)

        self.apolice_layout = QHBoxLayout()
        self.apolice_layout.setObjectName(u"apolice_layout")
        self.apolice_singular_checkbutton = QCheckBox(self.singular_tab)
        self.apolice_singular_checkbutton.setObjectName(u"apolice_singular_checkbutton")
        sizePolicy1.setHeightForWidth(self.apolice_singular_checkbutton.sizePolicy().hasHeightForWidth())
        self.apolice_singular_checkbutton.setSizePolicy(sizePolicy1)

        self.apolice_layout.addWidget(self.apolice_singular_checkbutton)

        self.apolice_lineedit = QLineEdit(self.singular_tab)
        self.apolice_lineedit.setObjectName(u"apolice_lineedit")
        self.apolice_lineedit.setEnabled(False)

        self.apolice_layout.addWidget(self.apolice_lineedit)


        self.gridLayout_2.addLayout(self.apolice_layout, 8, 3, 1, 3)

        self.output_label = QLabel(self.singular_tab)
        self.output_label.setObjectName(u"output_label")
        sizePolicy3.setHeightForWidth(self.output_label.sizePolicy().hasHeightForWidth())
        self.output_label.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.output_label, 0, 2, 1, 4)

        self.cobertura_label = QLabel(self.singular_tab)
        self.cobertura_label.setObjectName(u"cobertura_label")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.cobertura_label.sizePolicy().hasHeightForWidth())
        self.cobertura_label.setSizePolicy(sizePolicy6)

        self.gridLayout_2.addWidget(self.cobertura_label, 9, 1, 1, 5)

        self.cobertura_header_label = QLabel(self.singular_tab)
        self.cobertura_header_label.setObjectName(u"cobertura_header_label")
        sizePolicy1.setHeightForWidth(self.cobertura_header_label.sizePolicy().hasHeightForWidth())
        self.cobertura_header_label.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.cobertura_header_label, 9, 0, 1, 1)

        self.start_date_layout_multiple = QHBoxLayout()
        self.start_date_layout_multiple.setObjectName(u"start_date_layout_multiple")
        self.start_date_singular_label = QLabel(self.singular_tab)
        self.start_date_singular_label.setObjectName(u"start_date_singular_label")
        sizePolicy4.setHeightForWidth(self.start_date_singular_label.sizePolicy().hasHeightForWidth())
        self.start_date_singular_label.setSizePolicy(sizePolicy4)
        self.start_date_singular_label.setMinimumSize(QSize(90, 0))

        self.start_date_layout_multiple.addWidget(self.start_date_singular_label)

        self.start_date_singular_dateedit = QDateEdit(self.singular_tab)
        self.start_date_singular_dateedit.setObjectName(u"start_date_singular_dateedit")
        sizePolicy5.setHeightForWidth(self.start_date_singular_dateedit.sizePolicy().hasHeightForWidth())
        self.start_date_singular_dateedit.setSizePolicy(sizePolicy5)
        self.start_date_singular_dateedit.setDateTime(QDateTime(QDate(2023, 1, 1), QTime(0, 0, 0)))
        self.start_date_singular_dateedit.setTime(QTime(0, 0, 0))
        self.start_date_singular_dateedit.setMaximumDate(QDate(2032, 12, 31))
        self.start_date_singular_dateedit.setMinimumDate(QDate(2023, 1, 1))
        self.start_date_singular_dateedit.setCalendarPopup(True)

        self.start_date_layout_multiple.addWidget(self.start_date_singular_dateedit)


        self.gridLayout_2.addLayout(self.start_date_layout_multiple, 6, 3, 1, 3)

        self.emit_button = QPushButton(self.singular_tab)
        self.emit_button.setObjectName(u"emit_button")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.emit_button.sizePolicy().hasHeightForWidth())
        self.emit_button.setSizePolicy(sizePolicy7)
        self.emit_button.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.emit_button, 10, 0, 1, 6)

        self.coberturas_list = QListWidget(self.singular_tab)
        self.coberturas_list.setObjectName(u"coberturas_list")
        self.coberturas_list.addItems(get_coberturas(var.coberturas_path))

        self.gridLayout_2.addWidget(self.coberturas_list, 2, 0, 7, 3)

        self.cnpj_layout = QHBoxLayout()
        self.cnpj_layout.setObjectName(u"cnpj_layout")
        self.cnpj_label = QLabel(self.singular_tab)
        self.cnpj_label.setObjectName(u"cnpj_label")
        sizePolicy4.setHeightForWidth(self.cnpj_label.sizePolicy().hasHeightForWidth())
        self.cnpj_label.setSizePolicy(sizePolicy4)
        self.cnpj_label.setMinimumSize(QSize(60, 0))

        self.cnpj_layout.addWidget(self.cnpj_label)

        self.cnpj_lineedit = QLineEdit(self.singular_tab)
        self.cnpj_lineedit.setObjectName(u"cnpj_lineedit")
        sizePolicy7.setHeightForWidth(self.cnpj_lineedit.sizePolicy().hasHeightForWidth())
        self.cnpj_lineedit.setSizePolicy(sizePolicy7)
        self.cnpj_lineedit.setMaximumSize(QSize(16777215, 16777215))
        self.cnpj_lineedit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.cnpj_layout.addWidget(self.cnpj_lineedit)


        self.gridLayout_2.addLayout(self.cnpj_layout, 4, 3, 1, 3)

        self.success_label = QLabel(self.singular_tab)
        self.success_label.setObjectName(u"success_label")
        sizePolicy6.setHeightForWidth(self.success_label.sizePolicy().hasHeightForWidth())
        self.success_label.setSizePolicy(sizePolicy6)
        self.success_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.success_label, 11, 0, 1, 6)

        self.tabs.addTab(self.singular_tab, "")

        self.gridLayout.addWidget(self.tabs, 2, 0, 1, 1)


        self.retranslateUi(Widget)
        self.input_button.released.connect(self.select_input_directory)
        self.output_multiple_button.released.connect(self.select_output_directory)
        self.start_date_multiple_dateedit.dateChanged.connect(self.change_start_date_multiple)
        self.end_date_multiple_dateedit.dateChanged.connect(self.change_end_date_multiple)
        self.apolice_checkbox.toggled.connect(self.toggle_apolice_multiple)
        self.emission_button.released.connect(self.emit_multiple)
        self.output_button.released.connect(self.select_output_directory)
        self.apolice_singular_checkbutton.toggled.connect(self.toggle_apolice_singular)
        self.emit_button.released.connect(self.emit_singular)
        self.coberturas_list.itemSelectionChanged.connect(self.select_item)

        self.tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.output_multiple_button.setText(QCoreApplication.translate("Widget", u"Selecionar pasta de destino", None))
        self.output_header_multiple_label.setText(QCoreApplication.translate("Widget", u"Pasta de destino:", None))
        self.output_multiple_label.setText("")
        self.speed_label.setText("")
        self.speed_header_label.setText(QCoreApplication.translate("Widget", u"Velocidade de emiss\u00e3o:", None))
        self.time_header_label.setText(QCoreApplication.translate("Widget", u"Tempo de emiss\u00e3o:", None))
        self.time_label.setText("")
        self.emission_button.setText(QCoreApplication.translate("Widget", u"Emitir certificados", None))
        self.start_date_label.setText(QCoreApplication.translate("Widget", u"Vig\u00eancia inicial:", None))
        self.end_date_label.setText(QCoreApplication.translate("Widget", u"Vig\u00eancia final:", None))
        self.input_button.setText(QCoreApplication.translate("Widget", u"Selecionar arquivo", None))
        self.input_header_label.setText(QCoreApplication.translate("Widget", u"Arquivo selecionado:", None))
        self.input_label.setText("")
        self.apolice_checkbox.setText(QCoreApplication.translate("Widget", u"Emitir com n\u00famero de ap\u00f3lice", None))
        self.tabs.setTabText(self.tabs.indexOf(self.multiple_tab), QCoreApplication.translate("Widget", u"M\u00faltiplos", None))
        self.output_header_label.setText(QCoreApplication.translate("Widget", u"Pasta de destino:", None))
        self.output_button.setText(QCoreApplication.translate("Widget", u"Escolher diret\u00f3rio de destino", None))
        self.name_label.setText(QCoreApplication.translate("Widget", u"Nome:", None))
        self.matricula_label.setText(QCoreApplication.translate("Widget", u"Matr\u00edcula: ", None))
        self.end_date_singular_label.setText(QCoreApplication.translate("Widget", u"Vig\u00eancia final:", None))
        self.cpf_label.setText(QCoreApplication.translate("Widget", u"CPF: ", None))
        self.apolice_singular_checkbutton.setText(QCoreApplication.translate("Widget", u"Ap\u00f3lice:", None))
        self.output_label.setText("")
        self.cobertura_label.setText("")
        self.cobertura_header_label.setText(QCoreApplication.translate("Widget", u"Cobertura selecionada:", None))
        self.start_date_singular_label.setText(QCoreApplication.translate("Widget", u"Vig\u00eancia inicial:", None))
        self.emit_button.setText(QCoreApplication.translate("Widget", u"Emitir certificado", None))
        self.cnpj_label.setText(QCoreApplication.translate("Widget", u"CNPJ: ", None))
        self.success_label.setText("")
        self.tabs.setTabText(self.tabs.indexOf(self.singular_tab), QCoreApplication.translate("Widget", u"Individual", None))
    # retranslateUi

    def toggle_apolice_multiple(self):
        if self.apolice_checkbox.isChecked():
            self.apolice_singular_checkbutton.setChecked(True)
            self.apolice_lineedit.setEnabled(True)
            var.apolice = True
        else:
            self.apolice_singular_checkbutton.setChecked(False)
            self.apolice_lineedit.setEnabled(False)
            var.apolice = False

    def toggle_apolice_singular(self):
        if self.apolice_singular_checkbutton.isChecked():
            self.apolice_checkbox.setChecked(True)
            self.apolice_lineedit.setEnabled(True)
            var.apolice = True
        else:
            self.apolice_checkbox.setChecked(False)
            self.apolice_lineedit.setEnabled(False)
            var.apolice = False

    def select_input_directory(self):
        var.data_dir = QFileDialog.getOpenFileName()[0]
        self.input_label.setText(var.data_dir)

    def select_output_directory(self):
        var.output_dir = QFileDialog.getExistingDirectory() + '/'
        self.output_multiple_label.setText(var.output_dir)
        self.output_label.setText(var.output_dir)

    def change_start_date_multiple(self):
        day = str(self.start_date_multiple_dateedit.date().day())
        mon = str(self.start_date_multiple_dateedit.date().month())
        yea = str(self.start_date_multiple_dateedit.date().year())

        if len(day) < 2: day = '0' + day
        if len(mon) < 2: mon = '0' + mon

        var.start_period = day + '/' + mon + '/' + yea
        self.start_date_singular_dateedit.setDate(self.start_date_multiple_dateedit.date())

    def change_end_date_multiple(self):
        day = str(self.end_date_multiple_dateedit.date().day())
        mon = str(self.end_date_multiple_dateedit.date().month())
        yea = str(self.end_date_multiple_dateedit.date().year())

        if len(day) < 2: day = '0' + day
        if len(mon) < 2: mon = '0' + mon

        var.end_period = day + '/' + mon + '/' + yea
        self.end_date_singular_dateedit.setDate(self.end_date_multiple_dateedit.date())

    def update_progress_bar(self):
        while var.progress < var.max_progress:
            self.progressBar.setValue(var.progress)
            sleep(0.001)

        self.progressBar.setValue(0)

    def emit_multiple(self):
        progress_thread = threading.Thread(target=self.update_progress_bar, daemon=True)
        progress_thread.start()
        emit_from_source()

        self.speed_label.setText(f"{var.certificates_per_second:.2f} certificados por segundo")
        self.time_label.setText(f"{var.emission_time:.2f} segundos")

    def select_item(self):
        self.cobertura_label.setText(self.coberturas_list.selectedItems()[0].text())

    def emit_singular(self):

        name = self.name_lineedit.text()
        cpf = self.cpf_lineedit.text()
        cnpj = self.cnpj_lineedit.text()
        matr = self.matricula_lineedit.text()
        apol = self.apolice_lineedit.text()
        try:
            cobe = self.coberturas_list.selectedItems()[0].text()
        except (AttributeError, IndexError):
            cobe = ''

        if var.output_dir == '':
            warning = QMessageBox()
            warning.setText('Selecione um diretório.')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

        elif var.apolice and any(char.isalpha() for char in apol):
            warning = QMessageBox()
            warning.setText('Não digite letras na apólice.')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

        elif var.apolice and apol == '':
            warning = QMessageBox()
            warning.setText('Preencha ou desabilite o campo de apólice.')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

        elif any(char.isdigit() for char in name):
            warning = QMessageBox()
            warning.setText('Não digite números no nome.')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

        elif not cpf.isdecimal():
            warning = QMessageBox()
            warning.setText('Digite apenas números no campo CPF')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

        elif not cnpj.isdecimal():
            warning = QMessageBox()
            warning.setText('Digite apenas números no campo CNPJ')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

        elif not matr.isdecimal():
            warning = QMessageBox()
            warning.setText('Digite apenas números no campo Matrícula')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

        elif cobe == '':
            warning = QMessageBox()
            warning.setText('Selecione uma cobertura')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

        elif name == '':
            warning = QMessageBox()
            warning.setText('Preencha o campo de nome.')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

        elif len(cpf) > 11:
            warning = QMessageBox()
            warning.setText('CPF digitado tem mais de 11 dígitos.')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

        elif len(cnpj) > 14:
            warning = QMessageBox()
            warning.setText('CNPJ digitado tem mais de 14 dígitos.')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

        elif len(matr) > 6:
            warning = QMessageBox()
            warning.setText('Matrícula digitada tem mais de 6 dígitos.')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

        else:
            if var.apolice:
                emit_singular(name, cpf, cnpj,  matr, cobe, apol)
            else:
                emit_singular(name, cpf, cnpj, matr, cobe)


            self.success_label.setText(f'arquivo {var.progress} - {nm(name)} emitido com êxito.')
