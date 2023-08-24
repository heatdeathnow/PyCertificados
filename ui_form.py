from PySide6.QtWidgets import (QDateEdit, QFrame, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QListWidget,
                               QProgressBar, QPushButton, QSizePolicy, QTabWidget, QWidget, QMessageBox, QFileDialog,
                               QVBoxLayout, QFormLayout, QSlider, QScrollArea, QPlainTextEdit, QComboBox, QCheckBox)
from PySide6.QtCore import (QCoreApplication, QDate, QMetaObject, QSize, Qt)
from reader import get_coberturas, get_headers, get_cnv_values, push
from PySide6.QtGui import QIcon, QFont, QFontDatabase
from emitter import emit_singular, emit_from_source
from multiprocessing import cpu_count
from threading import active_count
from unidecode import unidecode
from threading import Thread
from neat import name as nm
from neat import cpf as cp
from reader import get_cnv
from time import sleep
from os import listdir
import var


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(780, 540)
        MainWindow.setMinimumSize(QSize(70, 0))
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_console = QLabel(self.centralwidget)
        self.label_console.setObjectName(u"label_console")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_console.sizePolicy().hasHeightForWidth())
        self.label_console.setSizePolicy(sizePolicy)
        self.label_console.setAlignment(Qt.AlignCenter)
        self.label_console.setWordWrap(True)

        self.gridLayout_5.addWidget(self.label_console, 1, 0, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setMinimumSize(QSize(0, 30))
        self.tab_multiple = QWidget()
        self.tab_multiple.setObjectName(u"tab_multiple")
        self.gridLayout = QGridLayout(self.tab_multiple)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_multiple_select = QVBoxLayout()
        self.verticalLayout_multiple_select.setObjectName(u"verticalLayout_multiple_select")
        self.pushButton_multiple_input = QPushButton(self.tab_multiple)
        self.pushButton_multiple_input.setObjectName(u"pushButton_multiple_input")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_multiple_input.sizePolicy().hasHeightForWidth())
        self.pushButton_multiple_input.setSizePolicy(sizePolicy2)
        self.pushButton_multiple_input.setMinimumSize(QSize(0, 40))
        self.pushButton_multiple_input.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout_multiple_select.addWidget(self.pushButton_multiple_input)

        self.label_multiple_input_header = QLabel(self.tab_multiple)
        self.label_multiple_input_header.setObjectName(u"label_multiple_input_header")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_multiple_input_header.sizePolicy().hasHeightForWidth())
        self.label_multiple_input_header.setSizePolicy(sizePolicy3)

        self.verticalLayout_multiple_select.addWidget(self.label_multiple_input_header)

        self.label_multiple_input_text = QLabel(self.tab_multiple)
        self.label_multiple_input_text.setObjectName(u"label_multiple_input_text")
        sizePolicy2.setHeightForWidth(self.label_multiple_input_text.sizePolicy().hasHeightForWidth())
        self.label_multiple_input_text.setSizePolicy(sizePolicy2)

        self.verticalLayout_multiple_select.addWidget(self.label_multiple_input_text)

        self.line_multiple_input_output = QFrame(self.tab_multiple)
        self.line_multiple_input_output.setObjectName(u"line_multiple_input_output")
        self.line_multiple_input_output.setFrameShape(QFrame.HLine)
        self.line_multiple_input_output.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_multiple_select.addWidget(self.line_multiple_input_output)

        self.pushButton_multiple_output = QPushButton(self.tab_multiple)
        self.pushButton_multiple_output.setObjectName(u"pushButton_multiple_output")
        self.pushButton_multiple_output.setMinimumSize(QSize(0, 40))
        self.pushButton_multiple_output.setMaximumSize(QSize(150, 16777215))
        self.pushButton_multiple_output.setAcceptDrops(False)
        self.pushButton_multiple_output.setAutoFillBackground(False)
        self.pushButton_multiple_output.setAutoDefault(False)
        self.pushButton_multiple_output.setFlat(False)

        self.verticalLayout_multiple_select.addWidget(self.pushButton_multiple_output)

        self.label_multiple_output_header = QLabel(self.tab_multiple)
        self.label_multiple_output_header.setObjectName(u"label_multiple_output_header")
        sizePolicy3.setHeightForWidth(self.label_multiple_output_header.sizePolicy().hasHeightForWidth())
        self.label_multiple_output_header.setSizePolicy(sizePolicy3)

        self.verticalLayout_multiple_select.addWidget(self.label_multiple_output_header)

        self.label_multiple_output_text = QLabel(self.tab_multiple)
        self.label_multiple_output_text.setObjectName(u"label_multiple_output_text")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_multiple_output_text.sizePolicy().hasHeightForWidth())
        self.label_multiple_output_text.setSizePolicy(sizePolicy4)

        self.verticalLayout_multiple_select.addWidget(self.label_multiple_output_text)


        self.gridLayout.addLayout(self.verticalLayout_multiple_select, 0, 0, 1, 1)

        self.horizontalLayout_multiple_bar_emit = QHBoxLayout()
        self.horizontalLayout_multiple_bar_emit.setObjectName(u"horizontalLayout_multiple_bar_emit")
        self.progressBar_multiple = QProgressBar(self.tab_multiple)
        self.progressBar_multiple.setObjectName(u"progressBar_multiple")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.progressBar_multiple.sizePolicy().hasHeightForWidth())
        self.progressBar_multiple.setSizePolicy(sizePolicy5)
        self.progressBar_multiple.setValue(0)
        self.progressBar_multiple.setTextVisible(False)
        self.progressBar_multiple.setInvertedAppearance(False)

        self.horizontalLayout_multiple_bar_emit.addWidget(self.progressBar_multiple)

        self.pushButton_multiple_emit = QPushButton(self.tab_multiple)
        self.pushButton_multiple_emit.setObjectName(u"pushButton_multiple_emit")

        self.horizontalLayout_multiple_bar_emit.addWidget(self.pushButton_multiple_emit)


        self.gridLayout.addLayout(self.horizontalLayout_multiple_bar_emit, 2, 0, 1, 2)

        self.verticalLayout_multiple_dates = QVBoxLayout()
        self.verticalLayout_multiple_dates.setObjectName(u"verticalLayout_multiple_dates")
        self.label_multiple_start = QLabel(self.tab_multiple)
        self.label_multiple_start.setObjectName(u"label_multiple_start")
        sizePolicy4.setHeightForWidth(self.label_multiple_start.sizePolicy().hasHeightForWidth())
        self.label_multiple_start.setSizePolicy(sizePolicy4)

        self.verticalLayout_multiple_dates.addWidget(self.label_multiple_start)

        self.dateEdit_multiple_start = QDateEdit(self.tab_multiple)
        self.dateEdit_multiple_start.setObjectName(u"dateEdit_multiple_start")
        sizePolicy2.setHeightForWidth(self.dateEdit_multiple_start.sizePolicy().hasHeightForWidth())
        self.dateEdit_multiple_start.setSizePolicy(sizePolicy2)
        self.dateEdit_multiple_start.setProperty("showGroupSeparator", False)
        self.dateEdit_multiple_start.setMaximumDate(QDate(2030, 12, 31))
        self.dateEdit_multiple_start.setMinimumDate(QDate(2023, 1, 1))
        self.dateEdit_multiple_start.setCalendarPopup(True)
        self.dateEdit_multiple_start.setDate(QDate(2023, 1, 1))

        self.verticalLayout_multiple_dates.addWidget(self.dateEdit_multiple_start)

        self.label_multiple_end = QLabel(self.tab_multiple)
        self.label_multiple_end.setObjectName(u"label_multiple_end")
        sizePolicy4.setHeightForWidth(self.label_multiple_end.sizePolicy().hasHeightForWidth())
        self.label_multiple_end.setSizePolicy(sizePolicy4)

        self.verticalLayout_multiple_dates.addWidget(self.label_multiple_end)

        self.dateEdit_multiple_end = QDateEdit(self.tab_multiple)
        self.dateEdit_multiple_end.setObjectName(u"dateEdit_multiple_end")
        self.dateEdit_multiple_end.setMaximumDate(QDate(2030, 12, 31))
        self.dateEdit_multiple_end.setMinimumDate(QDate(2023, 1, 1))
        self.dateEdit_multiple_end.setCalendarPopup(True)
        self.dateEdit_multiple_end.setDate(QDate(2023, 1, 1))

        self.verticalLayout_multiple_dates.addWidget(self.dateEdit_multiple_end)


        self.gridLayout.addLayout(self.verticalLayout_multiple_dates, 0, 1, 1, 1)

        self.line_multiple_progress = QFrame(self.tab_multiple)
        self.line_multiple_progress.setObjectName(u"line_multiple_progress")
        self.line_multiple_progress.setFrameShadow(QFrame.Sunken)
        self.line_multiple_progress.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line_multiple_progress, 1, 0, 1, 2)

        self.tabWidget.addTab(self.tab_multiple, "")
        self.tab_singular = QWidget()
        self.tab_singular.setObjectName(u"tab_singular")
        self.gridLayout_2 = QGridLayout(self.tab_singular)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.listWidget_singular_cobertura = QListWidget(self.tab_singular)
        self.listWidget_singular_cobertura.setObjectName(u"listWidget_singular_cobertura")

        self.gridLayout_2.addWidget(self.listWidget_singular_cobertura, 2, 0, 2, 1)

        self.pushButton_singular_emit = QPushButton(self.tab_singular)
        self.pushButton_singular_emit.setObjectName(u"pushButton_singular_emit")
        self.pushButton_singular_emit.setMinimumSize(QSize(0, 40))
        self.pushButton_singular_emit.setMaximumSize(QSize(200, 16777215))
        self.pushButton_singular_emit.setAutoRepeat(False)

        self.gridLayout_2.addWidget(self.pushButton_singular_emit, 3, 1, 1, 1)

        self.formLayout_singular_write = QFormLayout()
        self.formLayout_singular_write.setObjectName(u"formLayout_singular_write")
        self.label_singular_name = QLabel(self.tab_singular)
        self.label_singular_name.setObjectName(u"label_singular_name")
        sizePolicy3.setHeightForWidth(self.label_singular_name.sizePolicy().hasHeightForWidth())
        self.label_singular_name.setSizePolicy(sizePolicy3)

        self.formLayout_singular_write.setWidget(0, QFormLayout.LabelRole, self.label_singular_name)

        self.lineEdit_singular_name = QLineEdit(self.tab_singular)
        self.lineEdit_singular_name.setObjectName(u"lineEdit_singular_name")

        self.formLayout_singular_write.setWidget(0, QFormLayout.FieldRole, self.lineEdit_singular_name)

        self.label_singular_cpf = QLabel(self.tab_singular)
        self.label_singular_cpf.setObjectName(u"label_singular_cpf")
        sizePolicy3.setHeightForWidth(self.label_singular_cpf.sizePolicy().hasHeightForWidth())
        self.label_singular_cpf.setSizePolicy(sizePolicy3)

        self.formLayout_singular_write.setWidget(1, QFormLayout.LabelRole, self.label_singular_cpf)

        self.label_singular_matricula = QLabel(self.tab_singular)
        self.label_singular_matricula.setObjectName(u"label_singular_matricula")
        sizePolicy3.setHeightForWidth(self.label_singular_matricula.sizePolicy().hasHeightForWidth())
        self.label_singular_matricula.setSizePolicy(sizePolicy3)

        self.formLayout_singular_write.setWidget(2, QFormLayout.LabelRole, self.label_singular_matricula)

        self.label_singular_cnpj = QLabel(self.tab_singular)
        self.label_singular_cnpj.setObjectName(u"label_singular_cnpj")
        sizePolicy3.setHeightForWidth(self.label_singular_cnpj.sizePolicy().hasHeightForWidth())
        self.label_singular_cnpj.setSizePolicy(sizePolicy3)

        self.formLayout_singular_write.setWidget(4, QFormLayout.LabelRole, self.label_singular_cnpj)

        self.lineEdit_singular_cpf = QLineEdit(self.tab_singular)
        self.lineEdit_singular_cpf.setObjectName(u"lineEdit_singular_cpf")

        self.formLayout_singular_write.setWidget(1, QFormLayout.FieldRole, self.lineEdit_singular_cpf)

        self.lineEdit_singular_matricula = QLineEdit(self.tab_singular)
        self.lineEdit_singular_matricula.setObjectName(u"lineEdit_singular_matricula")

        self.formLayout_singular_write.setWidget(2, QFormLayout.FieldRole, self.lineEdit_singular_matricula)

        self.lineEdit_singular_cnpj = QLineEdit(self.tab_singular)
        self.lineEdit_singular_cnpj.setObjectName(u"lineEdit_singular_cnpj")

        self.formLayout_singular_write.setWidget(4, QFormLayout.FieldRole, self.lineEdit_singular_cnpj)

        self.label_singular_apolice = QLabel(self.tab_singular)
        self.label_singular_apolice.setObjectName(u"label_singular_apolice")
        sizePolicy3.setHeightForWidth(self.label_singular_apolice.sizePolicy().hasHeightForWidth())
        self.label_singular_apolice.setSizePolicy(sizePolicy3)

        self.formLayout_singular_write.setWidget(5, QFormLayout.LabelRole, self.label_singular_apolice)

        self.lineEdit_singular_apolice = QLineEdit(self.tab_singular)
        self.lineEdit_singular_apolice.setObjectName(u"lineEdit_singular_apolice")

        self.formLayout_singular_write.setWidget(5, QFormLayout.FieldRole, self.lineEdit_singular_apolice)

        self.label_singular_client = QLabel(self.tab_singular)
        self.label_singular_client.setObjectName(u"label_singular_client")
        sizePolicy3.setHeightForWidth(self.label_singular_client.sizePolicy().hasHeightForWidth())
        self.label_singular_client.setSizePolicy(sizePolicy3)

        self.formLayout_singular_write.setWidget(3, QFormLayout.LabelRole, self.label_singular_client)

        self.lineEdit_singular_client = QLineEdit(self.tab_singular)
        self.lineEdit_singular_client.setObjectName(u"lineEdit_singular_client")

        self.formLayout_singular_write.setWidget(3, QFormLayout.FieldRole, self.lineEdit_singular_client)

        self.label_singular_startdate = QLabel(self.tab_singular)
        self.label_singular_startdate.setObjectName(u"label_singular_startdate")
        sizePolicy3.setHeightForWidth(self.label_singular_startdate.sizePolicy().hasHeightForWidth())
        self.label_singular_startdate.setSizePolicy(sizePolicy3)

        self.formLayout_singular_write.setWidget(7, QFormLayout.LabelRole, self.label_singular_startdate)

        self.label_singular_enddate = QLabel(self.tab_singular)
        self.label_singular_enddate.setObjectName(u"label_singular_enddate")
        sizePolicy3.setHeightForWidth(self.label_singular_enddate.sizePolicy().hasHeightForWidth())
        self.label_singular_enddate.setSizePolicy(sizePolicy3)

        self.formLayout_singular_write.setWidget(8, QFormLayout.LabelRole, self.label_singular_enddate)

        self.dateEdit_singular_start = QDateEdit(self.tab_singular)
        self.dateEdit_singular_start.setObjectName(u"dateEdit_singular_start")
        self.dateEdit_singular_start.setCalendarPopup(True)

        self.formLayout_singular_write.setWidget(7, QFormLayout.FieldRole, self.dateEdit_singular_start)

        self.dateEdit_singular_end = QDateEdit(self.tab_singular)
        self.dateEdit_singular_end.setObjectName(u"dateEdit_singular_end")
        self.dateEdit_singular_end.setCalendarPopup(True)

        self.formLayout_singular_write.setWidget(8, QFormLayout.FieldRole, self.dateEdit_singular_end)

        self.label_singular_capital = QLabel(self.tab_singular)
        self.label_singular_capital.setObjectName(u"label_singular_capital")
        sizePolicy3.setHeightForWidth(self.label_singular_capital.sizePolicy().hasHeightForWidth())
        self.label_singular_capital.setSizePolicy(sizePolicy3)

        self.formLayout_singular_write.setWidget(6, QFormLayout.LabelRole, self.label_singular_capital)

        self.lineEdit_singular_capital = QLineEdit(self.tab_singular)
        self.lineEdit_singular_capital.setObjectName(u"lineEdit_singular_capital")

        self.formLayout_singular_write.setWidget(6, QFormLayout.FieldRole, self.lineEdit_singular_capital)


        self.gridLayout_2.addLayout(self.formLayout_singular_write, 2, 1, 1, 1)

        self.verticalLayout_singular_output_and_cnv = QVBoxLayout()
        self.verticalLayout_singular_output_and_cnv.setObjectName(u"verticalLayout_singular_output_and_cnv")
        self.horizontalLayout_singular_select_output = QHBoxLayout()
        self.horizontalLayout_singular_select_output.setObjectName(u"horizontalLayout_singular_select_output")
        self.pushButton_singular_select_output = QPushButton(self.tab_singular)
        self.pushButton_singular_select_output.setObjectName(u"pushButton_singular_select_output")

        self.horizontalLayout_singular_select_output.addWidget(self.pushButton_singular_select_output)

        self.label_singular_output_header = QLabel(self.tab_singular)
        self.label_singular_output_header.setObjectName(u"label_singular_output_header")
        sizePolicy3.setHeightForWidth(self.label_singular_output_header.sizePolicy().hasHeightForWidth())
        self.label_singular_output_header.setSizePolicy(sizePolicy3)

        self.horizontalLayout_singular_select_output.addWidget(self.label_singular_output_header)

        self.label_singular_output_text = QLabel(self.tab_singular)
        self.label_singular_output_text.setObjectName(u"label_singular_output_text")
        sizePolicy5.setHeightForWidth(self.label_singular_output_text.sizePolicy().hasHeightForWidth())
        self.label_singular_output_text.setSizePolicy(sizePolicy5)

        self.horizontalLayout_singular_select_output.addWidget(self.label_singular_output_text)


        self.verticalLayout_singular_output_and_cnv.addLayout(self.horizontalLayout_singular_select_output)

        self.horizontalLayout_singular_select_cnv = QHBoxLayout()
        self.horizontalLayout_singular_select_cnv.setObjectName(u"horizontalLayout_singular_select_cnv")
        self.checkBox_singular_allow_cnv = QCheckBox(self.tab_singular)
        self.checkBox_singular_allow_cnv.setObjectName(u"checkBox_singular_allow_cnv")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.checkBox_singular_allow_cnv.sizePolicy().hasHeightForWidth())
        self.checkBox_singular_allow_cnv.setSizePolicy(sizePolicy6)

        self.horizontalLayout_singular_select_cnv.addWidget(self.checkBox_singular_allow_cnv)

        self.comboBox_singular_cnv = QComboBox(self.tab_singular)
        self.comboBox_singular_cnv.setObjectName(u"comboBox_singular_cnv")
        self.comboBox_singular_cnv.setEnabled(False)

        self.horizontalLayout_singular_select_cnv.addWidget(self.comboBox_singular_cnv)


        self.verticalLayout_singular_output_and_cnv.addLayout(self.horizontalLayout_singular_select_cnv)


        self.gridLayout_2.addLayout(self.verticalLayout_singular_output_and_cnv, 0, 0, 1, 2)

        self.tabWidget.addTab(self.tab_singular, "")
        self.tab_config = QWidget()
        self.tab_config.setObjectName(u"tab_config")
        self.verticalLayout = QVBoxLayout(self.tab_config)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(self.tab_config)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(70, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.formLayout = QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName(u"formLayout")
        self.label_config_performance_title = QLabel(self.scrollAreaWidgetContents)
        self.label_config_performance_title.setObjectName(u"label_config_performance_title")
        self.label_config_performance_title.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label_config_performance_title)

        self.label_config_max_threads = QLabel(self.scrollAreaWidgetContents)
        self.label_config_max_threads.setObjectName(u"label_config_max_threads")
        sizePolicy3.setHeightForWidth(self.label_config_max_threads.sizePolicy().hasHeightForWidth())
        self.label_config_max_threads.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_config_max_threads)

        self.horizontalLayout_config_max_threads = QHBoxLayout()
        self.horizontalLayout_config_max_threads.setObjectName(u"horizontalLayout_config_max_threads")
        self.horizontalSlider_config_max_threads = QSlider(self.scrollAreaWidgetContents)
        self.horizontalSlider_config_max_threads.setObjectName(u"horizontalSlider_config_max_threads")
        self.horizontalSlider_config_max_threads.setMinimum(4)
        self.horizontalSlider_config_max_threads.setMaximum(150)
        self.horizontalSlider_config_max_threads.setSingleStep(1)
        self.horizontalSlider_config_max_threads.setValue(150)
        self.horizontalSlider_config_max_threads.setOrientation(Qt.Horizontal)

        self.horizontalLayout_config_max_threads.addWidget(self.horizontalSlider_config_max_threads)

        self.label_config_max_thread_number = QLabel(self.scrollAreaWidgetContents)
        self.label_config_max_thread_number.setObjectName(u"label_config_max_thread_number")
        sizePolicy3.setHeightForWidth(self.label_config_max_thread_number.sizePolicy().hasHeightForWidth())
        self.label_config_max_thread_number.setSizePolicy(sizePolicy3)
        self.label_config_max_thread_number.setMinimumSize(QSize(20, 0))
        self.label_config_max_thread_number.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_config_max_threads.addWidget(self.label_config_max_thread_number)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_config_max_threads)

        self.label_config_target_threads = QLabel(self.scrollAreaWidgetContents)
        self.label_config_target_threads.setObjectName(u"label_config_target_threads")
        sizePolicy3.setHeightForWidth(self.label_config_target_threads.sizePolicy().hasHeightForWidth())
        self.label_config_target_threads.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_config_target_threads)

        self.horizontalLayout_config_target_threads = QHBoxLayout()
        self.horizontalLayout_config_target_threads.setObjectName(u"horizontalLayout_config_target_threads")
        self.horizontalSlider_config_target_threads = QSlider(self.scrollAreaWidgetContents)
        self.horizontalSlider_config_target_threads.setObjectName(u"horizontalSlider_config_target_threads")
        self.horizontalSlider_config_target_threads.setMinimum(4)
        self.horizontalSlider_config_target_threads.setMaximum(150)
        self.horizontalSlider_config_target_threads.setValue(15)
        self.horizontalSlider_config_target_threads.setOrientation(Qt.Horizontal)

        self.horizontalLayout_config_target_threads.addWidget(self.horizontalSlider_config_target_threads)

        self.label_config_target_thread_number = QLabel(self.scrollAreaWidgetContents)
        self.label_config_target_thread_number.setObjectName(u"label_config_target_thread_number")
        sizePolicy3.setHeightForWidth(self.label_config_target_thread_number.sizePolicy().hasHeightForWidth())
        self.label_config_target_thread_number.setSizePolicy(sizePolicy3)
        self.label_config_target_thread_number.setMinimumSize(QSize(20, 0))
        self.label_config_target_thread_number.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_config_target_threads.addWidget(self.label_config_target_thread_number)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_config_target_threads)

        self.label_config_max_processes = QLabel(self.scrollAreaWidgetContents)
        self.label_config_max_processes.setObjectName(u"label_config_max_processes")
        sizePolicy3.setHeightForWidth(self.label_config_max_processes.sizePolicy().hasHeightForWidth())
        self.label_config_max_processes.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_config_max_processes)

        self.horizontalLayout_config_max_processes = QHBoxLayout()
        self.horizontalLayout_config_max_processes.setObjectName(u"horizontalLayout_config_max_processes")
        self.horizontalSlider_config_max_processes = QSlider(self.scrollAreaWidgetContents)
        self.horizontalSlider_config_max_processes.setObjectName(u"horizontalSlider_config_max_processes")
        self.horizontalSlider_config_max_processes.setMinimum(1)
        self.horizontalSlider_config_max_processes.setMaximum(4)
        self.horizontalSlider_config_max_processes.setValue(4)
        self.horizontalSlider_config_max_processes.setOrientation(Qt.Horizontal)

        self.horizontalLayout_config_max_processes.addWidget(self.horizontalSlider_config_max_processes)

        self.label_config_max_processes_number = QLabel(self.scrollAreaWidgetContents)
        self.label_config_max_processes_number.setObjectName(u"label_config_max_processes_number")
        sizePolicy3.setHeightForWidth(self.label_config_max_processes_number.sizePolicy().hasHeightForWidth())
        self.label_config_max_processes_number.setSizePolicy(sizePolicy3)
        self.label_config_max_processes_number.setMinimumSize(QSize(20, 0))
        self.label_config_max_processes_number.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_config_max_processes.addWidget(self.label_config_max_processes_number)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout_config_max_processes)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.line)

        self.label_config_file_option_titles = QLabel(self.scrollAreaWidgetContents)
        self.label_config_file_option_titles.setObjectName(u"label_config_file_option_titles")
        self.label_config_file_option_titles.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.label_config_file_option_titles)

        self.pushButton_config_cobertura_source = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_config_cobertura_source.setObjectName(u"pushButton_config_cobertura_source")
        self.pushButton_config_cobertura_source.setMinimumSize(QSize(0, 30))

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.pushButton_config_cobertura_source)

        self.horizontalLayout_config_cobertura_source = QHBoxLayout()
        self.horizontalLayout_config_cobertura_source.setObjectName(u"horizontalLayout_config_cobertura_source")
        self.label_config_selection_cobertura = QLabel(self.scrollAreaWidgetContents)
        self.label_config_selection_cobertura.setObjectName(u"label_config_selection_cobertura")
        sizePolicy3.setHeightForWidth(self.label_config_selection_cobertura.sizePolicy().hasHeightForWidth())
        self.label_config_selection_cobertura.setSizePolicy(sizePolicy3)

        self.horizontalLayout_config_cobertura_source.addWidget(self.label_config_selection_cobertura)

        self.label_config_cobertura_text = QLabel(self.scrollAreaWidgetContents)
        self.label_config_cobertura_text.setObjectName(u"label_config_cobertura_text")
        sizePolicy5.setHeightForWidth(self.label_config_cobertura_text.sizePolicy().hasHeightForWidth())
        self.label_config_cobertura_text.setSizePolicy(sizePolicy5)

        self.horizontalLayout_config_cobertura_source.addWidget(self.label_config_cobertura_text)


        self.formLayout.setLayout(6, QFormLayout.FieldRole, self.horizontalLayout_config_cobertura_source)

        self.pushButton_config_cnv_source = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_config_cnv_source.setObjectName(u"pushButton_config_cnv_source")
        self.pushButton_config_cnv_source.setMinimumSize(QSize(0, 30))

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.pushButton_config_cnv_source)

        self.horizontalLayout_config_cnv_source = QHBoxLayout()
        self.horizontalLayout_config_cnv_source.setObjectName(u"horizontalLayout_config_cnv_source")
        self.label_config_selection_cnv = QLabel(self.scrollAreaWidgetContents)
        self.label_config_selection_cnv.setObjectName(u"label_config_selection_cnv")
        sizePolicy3.setHeightForWidth(self.label_config_selection_cnv.sizePolicy().hasHeightForWidth())
        self.label_config_selection_cnv.setSizePolicy(sizePolicy3)

        self.horizontalLayout_config_cnv_source.addWidget(self.label_config_selection_cnv)

        self.label_config_cnv_text = QLabel(self.scrollAreaWidgetContents)
        self.label_config_cnv_text.setObjectName(u"label_config_cnv_text")
        sizePolicy5.setHeightForWidth(self.label_config_cnv_text.sizePolicy().hasHeightForWidth())
        self.label_config_cnv_text.setSizePolicy(sizePolicy5)

        self.horizontalLayout_config_cnv_source.addWidget(self.label_config_cnv_text)


        self.formLayout.setLayout(7, QFormLayout.FieldRole, self.horizontalLayout_config_cnv_source)

        self.pushButton_config_change_pdf_template = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_config_change_pdf_template.setObjectName(u"pushButton_config_change_pdf_template")
        self.pushButton_config_change_pdf_template.setMinimumSize(QSize(0, 30))

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.pushButton_config_change_pdf_template)

        self.horizontalLayout_config_pdf_template = QHBoxLayout()
        self.horizontalLayout_config_pdf_template.setObjectName(u"horizontalLayout_config_pdf_template")
        self.label_config_selection_pdf = QLabel(self.scrollAreaWidgetContents)
        self.label_config_selection_pdf.setObjectName(u"label_config_selection_pdf")
        sizePolicy3.setHeightForWidth(self.label_config_selection_pdf.sizePolicy().hasHeightForWidth())
        self.label_config_selection_pdf.setSizePolicy(sizePolicy3)

        self.horizontalLayout_config_pdf_template.addWidget(self.label_config_selection_pdf)

        self.label_config_pdf_text = QLabel(self.scrollAreaWidgetContents)
        self.label_config_pdf_text.setObjectName(u"label_config_pdf_text")
        sizePolicy5.setHeightForWidth(self.label_config_pdf_text.sizePolicy().hasHeightForWidth())
        self.label_config_pdf_text.setSizePolicy(sizePolicy5)

        self.horizontalLayout_config_pdf_template.addWidget(self.label_config_pdf_text)


        self.formLayout.setLayout(8, QFormLayout.FieldRole, self.horizontalLayout_config_pdf_template)

        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(9, QFormLayout.SpanningRole, self.line_2)

        self.label_config_dates_title = QLabel(self.scrollAreaWidgetContents)
        self.label_config_dates_title.setObjectName(u"label_config_dates_title")
        self.label_config_dates_title.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(10, QFormLayout.SpanningRole, self.label_config_dates_title)

        self.label_config_start_date = QLabel(self.scrollAreaWidgetContents)
        self.label_config_start_date.setObjectName(u"label_config_start_date")
        sizePolicy3.setHeightForWidth(self.label_config_start_date.sizePolicy().hasHeightForWidth())
        self.label_config_start_date.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.label_config_start_date)

        self.dateEdit_config_start = QDateEdit(self.scrollAreaWidgetContents)
        self.dateEdit_config_start.setObjectName(u"dateEdit_config_start")
        self.dateEdit_config_start.setMaximumDate(QDate(2030, 12, 31))
        self.dateEdit_config_start.setMinimumDate(QDate(2023, 1, 1))
        self.dateEdit_config_start.setCalendarPopup(True)
        self.dateEdit_config_start.setDate(QDate(2023, 1, 1))

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.dateEdit_config_start)

        self.label_config_end_date = QLabel(self.scrollAreaWidgetContents)
        self.label_config_end_date.setObjectName(u"label_config_end_date")
        sizePolicy3.setHeightForWidth(self.label_config_end_date.sizePolicy().hasHeightForWidth())
        self.label_config_end_date.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.label_config_end_date)

        self.dateEdit_config_end = QDateEdit(self.scrollAreaWidgetContents)
        self.dateEdit_config_end.setObjectName(u"dateEdit_config_end")
        self.dateEdit_config_end.setMaximumDate(QDate(2030, 12, 31))
        self.dateEdit_config_end.setMinimumDate(QDate(2023, 1, 1))
        self.dateEdit_config_end.setCalendarPopup(True)
        self.dateEdit_config_end.setDate(QDate(2023, 1, 1))

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.dateEdit_config_end)

        self.line_3 = QFrame(self.scrollAreaWidgetContents)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(13, QFormLayout.SpanningRole, self.line_3)

        self.label_config_data_input_and_output_title = QLabel(self.scrollAreaWidgetContents)
        self.label_config_data_input_and_output_title.setObjectName(u"label_config_data_input_and_output_title")
        self.label_config_data_input_and_output_title.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(14, QFormLayout.SpanningRole, self.label_config_data_input_and_output_title)

        self.pushButton_config_source = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_config_source.setObjectName(u"pushButton_config_source")
        self.pushButton_config_source.setMinimumSize(QSize(0, 30))

        self.formLayout.setWidget(15, QFormLayout.LabelRole, self.pushButton_config_source)

        self.horizontalLayout_config_data_source = QHBoxLayout()
        self.horizontalLayout_config_data_source.setObjectName(u"horizontalLayout_config_data_source")
        self.label_config_selection_data_source = QLabel(self.scrollAreaWidgetContents)
        self.label_config_selection_data_source.setObjectName(u"label_config_selection_data_source")
        sizePolicy3.setHeightForWidth(self.label_config_selection_data_source.sizePolicy().hasHeightForWidth())
        self.label_config_selection_data_source.setSizePolicy(sizePolicy3)

        self.horizontalLayout_config_data_source.addWidget(self.label_config_selection_data_source)

        self.label_config_source_text = QLabel(self.scrollAreaWidgetContents)
        self.label_config_source_text.setObjectName(u"label_config_source_text")
        sizePolicy5.setHeightForWidth(self.label_config_source_text.sizePolicy().hasHeightForWidth())
        self.label_config_source_text.setSizePolicy(sizePolicy5)

        self.horizontalLayout_config_data_source.addWidget(self.label_config_source_text)


        self.formLayout.setLayout(15, QFormLayout.FieldRole, self.horizontalLayout_config_data_source)

        self.pushButton_config_output_dir = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_config_output_dir.setObjectName(u"pushButton_config_output_dir")
        self.pushButton_config_output_dir.setMinimumSize(QSize(0, 30))

        self.formLayout.setWidget(16, QFormLayout.LabelRole, self.pushButton_config_output_dir)

        self.horizontalLayout_config_default_output_dir = QHBoxLayout()
        self.horizontalLayout_config_default_output_dir.setObjectName(u"horizontalLayout_config_default_output_dir")
        self.label_config_selection_output_dir = QLabel(self.scrollAreaWidgetContents)
        self.label_config_selection_output_dir.setObjectName(u"label_config_selection_output_dir")
        sizePolicy3.setHeightForWidth(self.label_config_selection_output_dir.sizePolicy().hasHeightForWidth())
        self.label_config_selection_output_dir.setSizePolicy(sizePolicy3)

        self.horizontalLayout_config_default_output_dir.addWidget(self.label_config_selection_output_dir)

        self.label_config_output_dir_text = QLabel(self.scrollAreaWidgetContents)
        self.label_config_output_dir_text.setObjectName(u"label_config_output_dir_text")
        sizePolicy5.setHeightForWidth(self.label_config_output_dir_text.sizePolicy().hasHeightForWidth())
        self.label_config_output_dir_text.setSizePolicy(sizePolicy5)

        self.horizontalLayout_config_default_output_dir.addWidget(self.label_config_output_dir_text)


        self.formLayout.setLayout(16, QFormLayout.FieldRole, self.horizontalLayout_config_default_output_dir)

        self.line_4 = QFrame(self.scrollAreaWidgetContents)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(17, QFormLayout.SpanningRole, self.line_4)

        self.label_config_formatting_title = QLabel(self.scrollAreaWidgetContents)
        self.label_config_formatting_title.setObjectName(u"label_config_formatting_title")
        self.label_config_formatting_title.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(18, QFormLayout.SpanningRole, self.label_config_formatting_title)

        self.label_config_text_left = QLabel(self.scrollAreaWidgetContents)
        self.label_config_text_left.setObjectName(u"label_config_text_left")
        sizePolicy3.setHeightForWidth(self.label_config_text_left.sizePolicy().hasHeightForWidth())
        self.label_config_text_left.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(21, QFormLayout.LabelRole, self.label_config_text_left)

        self.horizontalLayout_config_text_left = QHBoxLayout()
        self.horizontalLayout_config_text_left.setObjectName(u"horizontalLayout_config_text_left")
        self.horizontalSlider_config_text_left = QSlider(self.scrollAreaWidgetContents)
        self.horizontalSlider_config_text_left.setObjectName(u"horizontalSlider_config_text_left")
        self.horizontalSlider_config_text_left.setMinimum(1)
        self.horizontalSlider_config_text_left.setMaximum(100)
        self.horizontalSlider_config_text_left.setValue(65)
        self.horizontalSlider_config_text_left.setOrientation(Qt.Horizontal)

        self.horizontalLayout_config_text_left.addWidget(self.horizontalSlider_config_text_left)

        self.label_config_text_left_text = QLabel(self.scrollAreaWidgetContents)
        self.label_config_text_left_text.setObjectName(u"label_config_text_left_text")
        self.label_config_text_left_text.setMinimumSize(QSize(20, 0))
        self.label_config_text_left_text.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_config_text_left.addWidget(self.label_config_text_left_text)


        self.formLayout.setLayout(21, QFormLayout.FieldRole, self.horizontalLayout_config_text_left)

        self.label_config_text_right = QLabel(self.scrollAreaWidgetContents)
        self.label_config_text_right.setObjectName(u"label_config_text_right")
        sizePolicy3.setHeightForWidth(self.label_config_text_right.sizePolicy().hasHeightForWidth())
        self.label_config_text_right.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(22, QFormLayout.LabelRole, self.label_config_text_right)

        self.horizontalLayout_config_text_height = QHBoxLayout()
        self.horizontalLayout_config_text_height.setObjectName(u"horizontalLayout_config_text_height")
        self.horizontalSlider_config_text_height = QSlider(self.scrollAreaWidgetContents)
        self.horizontalSlider_config_text_height.setObjectName(u"horizontalSlider_config_text_height")
        self.horizontalSlider_config_text_height.setMinimum(500)
        self.horizontalSlider_config_text_height.setMaximum(700)
        self.horizontalSlider_config_text_height.setValue(620)
        self.horizontalSlider_config_text_height.setOrientation(Qt.Horizontal)

        self.horizontalLayout_config_text_height.addWidget(self.horizontalSlider_config_text_height)

        self.label_config_text_height_text = QLabel(self.scrollAreaWidgetContents)
        self.label_config_text_height_text.setObjectName(u"label_config_text_height_text")
        self.label_config_text_height_text.setMinimumSize(QSize(20, 0))
        self.label_config_text_height_text.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_config_text_height.addWidget(self.label_config_text_height_text)


        self.formLayout.setLayout(22, QFormLayout.FieldRole, self.horizontalLayout_config_text_height)

        self.label_config_text_space = QLabel(self.scrollAreaWidgetContents)
        self.label_config_text_space.setObjectName(u"label_config_text_space")
        sizePolicy3.setHeightForWidth(self.label_config_text_space.sizePolicy().hasHeightForWidth())
        self.label_config_text_space.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(23, QFormLayout.LabelRole, self.label_config_text_space)

        self.horizontalLayout_config_text_space = QHBoxLayout()
        self.horizontalLayout_config_text_space.setObjectName(u"horizontalLayout_config_text_space")
        self.horizontalSlider_config_text_space = QSlider(self.scrollAreaWidgetContents)
        self.horizontalSlider_config_text_space.setObjectName(u"horizontalSlider_config_text_space")
        self.horizontalSlider_config_text_space.setMinimum(1)
        self.horizontalSlider_config_text_space.setMaximum(50)
        self.horizontalSlider_config_text_space.setValue(15)
        self.horizontalSlider_config_text_space.setOrientation(Qt.Horizontal)

        self.horizontalLayout_config_text_space.addWidget(self.horizontalSlider_config_text_space)

        self.label_config_text_space_text = QLabel(self.scrollAreaWidgetContents)
        self.label_config_text_space_text.setObjectName(u"label_config_text_space_text")
        self.label_config_text_space_text.setMinimumSize(QSize(20, 0))
        self.label_config_text_space_text.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_config_text_space.addWidget(self.label_config_text_space_text)


        self.formLayout.setLayout(23, QFormLayout.FieldRole, self.horizontalLayout_config_text_space)

        self.label_config_text_break = QLabel(self.scrollAreaWidgetContents)
        self.label_config_text_break.setObjectName(u"label_config_text_break")
        sizePolicy3.setHeightForWidth(self.label_config_text_break.sizePolicy().hasHeightForWidth())
        self.label_config_text_break.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(24, QFormLayout.LabelRole, self.label_config_text_break)

        self.horizontalLayout_config_text_break = QHBoxLayout()
        self.horizontalLayout_config_text_break.setObjectName(u"horizontalLayout_config_text_break")
        self.horizontalSlider_config_text_break = QSlider(self.scrollAreaWidgetContents)
        self.horizontalSlider_config_text_break.setObjectName(u"horizontalSlider_config_text_break")
        self.horizontalSlider_config_text_break.setMinimum(1)
        self.horizontalSlider_config_text_break.setMaximum(150)
        self.horizontalSlider_config_text_break.setValue(80)
        self.horizontalSlider_config_text_break.setOrientation(Qt.Horizontal)

        self.horizontalLayout_config_text_break.addWidget(self.horizontalSlider_config_text_break)

        self.label_config_text_break_text = QLabel(self.scrollAreaWidgetContents)
        self.label_config_text_break_text.setObjectName(u"label_config_text_break_text")
        self.label_config_text_break_text.setMinimumSize(QSize(20, 0))
        self.label_config_text_break_text.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_config_text_break.addWidget(self.label_config_text_break_text)


        self.formLayout.setLayout(24, QFormLayout.FieldRole, self.horizontalLayout_config_text_break)

        self.line_5 = QFrame(self.scrollAreaWidgetContents)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(26, QFormLayout.SpanningRole, self.line_5)

        self.label_config_text_editor_title = QLabel(self.scrollAreaWidgetContents)
        self.label_config_text_editor_title.setObjectName(u"label_config_text_editor_title")
        self.label_config_text_editor_title.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(27, QFormLayout.SpanningRole, self.label_config_text_editor_title)

        self.plainTextEdit_config = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit_config.setObjectName(u"plainTextEdit_config")
        self.plainTextEdit_config.setFrameShape(QFrame.StyledPanel)
        self.plainTextEdit_config.setFrameShadow(QFrame.Sunken)
        self.plainTextEdit_config.setOverwriteMode(False)

        self.formLayout.setWidget(28, QFormLayout.SpanningRole, self.plainTextEdit_config)

        self.label_config_text_editor_description = QLabel(self.scrollAreaWidgetContents)
        self.label_config_text_editor_description.setObjectName(u"label_config_text_editor_description")
        self.label_config_text_editor_description.setWordWrap(True)

        self.formLayout.setWidget(29, QFormLayout.SpanningRole, self.label_config_text_editor_description)

        self.line_6 = QFrame(self.scrollAreaWidgetContents)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(30, QFormLayout.SpanningRole, self.line_6)

        self.label_config_keywords_title = QLabel(self.scrollAreaWidgetContents)
        self.label_config_keywords_title.setObjectName(u"label_config_keywords_title")
        self.label_config_keywords_title.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(32, QFormLayout.SpanningRole, self.label_config_keywords_title)

        self.horizontalLayout_config_name = QHBoxLayout()
        self.horizontalLayout_config_name.setObjectName(u"horizontalLayout_config_name")
        self.label_config_name = QLabel(self.scrollAreaWidgetContents)
        self.label_config_name.setObjectName(u"label_config_name")
        sizePolicy3.setHeightForWidth(self.label_config_name.sizePolicy().hasHeightForWidth())
        self.label_config_name.setSizePolicy(sizePolicy3)
        self.label_config_name.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_config_name.addWidget(self.label_config_name)

        self.lineEdit_config_name = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_config_name.setObjectName(u"lineEdit_config_name")
        sizePolicy5.setHeightForWidth(self.lineEdit_config_name.sizePolicy().hasHeightForWidth())
        self.lineEdit_config_name.setSizePolicy(sizePolicy5)
        self.lineEdit_config_name.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_config_name.addWidget(self.lineEdit_config_name)


        self.formLayout.setLayout(33, QFormLayout.SpanningRole, self.horizontalLayout_config_name)

        self.horizontalLayout_config_cpf = QHBoxLayout()
        self.horizontalLayout_config_cpf.setObjectName(u"horizontalLayout_config_cpf")
        self.label_config_cpf = QLabel(self.scrollAreaWidgetContents)
        self.label_config_cpf.setObjectName(u"label_config_cpf")
        sizePolicy3.setHeightForWidth(self.label_config_cpf.sizePolicy().hasHeightForWidth())
        self.label_config_cpf.setSizePolicy(sizePolicy3)
        self.label_config_cpf.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_config_cpf.addWidget(self.label_config_cpf)

        self.lineEdit_config_cpf = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_config_cpf.setObjectName(u"lineEdit_config_cpf")
        sizePolicy5.setHeightForWidth(self.lineEdit_config_cpf.sizePolicy().hasHeightForWidth())
        self.lineEdit_config_cpf.setSizePolicy(sizePolicy5)

        self.horizontalLayout_config_cpf.addWidget(self.lineEdit_config_cpf)


        self.formLayout.setLayout(34, QFormLayout.SpanningRole, self.horizontalLayout_config_cpf)

        self.horizontalLayout_config_cnpj = QHBoxLayout()
        self.horizontalLayout_config_cnpj.setObjectName(u"horizontalLayout_config_cnpj")
        self.label_config_cnpj = QLabel(self.scrollAreaWidgetContents)
        self.label_config_cnpj.setObjectName(u"label_config_cnpj")
        sizePolicy3.setHeightForWidth(self.label_config_cnpj.sizePolicy().hasHeightForWidth())
        self.label_config_cnpj.setSizePolicy(sizePolicy3)
        self.label_config_cnpj.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_config_cnpj.addWidget(self.label_config_cnpj)

        self.lineEdit_config_cnpj = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_config_cnpj.setObjectName(u"lineEdit_config_cnpj")
        sizePolicy5.setHeightForWidth(self.lineEdit_config_cnpj.sizePolicy().hasHeightForWidth())
        self.lineEdit_config_cnpj.setSizePolicy(sizePolicy5)

        self.horizontalLayout_config_cnpj.addWidget(self.lineEdit_config_cnpj)


        self.formLayout.setLayout(35, QFormLayout.SpanningRole, self.horizontalLayout_config_cnpj)

        self.horizontalLayout_config_matricula = QHBoxLayout()
        self.horizontalLayout_config_matricula.setObjectName(u"horizontalLayout_config_matricula")
        self.label_config_matricula = QLabel(self.scrollAreaWidgetContents)
        self.label_config_matricula.setObjectName(u"label_config_matricula")
        sizePolicy3.setHeightForWidth(self.label_config_matricula.sizePolicy().hasHeightForWidth())
        self.label_config_matricula.setSizePolicy(sizePolicy3)
        self.label_config_matricula.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_config_matricula.addWidget(self.label_config_matricula)

        self.lineEdit_config_matricula = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_config_matricula.setObjectName(u"lineEdit_config_matricula")
        sizePolicy5.setHeightForWidth(self.lineEdit_config_matricula.sizePolicy().hasHeightForWidth())
        self.lineEdit_config_matricula.setSizePolicy(sizePolicy5)

        self.horizontalLayout_config_matricula.addWidget(self.lineEdit_config_matricula)


        self.formLayout.setLayout(36, QFormLayout.SpanningRole, self.horizontalLayout_config_matricula)

        self.horizontalLayout_config_cliente = QHBoxLayout()
        self.horizontalLayout_config_cliente.setObjectName(u"horizontalLayout_config_cliente")
        self.label_config_cliente = QLabel(self.scrollAreaWidgetContents)
        self.label_config_cliente.setObjectName(u"label_config_cliente")
        sizePolicy3.setHeightForWidth(self.label_config_cliente.sizePolicy().hasHeightForWidth())
        self.label_config_cliente.setSizePolicy(sizePolicy3)
        self.label_config_cliente.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_config_cliente.addWidget(self.label_config_cliente)

        self.lineEdit_config_cliente = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_config_cliente.setObjectName(u"lineEdit_config_cliente")
        sizePolicy5.setHeightForWidth(self.lineEdit_config_cliente.sizePolicy().hasHeightForWidth())
        self.lineEdit_config_cliente.setSizePolicy(sizePolicy5)

        self.horizontalLayout_config_cliente.addWidget(self.lineEdit_config_cliente)


        self.formLayout.setLayout(37, QFormLayout.SpanningRole, self.horizontalLayout_config_cliente)

        self.horizontalLayout_config_apolice = QHBoxLayout()
        self.horizontalLayout_config_apolice.setObjectName(u"horizontalLayout_config_apolice")
        self.label_config_apolice = QLabel(self.scrollAreaWidgetContents)
        self.label_config_apolice.setObjectName(u"label_config_apolice")
        sizePolicy3.setHeightForWidth(self.label_config_apolice.sizePolicy().hasHeightForWidth())
        self.label_config_apolice.setSizePolicy(sizePolicy3)
        self.label_config_apolice.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_config_apolice.addWidget(self.label_config_apolice)

        self.lineEdit_config_apolice = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_config_apolice.setObjectName(u"lineEdit_config_apolice")
        sizePolicy5.setHeightForWidth(self.lineEdit_config_apolice.sizePolicy().hasHeightForWidth())
        self.lineEdit_config_apolice.setSizePolicy(sizePolicy5)

        self.horizontalLayout_config_apolice.addWidget(self.lineEdit_config_apolice)


        self.formLayout.setLayout(38, QFormLayout.SpanningRole, self.horizontalLayout_config_apolice)

        self.horizontalLayout_config_cobertura = QHBoxLayout()
        self.horizontalLayout_config_cobertura.setObjectName(u"horizontalLayout_config_cobertura")
        self.label_config_cobertura = QLabel(self.scrollAreaWidgetContents)
        self.label_config_cobertura.setObjectName(u"label_config_cobertura")
        sizePolicy3.setHeightForWidth(self.label_config_cobertura.sizePolicy().hasHeightForWidth())
        self.label_config_cobertura.setSizePolicy(sizePolicy3)
        self.label_config_cobertura.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_config_cobertura.addWidget(self.label_config_cobertura)

        self.lineEdit_config_cobertura = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_config_cobertura.setObjectName(u"lineEdit_config_cobertura")
        sizePolicy5.setHeightForWidth(self.lineEdit_config_cobertura.sizePolicy().hasHeightForWidth())
        self.lineEdit_config_cobertura.setSizePolicy(sizePolicy5)

        self.horizontalLayout_config_cobertura.addWidget(self.lineEdit_config_cobertura)


        self.formLayout.setLayout(40, QFormLayout.SpanningRole, self.horizontalLayout_config_cobertura)

        self.horizontalLayout_config_cnv = QHBoxLayout()
        self.horizontalLayout_config_cnv.setObjectName(u"horizontalLayout_config_cnv")
        self.label_config_cnv = QLabel(self.scrollAreaWidgetContents)
        self.label_config_cnv.setObjectName(u"label_config_cnv")
        sizePolicy3.setHeightForWidth(self.label_config_cnv.sizePolicy().hasHeightForWidth())
        self.label_config_cnv.setSizePolicy(sizePolicy3)
        self.label_config_cnv.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_config_cnv.addWidget(self.label_config_cnv)

        self.lineEdit_config_cnv = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_config_cnv.setObjectName(u"lineEdit_config_cnv")
        sizePolicy5.setHeightForWidth(self.lineEdit_config_cnv.sizePolicy().hasHeightForWidth())
        self.lineEdit_config_cnv.setSizePolicy(sizePolicy5)
        self.lineEdit_config_cnv.setMinimumSize(QSize(70, 0))

        self.horizontalLayout_config_cnv.addWidget(self.lineEdit_config_cnv)


        self.formLayout.setLayout(41, QFormLayout.SpanningRole, self.horizontalLayout_config_cnv)

        self.label_config_keywords_description = QLabel(self.scrollAreaWidgetContents)
        self.label_config_keywords_description.setObjectName(u"label_config_keywords_description")
        self.label_config_keywords_description.setWordWrap(True)

        self.formLayout.setWidget(42, QFormLayout.SpanningRole, self.label_config_keywords_description)

        self.horizontalLayout_config_capital = QHBoxLayout()
        self.horizontalLayout_config_capital.setObjectName(u"horizontalLayout_config_capital")
        self.label_config_capital = QLabel(self.scrollAreaWidgetContents)
        self.label_config_capital.setObjectName(u"label_config_capital")
        sizePolicy3.setHeightForWidth(self.label_config_capital.sizePolicy().hasHeightForWidth())
        self.label_config_capital.setSizePolicy(sizePolicy3)
        self.label_config_capital.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_config_capital.addWidget(self.label_config_capital)

        self.lineEdit_config_capital = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_config_capital.setObjectName(u"lineEdit_config_capital")

        self.horizontalLayout_config_capital.addWidget(self.lineEdit_config_capital)


        self.formLayout.setLayout(39, QFormLayout.SpanningRole, self.horizontalLayout_config_capital)

        self.label_config_text_size = QLabel(self.scrollAreaWidgetContents)
        self.label_config_text_size.setObjectName(u"label_config_text_size")
        sizePolicy3.setHeightForWidth(self.label_config_text_size.sizePolicy().hasHeightForWidth())
        self.label_config_text_size.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(20, QFormLayout.LabelRole, self.label_config_text_size)

        self.label_config_font = QLabel(self.scrollAreaWidgetContents)
        self.label_config_font.setObjectName(u"label_config_font")
        sizePolicy3.setHeightForWidth(self.label_config_font.sizePolicy().hasHeightForWidth())
        self.label_config_font.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(19, QFormLayout.LabelRole, self.label_config_font)

        self.horizontalLayout_config_text_size = QHBoxLayout()
        self.horizontalLayout_config_text_size.setObjectName(u"horizontalLayout_config_text_size")
        self.horizontalSlider_config_text_size = QSlider(self.scrollAreaWidgetContents)
        self.horizontalSlider_config_text_size.setObjectName(u"horizontalSlider_config_text_size")
        self.horizontalSlider_config_text_size.setMinimum(6)
        self.horizontalSlider_config_text_size.setMaximum(16)
        self.horizontalSlider_config_text_size.setValue(10)
        self.horizontalSlider_config_text_size.setOrientation(Qt.Horizontal)

        self.horizontalLayout_config_text_size.addWidget(self.horizontalSlider_config_text_size)

        self.label_config_text_size_text = QLabel(self.scrollAreaWidgetContents)
        self.label_config_text_size_text.setObjectName(u"label_config_text_size_text")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_config_text_size_text.sizePolicy().hasHeightForWidth())
        self.label_config_text_size_text.setSizePolicy(sizePolicy7)
        self.label_config_text_size_text.setMinimumSize(QSize(20, 0))
        self.label_config_text_size_text.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_config_text_size.addWidget(self.label_config_text_size_text)


        self.formLayout.setLayout(20, QFormLayout.FieldRole, self.horizontalLayout_config_text_size)

        self.comboBox_config_font = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_config_font.setObjectName(u"comboBox_config_font")

        self.formLayout.setWidget(19, QFormLayout.FieldRole, self.comboBox_config_font)

        self.pushButton_config_load_font = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_config_load_font.setObjectName(u"pushButton_config_load_font")
        self.pushButton_config_load_font.setMinimumSize(QSize(0, 30))
        self.pushButton_config_load_font.setAutoExclusive(False)

        self.formLayout.setWidget(25, QFormLayout.LabelRole, self.pushButton_config_load_font)

        self.verticalLayout_config_load_font = QVBoxLayout()
        self.verticalLayout_config_load_font.setObjectName(u"verticalLayout_config_load_font")
        self.label_config_example_text_text = QLabel(self.scrollAreaWidgetContents)
        self.label_config_example_text_text.setObjectName(u"label_config_example_text_text")

        self.verticalLayout_config_load_font.addWidget(self.label_config_example_text_text)

        self.label_config_example_text = QLabel(self.scrollAreaWidgetContents)
        self.label_config_example_text.setObjectName(u"label_config_example_text")
        self.label_config_example_text.setWordWrap(True)

        self.verticalLayout_config_load_font.addWidget(self.label_config_example_text)


        self.formLayout.setLayout(25, QFormLayout.FieldRole, self.verticalLayout_config_load_font)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.tab_config, "")

        self.gridLayout_5.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        # Coisas adicionadas manualmente, e não pelo PyCreator. --------------------------------------------------------
        self.listWidget_singular_cobertura.addItems(get_coberturas(var.cobertura_dir))
        self.horizontalSlider_config_max_threads.setValue(var.max_threads)
        self.horizontalSlider_config_target_threads.setValue(var.target_threads)
        self.horizontalSlider_config_max_processes.setMaximum(cpu_count())
        self.horizontalSlider_config_max_processes.setValue(var.max_processes)
        self.dateEdit_multiple_start.setDate(var.start_period)
        self.dateEdit_multiple_end.setDate(var.end_period)
        self.dateEdit_singular_start.setDate(var.start_period)
        self.dateEdit_singular_end.setDate(var.end_period)
        self.dateEdit_config_start.setDate(var.start_period)
        self.dateEdit_config_end.setDate(var.end_period)
        self.horizontalSlider_config_text_left.setValue(var.dist_left)
        self.horizontalSlider_config_text_height.setValue(var.text_height)
        self.horizontalSlider_config_text_space.setValue(var.line_space)
        self.horizontalSlider_config_text_break.setValue(var.max_chars)
        self.plainTextEdit_config.setPlainText(var.base_text)
        self.lineEdit_config_name.setText(';'.join(var.name_keywords))
        self.lineEdit_config_cpf.setText(';'.join(var.cpf_keywords))
        self.lineEdit_config_cnpj.setText(';'.join(var.cnpj_keywords))
        self.lineEdit_config_matricula.setText(';'.join(var.matricula_keywords))
        self.lineEdit_config_cliente.setText(';'.join(var.cliente_keywords))
        self.lineEdit_config_apolice.setText(';'.join(var.apolice_keywords))
        self.lineEdit_config_capital.setText(';'.join(var.capital_keywords))
        self.lineEdit_config_cobertura.setText(';'.join(var.cobertura_keywords))
        self.lineEdit_config_cnv.setText(';'.join(var.cnv_keywords))
        self.comboBox_singular_cnv.addItems(get_cnv_values(var.cnv_dir))
        self.comboBox_config_font.addItems([font for font in listdir('dados\\fontes\\')])
        self.horizontalSlider_config_text_size.setValue(var.text_size)
        self.label_config_example_text.setFont(QFont(f"{var.text_font.replace('.ttf', '').replace('.TTF', '').replace('.ttc', '').replace('.TTC', '')}", var.text_size))

        try:
            self.comboBox_config_font.setCurrentIndex(self.comboBox_config_font.findText(var.text_font))
        except ValueError:
            pass

        try:
            MainWindow.setWindowIcon(QIcon('dados\\ícone.ico'))
        except FileNotFoundError:
            print('Arquivo ícone não encontrado.')
        # Fim das coisas adicionadas manualmente. Essas linhas devem estar ACIMA dos connects com os slots. ------------

        self.retranslateUi(MainWindow)
        self.pushButton_multiple_input.clicked.connect(self.select_input_directory)
        self.pushButton_multiple_output.clicked.connect(self.select_output_directory)
        self.dateEdit_multiple_start.dateChanged.connect(self.change_start_date_multiple)
        self.dateEdit_multiple_end.dateChanged.connect(self.change_end_date_multiple)
        self.pushButton_multiple_emit.clicked.connect(self.emit_multiple)
        self.pushButton_singular_select_output.clicked.connect(self.select_output_directory)
        self.dateEdit_singular_start.dateChanged.connect(self.change_start_date_singular)
        self.dateEdit_singular_end.dateChanged.connect(self.change_end_date_singular)
        self.pushButton_singular_emit.clicked.connect(self.emit_singular)
        self.pushButton_config_cobertura_source.clicked.connect(self.change_coberturas_file)
        self.pushButton_config_cnv_source.clicked.connect(self.change_cnv_file)
        self.pushButton_config_change_pdf_template.clicked.connect(self.change_pdf_template)
        self.pushButton_config_source.clicked.connect(self.change_default_data_source)
        self.pushButton_config_output_dir.clicked.connect(self.change_default_output_dir)
        self.horizontalSlider_config_max_threads.valueChanged.connect(self.change_max_threads)
        self.horizontalSlider_config_target_threads.valueChanged.connect(self.change_target_threads)
        self.horizontalSlider_config_max_processes.valueChanged.connect(self.change_max_processes)
        self.dateEdit_config_start.dateChanged.connect(self.change_default_start_date)
        self.dateEdit_config_end.dateChanged.connect(self.change_default_end_date)
        self.horizontalSlider_config_text_left.valueChanged.connect(self.change_left_spacing)
        self.horizontalSlider_config_text_height.valueChanged.connect(self.change_text_height)
        self.horizontalSlider_config_text_space.valueChanged.connect(self.change_line_spacing)
        self.horizontalSlider_config_text_break.valueChanged.connect(self.change_line_breaking)
        self.plainTextEdit_config.textChanged.connect(self.base_text_changed)
        self.lineEdit_config_name.textEdited.connect(self.change_name_keywords)
        self.lineEdit_config_cpf.textEdited.connect(self.change_cpf_keywords)
        self.lineEdit_config_cnpj.textEdited.connect(self.change_cnpj_keywords)
        self.lineEdit_config_matricula.textEdited.connect(self.change_matricula_keywords)
        self.lineEdit_config_cliente.textEdited.connect(self.change_cliente_keywords)
        self.lineEdit_config_apolice.textEdited.connect(self.change_apolice_keywords)
        self.lineEdit_config_cobertura.textEdited.connect(self.change_cobertura_keywords)
        self.checkBox_singular_allow_cnv.toggled.connect(self.listWidget_singular_cobertura.setDisabled)
        self.checkBox_singular_allow_cnv.toggled.connect(self.comboBox_singular_cnv.setEnabled)
        self.lineEdit_config_cnv.textEdited.connect(self.change_cnv_keywords)
        self.lineEdit_config_capital.textEdited.connect(self.change_capital_keywords)
        self.horizontalSlider_config_text_size.valueChanged.connect(self.change_text_size)
        self.comboBox_config_font.currentTextChanged.connect(self.change_text_font)

        self.pushButton_multiple_output.setDefault(False)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_console.setText("")
        self.pushButton_multiple_input.setText(QCoreApplication.translate("MainWindow", u"Selecionar arquivo", None))
        self.label_multiple_input_header.setText(QCoreApplication.translate("MainWindow", u"Arquivo selecionado:", None))
        self.label_multiple_input_text.setText("")
        self.pushButton_multiple_output.setText(QCoreApplication.translate("MainWindow", u"Selecionar diret\u00f3rio\n"
"de destino", None))
        self.label_multiple_output_header.setText(QCoreApplication.translate("MainWindow", u"Diret\u00f3rio de destino selecionado:", None))
        self.label_multiple_output_text.setText("")
        self.pushButton_multiple_emit.setText(QCoreApplication.translate("MainWindow", u"Emitir", None))
        self.label_multiple_start.setText(QCoreApplication.translate("MainWindow", u"In\u00edcio da vig\u00eancia:", None))
        self.label_multiple_end.setText(QCoreApplication.translate("MainWindow", u"Final da vig\u00eancia:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_multiple), QCoreApplication.translate("MainWindow", u"M\u00faltiplos", None))
        self.pushButton_singular_emit.setText(QCoreApplication.translate("MainWindow", u"Emitir", None))
        self.label_singular_name.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.label_singular_cpf.setText(QCoreApplication.translate("MainWindow", u"CPF:", None))
        self.label_singular_matricula.setText(QCoreApplication.translate("MainWindow", u"Matr\u00edcula:", None))
        self.label_singular_cnpj.setText(QCoreApplication.translate("MainWindow", u"CNPJ:", None))
        self.label_singular_apolice.setText(QCoreApplication.translate("MainWindow", u"Ap\u00f3lice:", None))
        self.label_singular_client.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.label_singular_startdate.setText(QCoreApplication.translate("MainWindow", u"In\u00edcio de vig\u00eancia:", None))
        self.label_singular_enddate.setText(QCoreApplication.translate("MainWindow", u"Fim de vig\u00eancia:", None))
        self.label_singular_capital.setText(QCoreApplication.translate("MainWindow", u"Capital:", None))
        self.pushButton_singular_select_output.setText(QCoreApplication.translate("MainWindow", u"Selecionar diret\u00f3rio de destino", None))
        self.label_singular_output_header.setText(QCoreApplication.translate("MainWindow", u"Diret\u00f3rio selecionado:", None))
        self.label_singular_output_text.setText("")
        self.checkBox_singular_allow_cnv.setText(QCoreApplication.translate("MainWindow", u"Usar CNV", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_singular), QCoreApplication.translate("MainWindow", u"Individual", None))
        self.label_config_performance_title.setText(QCoreApplication.translate("MainWindow", u"Performance - threading e multiprocessamento", None))
        self.label_config_max_threads.setText(QCoreApplication.translate("MainWindow", u"Quantidade m\u00e1xima de threads:", None))
        self.label_config_max_thread_number.setText(QCoreApplication.translate("MainWindow", u"150", None))
        self.label_config_target_threads.setText(QCoreApplication.translate("MainWindow", u"Quantidade alvo de threads:", None))
        self.label_config_target_thread_number.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.label_config_max_processes.setText(QCoreApplication.translate("MainWindow", u"Quantiade m\u00e1xima de processos:", None))
        self.label_config_max_processes_number.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_config_file_option_titles.setText(QCoreApplication.translate("MainWindow", u"Op\u00e7\u00f5es de arquivos", None))
        self.pushButton_config_cobertura_source.setText(QCoreApplication.translate("MainWindow", u"Trocar arquivo de corberturas", None))
        self.label_config_selection_cobertura.setText(QCoreApplication.translate("MainWindow", u"Sele\u00e7\u00e3o:", None))
        self.label_config_cobertura_text.setText("")
        self.pushButton_config_cnv_source.setText(QCoreApplication.translate("MainWindow", u"Trocar arquivo de c\u00f3digos CNV", None))
        self.label_config_selection_cnv.setText(QCoreApplication.translate("MainWindow", u"Sele\u00e7\u00e3o:", None))
        self.label_config_cnv_text.setText("")
        self.pushButton_config_change_pdf_template.setText(QCoreApplication.translate("MainWindow", u"Trocar PDF modelo", None))
        self.label_config_selection_pdf.setText(QCoreApplication.translate("MainWindow", u"Sele\u00e7\u00e3o:", None))
        self.label_config_pdf_text.setText("")
        self.label_config_dates_title.setText(QCoreApplication.translate("MainWindow", u"Datas de vig\u00eancia", None))
        self.label_config_start_date.setText(QCoreApplication.translate("MainWindow", u"Data de vig\u00eancia inicial padr\u00e3o:", None))
        self.label_config_end_date.setText(QCoreApplication.translate("MainWindow", u"Data de vig\u00eancia final padr\u00e3o", None))
        self.label_config_data_input_and_output_title.setText(QCoreApplication.translate("MainWindow", u"Entrada e sa\u00edda de dados", None))
        self.pushButton_config_source.setText(QCoreApplication.translate("MainWindow", u"Trocar fonte de dados padr\u00e3o", None))
        self.label_config_selection_data_source.setText(QCoreApplication.translate("MainWindow", u"Sele\u00e7\u00e3o:", None))
        self.label_config_source_text.setText("")
        self.pushButton_config_output_dir.setText(QCoreApplication.translate("MainWindow", u"Diret\u00f3rio padr\u00e3o de salvamento", None))
        self.label_config_selection_output_dir.setText(QCoreApplication.translate("MainWindow", u"Sele\u00e7\u00e3o:", None))
        self.label_config_output_dir_text.setText("")
        self.label_config_formatting_title.setText(QCoreApplication.translate("MainWindow", u"Formata\u00e7\u00e3o de texto", None))
        self.label_config_text_left.setText(QCoreApplication.translate("MainWindow", u"Dist\u00e2ncia do texto \u00e0 esquerda:", None))
        self.label_config_text_left_text.setText(QCoreApplication.translate("MainWindow", u"65", None))
        self.label_config_text_right.setText(QCoreApplication.translate("MainWindow", u"Altura inicial do texto:", None))
        self.label_config_text_height_text.setText(QCoreApplication.translate("MainWindow", u"620", None))
        self.label_config_text_space.setText(QCoreApplication.translate("MainWindow", u"Espa\u00e7amento entre linhas:", None))
        self.label_config_text_space_text.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.label_config_text_break.setText(QCoreApplication.translate("MainWindow", u"Caracteres ante quebra de linha:", None))
        self.label_config_text_break_text.setText(QCoreApplication.translate("MainWindow", u"80", None))
        self.label_config_text_editor_title.setText(QCoreApplication.translate("MainWindow", u"Editor de texto do PDF", None))
        self.label_config_text_editor_description.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Use os formato &lt;NOME&gt;, &lt;CPF&gt;, &lt;MATRICULA&gt;, &lt;CLIENTE&gt;, &lt;CNPJ&gt;, &lt;APOLICE&gt;, &lt;COBERTURA&gt;, &lt;COMECO&gt; e &lt;FINAL&gt; para os respectivos campos din\u00e2micos. N\u00e3o digite os campos din\u00e2micos com acentos, ou eles n\u00e3o ser\u00e3o interpretados corretamente pelo programa. Al\u00e9m das quebras de linhas manuais o programa divide as linhas automaticamente caso estejam muito grandes.</p></body></html>", None))
        self.label_config_keywords_title.setText(QCoreApplication.translate("MainWindow", u"Palavras-chave", None))
        self.label_config_name.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.label_config_cpf.setText(QCoreApplication.translate("MainWindow", u"CPF:", None))
        self.label_config_cnpj.setText(QCoreApplication.translate("MainWindow", u"CNPJ:", None))
        self.label_config_matricula.setText(QCoreApplication.translate("MainWindow", u"Matr\u00edcula:", None))
        self.label_config_cliente.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.label_config_apolice.setText(QCoreApplication.translate("MainWindow", u"Ap\u00f3lice:", None))
        self.label_config_cobertura.setText(QCoreApplication.translate("MainWindow", u"Cobertura:", None))
        self.label_config_cnv.setText(QCoreApplication.translate("MainWindow", u"CNV:", None))
        self.label_config_keywords_description.setText(QCoreApplication.translate("MainWindow", u"Estas s\u00e3o palavras-chaves que o programa procurar\u00e1 na primeira linha das planilhas numa tentativa de encontrar as colunas dos campos repectivos. Letras mai\u00fasculas e acentos ser\u00e3o desconsiderados. Separe cada palavra-chave com um ponto e v\u00edrgula ( ; ). Uma planilha n\u00e3o precisa ter simultaneamente uma coluna para cobertura e para CNV, apenas um \u00e9 necess\u00e1rio. Ademais, se o programa n\u00e3o encontrar todas as colunas necess\u00e1rias, ele lhe perguntar\u00e1 se deve prosseguir ou abortar.", None))
        self.label_config_capital.setText(QCoreApplication.translate("MainWindow", u"Capital:", None))
        self.label_config_text_size.setText(QCoreApplication.translate("MainWindow", u"Tamanho do texto:", None))
        self.label_config_font.setText(QCoreApplication.translate("MainWindow", u"Fonte:", None))
        self.label_config_text_size_text.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.pushButton_config_load_font.setText(QCoreApplication.translate("MainWindow", u"Carregar nova fonte", None))
        self.label_config_example_text_text.setText(QCoreApplication.translate("MainWindow", u"Texto exemplo para fonte selecionada:", None))
        self.label_config_example_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla at risus. Quisque purus magna, auctor et, sagittis ac, posuere eu, lectus. Nam mattis, felis ut adipiscing. 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_config), QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))

        # Coisas adicionadas manualmente. ------------------------------------------------------------------------------
        self.label_multiple_input_text.setText(var.data_dir)
        self.label_multiple_output_text.setText(var.output_dir)
        self.label_singular_output_text.setText(var.output_dir)

        self.label_config_target_thread_number.setText(
            QCoreApplication.translate("MainWindow", f"{var.target_threads}", None))
        self.label_config_max_processes_number.setText(
            QCoreApplication.translate("MainWindow", f"{var.max_processes}", None))
        self.label_config_max_thread_number.setText(
            QCoreApplication.translate("MainWindow", f"{var.max_threads}", None))

        self.label_config_text_left_text.setText(QCoreApplication.translate("MainWindow", f"{var.dist_left}", None))
        self.label_config_text_height_text.setText(QCoreApplication.translate("MainWindow", f"{var.text_height}", None))
        self.label_config_text_space_text.setText(QCoreApplication.translate("MainWindow", f"{var.line_space}", None))
        self.label_config_text_break_text.setText(QCoreApplication.translate("MainWindow", f"{var.max_chars}", None))
        self.label_config_text_size_text.setText(QCoreApplication.translate("MainWindow", f"{var.text_size}", None))

        self.label_config_source_text.setText(var.data_dir)
        self.label_config_output_dir_text.setText(var.output_dir)
        self.label_config_cobertura_text.setText(var.cobertura_dir)
        self.label_config_cnv_text.setText(var.cnv_dir)
        self.label_config_pdf_text.setText(var.template_dir)

    # retranslateUi
    def select_input_directory(self):
        file = QFileDialog.getOpenFileName()[0]

        if file[-4:].lower() in ('xlsx', '.xls', '.csv',
                                 'xlsm'):  # Serve para encurtar o diretório e para não trocar o diretório quando nada é selecionado.
            var.data_dir = file.replace(var.work_directory, '')
            self.label_multiple_input_text.setText(var.data_dir)

            self.label_console.setText('Diretório de entrada atualizado com sucesso.')
        else:
            self.label_console.setText('Falha ao atualizar o diretório de entrada.')

            warning = QMessageBox()
            warning.setText('Selecione apenas planilhas.')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

    def select_output_directory(self):
        dire = QFileDialog.getExistingDirectory() + '/'

        if dire != '/':
            var.output_dir = dire.replace(var.work_directory, '')
            self.label_multiple_output_text.setText(var.output_dir)
            self.label_singular_output_text.setText(var.output_dir)

            self.label_console.setText('Diretório de saída atualizado com sucesso.')

        else:
            self.label_console.setText('Falha ao atualizar o diretório de saída')

    def change_start_date_multiple(self):
        var.start_period = self.dateEdit_multiple_start.date().toPython()
        self.dateEdit_singular_start.setDate(self.dateEdit_multiple_start.date())

        if self.dateEdit_multiple_start.date() > self.dateEdit_multiple_end.date():  # Se trocar a data inicial para depois da data final, troque a final também.
            self.dateEdit_multiple_end.setDate(self.dateEdit_multiple_start.date())
            self.change_end_date_multiple()

        self.label_console.setText(
            f'Data de vigência inicial atualizada para {var.start_period.day:02}/{var.start_period.month:02}/{var.start_period.year}.')

    def change_end_date_multiple(self):
        var.end_period = self.dateEdit_multiple_end.date().toPython()
        self.dateEdit_singular_end.setDate(self.dateEdit_multiple_end.date())

        if self.dateEdit_multiple_end.date() < self.dateEdit_multiple_start.date():  # Se trocar a data final para antes da data inicial, troque a inicial também.
            self.dateEdit_multiple_start.setDate(self.dateEdit_multiple_end.date())
            self.change_start_date_multiple()

        self.label_console.setText(
            f'Data de vigência final atualizada para {var.end_period.day:02}/{var.end_period.month:02}/{var.end_period.year}.')

    def change_start_date_singular(self):
        var.start_period = self.dateEdit_singular_start.date().toPython()
        self.dateEdit_multiple_start.setDate(self.dateEdit_singular_start.date())

        if self.dateEdit_singular_start.date() > self.dateEdit_singular_end.date():  # Se trocar a data inicial para depois da data final, troque a final também.
            self.dateEdit_singular_end.setDate(self.dateEdit_singular_start.date())
            self.change_end_date_singular()

        self.label_console.setText(
            f'Data de vigência inicial atualizada para {var.start_period.day:02}/{var.start_period.month:02}/{var.start_period.year}.')

    def change_end_date_singular(self):
        var.end_period = self.dateEdit_singular_end.date().toPython()
        self.dateEdit_multiple_end.setDate(self.dateEdit_singular_end.date())

        if self.dateEdit_singular_end.date() < self.dateEdit_singular_start.date():  # Se trocar a data final para antes da data inicial, troque a inicial também.
            self.dateEdit_singular_start.setDate(self.dateEdit_singular_end.date())
            self.change_start_date_singular()

        self.label_console.setText(
            f'Data de vigência final atualizada para {var.end_period.day:02}/{var.end_period.month:02}/{var.end_period.year}.')

    def update_progress_bar(self):
        sleep(0.001)

        while active_count() > 2:  # Quando só sobre a thread da janela e a thread da barra de progresso
            try:
                self.progressBar_multiple.setValue(100 * var.progress / var.max_progress)
            except ZeroDivisionError:
                self.progressBar_multiple.setValue(100)
            sleep(0.001)

        self.label_console.setText(
            f'Tempo para emitir {var.max_progress} certificados: {var.emission_time / 60:.2f} minutos | Velocidade: {var.certificates_per_second:.2f} certificados por segundo')
        var.max_progress = 1
        var.certificates_per_second = 0
        var.emission_time = 0

        self.progressBar_multiple.setValue(0)
        self.pushButton_multiple_emit.setEnabled(True)
        self.pushButton_singular_emit.setEnabled(True)

    def emit_multiple(self):
        var.headers = get_headers(var.data_dir)

        if var.data_dir == '':
            warning = QMessageBox()
            warning.setText('Nenhuma planilha selecionada para a emissão.')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()
            var.abort_emission = True

        if var.headers['name'] == '' and not var.abort_emission and not any(var.name_keywords):
            warning = QMessageBox()
            warning.setWindowTitle('AVISO')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Abort)
            warning.setText('Campo "nome" não foi encontrado na planilha\n'
                            'Clique ok para continuar sem ele\n'
                            'Clique abort para abortar a emissão.')

            if warning.exec() == QMessageBox.StandardButton.Abort:
                var.abort_emission = True

        if var.headers['cpf'] == '' and not var.abort_emission and not any(var.cpf_keywords):
            warning = QMessageBox()
            warning.setWindowTitle('AVISO')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Abort)
            warning.setText('Campo "cpf" não foi encontrado na planilha\n'
                            'Clique ok para continuar sem ele\n'
                            'Clique abort para abortar a emissão.')

            if warning.exec() == QMessageBox.StandardButton.Abort:
                var.abort_emission = True

        if var.headers['cnpj'] == '' and not var.abort_emission and not any(var.cnpj_keywords):
            warning = QMessageBox()
            warning.setWindowTitle('AVISO')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Abort)
            warning.setText('Campo "cnpj" não foi encontrado na planilha\n'
                            'Clique ok para continuar sem ele\n'
                            'Clique abort para abortar a emissão.')

            if warning.exec() == QMessageBox.StandardButton.Abort:
                var.abort_emission = True

        if var.headers['clie'] == '' and not var.abort_emission and not any(var.cliente_keywords):
            warning = QMessageBox()
            warning.setWindowTitle('AVISO')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Abort)
            warning.setText('Campo "cliente" não foi encontrado na planilha\n'
                            'Clique ok para continuar sem ele\n'
                            'Clique abort para abortar a emissão.')

            if warning.exec() == QMessageBox.StandardButton.Abort:
                var.abort_emission = True

        if var.headers['matr'] == '' and not var.abort_emission and not any(var.matricula_keywords):
            warning = QMessageBox()
            warning.setWindowTitle('AVISO')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Abort)
            warning.setText('Campo "matricula" não foi encontrado na planilha\n'
                            'Clique ok para continuar sem ele\n'
                            'Clique abort para abortar a emissão.')

            if warning.exec() == QMessageBox.StandardButton.Abort:
                var.abort_emission = True

        if var.headers['cobe'] == '' and not any(var.cobertura_keywords) and var.headers['cnv'] == '' and not any(
                var.cnv_keywords) and not var.abort_emission:
            warning = QMessageBox()
            warning.setWindowTitle('AVISO')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Abort)
            warning.setText('Campos "cobertura" ou "cnv" não foram encontrados na planilha\n'
                            'Clique ok para continuar sem ele\n'
                            'Clique abort para abortar a emissão.')

            if warning.exec() == QMessageBox.StandardButton.Abort:
                var.abort_emission = True

        if var.headers['apol'] == '' and not var.abort_emission and not any(var.apolice_keywords):
            warning = QMessageBox()
            warning.setWindowTitle('AVISO')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Abort)
            warning.setText('Campo "apolice" não foi encontrado na planilha\n'
                            'Clique ok para continuar sem ele\n'
                            'Clique abort para abortar a emissão.')

            if warning.exec() == QMessageBox.StandardButton.Abort:
                var.abort_emission = True

        # Depois de tudo o boilerplate impedindo de carregar um diretório vazio ou pedindo confirmação para colunas ausentes...
        if not var.abort_emission:
            self.pushButton_multiple_emit.setEnabled(False)
            self.pushButton_singular_emit.setEnabled(False)

            progress_thread = Thread(target=self.update_progress_bar, daemon=True)
            emission_thread = Thread(target=emit_from_source)

            progress_thread.start()
            emission_thread.start()

    def select_item(self):
        self.label_console.setText(self.listWidget_singular_cobertura.selectedItems()[0].text())

    def emit_singular(self):
        cnv_df = get_cnv(var.cnv_dir)

        if self.comboBox_singular_cnv.isEnabled():
            cnv = self.comboBox_singular_cnv.currentText()
            cobe = False

        else:
            try:
                cobe = self.listWidget_singular_cobertura.selectedItems()[0].text()
            except (AttributeError, IndexError):
                cobe = ''

            cnv = False

        name = self.lineEdit_singular_name.text()
        cpf  = self.lineEdit_singular_cpf.text()
        cnpj = self.lineEdit_singular_cnpj.text()
        clie = self.lineEdit_singular_client.text()
        matr = self.lineEdit_singular_matricula.text()
        apol = self.lineEdit_singular_apolice.text()
        capi = self.lineEdit_singular_capital.text()

        if var.output_dir == '':
            warning = QMessageBox()
            warning.setText('Selecione um diretório.')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

        elif apol == '' and '<APOLICE>' in var.base_text:
            warning = QMessageBox()
            warning.setText('Preencha o campo apólice.')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

        elif name == '' and '<NOME>' in var.base_text:
            warning = QMessageBox()
            warning.setText('Preencha o campo nome.')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

        elif any(char.isdigit() for char in name) and '<NOME>' in var.base_text:
            warning = QMessageBox()
            warning.setText('Não digite números no nome.')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

        elif cpf == '' and '<CPF>' in var.base_text:
            warning = QMessageBox()
            warning.setText('Preencha o campo cpf.')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

        elif not cpf.isdecimal() and '<CPF>' in var.base_text:
            warning = QMessageBox()
            warning.setText('Digite apenas números no campo CPF')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

        elif cnpj == '' and '<CNPJ>' in var.base_text:
            warning = QMessageBox()
            warning.setText('Preencha o campo cnpj.')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

        elif not cnpj.isdecimal() and '<CNPJ>' in var.base_text:
            warning = QMessageBox()
            warning.setText('Digite apenas números no campo CNPJ')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

        elif matr == '' and '<MATRICULA>' in var.base_text:
            warning = QMessageBox()
            warning.setText('Preencha o campo matrícula.')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

        elif cobe == '' and '<COBERTURA>' in var.base_text:
            warning = QMessageBox()
            warning.setText('Selecione uma cobertura')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

        elif clie == '' and '<CLIENTE>' in var.base_text:
            warning = QMessageBox()
            warning.setText('Preencha o campo cliente')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

        elif len(cpf) > 11 and '<CPF>' in var.base_text:
            warning = QMessageBox()
            warning.setText('CPF digitado tem mais de 11 dígitos.')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

        elif len(cnpj) > 14 and '<CNPJ>' in var.base_text:
            warning = QMessageBox()
            warning.setText('CNPJ digitado tem mais de 14 dígitos.')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

        else:
            if cnv is False:
                emit_singular(name, cpf, cnpj, matr, clie, apol, capi, cobe, '')
            else:
                emit_singular(name, cpf, cnpj, matr, clie, apol, capi, '', cnv_df.loc[cnv])

            self.label_console.setText(f'arquivo {cp(cpf)} - {nm(name)} emitido com êxito.')
            var.progress = 0

    def change_coberturas_file(self):
        file = QFileDialog.getOpenFileName()[0]

        if file[-4:].lower() in ('xlsx', '.xls', '.csv', 'xlsm'):
            var.cobertura_dir = file.replace(var.work_directory, '')
            push('cobertura_dir', var.cobertura_dir)

            self.listWidget_singular_cobertura.clear()
            self.listWidget_singular_cobertura.addItems(get_coberturas(var.cobertura_dir))
            self.label_config_cobertura_text.setText(var.cobertura_dir)
            self.label_console.setText('Arquivo de coberturas atualizado.')

        else:
            warning = QMessageBox()
            warning.setText('Extensão de arquivo não permitida')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

    def change_cnv_file(self):
        file = QFileDialog.getOpenFileName()[0]

        if file[-4:].lower() in ('xlsx', '.xls', '.csv', 'xlsm'):
            var.cnv_dir = file.replace(var.work_directory, '')
            push('cnv_dir', var.cnv_dir)

            self.label_config_cnv_text.setText(var.cnv_dir)
            self.label_console.setText('Arquivo com códigos CNV atualizado.')

        else:
            warning = QMessageBox()
            warning.setText('Extensão de arquivo não permitida')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

    def change_pdf_template(self):
        file = QFileDialog.getOpenFileName()[0]

        if file[-4:].lower() == '.pdf':
            var.template_dir = file.replace(var.work_directory, '')
            push('template_dir', var.template_dir)
            var.template_obj = var.get_pdf_template()

            self.label_config_pdf_text.setText(var.template_dir)
            self.label_console.setText('Arquivo modelo PDF trocado.')

        else:
            warning = QMessageBox()
            warning.setText('Apenas arquivos PDFs são permitidos')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

    def change_default_data_source(self):
        file = QFileDialog.getOpenFileName()[0]
        if file[-4:].lower() in ('xlsx', '.xls', '.csv', 'xlsm'):
            var.data_dir = file.replace(var.work_directory, '')
            push('data_dir', var.data_dir)

            self.label_multiple_input_text.setText(var.data_dir)
            self.label_config_source_text.setText(var.data_dir)

            self.label_console.setText('Diretório de entrada padrão atualizado.')

        else:
            warning = QMessageBox()
            warning.setText('Extensão de arquivo não permitida')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

    def change_default_output_dir(self):
        dire = QFileDialog.getExistingDirectory() + '/'

        if dire != '/':
            var.output_dir = dire.replace(var.work_directory, '')
            push('output_dir', var.output_dir)

            self.label_multiple_output_text.setText(var.output_dir)
            self.label_singular_output_text.setText(var.output_dir)
            self.label_config_output_dir_text.setText(var.output_dir)
            self.label_console.setText('Diretório de saída padrão atualizado.')

        else:
            warning = QMessageBox()
            warning.setText('Nenhum diretório selecionado.')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

    def change_max_threads(self):
        if self.horizontalSlider_config_max_threads.value() < self.horizontalSlider_config_target_threads.value():
            self.label_config_max_thread_number.setNum(self.horizontalSlider_config_max_threads.value())
            self.label_config_target_thread_number.setNum(self.horizontalSlider_config_max_threads.value())
            self.horizontalSlider_config_target_threads.setValue(self.horizontalSlider_config_max_threads.value())

            var.max_threads = self.horizontalSlider_config_max_threads.value()
            var.target_threads = var.max_threads
            push('max_threads', var.max_threads)
            push('target_threads', var.target_threads)

        else:
            self.label_config_max_thread_number.setNum(self.horizontalSlider_config_max_threads.value())

            var.max_threads = self.horizontalSlider_config_max_threads.value()
            push('max_threads', var.max_threads)

        self.label_console.setText('Número máximo de threads permitidas atualizado.')

    def change_target_threads(self):
        if self.horizontalSlider_config_target_threads.value() > self.horizontalSlider_config_max_threads.value():
            self.label_config_max_thread_number.setNum(self.horizontalSlider_config_target_threads.value())
            self.label_config_target_thread_number.setNum(self.horizontalSlider_config_target_threads.value())
            self.horizontalSlider_config_max_threads.setValue(self.horizontalSlider_config_target_threads.value())

            var.target_threads = self.horizontalSlider_config_target_threads.value()
            var.max_threads = var.target_threads
            push('max_threads', var.target_threads)
            push('target_threads', var.target_threads)

        else:
            self.label_config_target_thread_number.setNum(self.horizontalSlider_config_target_threads.value())

            var.target_threads = self.horizontalSlider_config_target_threads.value()
            push('target_threads', var.target_threads)

        self.label_console.setText('Número alvo de threads atualizado.')

    def change_max_processes(self):
        self.label_config_max_processes_number.setNum(self.horizontalSlider_config_max_processes.value())

        var.max_processes = self.horizontalSlider_config_max_processes.value()
        push('max_processes', var.max_processes)

        self.label_console.setText('Número máximo de processos permitidos atualizado.')

    def change_default_start_date(self):
        var.start_period = self.dateEdit_config_start.date().toPython()
        push('start_period', var.start_period)

        self.label_console.setText('Data de vigência inicial padrão atualizada.')

    def change_default_end_date(self):
        var.end_period = self.dateEdit_config_end.date().toPython()
        push('end_period', var.end_period)

        self.label_console.setText('Data de vigência final padrão atualizada.')

    def change_text_font(self):
        var.text_font = self.comboBox_config_font.currentText()
        QFontDatabase.addApplicationFont(var.text_font)
        self.label_config_example_text.setFont(QFont(
            f"{var.text_font.replace('.ttf', '').replace('.TTF', '').replace('.ttc', '').replace('.TTC', '')}", var.text_size))

        push('text_font', var.text_font)
        self.label_console.setText('Fonte atualizada.')

    def change_text_size(self):
        self.label_config_text_size_text.setNum(self.horizontalSlider_config_text_size.value())

        var.text_size = self.horizontalSlider_config_text_size.value()
        self.label_config_example_text.setFont(QFont('Arial', var.text_size))
        push('text_size', var.text_size)

        self.label_console.setText('Tamanho do texto atualizado.')

    def change_left_spacing(self):
        self.label_config_text_left_text.setNum(self.horizontalSlider_config_text_left.value())

        var.dist_left = self.horizontalSlider_config_text_left.value()
        push('dist_left', var.dist_left)

        self.label_console.setText('Distância do texto à esquerda atualizada.')

    def change_text_height(self):
        self.label_config_text_height_text.setNum(self.horizontalSlider_config_text_height.value())

        var.text_height = self.horizontalSlider_config_text_height.value()
        push('text_height', var.text_height)

        self.label_console.setText('Altura do texto atualizada.')

    def change_line_spacing(self):
        self.label_config_text_space_text.setNum(self.horizontalSlider_config_text_space.value())

        var.line_space = self.horizontalSlider_config_text_space.value()
        push('line_space', var.line_space)

        self.label_console.setText('Espaçamento entre as linhas atualizado.')

    def change_line_breaking(self):
        self.label_config_text_break_text.setNum(self.horizontalSlider_config_text_break.value())

        var.max_chars = self.horizontalSlider_config_text_break.value()
        push('max_chars', var.max_chars)

        self.label_console.setText('Número de caracteres até a quebra de texto atualizado.')

    def base_text_changed(self):
        var.base_text = self.plainTextEdit_config.toPlainText()
        push('base_text', var.base_text)

        self.label_console.setText('Texto base atualizado.')

    def change_name_keywords(self):
        keywords = []
        for i in self.lineEdit_config_name.text().split(';'):
            keywords.append(unidecode(i.strip().lower()))  # Salva em minúsculo e sem acentos.

        var.name_keywords = keywords
        push('name_keywords', keywords)

        self.label_console.setText('Palavras-chave para nome atualizadas.')

    def change_cpf_keywords(self):
        keywords = []
        for i in self.lineEdit_config_cpf.text().split(';'):
            keywords.append(unidecode(i.strip().lower()))

        var.cpf_keywords = keywords
        push('cpf_keywords', keywords)

        self.label_console.setText('Palavras-chave para CPF.')

    def change_cnpj_keywords(self):
        keywords = []
        for i in self.lineEdit_config_cnpj.text().split(';'):
            keywords.append(unidecode(i.strip().lower()))

        var.cnpj_keywords = keywords
        push('cnpj_keywords', keywords)

        self.label_console.setText('Palavras-chave para CNPJ atualizadas.')

    def change_matricula_keywords(self):
        keywords = []
        for i in self.lineEdit_config_matricula.text().split(';'):
            keywords.append(unidecode(i.strip().lower()))

        var.matricula_keywords = keywords
        push('matricula_keywords', keywords)

        self.label_console.setText('Palavras-chave para matrícula atualizadas.')

    def change_cliente_keywords(self):
        keywords = []
        for i in self.lineEdit_config_cliente.text().split(';'):
            keywords.append(unidecode(i.strip().lower()))

        var.cliente_keywords = keywords
        push('cliente_keywords', keywords)

        self.label_console.setText('Palavras-chave para clientes atualizadas.')

    def change_apolice_keywords(self):
        keywords = []
        for i in self.lineEdit_config_apolice.text().split(';'):
            keywords.append(unidecode(i.strip().lower()))

        var.apolice_keywords = keywords
        push('apolice_keywords', keywords)

        self.label_console.setText('Palavras-chave para apólice atualizadas.')

    def change_cobertura_keywords(self):
        keywords = []
        for i in self.lineEdit_config_cobertura.text().split(';'):
            keywords.append(unidecode(i.strip().lower()))

        var.cobertura_keywords = keywords
        push('cobertura_keywords', keywords)

        self.label_console.setText('Palavras-chave para coberturas atualizadas.')

    def change_capital_keywords(self):
        keywords = []
        for i in self.lineEdit_config_capital.text().split(';'):
            keywords.append(unidecode(i.strip().lower()))

        var.capital_keywords = keywords
        push('capital_keywords', keywords)

        self.label_console.setText('Palavras-chave para capital atualizadas.')

    def change_cnv_keywords(self):
        keywords = []
        for i in self.lineEdit_config_cnv.text().split(';'):
            keywords.append(unidecode(i.strip().lower()))

        var.cnv_keywords = keywords
        push('cnv_keywords', keywords)

        self.label_console.setText('Palavras-chave para CNV atualizadas.')
