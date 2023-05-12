from PySide6.QtCore import (QCoreApplication, QDate, QMetaObject, QSize, Qt)
from PySide6.QtWidgets import (QDateEdit, QFrame, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QListWidget,
                               QProgressBar, QPushButton, QSizePolicy, QTabWidget, QWidget, QMessageBox, QFileDialog,
                               QVBoxLayout, QFormLayout, QSlider)
from emitter import emit_singular, emit_from_source
from reader import get_coberturas, save_configs
from multiprocessing import cpu_count
from PySide6.QtGui import QIcon
from threading import Thread
from neat import name as nm
from neat import cpf as cp
from time import sleep
import var


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(780, 540)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QSize(0, 30))
        self.tab_multiple = QWidget()
        self.tab_multiple.setObjectName(u"tab_multiple")
        self.gridLayout = QGridLayout(self.tab_multiple)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_multiple_select = QVBoxLayout()
        self.verticalLayout_multiple_select.setObjectName(u"verticalLayout_multiple_select")
        self.pushButton_multiple_input = QPushButton(self.tab_multiple)
        self.pushButton_multiple_input.setObjectName(u"pushButton_multiple_input")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_multiple_input.sizePolicy().hasHeightForWidth())
        self.pushButton_multiple_input.setSizePolicy(sizePolicy1)
        self.pushButton_multiple_input.setMinimumSize(QSize(0, 40))
        self.pushButton_multiple_input.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout_multiple_select.addWidget(self.pushButton_multiple_input)

        self.label_multiple_input_header = QLabel(self.tab_multiple)
        self.label_multiple_input_header.setObjectName(u"label_multiple_input_header")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_multiple_input_header.sizePolicy().hasHeightForWidth())
        self.label_multiple_input_header.setSizePolicy(sizePolicy2)

        self.verticalLayout_multiple_select.addWidget(self.label_multiple_input_header)

        self.label_multiple_input_text = QLabel(self.tab_multiple)
        self.label_multiple_input_text.setObjectName(u"label_multiple_input_text")
        sizePolicy1.setHeightForWidth(self.label_multiple_input_text.sizePolicy().hasHeightForWidth())
        self.label_multiple_input_text.setSizePolicy(sizePolicy1)

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
        sizePolicy2.setHeightForWidth(self.label_multiple_output_header.sizePolicy().hasHeightForWidth())
        self.label_multiple_output_header.setSizePolicy(sizePolicy2)

        self.verticalLayout_multiple_select.addWidget(self.label_multiple_output_header)

        self.label_multiple_output_text = QLabel(self.tab_multiple)
        self.label_multiple_output_text.setObjectName(u"label_multiple_output_text")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_multiple_output_text.sizePolicy().hasHeightForWidth())
        self.label_multiple_output_text.setSizePolicy(sizePolicy3)

        self.verticalLayout_multiple_select.addWidget(self.label_multiple_output_text)


        self.gridLayout.addLayout(self.verticalLayout_multiple_select, 0, 0, 1, 1)

        self.horizontalLayout_multiple_bar_emit = QHBoxLayout()
        self.horizontalLayout_multiple_bar_emit.setObjectName(u"horizontalLayout_multiple_bar_emit")
        self.progressBar_multiple = QProgressBar(self.tab_multiple)
        self.progressBar_multiple.setObjectName(u"progressBar_multiple")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.progressBar_multiple.sizePolicy().hasHeightForWidth())
        self.progressBar_multiple.setSizePolicy(sizePolicy4)
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
        sizePolicy3.setHeightForWidth(self.label_multiple_start.sizePolicy().hasHeightForWidth())
        self.label_multiple_start.setSizePolicy(sizePolicy3)

        self.verticalLayout_multiple_dates.addWidget(self.label_multiple_start)

        self.dateEdit_multiple_start = QDateEdit(self.tab_multiple)
        self.dateEdit_multiple_start.setObjectName(u"dateEdit_multiple_start")
        sizePolicy1.setHeightForWidth(self.dateEdit_multiple_start.sizePolicy().hasHeightForWidth())
        self.dateEdit_multiple_start.setSizePolicy(sizePolicy1)
        self.dateEdit_multiple_start.setProperty("showGroupSeparator", False)
        self.dateEdit_multiple_start.setMaximumDate(QDate(2030, 12, 31))
        self.dateEdit_multiple_start.setMinimumDate(QDate(2023, 1, 1))
        self.dateEdit_multiple_start.setCalendarPopup(True)

        self.verticalLayout_multiple_dates.addWidget(self.dateEdit_multiple_start)

        self.label_multiple_end = QLabel(self.tab_multiple)
        self.label_multiple_end.setObjectName(u"label_multiple_end")
        sizePolicy3.setHeightForWidth(self.label_multiple_end.sizePolicy().hasHeightForWidth())
        self.label_multiple_end.setSizePolicy(sizePolicy3)

        self.verticalLayout_multiple_dates.addWidget(self.label_multiple_end)

        self.dateEdit_multiple_end = QDateEdit(self.tab_multiple)
        self.dateEdit_multiple_end.setObjectName(u"dateEdit_multiple_end")
        self.dateEdit_multiple_end.setMaximumDate(QDate(2030, 12, 31))
        self.dateEdit_multiple_end.setMinimumDate(QDate(2023, 1, 1))
        self.dateEdit_multiple_end.setCalendarPopup(True)

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
        self.formLayout_singular_write = QFormLayout()
        self.formLayout_singular_write.setObjectName(u"formLayout_singular_write")
        self.label_singular_name = QLabel(self.tab_singular)
        self.label_singular_name.setObjectName(u"label_singular_name")
        sizePolicy2.setHeightForWidth(self.label_singular_name.sizePolicy().hasHeightForWidth())
        self.label_singular_name.setSizePolicy(sizePolicy2)

        self.formLayout_singular_write.setWidget(0, QFormLayout.LabelRole, self.label_singular_name)

        self.lineEdit_singular_name = QLineEdit(self.tab_singular)
        self.lineEdit_singular_name.setObjectName(u"lineEdit_singular_name")

        self.formLayout_singular_write.setWidget(0, QFormLayout.FieldRole, self.lineEdit_singular_name)

        self.label_singular_cpf = QLabel(self.tab_singular)
        self.label_singular_cpf.setObjectName(u"label_singular_cpf")
        sizePolicy2.setHeightForWidth(self.label_singular_cpf.sizePolicy().hasHeightForWidth())
        self.label_singular_cpf.setSizePolicy(sizePolicy2)

        self.formLayout_singular_write.setWidget(1, QFormLayout.LabelRole, self.label_singular_cpf)

        self.label_singular_matricula = QLabel(self.tab_singular)
        self.label_singular_matricula.setObjectName(u"label_singular_matricula")
        sizePolicy2.setHeightForWidth(self.label_singular_matricula.sizePolicy().hasHeightForWidth())
        self.label_singular_matricula.setSizePolicy(sizePolicy2)

        self.formLayout_singular_write.setWidget(2, QFormLayout.LabelRole, self.label_singular_matricula)

        self.label_singular_cnpj = QLabel(self.tab_singular)
        self.label_singular_cnpj.setObjectName(u"label_singular_cnpj")
        sizePolicy2.setHeightForWidth(self.label_singular_cnpj.sizePolicy().hasHeightForWidth())
        self.label_singular_cnpj.setSizePolicy(sizePolicy2)

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
        sizePolicy2.setHeightForWidth(self.label_singular_apolice.sizePolicy().hasHeightForWidth())
        self.label_singular_apolice.setSizePolicy(sizePolicy2)

        self.formLayout_singular_write.setWidget(5, QFormLayout.LabelRole, self.label_singular_apolice)

        self.lineEdit_singular_apolice = QLineEdit(self.tab_singular)
        self.lineEdit_singular_apolice.setObjectName(u"lineEdit_singular_apolice")

        self.formLayout_singular_write.setWidget(5, QFormLayout.FieldRole, self.lineEdit_singular_apolice)

        self.label_singular_client = QLabel(self.tab_singular)
        self.label_singular_client.setObjectName(u"label_singular_client")
        sizePolicy2.setHeightForWidth(self.label_singular_client.sizePolicy().hasHeightForWidth())
        self.label_singular_client.setSizePolicy(sizePolicy2)

        self.formLayout_singular_write.setWidget(3, QFormLayout.LabelRole, self.label_singular_client)

        self.lineEdit_singular_client = QLineEdit(self.tab_singular)
        self.lineEdit_singular_client.setObjectName(u"lineEdit_singular_client")

        self.formLayout_singular_write.setWidget(3, QFormLayout.FieldRole, self.lineEdit_singular_client)

        self.label_singular_startdate = QLabel(self.tab_singular)
        self.label_singular_startdate.setObjectName(u"label_singular_startdate")
        sizePolicy2.setHeightForWidth(self.label_singular_startdate.sizePolicy().hasHeightForWidth())
        self.label_singular_startdate.setSizePolicy(sizePolicy2)

        self.formLayout_singular_write.setWidget(6, QFormLayout.LabelRole, self.label_singular_startdate)

        self.label_singular_enddate = QLabel(self.tab_singular)
        self.label_singular_enddate.setObjectName(u"label_singular_enddate")
        sizePolicy2.setHeightForWidth(self.label_singular_enddate.sizePolicy().hasHeightForWidth())
        self.label_singular_enddate.setSizePolicy(sizePolicy2)

        self.formLayout_singular_write.setWidget(7, QFormLayout.LabelRole, self.label_singular_enddate)

        self.dateEdit_singular_start = QDateEdit(self.tab_singular)
        self.dateEdit_singular_start.setObjectName(u"dateEdit_singular_start")
        self.dateEdit_singular_start.setCalendarPopup(True)

        self.formLayout_singular_write.setWidget(6, QFormLayout.FieldRole, self.dateEdit_singular_start)

        self.dateEdit_singular_end = QDateEdit(self.tab_singular)
        self.dateEdit_singular_end.setObjectName(u"dateEdit_singular_end")
        self.dateEdit_singular_end.setCalendarPopup(True)

        self.formLayout_singular_write.setWidget(7, QFormLayout.FieldRole, self.dateEdit_singular_end)

        self.gridLayout_2.addLayout(self.formLayout_singular_write, 1, 1, 1, 1)

        self.horizontalLayout_singular_select_output = QHBoxLayout()
        self.horizontalLayout_singular_select_output.setObjectName(u"horizontalLayout_singular_select_output")
        self.pushButton_singular_select_output = QPushButton(self.tab_singular)
        self.pushButton_singular_select_output.setObjectName(u"pushButton_singular_select_output")

        self.horizontalLayout_singular_select_output.addWidget(self.pushButton_singular_select_output)

        self.label_singular_output_header = QLabel(self.tab_singular)
        self.label_singular_output_header.setObjectName(u"label_singular_output_header")
        sizePolicy2.setHeightForWidth(self.label_singular_output_header.sizePolicy().hasHeightForWidth())
        self.label_singular_output_header.setSizePolicy(sizePolicy2)

        self.horizontalLayout_singular_select_output.addWidget(self.label_singular_output_header)

        self.label_singular_output_text = QLabel(self.tab_singular)
        self.label_singular_output_text.setObjectName(u"label_singular_output_text")
        sizePolicy4.setHeightForWidth(self.label_singular_output_text.sizePolicy().hasHeightForWidth())
        self.label_singular_output_text.setSizePolicy(sizePolicy4)

        self.horizontalLayout_singular_select_output.addWidget(self.label_singular_output_text)


        self.gridLayout_2.addLayout(self.horizontalLayout_singular_select_output, 0, 0, 1, 2)

        self.listWidget_singular_cobertura = QListWidget(self.tab_singular)
        self.listWidget_singular_cobertura.setObjectName(u"listWidget_singular_cobertura")

        self.gridLayout_2.addWidget(self.listWidget_singular_cobertura, 1, 0, 2, 1)

        self.pushButton_singular_emit = QPushButton(self.tab_singular)
        self.pushButton_singular_emit.setObjectName(u"pushButton_singular_emit")
        self.pushButton_singular_emit.setMinimumSize(QSize(0, 40))
        self.pushButton_singular_emit.setMaximumSize(QSize(200, 16777215))
        self.pushButton_singular_emit.setAutoRepeat(False)

        self.gridLayout_2.addWidget(self.pushButton_singular_emit, 2, 1, 1, 1)

        self.tabWidget.addTab(self.tab_singular, "")
        self.tab_config = QWidget()
        self.tab_config.setObjectName(u"tab_config")
        self.verticalLayout_2 = QVBoxLayout(self.tab_config)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout_config_all = QFormLayout()
        self.formLayout_config_all.setObjectName(u"formLayout_config_all")
        self.label_config_max_threads = QLabel(self.tab_config)
        self.label_config_max_threads.setObjectName(u"label_config_max_threads")
        sizePolicy2.setHeightForWidth(self.label_config_max_threads.sizePolicy().hasHeightForWidth())
        self.label_config_max_threads.setSizePolicy(sizePolicy2)

        self.formLayout_config_all.setWidget(0, QFormLayout.LabelRole, self.label_config_max_threads)

        self.horizontalLayout_config_max_threads = QHBoxLayout()
        self.horizontalLayout_config_max_threads.setObjectName(u"horizontalLayout_config_max_threads")
        self.horizontalSlider_config_max_threads = QSlider(self.tab_config)
        self.horizontalSlider_config_max_threads.setObjectName(u"horizontalSlider_config_max_threads")
        self.horizontalSlider_config_max_threads.setMinimum(4)
        self.horizontalSlider_config_max_threads.setMaximum(150)
        self.horizontalSlider_config_max_threads.setSingleStep(1)
        self.horizontalSlider_config_max_threads.setOrientation(Qt.Horizontal)

        self.horizontalLayout_config_max_threads.addWidget(self.horizontalSlider_config_max_threads)

        self.label_config_max_thread_number = QLabel(self.tab_config)
        self.label_config_max_thread_number.setObjectName(u"label_config_max_thread_number")
        sizePolicy2.setHeightForWidth(self.label_config_max_thread_number.sizePolicy().hasHeightForWidth())
        self.label_config_max_thread_number.setSizePolicy(sizePolicy2)
        self.label_config_max_thread_number.setMinimumSize(QSize(20, 0))
        self.label_config_max_thread_number.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_config_max_threads.addWidget(self.label_config_max_thread_number)


        self.formLayout_config_all.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_config_max_threads)

        self.label_config_target_threads = QLabel(self.tab_config)
        self.label_config_target_threads.setObjectName(u"label_config_target_threads")
        sizePolicy2.setHeightForWidth(self.label_config_target_threads.sizePolicy().hasHeightForWidth())
        self.label_config_target_threads.setSizePolicy(sizePolicy2)

        self.formLayout_config_all.setWidget(1, QFormLayout.LabelRole, self.label_config_target_threads)

        self.horizontalLayout_config_target_threads = QHBoxLayout()
        self.horizontalLayout_config_target_threads.setObjectName(u"horizontalLayout_config_target_threads")
        self.horizontalSlider_config_target_threads = QSlider(self.tab_config)
        self.horizontalSlider_config_target_threads.setObjectName(u"horizontalSlider_config_target_threads")
        self.horizontalSlider_config_target_threads.setMinimum(4)
        self.horizontalSlider_config_target_threads.setMaximum(150)
        self.horizontalSlider_config_target_threads.setOrientation(Qt.Horizontal)

        self.horizontalLayout_config_target_threads.addWidget(self.horizontalSlider_config_target_threads)

        self.label_config_target_thread_number = QLabel(self.tab_config)
        self.label_config_target_thread_number.setObjectName(u"label_config_target_thread_number")
        sizePolicy2.setHeightForWidth(self.label_config_target_thread_number.sizePolicy().hasHeightForWidth())
        self.label_config_target_thread_number.setSizePolicy(sizePolicy2)
        self.label_config_target_thread_number.setMinimumSize(QSize(20, 0))
        self.label_config_target_thread_number.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_config_target_threads.addWidget(self.label_config_target_thread_number)


        self.formLayout_config_all.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_config_target_threads)

        self.label_config_max_processes = QLabel(self.tab_config)
        self.label_config_max_processes.setObjectName(u"label_config_max_processes")
        sizePolicy2.setHeightForWidth(self.label_config_max_processes.sizePolicy().hasHeightForWidth())
        self.label_config_max_processes.setSizePolicy(sizePolicy2)

        self.formLayout_config_all.setWidget(2, QFormLayout.LabelRole, self.label_config_max_processes)

        self.horizontalLayout_config_max_processes = QHBoxLayout()
        self.horizontalLayout_config_max_processes.setObjectName(u"horizontalLayout_config_max_processes")
        self.horizontalSlider_config_max_processes = QSlider(self.tab_config)
        self.horizontalSlider_config_max_processes.setObjectName(u"horizontalSlider_config_max_processes")
        self.horizontalSlider_config_max_processes.setMinimum(1)
        self.horizontalSlider_config_max_processes.setOrientation(Qt.Horizontal)

        self.horizontalLayout_config_max_processes.addWidget(self.horizontalSlider_config_max_processes)

        self.label_config_max_processes_number = QLabel(self.tab_config)
        self.label_config_max_processes_number.setObjectName(u"label_config_max_processes_number")
        sizePolicy2.setHeightForWidth(self.label_config_max_processes_number.sizePolicy().hasHeightForWidth())
        self.label_config_max_processes_number.setSizePolicy(sizePolicy2)
        self.label_config_max_processes_number.setMinimumSize(QSize(20, 0))
        self.label_config_max_processes_number.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_config_max_processes.addWidget(self.label_config_max_processes_number)


        self.formLayout_config_all.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_config_max_processes)

        self.line = QFrame(self.tab_config)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.formLayout_config_all.setWidget(3, QFormLayout.SpanningRole, self.line)

        self.pushButton_config_cobertura_source = QPushButton(self.tab_config)
        self.pushButton_config_cobertura_source.setObjectName(u"pushButton_config_cobertura_source")
        self.pushButton_config_cobertura_source.setMinimumSize(QSize(0, 30))

        self.formLayout_config_all.setWidget(4, QFormLayout.LabelRole, self.pushButton_config_cobertura_source)

        self.horizontalLayout_config_cobertura_source = QHBoxLayout()
        self.horizontalLayout_config_cobertura_source.setObjectName(u"horizontalLayout_config_cobertura_source")
        self.label_config_selection_cobertura = QLabel(self.tab_config)
        self.label_config_selection_cobertura.setObjectName(u"label_config_selection_cobertura")
        sizePolicy2.setHeightForWidth(self.label_config_selection_cobertura.sizePolicy().hasHeightForWidth())
        self.label_config_selection_cobertura.setSizePolicy(sizePolicy2)

        self.horizontalLayout_config_cobertura_source.addWidget(self.label_config_selection_cobertura)

        self.label_config_cobertura_text = QLabel(self.tab_config)
        self.label_config_cobertura_text.setObjectName(u"label_config_cobertura_text")
        sizePolicy4.setHeightForWidth(self.label_config_cobertura_text.sizePolicy().hasHeightForWidth())
        self.label_config_cobertura_text.setSizePolicy(sizePolicy4)

        self.horizontalLayout_config_cobertura_source.addWidget(self.label_config_cobertura_text)


        self.formLayout_config_all.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout_config_cobertura_source)

        self.pushButton_config_cnv_source = QPushButton(self.tab_config)
        self.pushButton_config_cnv_source.setObjectName(u"pushButton_config_cnv_source")
        self.pushButton_config_cnv_source.setMinimumSize(QSize(0, 30))

        self.formLayout_config_all.setWidget(5, QFormLayout.LabelRole, self.pushButton_config_cnv_source)

        self.horizontalLayout_config_cnv_source = QHBoxLayout()
        self.horizontalLayout_config_cnv_source.setObjectName(u"horizontalLayout_config_cnv_source")
        self.label_config_selection_cnv = QLabel(self.tab_config)
        self.label_config_selection_cnv.setObjectName(u"label_config_selection_cnv")
        sizePolicy2.setHeightForWidth(self.label_config_selection_cnv.sizePolicy().hasHeightForWidth())
        self.label_config_selection_cnv.setSizePolicy(sizePolicy2)

        self.horizontalLayout_config_cnv_source.addWidget(self.label_config_selection_cnv)

        self.label_config_cnv_text = QLabel(self.tab_config)
        self.label_config_cnv_text.setObjectName(u"label_config_cnv_text")
        sizePolicy4.setHeightForWidth(self.label_config_cnv_text.sizePolicy().hasHeightForWidth())
        self.label_config_cnv_text.setSizePolicy(sizePolicy4)

        self.horizontalLayout_config_cnv_source.addWidget(self.label_config_cnv_text)


        self.formLayout_config_all.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout_config_cnv_source)

        self.pushButton_config_change_pdf_template = QPushButton(self.tab_config)
        self.pushButton_config_change_pdf_template.setObjectName(u"pushButton_config_change_pdf_template")
        self.pushButton_config_change_pdf_template.setMinimumSize(QSize(0, 30))

        self.formLayout_config_all.setWidget(6, QFormLayout.LabelRole, self.pushButton_config_change_pdf_template)

        self.horizontalLayout_config_pdf_template = QHBoxLayout()
        self.horizontalLayout_config_pdf_template.setObjectName(u"horizontalLayout_config_pdf_template")
        self.label_config_selection_pdf = QLabel(self.tab_config)
        self.label_config_selection_pdf.setObjectName(u"label_config_selection_pdf")
        sizePolicy2.setHeightForWidth(self.label_config_selection_pdf.sizePolicy().hasHeightForWidth())
        self.label_config_selection_pdf.setSizePolicy(sizePolicy2)

        self.horizontalLayout_config_pdf_template.addWidget(self.label_config_selection_pdf)

        self.label_config_pdf_text = QLabel(self.tab_config)
        self.label_config_pdf_text.setObjectName(u"label_config_pdf_text")
        sizePolicy4.setHeightForWidth(self.label_config_pdf_text.sizePolicy().hasHeightForWidth())
        self.label_config_pdf_text.setSizePolicy(sizePolicy4)

        self.horizontalLayout_config_pdf_template.addWidget(self.label_config_pdf_text)


        self.formLayout_config_all.setLayout(6, QFormLayout.FieldRole, self.horizontalLayout_config_pdf_template)

        self.label_config_start_date = QLabel(self.tab_config)
        self.label_config_start_date.setObjectName(u"label_config_start_date")
        sizePolicy2.setHeightForWidth(self.label_config_start_date.sizePolicy().hasHeightForWidth())
        self.label_config_start_date.setSizePolicy(sizePolicy2)

        self.formLayout_config_all.setWidget(8, QFormLayout.LabelRole, self.label_config_start_date)

        self.dateEdit_config_start = QDateEdit(self.tab_config)
        self.dateEdit_config_start.setObjectName(u"dateEdit_config_start")
        self.dateEdit_config_start.setMaximumDate(QDate(2030, 12, 31))
        self.dateEdit_config_start.setMinimumDate(QDate(2023, 1, 1))
        self.dateEdit_config_start.setCalendarPopup(True)

        self.formLayout_config_all.setWidget(8, QFormLayout.FieldRole, self.dateEdit_config_start)

        self.line_2 = QFrame(self.tab_config)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.formLayout_config_all.setWidget(7, QFormLayout.SpanningRole, self.line_2)

        self.label_config_end_date = QLabel(self.tab_config)
        self.label_config_end_date.setObjectName(u"label_config_end_date")
        sizePolicy2.setHeightForWidth(self.label_config_end_date.sizePolicy().hasHeightForWidth())
        self.label_config_end_date.setSizePolicy(sizePolicy2)

        self.formLayout_config_all.setWidget(9, QFormLayout.LabelRole, self.label_config_end_date)

        self.dateEdit_config_end = QDateEdit(self.tab_config)
        self.dateEdit_config_end.setObjectName(u"dateEdit_config_end")
        self.dateEdit_config_end.setMaximumDate(QDate(2030, 12, 31))
        self.dateEdit_config_end.setMinimumDate(QDate(2023, 1, 1))
        self.dateEdit_config_end.setCalendarPopup(True)

        self.formLayout_config_all.setWidget(9, QFormLayout.FieldRole, self.dateEdit_config_end)

        self.pushButton_config_source = QPushButton(self.tab_config)
        self.pushButton_config_source.setObjectName(u"pushButton_config_source")
        self.pushButton_config_source.setMinimumSize(QSize(0, 30))

        self.formLayout_config_all.setWidget(11, QFormLayout.LabelRole, self.pushButton_config_source)

        self.horizontalLayout_config_data_source = QHBoxLayout()
        self.horizontalLayout_config_data_source.setObjectName(u"horizontalLayout_config_data_source")
        self.label_config_selection_data_source = QLabel(self.tab_config)
        self.label_config_selection_data_source.setObjectName(u"label_config_selection_data_source")
        sizePolicy2.setHeightForWidth(self.label_config_selection_data_source.sizePolicy().hasHeightForWidth())
        self.label_config_selection_data_source.setSizePolicy(sizePolicy2)

        self.horizontalLayout_config_data_source.addWidget(self.label_config_selection_data_source)

        self.label_config_source_text = QLabel(self.tab_config)
        self.label_config_source_text.setObjectName(u"label_config_source_text")
        sizePolicy4.setHeightForWidth(self.label_config_source_text.sizePolicy().hasHeightForWidth())
        self.label_config_source_text.setSizePolicy(sizePolicy4)

        self.horizontalLayout_config_data_source.addWidget(self.label_config_source_text)


        self.formLayout_config_all.setLayout(11, QFormLayout.FieldRole, self.horizontalLayout_config_data_source)

        self.line_3 = QFrame(self.tab_config)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.formLayout_config_all.setWidget(10, QFormLayout.SpanningRole, self.line_3)

        self.pushButton_config_output_dir = QPushButton(self.tab_config)
        self.pushButton_config_output_dir.setObjectName(u"pushButton_config_output_dir")
        self.pushButton_config_output_dir.setMinimumSize(QSize(0, 30))

        self.formLayout_config_all.setWidget(12, QFormLayout.LabelRole, self.pushButton_config_output_dir)

        self.horizontalLayout_config_default_output_dir = QHBoxLayout()
        self.horizontalLayout_config_default_output_dir.setObjectName(u"horizontalLayout_config_default_output_dir")
        self.label_config_selection_output_dir = QLabel(self.tab_config)
        self.label_config_selection_output_dir.setObjectName(u"label_config_selection_output_dir")
        sizePolicy2.setHeightForWidth(self.label_config_selection_output_dir.sizePolicy().hasHeightForWidth())
        self.label_config_selection_output_dir.setSizePolicy(sizePolicy2)

        self.horizontalLayout_config_default_output_dir.addWidget(self.label_config_selection_output_dir)

        self.label_config_output_dir_text = QLabel(self.tab_config)
        self.label_config_output_dir_text.setObjectName(u"label_config_output_dir_text")
        sizePolicy4.setHeightForWidth(self.label_config_output_dir_text.sizePolicy().hasHeightForWidth())
        self.label_config_output_dir_text.setSizePolicy(sizePolicy4)

        self.horizontalLayout_config_default_output_dir.addWidget(self.label_config_output_dir_text)


        self.formLayout_config_all.setLayout(12, QFormLayout.FieldRole, self.horizontalLayout_config_default_output_dir)


        self.verticalLayout_2.addLayout(self.formLayout_config_all)

        self.pushButton_config_confirm = QPushButton(self.tab_config)
        self.pushButton_config_confirm.setObjectName(u"pushButton_config_confirm")
        self.pushButton_config_confirm.setMinimumSize(QSize(0, 40))
        self.pushButton_config_confirm.setMaximumSize(QSize(150, 16777215))
        self.pushButton_config_confirm.setToolTipDuration(0)
        self.pushButton_config_confirm.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_2.addWidget(self.pushButton_config_confirm)

        self.tabWidget.addTab(self.tab_config, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.label_console = QLabel(self.centralwidget)
        self.label_console.setObjectName(u"label_console")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_console.sizePolicy().hasHeightForWidth())
        self.label_console.setSizePolicy(sizePolicy5)
        self.label_console.setAlignment(Qt.AlignCenter)
        self.label_console.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_console)

        MainWindow.setCentralWidget(self.centralwidget)

        # Coisas adicionadas manualmente, e não pelo PyCreator. --------------------------------------------------------
        MainWindow.setWindowIcon(QIcon('dados/ícone.ico'))
        self.listWidget_singular_cobertura.addItems(get_coberturas(var.coberturas_path))
        self.horizontalSlider_config_max_threads.setValue(var.max_threads)
        self.horizontalSlider_config_target_threads.setValue(var.target_threads)
        self.horizontalSlider_config_max_processes.setMaximum(cpu_count())
        self.horizontalSlider_config_max_processes.setValue(var.max_processes)
        self.dateEdit_multiple_start.setDate(QDate(int(var.start_period[6:11]), int(var.start_period[3:5]), int(var.start_period[:2])))
        self.dateEdit_multiple_end.setDate(QDate(int(var.end_period[6:11]), int(var.end_period[3:5]), int(var.end_period[:2])))
        self.dateEdit_singular_start.setDate(QDate(int(var.start_period[6:11]), int(var.start_period[3:5]), int(var.start_period[:2])))
        self.dateEdit_singular_end.setDate(QDate(int(var.end_period[6:11]), int(var.end_period[3:5]), int(var.end_period[:2])))
        self.dateEdit_config_start.setDate(QDate(int(var.start_period[6:11]), int(var.start_period[3:5]), int(var.start_period[:2])))
        self.dateEdit_config_end.setDate(QDate(int(var.end_period[6:11]), int(var.end_period[3:5]), int(var.end_period[:2])))
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
        self.horizontalSlider_config_max_threads.valueChanged.connect(self.label_config_max_thread_number.setNum)
        self.horizontalSlider_config_target_threads.valueChanged.connect(self.label_config_target_thread_number.setNum)
        self.horizontalSlider_config_max_processes.valueChanged.connect(self.label_config_max_processes_number.setNum)
        self.pushButton_config_confirm.clicked.connect(self.change_configs)

        self.pushButton_multiple_output.setDefault(False)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
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
        self.label_singular_name.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.label_singular_cpf.setText(QCoreApplication.translate("MainWindow", u"CPF:", None))
        self.label_singular_matricula.setText(QCoreApplication.translate("MainWindow", u"Matr\u00edcula:", None))
        self.label_singular_cnpj.setText(QCoreApplication.translate("MainWindow", u"CNPJ:", None))
        self.label_singular_apolice.setText(QCoreApplication.translate("MainWindow", u"Ap\u00f3lice:", None))
        self.label_singular_client.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.label_singular_startdate.setText(QCoreApplication.translate("MainWindow", u"In\u00edcio de vig\u00eancia:", None))
        self.label_singular_enddate.setText(QCoreApplication.translate("MainWindow", u"Fim de vig\u00eancia:", None))
        self.pushButton_singular_select_output.setText(QCoreApplication.translate("MainWindow", u"Selecionar diret\u00f3rio de destino", None))
        self.label_singular_output_header.setText(QCoreApplication.translate("MainWindow", u"Diret\u00f3rio selecionado:", None))
        self.label_singular_output_text.setText("")
        self.pushButton_singular_emit.setText(QCoreApplication.translate("MainWindow", u"Emitir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_singular), QCoreApplication.translate("MainWindow", u"Individual", None))
        self.label_config_max_threads.setText(QCoreApplication.translate("MainWindow", u"Quantidade m\u00e1xima de threads:", None))
        self.label_config_target_threads.setText(QCoreApplication.translate("MainWindow", u"Quantidade alvo de threads:", None))
        self.label_config_max_processes.setText(QCoreApplication.translate("MainWindow", u"Quantiade m\u00e1xima de processos:", None))
        self.pushButton_config_cobertura_source.setText(QCoreApplication.translate("MainWindow", u"Trocar arquivo de coberturas", None))
        self.label_config_selection_cobertura.setText(QCoreApplication.translate("MainWindow", u"Sele\u00e7\u00e3o:", None))
        self.label_config_cobertura_text.setText("")
        self.pushButton_config_cnv_source.setText(QCoreApplication.translate("MainWindow", u"Trocar arquivo de c\u00f3digos CNV", None))
        self.label_config_selection_cnv.setText(QCoreApplication.translate("MainWindow", u"Sele\u00e7\u00e3o:", None))
        self.label_config_cnv_text.setText("")
        self.pushButton_config_change_pdf_template.setText(QCoreApplication.translate("MainWindow", u"Trocar PDF modelo", None))
        self.label_config_selection_pdf.setText(QCoreApplication.translate("MainWindow", u"Sele\u00e7\u00e3o:", None))
        self.label_config_pdf_text.setText("")
        self.label_config_start_date.setText(QCoreApplication.translate("MainWindow", u"Data de vig\u00eancia inicial padr\u00e3o:", None))
        self.label_config_end_date.setText(QCoreApplication.translate("MainWindow", u"Data de vig\u00eancia final padr\u00e3o", None))
        self.pushButton_config_source.setText(QCoreApplication.translate("MainWindow", u"Trocar fonte de dados padr\u00e3o", None))
        self.label_config_selection_data_source.setText(QCoreApplication.translate("MainWindow", u"Sele\u00e7\u00e3o:", None))
        self.label_config_source_text.setText("")
        self.pushButton_config_output_dir.setText(QCoreApplication.translate("MainWindow", u"Diret\u00f3rio padr\u00e3o de salvamento", None))
        self.label_config_selection_output_dir.setText(QCoreApplication.translate("MainWindow", u"Sele\u00e7\u00e3o:", None))
        self.label_config_output_dir_text.setText("")
        self.pushButton_config_confirm.setText(QCoreApplication.translate("MainWindow", u"Aplicar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_config), QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
        self.label_console.setText("")

        # Coisas adicionadas manualmente. ------------------------------------------------------------------------------
        self.label_config_target_thread_number.setText(QCoreApplication.translate("MainWindow", f"{var.target_threads}", None))
        self.label_config_max_processes_number.setText(QCoreApplication.translate("MainWindow", f"{var.max_processes}", None))
        self.label_config_max_thread_number.setText(QCoreApplication.translate("MainWindow", f"{var.max_threads}", None))

    def select_input_directory(self):
        var.data_dir = QFileDialog.getOpenFileName()[0]
        self.label_multiple_input_text.setText(var.data_dir)

    def select_output_directory(self):
        var.output_dir = QFileDialog.getExistingDirectory() + '/'
        self.label_multiple_output_text.setText(var.output_dir)
        self.label_singular_output_text.setText(var.output_dir)

    def change_start_date_multiple(self):
        day = str(self.dateEdit_multiple_start.date().day())
        mon = str(self.dateEdit_multiple_start.date().month())
        yea = str(self.dateEdit_multiple_start.date().year())

        if len(day) < 2: day = '0' + day
        if len(mon) < 2: mon = '0' + mon

        var.start_period = day + '/' + mon + '/' + yea
        self.dateEdit_singular_start.setDate(self.dateEdit_multiple_start.date())

        if self.dateEdit_multiple_start.date() > self.dateEdit_multiple_end.date():  # Se trocar a data inicial para depois da data final, troque a final tamb�m.
            self.dateEdit_multiple_end.setDate(self.dateEdit_multiple_start.date())
            self.change_end_date_multiple()

    def change_end_date_multiple(self):
        day = str(self.dateEdit_multiple_end.date().day())
        mon = str(self.dateEdit_multiple_end.date().month())
        yea = str(self.dateEdit_multiple_end.date().year())

        if len(day) < 2: day = '0' + day
        if len(mon) < 2: mon = '0' + mon

        var.end_period = day + '/' + mon + '/' + yea
        self.dateEdit_singular_end.setDate(self.dateEdit_multiple_end.date())

        if self.dateEdit_multiple_end.date() < self.dateEdit_multiple_start.date():  # Se trocar a data final para antes da data inicial, troque a inicial tamb�m.
            self.selfdateEdit_multiple_start.setDate(self.dateEdit_multiple_end.date())
            self.change_start_date_multiple()

    def change_start_date_singular(self):
        day = str(self.dateEdit_singular_start.date().day())
        mon = str(self.dateEdit_singular_start.date().month())
        yea = str(self.dateEdit_singular_start.date().year())

        if len(day) < 2: day = '0' + day
        if len(mon) < 2: mon = '0' + mon

        var.start_period = day + '/' + mon + '/' + yea
        self.dateEdit_multiple_start.setDate(self.dateEdit_singular_start.date())

        if self.dateEdit_singular_start.date() > self.dateEdit_singular_end.date():  # Se trocar a data inicial para depois da data final, troque a final tamb�m.
            self.dateEdit_singular_end.setDate(self.dateEdit_singular_start.date())
            self.change_end_date_singular()

    def change_end_date_singular(self):
        day = str(self.dateEdit_singular_end.date().day())
        mon = str(self.dateEdit_singular_end.date().month())
        yea = str(self.dateEdit_singular_end.date().year())

        if len(day) < 2: day = '0' + day
        if len(mon) < 2: mon = '0' + mon

        var.end_period = day + '/' + mon + '/' + yea
        self.dateEdit_multiple_end.setDate(self.dateEdit_singular_end.date())

        if self.dateEdit_singular_end.date() < self.dateEdit_singular_start.date():  # Se trocar a data final para antes da data inicial, troque a inicial tamb�m.
            self.dateEdit_singular_start.setDate(self.dateEdit_singular_end.date())
            self.change_start_date_singular()

    def update_progress_bar(self):
        while var.progress < var.max_progress:
            self.progressBar_multiple.setValue(100 * var.progress / var.max_progress)
            sleep(0.001)

        while var.certificates_per_second == 0 or var.emission_time == 0:
            sleep(0.001)

        self.progressBar_multiple.setValue(0)
        self.pushButton_multiple_emit.setEnabled(True)
        self.pushButton_singular_emit.setEnabled(True)

        self.label_console.setText(
            f'Tempo de para emitir {var.max_progress} certificados: {var.emission_time / 60:.2f} minutos | Velocidade: {var.certificates_per_second:.2f} certificados por segundo')
        var.certificates_per_second = 0
        var.emission_time = 0

    def emit_multiple(self):
        self.pushButton_multiple_emit.setEnabled(False)
        self.pushButton_singular_emit.setEnabled(False)

        progress_thread = Thread(target=self.update_progress_bar, daemon=True)
        emission_thread = Thread(target=emit_from_source)

        progress_thread.start()
        emission_thread.start()

    def select_item(self):
        self.label_console.setText(self.listWidget_singular_cobertura.selectedItems()[0].text())

    def emit_singular(self):
        name = self.lineEdit_singular_name.text()
        cpf = self.lineEdit_singular_cpf.text()
        cnpj = self.lineEdit_singular_cnpj.text()
        clie = self.lineEdit_singular_client.text()
        matr = self.lineEdit_singular_matricula.text()
        apol = self.lineEdit_singular_apolice.text()
        try:
            cobe = self.listWidget_singular_cobertura.selectedItems()[0].text()
        except (AttributeError, IndexError):
            cobe = ''

        if var.output_dir == '':
            warning = QMessageBox()
            warning.setText('Selecione um diretório.')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

        elif apol == '':
            warning = QMessageBox()
            warning.setText('Preencha o campo apólice.')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

        elif any(char.isalpha() for char in apol):
            warning = QMessageBox()
            warning.setText('Não digite letras na ap�lice.')
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
            emit_singular(name, cpf, cnpj, matr, clie, apol, cobe, cnv='')
            self.label_console.setText(f'arquivo {cp(cpf)} - {nm(name)} emitido com êxito.')

    def change_coberturas_file(self):
        file = QFileDialog.getOpenFileName()[0]
        if file[-4:].lower() in ('xlsx', '.xls', '.csv', 'xlsm'):
            var.coberturas_path_tweak = file
            self.label_config_cobertura_text.setText(file)

        else:
            warning = QMessageBox()
            warning.setText('Extensão de arquivo não permitida')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

    def change_cnv_file(self):
        file = QFileDialog.getOpenFileName()[0]
        if file[-4:].lower() in ('xlsx', '.xls', '.csv', 'xlsm'):
            var.cnv_path_tweak = file
            self.label_config_cnv_text.setText(file)

        else:
            warning = QMessageBox()
            warning.setText('Extensão de arquivo não permitida')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

    def change_pdf_template(self):
        file = QFileDialog.getOpenFileName()[0]
        if file[-4:].lower() == '.pdf':
            var.template_tweak = file
            self.label_config_pdf_text.setText(file)

        else:
            warning = QMessageBox()
            warning.setText('Apenas arquivos PDFs são permitidos')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

    def change_default_data_source(self):
        file = QFileDialog.getOpenFileName()[0]
        if file[-4:].lower() in ('xlsx', '.xls', '.csv', 'xlsm'):
            var.data_dir_tweak = file
            self.label_config_source_text.setText(file)

        else:
            warning = QMessageBox()
            warning.setText('Extensão de arquivo não permitida')
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setWindowTitle('AVISO')
            warning.exec()

    def change_default_output_dir(self):
        var.output_dir_tweak = QFileDialog.getExistingDirectory() + '/'
        self.label_config_output_dir_text.setText(var.output_dir_tweak)

    def change_configs(self):

        # Coletando a data para a nova data inicial padrão
        if self.dateEdit_config_start.date() > self.dateEdit_config_end.date():  # Não deixa que a data inicial seja após a data final.
            day = str(self.dateEdit_config_start.date().day())
            mon = str(self.dateEdit_config_start.date().month())
            yea = str(self.dateEdit_config_start.date().year())
            if len(day) < 2: day = '0' + day
            if len(mon) < 2: mon = '0' + mon
            var.start_period_tweak = day + '/' + mon + '/' + yea

            var.end_period_tweak = var.start_period_tweak
            self.dateEdit_config_end.setDate(self.dateEdit_config_start.date())

        else:
            day = str(self.dateEdit_config_start.date().day())
            mon = str(self.dateEdit_config_start.date().month())
            yea = str(self.dateEdit_config_start.date().year())
            if len(day) < 2: day = '0' + day
            if len(mon) < 2: mon = '0' + mon
            var.start_period_tweak = day + '/' + mon + '/' + yea

            # Coletando a data para a nova data final padrão
            day = str(self.dateEdit_config_end.date().day())
            mon = str(self.dateEdit_config_end.date().month())
            yea = str(self.dateEdit_config_end.date().year())
            if len(day) < 2: day = '0' + day
            if len(mon) < 2: mon = '0' + mon
            var.end_period_tweak = day + '/' + mon + '/' + yea

        # Coleta os valores para threads e processos máximos e número de threads alvo.
        var.max_threads_tweak = self.horizontalSlider_config_max_threads.value()
        var.target_threads_tweak = self.horizontalSlider_config_target_threads.value()
        var.max_processes_tweak = self.horizontalSlider_config_max_processes.value()

        # Não permite que o número alvo de threads seja maior que o permitido
        if var.target_threads_tweak > var.max_threads_tweak:
            var.max_threads_tweak = var.target_threads_tweak
            self.horizontalSlider_config_max_threads.setValue(var.target_threads_tweak)
            self.label_config_max_thread_number.setNum(var.target_threads_tweak)

        if var.max_threads_tweak     is not None : var.max_threads     =     var.max_threads_tweak
        if var.max_processes_tweak   is not None : var.max_processes   =   var.max_processes_tweak
        if var.target_threads_tweak  is not None : var.target_threads  =  var.target_threads_tweak
        if var.data_dir_tweak        is not None : var.data_dir        =        var.data_dir_tweak
        if var.output_dir_tweak      is not None : var.output_dir      =      var.output_dir_tweak
        if var.start_period_tweak    is not None : var.start_period    =    var.start_period_tweak
        if var.end_period_tweak      is not None : var.end_period      =      var.end_period_tweak
        if var.coberturas_path_tweak is not None : var.coberturas_path = var.coberturas_path_tweak
        if var.cnv_path_tweak        is not None : var.cnv_path        =        var.cnv_path_tweak
        if var.template_tweak        is not None : var.template        =        var.template_tweak

        save_configs()

        var.max_threads_tweak     = None
        var.max_processes_tweak   = None
        var.target_threads_tweak  = None
        var.data_dir_tweak        = None
        var.output_dir_tweak      = None
        var.start_period_tweak    = None
        var.end_period_tweak      = None
        var.coberturas_path_tweak = None
        var.cnv_path_tweak        = None
        var.template_tweak        = None
