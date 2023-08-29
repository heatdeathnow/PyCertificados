from PySide6.QtWidgets import (QDateEdit, QFrame, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QListWidget,
                               QProgressBar, QPushButton, QSizePolicy, QTabWidget, QWidget, QMessageBox, QFileDialog,
                               QVBoxLayout, QFormLayout, QSlider, QScrollArea, QPlainTextEdit, QComboBox, QCheckBox)
from PySide6.QtCore import (QCoreApplication, QDate, QMetaObject, QSize, Qt)
from reader import get_coberturas, get_headers, get_grupo_values, get_grupo, push
from PySide6.QtGui import QIcon, QFont, QFontDatabase
from emitter import emit_singular, emit_from_source
from multiprocessing import cpu_count
from threading import active_count
from unidecode import unidecode
from threading import Thread
from neat import name as nm
from neat import cpf as cp
from time import sleep
from os import listdir
import var


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 540)
        MainWindow.setMinimumSize(QSize(70, 0))
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_console = QLabel(parent=self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_console.sizePolicy().hasHeightForWidth())
        self.label_console.setSizePolicy(sizePolicy)
        self.label_console.setText("")
        self.label_console.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_console.setWordWrap(True)
        self.label_console.setObjectName("label_console")
        self.gridLayout_5.addWidget(self.label_console, 1, 0, 1, 1)
        self.tabWidget = QTabWidget(parent=self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QSize(0, 30))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_multiple = QWidget()
        self.tab_multiple.setObjectName("tab_multiple")
        self.gridLayout = QGridLayout(self.tab_multiple)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_multiple_select = QVBoxLayout()
        self.verticalLayout_multiple_select.setObjectName("verticalLayout_multiple_select")
        self.pushButton_multiple_input = QPushButton(parent=self.tab_multiple)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_multiple_input.sizePolicy().hasHeightForWidth())
        self.pushButton_multiple_input.setSizePolicy(sizePolicy)
        self.pushButton_multiple_input.setMinimumSize(QSize(0, 40))
        self.pushButton_multiple_input.setMaximumSize(QSize(150, 16777215))
        self.pushButton_multiple_input.setObjectName("pushButton_multiple_input")
        self.verticalLayout_multiple_select.addWidget(self.pushButton_multiple_input)
        self.label_multiple_input_header = QLabel(parent=self.tab_multiple)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_multiple_input_header.sizePolicy().hasHeightForWidth())
        self.label_multiple_input_header.setSizePolicy(sizePolicy)
        self.label_multiple_input_header.setObjectName("label_multiple_input_header")
        self.verticalLayout_multiple_select.addWidget(self.label_multiple_input_header)
        self.label_multiple_input_text = QLabel(parent=self.tab_multiple)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_multiple_input_text.sizePolicy().hasHeightForWidth())
        self.label_multiple_input_text.setSizePolicy(sizePolicy)
        self.label_multiple_input_text.setText("")
        self.label_multiple_input_text.setObjectName("label_multiple_input_text")
        self.verticalLayout_multiple_select.addWidget(self.label_multiple_input_text)
        self.line_multiple_input_output = QFrame(parent=self.tab_multiple)
        self.line_multiple_input_output.setFrameShape(QFrame.Shape.HLine)
        self.line_multiple_input_output.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_multiple_input_output.setObjectName("line_multiple_input_output")
        self.verticalLayout_multiple_select.addWidget(self.line_multiple_input_output)
        self.pushButton_multiple_output = QPushButton(parent=self.tab_multiple)
        self.pushButton_multiple_output.setMinimumSize(QSize(0, 40))
        self.pushButton_multiple_output.setMaximumSize(QSize(150, 16777215))
        self.pushButton_multiple_output.setAcceptDrops(False)
        self.pushButton_multiple_output.setAutoFillBackground(False)
        self.pushButton_multiple_output.setAutoDefault(False)
        self.pushButton_multiple_output.setDefault(False)
        self.pushButton_multiple_output.setFlat(False)
        self.pushButton_multiple_output.setObjectName("pushButton_multiple_output")
        self.verticalLayout_multiple_select.addWidget(self.pushButton_multiple_output)
        self.label_multiple_output_header = QLabel(parent=self.tab_multiple)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_multiple_output_header.sizePolicy().hasHeightForWidth())
        self.label_multiple_output_header.setSizePolicy(sizePolicy)
        self.label_multiple_output_header.setObjectName("label_multiple_output_header")
        self.verticalLayout_multiple_select.addWidget(self.label_multiple_output_header)
        self.label_multiple_output_text = QLabel(parent=self.tab_multiple)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_multiple_output_text.sizePolicy().hasHeightForWidth())
        self.label_multiple_output_text.setSizePolicy(sizePolicy)
        self.label_multiple_output_text.setText("")
        self.label_multiple_output_text.setObjectName("label_multiple_output_text")
        self.verticalLayout_multiple_select.addWidget(self.label_multiple_output_text)
        self.gridLayout.addLayout(self.verticalLayout_multiple_select, 0, 0, 1, 1)
        self.horizontalLayout_multiple_bar_emit = QHBoxLayout()
        self.horizontalLayout_multiple_bar_emit.setObjectName("horizontalLayout_multiple_bar_emit")
        self.progressBar_multiple = QProgressBar(parent=self.tab_multiple)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_multiple.sizePolicy().hasHeightForWidth())
        self.progressBar_multiple.setSizePolicy(sizePolicy)
        self.progressBar_multiple.setProperty("value", 0)
        self.progressBar_multiple.setTextVisible(False)
        self.progressBar_multiple.setInvertedAppearance(False)
        self.progressBar_multiple.setObjectName("progressBar_multiple")
        self.horizontalLayout_multiple_bar_emit.addWidget(self.progressBar_multiple)
        self.pushButton_multiple_emit = QPushButton(parent=self.tab_multiple)
        self.pushButton_multiple_emit.setObjectName("pushButton_multiple_emit")
        self.horizontalLayout_multiple_bar_emit.addWidget(self.pushButton_multiple_emit)
        self.gridLayout.addLayout(self.horizontalLayout_multiple_bar_emit, 2, 0, 1, 2)
        self.verticalLayout_multiple_dates = QVBoxLayout()
        self.verticalLayout_multiple_dates.setObjectName("verticalLayout_multiple_dates")
        self.label_multiple_start = QLabel(parent=self.tab_multiple)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_multiple_start.sizePolicy().hasHeightForWidth())
        self.label_multiple_start.setSizePolicy(sizePolicy)
        self.label_multiple_start.setObjectName("label_multiple_start")
        self.verticalLayout_multiple_dates.addWidget(self.label_multiple_start)
        self.dateEdit_multiple_start = QDateEdit(parent=self.tab_multiple)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_multiple_start.sizePolicy().hasHeightForWidth())
        self.dateEdit_multiple_start.setSizePolicy(sizePolicy)
        self.dateEdit_multiple_start.setProperty("showGroupSeparator", False)
        self.dateEdit_multiple_start.setMaximumDate(QDate(2030, 12, 31))
        self.dateEdit_multiple_start.setMinimumDate(QDate(2023, 1, 1))
        self.dateEdit_multiple_start.setCalendarPopup(True)
        self.dateEdit_multiple_start.setDate(QDate(2023, 1, 1))
        self.dateEdit_multiple_start.setObjectName("dateEdit_multiple_start")
        self.verticalLayout_multiple_dates.addWidget(self.dateEdit_multiple_start)
        self.label_multiple_end = QLabel(parent=self.tab_multiple)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_multiple_end.sizePolicy().hasHeightForWidth())
        self.label_multiple_end.setSizePolicy(sizePolicy)
        self.label_multiple_end.setObjectName("label_multiple_end")
        self.verticalLayout_multiple_dates.addWidget(self.label_multiple_end)
        self.dateEdit_multiple_end = QDateEdit(parent=self.tab_multiple)
        self.dateEdit_multiple_end.setMaximumDate(QDate(2030, 12, 31))
        self.dateEdit_multiple_end.setMinimumDate(QDate(2023, 1, 1))
        self.dateEdit_multiple_end.setCalendarPopup(True)
        self.dateEdit_multiple_end.setDate(QDate(2023, 1, 1))
        self.dateEdit_multiple_end.setObjectName("dateEdit_multiple_end")
        self.verticalLayout_multiple_dates.addWidget(self.dateEdit_multiple_end)
        self.gridLayout.addLayout(self.verticalLayout_multiple_dates, 0, 1, 1, 1)
        self.line_multiple_progress = QFrame(parent=self.tab_multiple)
        self.line_multiple_progress.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_multiple_progress.setFrameShape(QFrame.Shape.HLine)
        self.line_multiple_progress.setObjectName("line_multiple_progress")
        self.gridLayout.addWidget(self.line_multiple_progress, 1, 0, 1, 2)
        self.tabWidget.addTab(self.tab_multiple, "")
        self.tab_singular = QWidget()
        self.tab_singular.setObjectName("tab_singular")
        self.gridLayout_2 = QGridLayout(self.tab_singular)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listWidget_singular_cobertura = QListWidget(parent=self.tab_singular)
        self.listWidget_singular_cobertura.setObjectName("listWidget_singular_cobertura")
        self.gridLayout_2.addWidget(self.listWidget_singular_cobertura, 2, 0, 2, 1)
        self.pushButton_singular_emit = QPushButton(parent=self.tab_singular)
        self.pushButton_singular_emit.setMinimumSize(QSize(0, 40))
        self.pushButton_singular_emit.setMaximumSize(QSize(200, 16777215))
        self.pushButton_singular_emit.setAutoRepeat(False)
        self.pushButton_singular_emit.setObjectName("pushButton_singular_emit")
        self.gridLayout_2.addWidget(self.pushButton_singular_emit, 3, 1, 1, 1)
        self.formLayout_singular_write = QFormLayout()
        self.formLayout_singular_write.setObjectName("formLayout_singular_write")
        self.label_singular_name = QLabel(parent=self.tab_singular)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_singular_name.sizePolicy().hasHeightForWidth())
        self.label_singular_name.setSizePolicy(sizePolicy)
        self.label_singular_name.setObjectName("label_singular_name")
        self.formLayout_singular_write.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_singular_name)
        self.lineEdit_singular_name = QLineEdit(parent=self.tab_singular)
        self.lineEdit_singular_name.setObjectName("lineEdit_singular_name")
        self.formLayout_singular_write.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit_singular_name)
        self.label_singular_cpf = QLabel(parent=self.tab_singular)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_singular_cpf.sizePolicy().hasHeightForWidth())
        self.label_singular_cpf.setSizePolicy(sizePolicy)
        self.label_singular_cpf.setObjectName("label_singular_cpf")
        self.formLayout_singular_write.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_singular_cpf)
        self.label_singular_matricula = QLabel(parent=self.tab_singular)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_singular_matricula.sizePolicy().hasHeightForWidth())
        self.label_singular_matricula.setSizePolicy(sizePolicy)
        self.label_singular_matricula.setObjectName("label_singular_matricula")
        self.formLayout_singular_write.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_singular_matricula)
        self.label_singular_cnpj = QLabel(parent=self.tab_singular)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_singular_cnpj.sizePolicy().hasHeightForWidth())
        self.label_singular_cnpj.setSizePolicy(sizePolicy)
        self.label_singular_cnpj.setObjectName("label_singular_cnpj")
        self.formLayout_singular_write.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_singular_cnpj)
        self.lineEdit_singular_cpf = QLineEdit(parent=self.tab_singular)
        self.lineEdit_singular_cpf.setObjectName("lineEdit_singular_cpf")
        self.formLayout_singular_write.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEdit_singular_cpf)
        self.lineEdit_singular_matricula = QLineEdit(parent=self.tab_singular)
        self.lineEdit_singular_matricula.setObjectName("lineEdit_singular_matricula")
        self.formLayout_singular_write.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lineEdit_singular_matricula)
        self.lineEdit_singular_cnpj = QLineEdit(parent=self.tab_singular)
        self.lineEdit_singular_cnpj.setObjectName("lineEdit_singular_cnpj")
        self.formLayout_singular_write.setWidget(4, QFormLayout.ItemRole.FieldRole, self.lineEdit_singular_cnpj)
        self.label_singular_apolice = QLabel(parent=self.tab_singular)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_singular_apolice.sizePolicy().hasHeightForWidth())
        self.label_singular_apolice.setSizePolicy(sizePolicy)
        self.label_singular_apolice.setObjectName("label_singular_apolice")
        self.formLayout_singular_write.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_singular_apolice)
        self.lineEdit_singular_apolice = QLineEdit(parent=self.tab_singular)
        self.lineEdit_singular_apolice.setObjectName("lineEdit_singular_apolice")
        self.formLayout_singular_write.setWidget(5, QFormLayout.ItemRole.FieldRole, self.lineEdit_singular_apolice)
        self.label_singular_client = QLabel(parent=self.tab_singular)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_singular_client.sizePolicy().hasHeightForWidth())
        self.label_singular_client.setSizePolicy(sizePolicy)
        self.label_singular_client.setObjectName("label_singular_client")
        self.formLayout_singular_write.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_singular_client)
        self.lineEdit_singular_client = QLineEdit(parent=self.tab_singular)
        self.lineEdit_singular_client.setObjectName("lineEdit_singular_client")
        self.formLayout_singular_write.setWidget(3, QFormLayout.ItemRole.FieldRole, self.lineEdit_singular_client)
        self.label_singular_startdate = QLabel(parent=self.tab_singular)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_singular_startdate.sizePolicy().hasHeightForWidth())
        self.label_singular_startdate.setSizePolicy(sizePolicy)
        self.label_singular_startdate.setObjectName("label_singular_startdate")
        self.formLayout_singular_write.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_singular_startdate)
        self.label_singular_enddate = QLabel(parent=self.tab_singular)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_singular_enddate.sizePolicy().hasHeightForWidth())
        self.label_singular_enddate.setSizePolicy(sizePolicy)
        self.label_singular_enddate.setObjectName("label_singular_enddate")
        self.formLayout_singular_write.setWidget(8, QFormLayout.ItemRole.LabelRole, self.label_singular_enddate)
        self.dateEdit_singular_start = QDateEdit(parent=self.tab_singular)
        self.dateEdit_singular_start.setCalendarPopup(True)
        self.dateEdit_singular_start.setObjectName("dateEdit_singular_start")
        self.formLayout_singular_write.setWidget(7, QFormLayout.ItemRole.FieldRole, self.dateEdit_singular_start)
        self.dateEdit_singular_end = QDateEdit(parent=self.tab_singular)
        self.dateEdit_singular_end.setCalendarPopup(True)
        self.dateEdit_singular_end.setObjectName("dateEdit_singular_end")
        self.formLayout_singular_write.setWidget(8, QFormLayout.ItemRole.FieldRole, self.dateEdit_singular_end)
        self.label_singular_capital = QLabel(parent=self.tab_singular)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_singular_capital.sizePolicy().hasHeightForWidth())
        self.label_singular_capital.setSizePolicy(sizePolicy)
        self.label_singular_capital.setObjectName("label_singular_capital")
        self.formLayout_singular_write.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_singular_capital)
        self.lineEdit_singular_capital = QLineEdit(parent=self.tab_singular)
        self.lineEdit_singular_capital.setObjectName("lineEdit_singular_capital")
        self.formLayout_singular_write.setWidget(6, QFormLayout.ItemRole.FieldRole, self.lineEdit_singular_capital)
        self.gridLayout_2.addLayout(self.formLayout_singular_write, 2, 1, 1, 1)
        self.verticalLayout_singular_output_and_grupo = QVBoxLayout()
        self.verticalLayout_singular_output_and_grupo.setObjectName("verticalLayout_singular_output_and_grupo")
        self.horizontalLayout_singular_select_output = QHBoxLayout()
        self.horizontalLayout_singular_select_output.setObjectName("horizontalLayout_singular_select_output")
        self.pushButton_singular_select_output = QPushButton(parent=self.tab_singular)
        self.pushButton_singular_select_output.setObjectName("pushButton_singular_select_output")
        self.horizontalLayout_singular_select_output.addWidget(self.pushButton_singular_select_output)
        self.label_singular_output_header = QLabel(parent=self.tab_singular)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_singular_output_header.sizePolicy().hasHeightForWidth())
        self.label_singular_output_header.setSizePolicy(sizePolicy)
        self.label_singular_output_header.setObjectName("label_singular_output_header")
        self.horizontalLayout_singular_select_output.addWidget(self.label_singular_output_header)
        self.label_singular_output_text = QLabel(parent=self.tab_singular)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_singular_output_text.sizePolicy().hasHeightForWidth())
        self.label_singular_output_text.setSizePolicy(sizePolicy)
        self.label_singular_output_text.setText("")
        self.label_singular_output_text.setObjectName("label_singular_output_text")
        self.horizontalLayout_singular_select_output.addWidget(self.label_singular_output_text)
        self.verticalLayout_singular_output_and_grupo.addLayout(self.horizontalLayout_singular_select_output)
        self.horizontalLayout_singular_select_grupo = QHBoxLayout()
        self.horizontalLayout_singular_select_grupo.setObjectName("horizontalLayout_singular_select_grupo")
        self.checkBox_singular_allow_grupo = QCheckBox(parent=self.tab_singular)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_singular_allow_grupo.sizePolicy().hasHeightForWidth())
        self.checkBox_singular_allow_grupo.setSizePolicy(sizePolicy)
        self.checkBox_singular_allow_grupo.setObjectName("checkBox_singular_allow_grupo")
        self.horizontalLayout_singular_select_grupo.addWidget(self.checkBox_singular_allow_grupo)
        self.comboBox_singular_grupo = QComboBox(parent=self.tab_singular)
        self.comboBox_singular_grupo.setEnabled(False)
        self.comboBox_singular_grupo.setObjectName("comboBox_singular_grupo")
        self.horizontalLayout_singular_select_grupo.addWidget(self.comboBox_singular_grupo)
        self.verticalLayout_singular_output_and_grupo.addLayout(self.horizontalLayout_singular_select_grupo)
        self.gridLayout_2.addLayout(self.verticalLayout_singular_output_and_grupo, 0, 0, 1, 2)
        self.tabWidget.addTab(self.tab_singular, "")
        self.tab_config = QWidget()
        self.tab_config.setObjectName("tab_config")
        self.verticalLayout = QVBoxLayout(self.tab_config)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QScrollArea(parent=self.tab_config)
        self.scrollArea.setMinimumSize(QSize(70, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout = QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName("formLayout")
        self.label_config_performance_title = QLabel(parent=self.scrollAreaWidgetContents)
        self.label_config_performance_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_config_performance_title.setObjectName("label_config_performance_title")
        self.formLayout.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.label_config_performance_title)
        self.label_config_max_threads = QLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config_max_threads.sizePolicy().hasHeightForWidth())
        self.label_config_max_threads.setSizePolicy(sizePolicy)
        self.label_config_max_threads.setObjectName("label_config_max_threads")
        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_config_max_threads)
        self.horizontalLayout_config_max_threads = QHBoxLayout()
        self.horizontalLayout_config_max_threads.setObjectName("horizontalLayout_config_max_threads")
        self.horizontalSlider_config_max_threads = QSlider(parent=self.scrollAreaWidgetContents)
        self.horizontalSlider_config_max_threads.setMinimum(4)
        self.horizontalSlider_config_max_threads.setMaximum(150)
        self.horizontalSlider_config_max_threads.setSingleStep(1)
        self.horizontalSlider_config_max_threads.setProperty("value", 150)
        self.horizontalSlider_config_max_threads.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider_config_max_threads.setObjectName("horizontalSlider_config_max_threads")
        self.horizontalLayout_config_max_threads.addWidget(self.horizontalSlider_config_max_threads)
        self.label_config_max_thread_number = QLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config_max_thread_number.sizePolicy().hasHeightForWidth())
        self.label_config_max_thread_number.setSizePolicy(sizePolicy)
        self.label_config_max_thread_number.setMinimumSize(QSize(20, 0))
        self.label_config_max_thread_number.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_config_max_thread_number.setObjectName("label_config_max_thread_number")
        self.horizontalLayout_config_max_threads.addWidget(self.label_config_max_thread_number)
        self.formLayout.setLayout(1, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_config_max_threads)
        self.label_config_target_threads = QLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config_target_threads.sizePolicy().hasHeightForWidth())
        self.label_config_target_threads.setSizePolicy(sizePolicy)
        self.label_config_target_threads.setObjectName("label_config_target_threads")
        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_config_target_threads)
        self.horizontalLayout_config_target_threads = QHBoxLayout()
        self.horizontalLayout_config_target_threads.setObjectName("horizontalLayout_config_target_threads")
        self.horizontalSlider_config_target_threads = QSlider(parent=self.scrollAreaWidgetContents)
        self.horizontalSlider_config_target_threads.setMinimum(4)
        self.horizontalSlider_config_target_threads.setMaximum(150)
        self.horizontalSlider_config_target_threads.setProperty("value", 15)
        self.horizontalSlider_config_target_threads.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider_config_target_threads.setObjectName("horizontalSlider_config_target_threads")
        self.horizontalLayout_config_target_threads.addWidget(self.horizontalSlider_config_target_threads)
        self.label_config_target_thread_number = QLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config_target_thread_number.sizePolicy().hasHeightForWidth())
        self.label_config_target_thread_number.setSizePolicy(sizePolicy)
        self.label_config_target_thread_number.setMinimumSize(QSize(20, 0))
        self.label_config_target_thread_number.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_config_target_thread_number.setObjectName("label_config_target_thread_number")
        self.horizontalLayout_config_target_threads.addWidget(self.label_config_target_thread_number)
        self.formLayout.setLayout(2, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_config_target_threads)
        self.label_config_max_processes = QLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config_max_processes.sizePolicy().hasHeightForWidth())
        self.label_config_max_processes.setSizePolicy(sizePolicy)
        self.label_config_max_processes.setObjectName("label_config_max_processes")
        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_config_max_processes)
        self.horizontalLayout_config_max_processes = QHBoxLayout()
        self.horizontalLayout_config_max_processes.setObjectName("horizontalLayout_config_max_processes")
        self.horizontalSlider_config_max_processes = QSlider(parent=self.scrollAreaWidgetContents)
        self.horizontalSlider_config_max_processes.setMinimum(1)
        self.horizontalSlider_config_max_processes.setMaximum(4)
        self.horizontalSlider_config_max_processes.setProperty("value", 4)
        self.horizontalSlider_config_max_processes.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider_config_max_processes.setObjectName("horizontalSlider_config_max_processes")
        self.horizontalLayout_config_max_processes.addWidget(self.horizontalSlider_config_max_processes)
        self.label_config_max_processes_number = QLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config_max_processes_number.sizePolicy().hasHeightForWidth())
        self.label_config_max_processes_number.setSizePolicy(sizePolicy)
        self.label_config_max_processes_number.setMinimumSize(QSize(20, 0))
        self.label_config_max_processes_number.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_config_max_processes_number.setObjectName("label_config_max_processes_number")
        self.horizontalLayout_config_max_processes.addWidget(self.label_config_max_processes_number)
        self.formLayout.setLayout(3, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_config_max_processes)
        self.line = QFrame(parent=self.scrollAreaWidgetContents)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.formLayout.setWidget(4, QFormLayout.ItemRole.SpanningRole, self.line)
        self.label_config_file_option_titles = QLabel(parent=self.scrollAreaWidgetContents)
        self.label_config_file_option_titles.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_config_file_option_titles.setObjectName("label_config_file_option_titles")
        self.formLayout.setWidget(5, QFormLayout.ItemRole.SpanningRole, self.label_config_file_option_titles)
        self.pushButton_config_grupo_source = QPushButton(parent=self.scrollAreaWidgetContents)
        self.pushButton_config_grupo_source.setMinimumSize(QSize(0, 30))
        self.pushButton_config_grupo_source.setObjectName("pushButton_config_grupo_source")
        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.pushButton_config_grupo_source)
        self.horizontalLayout_config_grupo_source = QHBoxLayout()
        self.horizontalLayout_config_grupo_source.setObjectName("horizontalLayout_config_grupo_source")
        self.label_config_selection_grupo = QLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config_selection_grupo.sizePolicy().hasHeightForWidth())
        self.label_config_selection_grupo.setSizePolicy(sizePolicy)
        self.label_config_selection_grupo.setObjectName("label_config_selection_grupo")
        self.horizontalLayout_config_grupo_source.addWidget(self.label_config_selection_grupo)
        self.label_config_grupo_text = QLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config_grupo_text.sizePolicy().hasHeightForWidth())
        self.label_config_grupo_text.setSizePolicy(sizePolicy)
        self.label_config_grupo_text.setText("")
        self.label_config_grupo_text.setObjectName("label_config_grupo_text")
        self.horizontalLayout_config_grupo_source.addWidget(self.label_config_grupo_text)
        self.formLayout.setLayout(6, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_config_grupo_source)
        self.pushButton_config_change_pdf_template = QPushButton(parent=self.scrollAreaWidgetContents)
        self.pushButton_config_change_pdf_template.setMinimumSize(QSize(0, 30))
        self.pushButton_config_change_pdf_template.setObjectName("pushButton_config_change_pdf_template")
        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.pushButton_config_change_pdf_template)
        self.horizontalLayout_config_pdf_template = QHBoxLayout()
        self.horizontalLayout_config_pdf_template.setObjectName("horizontalLayout_config_pdf_template")
        self.label_config_selection_pdf = QLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config_selection_pdf.sizePolicy().hasHeightForWidth())
        self.label_config_selection_pdf.setSizePolicy(sizePolicy)
        self.label_config_selection_pdf.setObjectName("label_config_selection_pdf")
        self.horizontalLayout_config_pdf_template.addWidget(self.label_config_selection_pdf)
        self.label_config_pdf_text = QLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config_pdf_text.sizePolicy().hasHeightForWidth())
        self.label_config_pdf_text.setSizePolicy(sizePolicy)
        self.label_config_pdf_text.setText("")
        self.label_config_pdf_text.setObjectName("label_config_pdf_text")
        self.horizontalLayout_config_pdf_template.addWidget(self.label_config_pdf_text)
        self.formLayout.setLayout(7, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_config_pdf_template)
        self.line_2 = QFrame(parent=self.scrollAreaWidgetContents)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.formLayout.setWidget(8, QFormLayout.ItemRole.SpanningRole, self.line_2)
        self.label_config_dates_title = QLabel(parent=self.scrollAreaWidgetContents)
        self.label_config_dates_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_config_dates_title.setObjectName("label_config_dates_title")
        self.formLayout.setWidget(9, QFormLayout.ItemRole.SpanningRole, self.label_config_dates_title)
        self.label_config_start_date = QLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config_start_date.sizePolicy().hasHeightForWidth())
        self.label_config_start_date.setSizePolicy(sizePolicy)
        self.label_config_start_date.setObjectName("label_config_start_date")
        self.formLayout.setWidget(10, QFormLayout.ItemRole.LabelRole, self.label_config_start_date)
        self.dateEdit_config_start = QDateEdit(parent=self.scrollAreaWidgetContents)
        self.dateEdit_config_start.setMaximumDate(QDate(2030, 12, 31))
        self.dateEdit_config_start.setMinimumDate(QDate(2023, 1, 1))
        self.dateEdit_config_start.setCalendarPopup(True)
        self.dateEdit_config_start.setDate(QDate(2023, 1, 1))
        self.dateEdit_config_start.setObjectName("dateEdit_config_start")
        self.formLayout.setWidget(10, QFormLayout.ItemRole.FieldRole, self.dateEdit_config_start)
        self.label_config_end_date = QLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config_end_date.sizePolicy().hasHeightForWidth())
        self.label_config_end_date.setSizePolicy(sizePolicy)
        self.label_config_end_date.setObjectName("label_config_end_date")
        self.formLayout.setWidget(11, QFormLayout.ItemRole.LabelRole, self.label_config_end_date)
        self.dateEdit_config_end = QDateEdit(parent=self.scrollAreaWidgetContents)
        self.dateEdit_config_end.setMaximumDate(QDate(2030, 12, 31))
        self.dateEdit_config_end.setMinimumDate(QDate(2023, 1, 1))
        self.dateEdit_config_end.setCalendarPopup(True)
        self.dateEdit_config_end.setDate(QDate(2023, 1, 1))
        self.dateEdit_config_end.setObjectName("dateEdit_config_end")
        self.formLayout.setWidget(11, QFormLayout.ItemRole.FieldRole, self.dateEdit_config_end)
        self.line_3 = QFrame(parent=self.scrollAreaWidgetContents)
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.formLayout.setWidget(12, QFormLayout.ItemRole.SpanningRole, self.line_3)
        self.label_config_data_input_and_output_title = QLabel(parent=self.scrollAreaWidgetContents)
        self.label_config_data_input_and_output_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_config_data_input_and_output_title.setObjectName("label_config_data_input_and_output_title")
        self.formLayout.setWidget(13, QFormLayout.ItemRole.SpanningRole, self.label_config_data_input_and_output_title)
        self.pushButton_config_source = QPushButton(parent=self.scrollAreaWidgetContents)
        self.pushButton_config_source.setMinimumSize(QSize(0, 30))
        self.pushButton_config_source.setObjectName("pushButton_config_source")
        self.formLayout.setWidget(14, QFormLayout.ItemRole.LabelRole, self.pushButton_config_source)
        self.horizontalLayout_config_data_source = QHBoxLayout()
        self.horizontalLayout_config_data_source.setObjectName("horizontalLayout_config_data_source")
        self.label_config_selection_data_source = QLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config_selection_data_source.sizePolicy().hasHeightForWidth())
        self.label_config_selection_data_source.setSizePolicy(sizePolicy)
        self.label_config_selection_data_source.setObjectName("label_config_selection_data_source")
        self.horizontalLayout_config_data_source.addWidget(self.label_config_selection_data_source)
        self.label_config_source_text = QLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config_source_text.sizePolicy().hasHeightForWidth())
        self.label_config_source_text.setSizePolicy(sizePolicy)
        self.label_config_source_text.setText("")
        self.label_config_source_text.setObjectName("label_config_source_text")
        self.horizontalLayout_config_data_source.addWidget(self.label_config_source_text)
        self.formLayout.setLayout(14, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_config_data_source)
        self.pushButton_config_output_dir = QPushButton(parent=self.scrollAreaWidgetContents)
        self.pushButton_config_output_dir.setMinimumSize(QSize(0, 30))
        self.pushButton_config_output_dir.setObjectName("pushButton_config_output_dir")
        self.formLayout.setWidget(15, QFormLayout.ItemRole.LabelRole, self.pushButton_config_output_dir)
        self.horizontalLayout_config_default_output_dir = QHBoxLayout()
        self.horizontalLayout_config_default_output_dir.setObjectName("horizontalLayout_config_default_output_dir")
        self.label_config_selection_output_dir = QLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config_selection_output_dir.sizePolicy().hasHeightForWidth())
        self.label_config_selection_output_dir.setSizePolicy(sizePolicy)
        self.label_config_selection_output_dir.setObjectName("label_config_selection_output_dir")
        self.horizontalLayout_config_default_output_dir.addWidget(self.label_config_selection_output_dir)
        self.label_config_output_dir_text = QLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config_output_dir_text.sizePolicy().hasHeightForWidth())
        self.label_config_output_dir_text.setSizePolicy(sizePolicy)
        self.label_config_output_dir_text.setText("")
        self.label_config_output_dir_text.setObjectName("label_config_output_dir_text")
        self.horizontalLayout_config_default_output_dir.addWidget(self.label_config_output_dir_text)
        self.formLayout.setLayout(15, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_config_default_output_dir)
        self.line_4 = QFrame(parent=self.scrollAreaWidgetContents)
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.formLayout.setWidget(16, QFormLayout.ItemRole.SpanningRole, self.line_4)
        self.label_config_formatting_title = QLabel(parent=self.scrollAreaWidgetContents)
        self.label_config_formatting_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_config_formatting_title.setObjectName("label_config_formatting_title")
        self.formLayout.setWidget(17, QFormLayout.ItemRole.SpanningRole, self.label_config_formatting_title)
        self.label_config_font = QLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config_font.sizePolicy().hasHeightForWidth())
        self.label_config_font.setSizePolicy(sizePolicy)
        self.label_config_font.setObjectName("label_config_font")
        self.formLayout.setWidget(18, QFormLayout.ItemRole.LabelRole, self.label_config_font)
        self.comboBox_config_font = QComboBox(parent=self.scrollAreaWidgetContents)
        self.comboBox_config_font.setObjectName("comboBox_config_font")
        self.formLayout.setWidget(18, QFormLayout.ItemRole.FieldRole, self.comboBox_config_font)
        self.label_config_text_size = QLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config_text_size.sizePolicy().hasHeightForWidth())
        self.label_config_text_size.setSizePolicy(sizePolicy)
        self.label_config_text_size.setObjectName("label_config_text_size")
        self.formLayout.setWidget(19, QFormLayout.ItemRole.LabelRole, self.label_config_text_size)
        self.horizontalLayout_config_text_size = QHBoxLayout()
        self.horizontalLayout_config_text_size.setObjectName("horizontalLayout_config_text_size")
        self.horizontalSlider_config_text_size = QSlider(parent=self.scrollAreaWidgetContents)
        self.horizontalSlider_config_text_size.setMinimum(6)
        self.horizontalSlider_config_text_size.setMaximum(16)
        self.horizontalSlider_config_text_size.setProperty("value", 10)
        self.horizontalSlider_config_text_size.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider_config_text_size.setObjectName("horizontalSlider_config_text_size")
        self.horizontalLayout_config_text_size.addWidget(self.horizontalSlider_config_text_size)
        self.label_config_text_size_text = QLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config_text_size_text.sizePolicy().hasHeightForWidth())
        self.label_config_text_size_text.setSizePolicy(sizePolicy)
        self.label_config_text_size_text.setMinimumSize(QSize(20, 0))
        self.label_config_text_size_text.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_config_text_size_text.setObjectName("label_config_text_size_text")
        self.horizontalLayout_config_text_size.addWidget(self.label_config_text_size_text)
        self.formLayout.setLayout(19, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_config_text_size)
        self.label_config_text_left = QLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config_text_left.sizePolicy().hasHeightForWidth())
        self.label_config_text_left.setSizePolicy(sizePolicy)
        self.label_config_text_left.setObjectName("label_config_text_left")
        self.formLayout.setWidget(20, QFormLayout.ItemRole.LabelRole, self.label_config_text_left)
        self.horizontalLayout_config_text_left = QHBoxLayout()
        self.horizontalLayout_config_text_left.setObjectName("horizontalLayout_config_text_left")
        self.horizontalSlider_config_text_left = QSlider(parent=self.scrollAreaWidgetContents)
        self.horizontalSlider_config_text_left.setMinimum(1)
        self.horizontalSlider_config_text_left.setMaximum(100)
        self.horizontalSlider_config_text_left.setProperty("value", 65)
        self.horizontalSlider_config_text_left.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider_config_text_left.setObjectName("horizontalSlider_config_text_left")
        self.horizontalLayout_config_text_left.addWidget(self.horizontalSlider_config_text_left)
        self.label_config_text_left_text = QLabel(parent=self.scrollAreaWidgetContents)
        self.label_config_text_left_text.setMinimumSize(QSize(20, 0))
        self.label_config_text_left_text.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_config_text_left_text.setObjectName("label_config_text_left_text")
        self.horizontalLayout_config_text_left.addWidget(self.label_config_text_left_text)
        self.formLayout.setLayout(20, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_config_text_left)
        self.label_config_text_right = QLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config_text_right.sizePolicy().hasHeightForWidth())
        self.label_config_text_right.setSizePolicy(sizePolicy)
        self.label_config_text_right.setObjectName("label_config_text_right")
        self.formLayout.setWidget(21, QFormLayout.ItemRole.LabelRole, self.label_config_text_right)
        self.horizontalLayout_config_text_height = QHBoxLayout()
        self.horizontalLayout_config_text_height.setObjectName("horizontalLayout_config_text_height")
        self.horizontalSlider_config_text_height = QSlider(parent=self.scrollAreaWidgetContents)
        self.horizontalSlider_config_text_height.setMinimum(500)
        self.horizontalSlider_config_text_height.setMaximum(700)
        self.horizontalSlider_config_text_height.setProperty("value", 620)
        self.horizontalSlider_config_text_height.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider_config_text_height.setObjectName("horizontalSlider_config_text_height")
        self.horizontalLayout_config_text_height.addWidget(self.horizontalSlider_config_text_height)
        self.label_config_text_height_text = QLabel(parent=self.scrollAreaWidgetContents)
        self.label_config_text_height_text.setMinimumSize(QSize(20, 0))
        self.label_config_text_height_text.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_config_text_height_text.setObjectName("label_config_text_height_text")
        self.horizontalLayout_config_text_height.addWidget(self.label_config_text_height_text)
        self.formLayout.setLayout(21, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_config_text_height)
        self.label_config_text_space = QLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config_text_space.sizePolicy().hasHeightForWidth())
        self.label_config_text_space.setSizePolicy(sizePolicy)
        self.label_config_text_space.setObjectName("label_config_text_space")
        self.formLayout.setWidget(22, QFormLayout.ItemRole.LabelRole, self.label_config_text_space)
        self.horizontalLayout_config_text_space = QHBoxLayout()
        self.horizontalLayout_config_text_space.setObjectName("horizontalLayout_config_text_space")
        self.horizontalSlider_config_text_space = QSlider(parent=self.scrollAreaWidgetContents)
        self.horizontalSlider_config_text_space.setMinimum(1)
        self.horizontalSlider_config_text_space.setMaximum(50)
        self.horizontalSlider_config_text_space.setProperty("value", 15)
        self.horizontalSlider_config_text_space.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider_config_text_space.setObjectName("horizontalSlider_config_text_space")
        self.horizontalLayout_config_text_space.addWidget(self.horizontalSlider_config_text_space)
        self.label_config_text_space_text = QLabel(parent=self.scrollAreaWidgetContents)
        self.label_config_text_space_text.setMinimumSize(QSize(20, 0))
        self.label_config_text_space_text.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_config_text_space_text.setObjectName("label_config_text_space_text")
        self.horizontalLayout_config_text_space.addWidget(self.label_config_text_space_text)
        self.formLayout.setLayout(22, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_config_text_space)
        self.label_config_text_break = QLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config_text_break.sizePolicy().hasHeightForWidth())
        self.label_config_text_break.setSizePolicy(sizePolicy)
        self.label_config_text_break.setObjectName("label_config_text_break")
        self.formLayout.setWidget(23, QFormLayout.ItemRole.LabelRole, self.label_config_text_break)
        self.horizontalLayout_config_text_break = QHBoxLayout()
        self.horizontalLayout_config_text_break.setObjectName("horizontalLayout_config_text_break")
        self.horizontalSlider_config_text_break = QSlider(parent=self.scrollAreaWidgetContents)
        self.horizontalSlider_config_text_break.setMinimum(1)
        self.horizontalSlider_config_text_break.setMaximum(150)
        self.horizontalSlider_config_text_break.setProperty("value", 80)
        self.horizontalSlider_config_text_break.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider_config_text_break.setObjectName("horizontalSlider_config_text_break")
        self.horizontalLayout_config_text_break.addWidget(self.horizontalSlider_config_text_break)
        self.label_config_text_break_text = QLabel(parent=self.scrollAreaWidgetContents)
        self.label_config_text_break_text.setMinimumSize(QSize(20, 0))
        self.label_config_text_break_text.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_config_text_break_text.setObjectName("label_config_text_break_text")
        self.horizontalLayout_config_text_break.addWidget(self.label_config_text_break_text)
        self.formLayout.setLayout(23, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_config_text_break)
        self.pushButton_config_load_font = QPushButton(parent=self.scrollAreaWidgetContents)
        self.pushButton_config_load_font.setMinimumSize(QSize(0, 30))
        self.pushButton_config_load_font.setAutoExclusive(False)
        self.pushButton_config_load_font.setObjectName("pushButton_config_load_font")
        self.formLayout.setWidget(24, QFormLayout.ItemRole.LabelRole, self.pushButton_config_load_font)
        self.verticalLayout_config_load_font = QVBoxLayout()
        self.verticalLayout_config_load_font.setObjectName("verticalLayout_config_load_font")
        self.label_config_example_text_text = QLabel(parent=self.scrollAreaWidgetContents)
        self.label_config_example_text_text.setObjectName("label_config_example_text_text")
        self.verticalLayout_config_load_font.addWidget(self.label_config_example_text_text)
        self.label_config_example_text = QLabel(parent=self.scrollAreaWidgetContents)
        self.label_config_example_text.setWordWrap(True)
        self.label_config_example_text.setObjectName("label_config_example_text")
        self.verticalLayout_config_load_font.addWidget(self.label_config_example_text)
        self.formLayout.setLayout(24, QFormLayout.ItemRole.FieldRole, self.verticalLayout_config_load_font)
        self.line_5 = QFrame(parent=self.scrollAreaWidgetContents)
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        self.formLayout.setWidget(25, QFormLayout.ItemRole.SpanningRole, self.line_5)
        self.label_config_text_editor_title = QLabel(parent=self.scrollAreaWidgetContents)
        self.label_config_text_editor_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_config_text_editor_title.setObjectName("label_config_text_editor_title")
        self.formLayout.setWidget(26, QFormLayout.ItemRole.SpanningRole, self.label_config_text_editor_title)
        self.plainTextEdit_config = QPlainTextEdit(parent=self.scrollAreaWidgetContents)
        self.plainTextEdit_config.setFrameShape(QFrame.Shape.StyledPanel)
        self.plainTextEdit_config.setFrameShadow(QFrame.Shadow.Sunken)
        self.plainTextEdit_config.setOverwriteMode(False)
        self.plainTextEdit_config.setObjectName("plainTextEdit_config")
        self.formLayout.setWidget(27, QFormLayout.ItemRole.SpanningRole, self.plainTextEdit_config)
        self.label_config_text_editor_description = QLabel(parent=self.scrollAreaWidgetContents)
        self.label_config_text_editor_description.setWordWrap(True)
        self.label_config_text_editor_description.setObjectName("label_config_text_editor_description")
        self.formLayout.setWidget(28, QFormLayout.ItemRole.SpanningRole, self.label_config_text_editor_description)
        self.line_6 = QFrame(parent=self.scrollAreaWidgetContents)
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_6.setObjectName("line_6")
        self.formLayout.setWidget(29, QFormLayout.ItemRole.SpanningRole, self.line_6)
        self.label_config_keywords_title = QLabel(parent=self.scrollAreaWidgetContents)
        self.label_config_keywords_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_config_keywords_title.setObjectName("label_config_keywords_title")
        self.formLayout.setWidget(31, QFormLayout.ItemRole.SpanningRole, self.label_config_keywords_title)
        self.horizontalLayout_config_name = QHBoxLayout()
        self.horizontalLayout_config_name.setObjectName("horizontalLayout_config_name")
        self.label_config_name = QLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config_name.sizePolicy().hasHeightForWidth())
        self.label_config_name.setSizePolicy(sizePolicy)
        self.label_config_name.setMinimumSize(QSize(60, 0))
        self.label_config_name.setObjectName("label_config_name")
        self.horizontalLayout_config_name.addWidget(self.label_config_name)
        self.lineEdit_config_name = QLineEdit(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_config_name.sizePolicy().hasHeightForWidth())
        self.lineEdit_config_name.setSizePolicy(sizePolicy)
        self.lineEdit_config_name.setMinimumSize(QSize(150, 0))
        self.lineEdit_config_name.setObjectName("lineEdit_config_name")
        self.horizontalLayout_config_name.addWidget(self.lineEdit_config_name)
        self.formLayout.setLayout(32, QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_config_name)
        self.horizontalLayout_config_cpf = QHBoxLayout()
        self.horizontalLayout_config_cpf.setObjectName("horizontalLayout_config_cpf")
        self.label_config_cpf = QLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config_cpf.sizePolicy().hasHeightForWidth())
        self.label_config_cpf.setSizePolicy(sizePolicy)
        self.label_config_cpf.setMinimumSize(QSize(60, 0))
        self.label_config_cpf.setObjectName("label_config_cpf")
        self.horizontalLayout_config_cpf.addWidget(self.label_config_cpf)
        self.lineEdit_config_cpf = QLineEdit(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_config_cpf.sizePolicy().hasHeightForWidth())
        self.lineEdit_config_cpf.setSizePolicy(sizePolicy)
        self.lineEdit_config_cpf.setObjectName("lineEdit_config_cpf")
        self.horizontalLayout_config_cpf.addWidget(self.lineEdit_config_cpf)
        self.formLayout.setLayout(33, QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_config_cpf)
        self.horizontalLayout_config_cnpj = QHBoxLayout()
        self.horizontalLayout_config_cnpj.setObjectName("horizontalLayout_config_cnpj")
        self.label_config_cnpj = QLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config_cnpj.sizePolicy().hasHeightForWidth())
        self.label_config_cnpj.setSizePolicy(sizePolicy)
        self.label_config_cnpj.setMinimumSize(QSize(60, 0))
        self.label_config_cnpj.setObjectName("label_config_cnpj")
        self.horizontalLayout_config_cnpj.addWidget(self.label_config_cnpj)
        self.lineEdit_config_cnpj = QLineEdit(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_config_cnpj.sizePolicy().hasHeightForWidth())
        self.lineEdit_config_cnpj.setSizePolicy(sizePolicy)
        self.lineEdit_config_cnpj.setObjectName("lineEdit_config_cnpj")
        self.horizontalLayout_config_cnpj.addWidget(self.lineEdit_config_cnpj)
        self.formLayout.setLayout(34, QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_config_cnpj)
        self.horizontalLayout_config_matricula = QHBoxLayout()
        self.horizontalLayout_config_matricula.setObjectName("horizontalLayout_config_matricula")
        self.label_config_matricula = QLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config_matricula.sizePolicy().hasHeightForWidth())
        self.label_config_matricula.setSizePolicy(sizePolicy)
        self.label_config_matricula.setMinimumSize(QSize(60, 0))
        self.label_config_matricula.setObjectName("label_config_matricula")
        self.horizontalLayout_config_matricula.addWidget(self.label_config_matricula)
        self.lineEdit_config_matricula = QLineEdit(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_config_matricula.sizePolicy().hasHeightForWidth())
        self.lineEdit_config_matricula.setSizePolicy(sizePolicy)
        self.lineEdit_config_matricula.setObjectName("lineEdit_config_matricula")
        self.horizontalLayout_config_matricula.addWidget(self.lineEdit_config_matricula)
        self.formLayout.setLayout(35, QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_config_matricula)
        self.horizontalLayout_config_cliente = QHBoxLayout()
        self.horizontalLayout_config_cliente.setObjectName("horizontalLayout_config_cliente")
        self.label_config_cliente = QLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config_cliente.sizePolicy().hasHeightForWidth())
        self.label_config_cliente.setSizePolicy(sizePolicy)
        self.label_config_cliente.setMinimumSize(QSize(60, 0))
        self.label_config_cliente.setObjectName("label_config_cliente")
        self.horizontalLayout_config_cliente.addWidget(self.label_config_cliente)
        self.lineEdit_config_cliente = QLineEdit(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_config_cliente.sizePolicy().hasHeightForWidth())
        self.lineEdit_config_cliente.setSizePolicy(sizePolicy)
        self.lineEdit_config_cliente.setObjectName("lineEdit_config_cliente")
        self.horizontalLayout_config_cliente.addWidget(self.lineEdit_config_cliente)
        self.formLayout.setLayout(36, QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_config_cliente)
        self.horizontalLayout_config_apolice = QHBoxLayout()
        self.horizontalLayout_config_apolice.setObjectName("horizontalLayout_config_apolice")
        self.label_config_apolice = QLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config_apolice.sizePolicy().hasHeightForWidth())
        self.label_config_apolice.setSizePolicy(sizePolicy)
        self.label_config_apolice.setMinimumSize(QSize(60, 0))
        self.label_config_apolice.setObjectName("label_config_apolice")
        self.horizontalLayout_config_apolice.addWidget(self.label_config_apolice)
        self.lineEdit_config_apolice = QLineEdit(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_config_apolice.sizePolicy().hasHeightForWidth())
        self.lineEdit_config_apolice.setSizePolicy(sizePolicy)
        self.lineEdit_config_apolice.setObjectName("lineEdit_config_apolice")
        self.horizontalLayout_config_apolice.addWidget(self.lineEdit_config_apolice)
        self.formLayout.setLayout(37, QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_config_apolice)
        self.horizontalLayout_config_capital = QHBoxLayout()
        self.horizontalLayout_config_capital.setObjectName("horizontalLayout_config_capital")
        self.label_config_capital = QLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config_capital.sizePolicy().hasHeightForWidth())
        self.label_config_capital.setSizePolicy(sizePolicy)
        self.label_config_capital.setMinimumSize(QSize(60, 0))
        self.label_config_capital.setObjectName("label_config_capital")
        self.horizontalLayout_config_capital.addWidget(self.label_config_capital)
        self.lineEdit_config_capital = QLineEdit(parent=self.scrollAreaWidgetContents)
        self.lineEdit_config_capital.setObjectName("lineEdit_config_capital")
        self.horizontalLayout_config_capital.addWidget(self.lineEdit_config_capital)
        self.formLayout.setLayout(38, QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_config_capital)
        self.horizontalLayout_config_cobertura = QHBoxLayout()
        self.horizontalLayout_config_cobertura.setObjectName("horizontalLayout_config_cobertura")
        self.label_config_cobertura = QLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config_cobertura.sizePolicy().hasHeightForWidth())
        self.label_config_cobertura.setSizePolicy(sizePolicy)
        self.label_config_cobertura.setMinimumSize(QSize(60, 0))
        self.label_config_cobertura.setObjectName("label_config_cobertura")
        self.horizontalLayout_config_cobertura.addWidget(self.label_config_cobertura)
        self.lineEdit_config_cobertura = QLineEdit(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_config_cobertura.sizePolicy().hasHeightForWidth())
        self.lineEdit_config_cobertura.setSizePolicy(sizePolicy)
        self.lineEdit_config_cobertura.setObjectName("lineEdit_config_cobertura")
        self.horizontalLayout_config_cobertura.addWidget(self.lineEdit_config_cobertura)
        self.formLayout.setLayout(39, QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_config_cobertura)
        self.horizontalLayout_config_grupo = QHBoxLayout()
        self.horizontalLayout_config_grupo.setObjectName("horizontalLayout_config_grupo")
        self.label_config_grupo = QLabel(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_config_grupo.sizePolicy().hasHeightForWidth())
        self.label_config_grupo.setSizePolicy(sizePolicy)
        self.label_config_grupo.setMinimumSize(QSize(60, 0))
        self.label_config_grupo.setObjectName("label_config_grupo")
        self.horizontalLayout_config_grupo.addWidget(self.label_config_grupo)
        self.lineEdit_config_grupo = QLineEdit(parent=self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_config_grupo.sizePolicy().hasHeightForWidth())
        self.lineEdit_config_grupo.setSizePolicy(sizePolicy)
        self.lineEdit_config_grupo.setMinimumSize(QSize(70, 0))
        self.lineEdit_config_grupo.setObjectName("lineEdit_config_grupo")
        self.horizontalLayout_config_grupo.addWidget(self.lineEdit_config_grupo)
        self.formLayout.setLayout(40, QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_config_grupo)
        self.label_config_keywords_description = QLabel(parent=self.scrollAreaWidgetContents)
        self.label_config_keywords_description.setWordWrap(True)
        self.label_config_keywords_description.setObjectName("label_config_keywords_description")
        self.formLayout.setWidget(41, QFormLayout.ItemRole.SpanningRole, self.label_config_keywords_description)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.tabWidget.addTab(self.tab_config, "")
        self.gridLayout_5.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        # Coisas adicionadas manualmente, e não pelo PyCreator. --------------------------------------------------------
        self.listWidget_singular_cobertura.addItems(get_coberturas(var.grupo_dir))
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
        self.lineEdit_config_grupo.setText(';'.join(var.grupo_keywords))
        self.comboBox_singular_grupo.addItems(get_grupo_values(var.grupo_dir))
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
        self.pushButton_config_grupo_source.clicked.connect(self.change_grupo_file)
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
        self.checkBox_singular_allow_grupo.toggled.connect(self.listWidget_singular_cobertura.setDisabled)
        self.checkBox_singular_allow_grupo.toggled.connect(self.comboBox_singular_grupo.setEnabled)
        self.lineEdit_config_grupo.textEdited.connect(self.change_grupo_keywords)
        self.lineEdit_config_capital.textEdited.connect(self.change_capital_keywords)
        self.horizontalSlider_config_text_size.valueChanged.connect(self.change_text_size)
        self.comboBox_config_font.currentTextChanged.connect(self.change_text_font)

        self.pushButton_multiple_output.setDefault(False)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_multiple_input.setText(_translate("MainWindow", "Selecionar arquivo"))
        self.label_multiple_input_header.setText(_translate("MainWindow", "Arquivo selecionado:"))
        self.pushButton_multiple_output.setText(_translate("MainWindow", "Selecionar diretório\n"
"de destino"))
        self.label_multiple_output_header.setText(_translate("MainWindow", "Diretório de destino selecionado:"))
        self.pushButton_multiple_emit.setText(_translate("MainWindow", "Emitir"))
        self.label_multiple_start.setText(_translate("MainWindow", "Início da vigência:"))
        self.label_multiple_end.setText(_translate("MainWindow", "Final da vigência:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_multiple), _translate("MainWindow", "Múltiplos"))
        self.pushButton_singular_emit.setText(_translate("MainWindow", "Emitir"))
        self.label_singular_name.setText(_translate("MainWindow", "Nome:"))
        self.label_singular_cpf.setText(_translate("MainWindow", "CPF:"))
        self.label_singular_matricula.setText(_translate("MainWindow", "Matrícula:"))
        self.label_singular_cnpj.setText(_translate("MainWindow", "CNPJ:"))
        self.label_singular_apolice.setText(_translate("MainWindow", "Apólice:"))
        self.label_singular_client.setText(_translate("MainWindow", "Cliente:"))
        self.label_singular_startdate.setText(_translate("MainWindow", "Início de vigência:"))
        self.label_singular_enddate.setText(_translate("MainWindow", "Fim de vigência:"))
        self.label_singular_capital.setText(_translate("MainWindow", "Capital:"))
        self.pushButton_singular_select_output.setText(_translate("MainWindow", "Selecionar diretório de destino"))
        self.label_singular_output_header.setText(_translate("MainWindow", "Diretório selecionado:"))
        self.checkBox_singular_allow_grupo.setText(_translate("MainWindow", "Usar grupos"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_singular), _translate("MainWindow", "Individual"))
        self.label_config_performance_title.setText(_translate("MainWindow", "Performance - threading e multiprocessamento"))
        self.label_config_max_threads.setText(_translate("MainWindow", "Quantidade máxima de threads:"))
        self.label_config_max_thread_number.setText(_translate("MainWindow", "150"))
        self.label_config_target_threads.setText(_translate("MainWindow", "Quantidade alvo de threads:"))
        self.label_config_target_thread_number.setText(_translate("MainWindow", "15"))
        self.label_config_max_processes.setText(_translate("MainWindow", "Quantiade máxima de processos:"))
        self.label_config_max_processes_number.setText(_translate("MainWindow", "4"))
        self.label_config_file_option_titles.setText(_translate("MainWindow", "Opções de arquivos"))
        self.pushButton_config_grupo_source.setText(_translate("MainWindow", "Trocar códigos de grupos"))
        self.label_config_selection_grupo.setText(_translate("MainWindow", "Seleção:"))
        self.pushButton_config_change_pdf_template.setText(_translate("MainWindow", "Trocar PDF modelo"))
        self.label_config_selection_pdf.setText(_translate("MainWindow", "Seleção:"))
        self.label_config_dates_title.setText(_translate("MainWindow", "Datas de vigência"))
        self.label_config_start_date.setText(_translate("MainWindow", "Data de vigência inicial padrão:"))
        self.label_config_end_date.setText(_translate("MainWindow", "Data de vigência final padrão"))
        self.label_config_data_input_and_output_title.setText(_translate("MainWindow", "Entrada e saída de dados"))
        self.pushButton_config_source.setText(_translate("MainWindow", "Trocar fonte de dados padrão"))
        self.label_config_selection_data_source.setText(_translate("MainWindow", "Seleção:"))
        self.pushButton_config_output_dir.setText(_translate("MainWindow", "Diretório padrão de salvamento"))
        self.label_config_selection_output_dir.setText(_translate("MainWindow", "Seleção:"))
        self.label_config_formatting_title.setText(_translate("MainWindow", "Formatação de texto"))
        self.label_config_font.setText(_translate("MainWindow", "Fonte:"))
        self.label_config_text_size.setText(_translate("MainWindow", "Tamanho do texto:"))
        self.label_config_text_size_text.setText(_translate("MainWindow", "10"))
        self.label_config_text_left.setText(_translate("MainWindow", "Distância do texto à esquerda:"))
        self.label_config_text_left_text.setText(_translate("MainWindow", "65"))
        self.label_config_text_right.setText(_translate("MainWindow", "Altura inicial do texto:"))
        self.label_config_text_height_text.setText(_translate("MainWindow", "620"))
        self.label_config_text_space.setText(_translate("MainWindow", "Espaçamento entre linhas:"))
        self.label_config_text_space_text.setText(_translate("MainWindow", "15"))
        self.label_config_text_break.setText(_translate("MainWindow", "Caracteres ante quebra de linha:"))
        self.label_config_text_break_text.setText(_translate("MainWindow", "80"))
        self.pushButton_config_load_font.setText(_translate("MainWindow", "Carregar nova fonte"))
        self.label_config_example_text_text.setText(_translate("MainWindow", "Texto exemplo para fonte selecionada:"))
        self.label_config_example_text.setText(_translate("MainWindow", "<html><head/><body><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla at risus. Quisque purus magna, auctor et, sagittis ac, posuere eu, lectus. Nam mattis, felis ut adipiscing. 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.</p></body></html>"))
        self.label_config_text_editor_title.setText(_translate("MainWindow", "Editor de texto do PDF"))
        self.label_config_text_editor_description.setText(_translate("MainWindow", "<html><head/><body><p>Use os formato &lt;NOME&gt;, &lt;CPF&gt;, &lt;MATRICULA&gt;, &lt;CLIENTE&gt;, &lt;CNPJ&gt;, &lt;APOLICE&gt;, &lt;COBERTURA&gt;, &lt;COMECO&gt; e &lt;FINAL&gt; para os respectivos campos dinâmicos. Não digite os campos dinâmicos com acentos, ou eles não serão interpretados corretamente pelo programa. Além das quebras de linhas manuais o programa divide as linhas automaticamente caso estejam muito grandes.</p></body></html>"))
        self.label_config_keywords_title.setText(_translate("MainWindow", "Palavras-chave"))
        self.label_config_name.setText(_translate("MainWindow", "Nome:"))
        self.label_config_cpf.setText(_translate("MainWindow", "CPF:"))
        self.label_config_cnpj.setText(_translate("MainWindow", "CNPJ:"))
        self.label_config_matricula.setText(_translate("MainWindow", "Matrícula:"))
        self.label_config_cliente.setText(_translate("MainWindow", "Cliente:"))
        self.label_config_apolice.setText(_translate("MainWindow", "Apólice:"))
        self.label_config_capital.setText(_translate("MainWindow", "Capital:"))
        self.label_config_cobertura.setText(_translate("MainWindow", "Cobertura:"))
        self.label_config_grupo.setText(_translate("MainWindow", "Grupos:"))
        self.label_config_keywords_description.setText(_translate("MainWindow", "<html><head/><body><p>Estas são palavras-chaves que o programa procurará na primeira linha das planilhas numa tentativa de encontrar as colunas dos campos repectivos. Letras maiúsculas e acentos serão desconsiderados. Separe cada palavra-chave com um ponto e vírgula ( ; ). Uma planilha não precisa ter simultaneamente uma coluna para cobertura e para grupos, apenas um é necessário. Ademais, se o programa não encontrar todas as colunas necessárias, ele lhe perguntará se deve prosseguir ou abortar.</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_config), _translate("MainWindow", "Configurações"))

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
        self.label_config_grupo_text.setText(var.grupo_dir)
        self.label_config_pdf_text.setText(var.template_dir)

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

        while active_count() > 2:  # Quando só sobra a thread da janela e a thread da barra de progresso
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

        if var.headers['cobe'] == '' and not any(var.cobertura_keywords) and var.headers['grupo'] == '' and not any(var.grupo_keywords) and not var.abort_emission:
            warning = QMessageBox()
            warning.setWindowTitle('AVISO')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Abort)
            warning.setText('Campos "cobertura" ou "grupos" não foram encontrados na planilha\n'
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
        grupo_df = get_grupo(var.grupo_dir)

        if self.comboBox_singular_grupo.isEnabled():
            grupo = self.comboBox_singular_grupo.currentText()
            cobe = False

        else:
            try:
                cobe = self.listWidget_singular_cobertura.selectedItems()[0].text()
            except (AttributeError, IndexError):
                cobe = ''

            grupo = False

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
            if grupo is False:
                emit_singular(name, cpf, cnpj, matr, clie, apol, capi, cobe, '')
            else:
                emit_singular(name, cpf, cnpj, matr, clie, apol, capi, '', grupo_df.loc[grupo])

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

    def change_grupo_file(self):
        file = QFileDialog.getOpenFileName()[0]

        if file[-4:].lower() in ('xlsx', '.xls', '.csv', 'xlsm'):
            var.grupo_dir = file.replace(var.work_directory, '')
            push('grupo_dir', var.grupo_dir)

            self.label_config_grupo_text.setText(var.grupo_dir)
            self.label_console.setText('Arquivo com códigos de grupos atualizado.')

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

    def change_grupo_keywords(self):
        keywords = []
        for i in self.lineEdit_config_grupo.text().split(';'):
            keywords.append(unidecode(i.strip().lower()))

        var.grupo_keywords = keywords
        push('grupo_keywords', keywords)

        self.label_console.setText('Palavras-chave para grupo atualizadas.')
