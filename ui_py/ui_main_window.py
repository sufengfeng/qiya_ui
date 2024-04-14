#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging
import os
import sys
import random
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtChart import (QChartView, QChart, QBarSet, QLineSeries, QPieSeries,
                           QLegend, QBarCategoryAxis, QValueAxis, QSplineSeries)

from ui.main_window import Ui_MainWindow

# def ReceiveData(name,_self):
#     while _self.m_bIsRunning:

from ctypes import *
# import xlwt

from ui_py.ui_setup import Setup_Dialog
from ui_py.ui_waveform import QCustomPlotWaveform

TransFormType_Can = 0
TransFormType_Uart = 1

UART_CANOPEN_FILE01 = 0xf4
UART_CANOPEN_FILE02 = 0xf5
UART_CANOPEN_FILE03 = 0xf6
UART_CANOPEN_FILE04 = 0xf7


def get_data_str(str_data, len):
    retStr = ""
    for i in range(len):
        value = str_data[i] & 0xff
        retStr = retStr + "  " + str('%02x' % (value))
    return retStr


_READ = 0
# 对象字典
# Direct_form = [
#     [0x2000, 0x01, _READ, "版本", ],  # g_sGlobalStatusParam.m_nVersion), 4},
#     [0x2000, 0x02, _READ, "设备类型", ],  # g_sGlobalFuncParam.m_eDeviceType), 4},
#     [0x2000, 0x03, _READ, "温度", ],  # g_sGlobalStatusParam.m_fTemperature), 4},
#     [0x2000, 0x04, _READ, "状态机", ],  # g_sGlobalStatusParam.m_eCurrentStatus), 4},
#
#     [0x2000, 0x05, _READ, "错误码", ],  # g_sGlobalStatusParam.m_nInterErrCode), 4},
#
#     [0x2001, 0x01, _READ, "编码器3速度", ],  # g_sGlobalStatusParam.m_sEncodeInfor[3].m_nCurrentSpeed), 4},
#     [0x2001, 0x02, _READ, "编码器3速度等级", ],
#     # g_sGlobalStatusParam.m_sEncodeInfor[3].m_nCurrentSpeedLevel), 4},
#     [0x2001, 0x03, _READ, "编码器4速度", ],  # g_sGlobalStatusParam.m_sEncodeInfor[4].m_nCurrentSpeed), 4},
#     [0x2001, 0x04, _READ, "编码器4速度等级", ],
#     # g_sGlobalStatusParam.m_sEncodeInfor[4].m_nCurrentSpeedLevel), 4},
#
#     [0x2002, 0x01, _READ, "机器人速度", ],  # g_sGlobalStatusParam.m_sRobotBasicnfo.m_nCurrentSpeed), 4},
#     [0x2002, 0x02, _READ, "机器人速度等级", ],  # g_sGlobalStatusParam.m_sRobotBasicnfo.m_nSpeedLevle), 4},
#     [0x2002, 0x03, _READ, "左右轮差速", ],  # g_sGlobalStatusParam.m_sRobotBasicnfo.m_nSpeedDiff), 4},
#     [0x2002, 0x04, _READ, "左右轮差速等级", ],  # g_sGlobalStatusParam.m_sRobotBasicnfo.m_nSpeedDiffLevle), 4},
#
#     [0x2002, 0x05, _READ, "机器人方向", ],  # g_sGlobalStatusParam.m_sRobotBasicnfo.m_nDirection), 4},
# ]
# Direct_form = []


logging.basicConfig(
    format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.DEBUG
)

logger = logging.getLogger(__name__)

# TYPE_DIRECT = [
#     "int8_t",
#     "int16_t",
#     "int32_t",
#     "uint8_t",
#     "uint16_t",
#     "uint32_t",
#     "uint32_t",
#     "HEX"
# ]
import sys
import time

# 继承QThread
# class Thread_Recieve(QThread):  # 线程1
#     _signal = pyqtSignal(int, int, list)
#     m_bIsConnect = False  # 是否连接
#     m_bIsStarted = False  # 是否启动
#     channel = 0
#     m_sControlCan_ = 0
#     m_sMainWindowSelf = 0
#
#     def __init__(self):
#         super().__init__()
#
#     def set_startStatus(self, value):  # 采集控制
#         self.m_bIsStarted = value
#
#     def set_connectStatus(self, value):  # 采集控制
#         self.m_bIsConnect = value
#
#     def set_channel(self, value):  # 采集控制
#         self.channel = value
#
#     def set_controlCan(self, value):  # 采集控制
#         self.m_sControlCan_ = value
#
#     def set_MainWindowSelf(self, value):  # 采集控制
#         self.m_sMainWindowSelf = value
#
#     def run(self):
#
#         while 1:
#             # 接收参数定义
#             if self.m_bIsStarted and self.m_bIsConnect:
#                 if self.m_sMainWindowSelf.m_nTransFormType == TransFormType_Can:
#                     try:
#                         recvnum = self.m_sControlCan_.VCI_Receive(4, 0, channel, pointer(recv_msg), 1, 0)
#                     except Exception as e:
#                         recvnum = 0
#                         logging.error(e)
#                     if recvnum != 0:
#                         self.m_sMainWindowSelf.hanleReceive(recvnum, recv_msg)
#                     elif recvnum == 0xFF:
#                         pass
#                 else:
#                     time.sleep(1)
#             else:
#                 time.sleep(1)
import datetime

import re

import qdarkstyle
class Main_Form(QtWidgets.QMainWindow, Ui_MainWindow):
    signal_TestControl = pyqtSignal(int)

    def __init__(self):
        super(Main_Form, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(qdarkstyle.load_stylesheet())

        self._setupdialog = Setup_Dialog()
        self._setupdialog.hide()

        self._Waveform = QCustomPlotWaveform()
        self._Waveform.hide()
        self.actionSetup.triggered.connect(self._setupdialog.show)
        # self.actionrefresh.triggered.connect(self.On_RefreshGraphics)
        self.actionDisplayWaveform.triggered.connect(self._Waveform.show)
        self.actionRecoder.triggered.connect(self.On_actionRecoder)
        self.actionexit.triggered.connect(self.close)

        self._setupdialog.signal_TestControl.connect(self.on_UartRecvHandle)

        self.pushButton_Empty.clicked.connect(self.on_pushButtonClicked)
        self.pushButton_Empty_2.clicked.connect(self.on_pushButtonClicked)
        self.pushButton_OutputValue_Setup.clicked.connect(self.on_pushButtonClicked)
        self.pushButton_output_rate_setup.clicked.connect(self.on_pushButtonClicked)
        self.pushButton_OutputValue_Setup_2.clicked.connect(self.on_pushButtonClicked)
        self.pushButton_output_rate_setup_2.clicked.connect(self.on_pushButtonClicked)

        self.checkBox_Channel00.stateChanged.connect(self.On_CheckBoxChanged)
        self.checkBox_Channel01.stateChanged.connect(self.On_CheckBoxChanged)
        self.checkBox_output_start.stateChanged.connect(self.On_CheckBoxChanged)
        self.checkBox_output_start_2.stateChanged.connect(self.On_CheckBoxChanged)

        self.checkBox_Zero.stateChanged.connect(self.On_CheckBoxChanged)
        self.checkBox_Zero_2.stateChanged.connect(self.On_CheckBoxChanged)

        self.comboBox_Range00.currentIndexChanged.connect(self.On_comboBox_Change)
        self.comboBox_Range01.currentIndexChanged.connect(self.On_comboBox_Change)

        self.comboBox_rate_mode.currentIndexChanged.connect(self.On_comboBox_Change)
        self.comboBox_rate_mode_2.currentIndexChanged.connect(self.On_comboBox_Change)

        self.comboBox_Unit00.currentIndexChanged.connect(self.On_comboBox_Change)
        self.comboBox_Unit01.currentIndexChanged.connect(self.On_comboBox_Change)
        # 定时接收数据
        self.timer_Channel00 = QTimer()  # 初始化定时器
        self.timer_Channel00.timeout.connect(self.on_timeout_Channel00)
        self.timer_Channel00.start(100)
        self.s_nFlagUpdate = True
        self._recDataBuff = ''

        self.s_nChannel00_Update_Enable = True
        self.s_nChannel01_Update_Enable = True
        self._IsRefresh00 = True  # 如果需要更新基础数据，则逐个发送数据
        self._IsRefresh01 = True  # 如果需要更新基础数据，则逐个发送数据
        self._FlagZeroEnable = False
        self._IsRecoder = False  # 是否记录标识
        self.counter_COMP = [0, 0]  # 周期更新正负压源
        self.currentModeIndex = [0, 0]
        self.lineEdit_output_rate.setDisabled(True)
        self.lineEdit_output_rate_2.setDisabled(True)
        self.IsUpdateMeasure = True     #更新单位序列，只发送一次
        self.currentUnitPres=["",""]    #保存数据时的单位
        # 开启通道发送命令列表
        self.cmdListChannel01 = [
            b"INST:SN?\r\n",  # SN码
            b"unit?\r\n",  # 单位
            b"INST:CAT:ALL?\r\n",  # 量程列表
            b"SOUR:PRES:RANG?\r\n",  # 当前量程
            b"SOUR:PRES?\r\n",  # 当前设置压力值
            b"SOUR:PRES:SLEW?\r\n",  # 当前设置变化率

        ]
        self.cmdListChannel02 = [
            b"INST:SN2?\r\n",
            b"unit2?\r\n",
            b"INST:CAT2:ALL?\r\n",
            b"SOUR2:PRES:RANG?\r\n",
            b"SOUR2:PRES?\r\n",  # 当前设置压力值
            b"SOUR2:PRES:SLEW?\r\n",  # 当前设置变化率

        ]

    def On_RefreshGraphics(self):
        self._IsRefresh00 = True  # 如果需要更新基础数据，则逐个发送数据
        self._IsRefresh01 = True  # 如果需要更新基础数据，则逐个发送数据

    def on_timeout_Channel00(self):  # reverse
        # 接收参数定义
        if self._setupdialog.m_bIsConnected:
            if self.IsUpdateMeasure:
                self.IsUpdateMeasure = False
                for i in range(29):
                    strSend = "INST:UNIT{}?\r\n".format(i)
                    self._setupdialog.SendDataByUart(strSend.encode())
                    time.sleep(0.01)

            if self.s_nFlagUpdate:
                self.s_nFlagUpdate = False
                if self.s_nChannel00_Update_Enable == True:  # 通道0压力值更新
                    self._setupdialog.SendDataByUart(b"Sens1?\r\n")
                    time.sleep(0.01)
                    self.counter_COMP[0] = self.counter_COMP[0] + 1
                    if self.counter_COMP[0] > 10:
                        self.counter_COMP[0] = 0
                        self._setupdialog.SendDataByUart(b"SOUR:COMP1?\r\n")
                        time.sleep(0.01)
                        self._setupdialog.SendDataByUart(b"SOUR:COMP2?\r\n")
                        time.sleep(0.01)
                if self._IsRefresh00 == True:  # 如果需要更新基础数据，则逐个发送数据
                    self._IsRefresh00 = False
                    try:
                        for cmd in self.cmdListChannel01:
                            self._setupdialog.SendDataByUart(cmd)
                            time.sleep(0.01)
                    except Exception as e:
                        logging.error(e)
            else:
                self.s_nFlagUpdate = True
                if self.s_nChannel01_Update_Enable == True:  # 通道1压力值更新
                    self._setupdialog.SendDataByUart(b":Sens2?\r\n")
                    time.sleep(0.01)
                    self.counter_COMP[1] = self.counter_COMP[1] + 1
                    if self.counter_COMP[1] > 10:
                        self.counter_COMP[1] = 0
                        self._setupdialog.SendDataByUart(b"SOUR2:COMP1?\r\n")
                        time.sleep(0.01)
                        self._setupdialog.SendDataByUart(b"SOUR2:COMP2?\r\n")
                        time.sleep(0.01)
                if self._IsRefresh01 == True:  # 如果需要更新基础数据，则逐个发送数据
                    self._IsRefresh01 = False
                    try:
                        for cmd in self.cmdListChannel02:
                            self._setupdialog.SendDataByUart(cmd)
                            time.sleep(0.01)
                    except Exception as e:
                        logging.error(e)

    def On_CheckBoxChanged(self, status):
        compnont = self.sender()
        if compnont == self.checkBox_Channel00:
            self.s_nChannel00_Update_Enable = compnont.isChecked()
            self._IsRefresh00 = compnont.isChecked()  # 如果需要更新基础数据，则逐个发送数据
        elif compnont == self.checkBox_Channel01:
            self.s_nChannel01_Update_Enable = compnont.isChecked()
            self._IsRefresh01 = compnont.isChecked()  # 如果需要更新基础数据，则逐个发送数据
        elif compnont == self.checkBox_output_start:
            str_send = "OUTPut1:STATe {}\r\n".format(int(compnont.isChecked()))
            self._setupdialog.SendDataByUart(str_send.encode())
            time.sleep(0.01)
        elif compnont == self.checkBox_output_start_2:
            str_send = "OUTPut2:STATe {}\r\n".format(int(compnont.isChecked()))
            self._setupdialog.SendDataByUart(str_send.encode())
            time.sleep(0.01)
        elif compnont == self.checkBox_Zero:
            str_send = ":CAL1:PRES:ZERO:VALV {}\r\n".format(int(compnont.isChecked()))
            self._setupdialog.SendDataByUart(str_send.encode())
        elif compnont == self.checkBox_Zero_2:
            str_send = ":CAL2:PRES:ZERO:VALV {}\r\n".format(int(compnont.isChecked()))
            self._setupdialog.SendDataByUart(str_send.encode())

    def on_pushButtonClicked(self):
        compnont = self.sender()
        if compnont == self.pushButton_Empty:  # 启动排空
            self._setupdialog.SendDataByUart(b"Sour1:Vent 1\r\n")
        elif compnont == self.pushButton_Empty_2:  # 启动排空
            self._setupdialog.SendDataByUart(b"Sour2:Vent 1\r\n")
        elif compnont == self.pushButton_OutputValue_Setup:
            value = self.lineEdit_OutputValue.text()  # 设置压力值
            str_send = "SOUR:PRES %f\r\n" % (float(value))
            self._setupdialog.SendDataByUart(str_send.encode())
            time.sleep(0.01)
            self._IsRefresh00 = True
        elif compnont == self.pushButton_OutputValue_Setup_2:
            value = self.lineEdit_OutputValue_2.text()  # 设置压力值
            str_send = "SOUR2:PRES %f\r\n" % (float(value))
            self._setupdialog.SendDataByUart(str_send.encode())
            time.sleep(0.01)
            self._IsRefresh01 = True
        elif compnont == self.pushButton_output_rate_setup:  # 设置压力变化率 self.currentModeIndex=[0,0]
            if self.currentModeIndex[0] == 0:
                self._setupdialog.SendDataByUart(b"SOUR:PRES:SLEW:MODE MAX\r\n")
                time.sleep(0.01)
            else:
                self._setupdialog.SendDataByUart(b"SOUR:PRES:SLEW:MODE linear\r\n")
                time.sleep(0.01)
                value = self.lineEdit_output_rate.text()  # 设置压力值
                str_send = ":SOURCE1:PRESsure:SLEW %f \r\n" % (float(value))
                self._setupdialog.SendDataByUart(str_send.encode())
                time.sleep(0.01)
            self._IsRefresh00 = True
        elif compnont == self.pushButton_output_rate_setup_2:
            if self.currentModeIndex[1] == 0:
                self._setupdialog.SendDataByUart(b"SOUR2:PRES:SLEW:MODE MAX\r\n")
                time.sleep(0.01)
            else:
                self._setupdialog.SendDataByUart(b"SOUR2:PRES:SLEW:MODE linear\r\n")
                time.sleep(0.01)
                value = self.lineEdit_output_rate_2.text()  # 设置压力值
                str_send = ":SOURCE2:PRESsure:SLEW %f \r\n" % (float(value))
                self._setupdialog.SendDataByUart(str_send.encode())
                time.sleep(0.01)
            self._IsRefresh01 = True

    def handle_uart_response(self, str_response):
        # INST:UNIT{}?
        ##########################################单位#####################################
        index = str_response.find(":INST:UNIT")
        if index >= 0:
            str_List = str_response.split(' ')  # 以空格为分隔符，分隔成两个
            self.comboBox_Unit00.addItem(str_List[1])
            self.comboBox_Unit01.addItem(str_List[1])

        ##########################################压力值#####################################
        index = str_response.find(":SENS:PRES ")
        if index >= 0:
            str_List = str_response.split(' ')  # 以空格为分隔符，分隔成两个
            self.label_Ch00Value.setText(str_List[1])
            self._Waveform._ch00Value = float(str_List[1])
            if self._IsRecoder:
                now = datetime.datetime.now()
                str_store = str(now)+" CH01 " + str(str_List[1]) +self.currentUnitPres[0]+ "\n"
                data = self._Savef.write(str_store)
        index = str_response.find(":SENS2:PRES ")
        if index >= 0:
            str_List = str_response.split(' ')  # 以空格为分隔符，分隔成两个
            self.label_Ch01Value.setText(str_List[1])
            self._Waveform._ch01Value = float(str_List[1])
            if self._IsRecoder:
                now = datetime.datetime.now()
                str_store = str(now)+" CH01 "+ str(str_List[1]) + self.currentUnitPres[1]+"\n"
                data = self._Savef.write(str_store)
        ##########################################正源压值#####################################
        index = str_response.find(":SOUR:PRES:COMP ")
        if index >= 0:
            str_List = str_response.split(' ')  # 以空格为分隔符，分隔成两个
            self.label_VE_POS.setText(str_List[1])
        index = str_response.find(":SOUR2:PRES:COMP ")
        if index >= 0:
            str_List = str_response.split(' ')  # 以空格为分隔符，分隔成两个
            self.label_VE_POS_2.setText(str_List[1])
        ##########################################负源压值#####################################
        index = str_response.find(":SOUR:PRES:COMP2 ")
        if index >= 0:
            str_List = str_response.split(' ')  # 以空格为分隔符，分隔成两个
            self.label_VE_NEG.setText(str_List[1])
        index = str_response.find(":SOUR2:PRES:COMP2 ")
        if index >= 0:
            str_List = str_response.split(' ')  # 以空格为分隔符，分隔成两个
            self.label_VE_NEG_2.setText(str_List[1])
        ##########################################SN码#####################################
        index = str_response.find(":INST:SN ")
        if index >= 0:
            str_List = str_response.split(' ')  # 以空格为分隔符，分隔成两个
            self.label_CH0_SN.setText(str_List[1])
        index = str_response.find(":INST:SN2 ")
        if index >= 0:
            str_List = str_response.split(' ')  # 以空格为分隔符，分隔成两个
            self.label_CH1_SN.setText(str_List[1])
        ##########################################压力值单位#####################################
        index = str_response.find(":UNIT:PRES ")
        if index >= 0:
            str_List = str_response.split(' ')  # 以空格为分隔符，分隔成两个
            self.comboBox_Unit00.setCurrentText(str_List[1])
            self.currentUnitPres[0]=str_List[1]
        index = str_response.find(":UNIT2:PRES ")
        if index >= 0:
            str_List = str_response.split(' ')  # 以空格为分隔符，分隔成两个
            self.comboBox_Unit01.setCurrentText(str_List[1])
            self.currentUnitPres[1] = str_List[1]
        ##########################################量程列表#####################################
        index = str_response.find(":INST:CAT:ALL ")
        if index >= 0:
            str_List = str_response.split(' ')  # 以空格为分隔符，分隔成两个
            str_List = str_List[1].split('"')  # 以空格为分隔符，分隔成两个
            if self.comboBox_Range00.findText(str_List[1]) == -1:
                self.comboBox_Range00.addItem(str_List[1])
            if self.comboBox_Range00.findText(str_List[9]) == -1:
                self.comboBox_Range00.addItem(str_List[9])
        index = str_response.find(":INST:CAT2:ALL ")
        if index >= 0:
            str_List = str_response.split(' ')  # 以空格为分隔符，分隔成两个
            str_List = str_List[1].split('"')  # 以空格为分隔符，分隔成两个
            if self.comboBox_Range01.findText(str_List[1]) == -1:
                self.comboBox_Range01.addItem(str_List[1])
            if self.comboBox_Range01.findText(str_List[9]) == -1:
                self.comboBox_Range01.addItem(str_List[9])
        ##########################################当前#####################################
        index = str_response.find(":SOUR:PRES:RANG ")
        if index >= 0:
            str_List = str_response.split(' ')  # 以空格为分隔符，分隔成两个
            str_List = str_List[1].split('"')  # 以空格为分隔符，分隔成两个
            index = self.comboBox_Range00.findText(str_List[1])
            if not index == -1:
                self.comboBox_Range00.setCurrentIndex(index)
            else:
                print("not find")
            if str_List[1].find("barg") >= 0:
                self.label_range01.setText("表压")
            elif str_List[1].find("bara") >= 0:
                self.label_range01.setText("绝压")
            else:
                print("not find RANG")
        index = str_response.find(":SOUR2:PRES:RANG ")
        if index >= 0:
            str_List = str_response.split(' ')  # 以空格为分隔符，分隔成两个
            str_List = str_List[1].split('"')  # 以空格为分隔符，分隔成两个
            index = self.comboBox_Range01.findText(str_List[1])
            if not index == -1:
                self.comboBox_Range01.setCurrentIndex(index)
            else:
                print("not find")
            if str_List[1].find("barg") >= 0:
                self.label_range02.setText("表压")
            elif str_List[1].find("bara") >= 0:
                self.label_range02.setText("绝压")
            else:
                print("not find RANG")
        ##########################################当前压力设定值#####################################
        index = str_response.find(":SOUR:PRES:LEV:IMM:AMPL ")
        if index >= 0:
            str_List = str_response.split(' ')  # 以空格为分隔符，分隔成两个
            self.label_val_set_current.setText(str_List[1])
        index = str_response.find(":SOUR2:PRES:LEV:IMM:AMPL ")
        if index >= 0:
            str_List = str_response.split(' ')  # 以空格为分隔符，分隔成两个
            self.label_val_set_current_2.setText(str_List[1])
        ##########################################当前压力变化率设定值#####################################
        index = str_response.find(":SOUR:PRES:SLEW ")
        if index >= 0:
            str_List = str_response.split(' ')  # 以空格为分隔符，分隔成两个
            self.label_rate_set_current.setText(str_List[1])
        index = str_response.find(":SOUR2:PRES:SLEW ")
        if index >= 0:
            str_List = str_response.split(' ')  # 以空格为分隔符，分隔成两个
            self.label_rate_set_current_2.setText(str_List[1])

    def on_UartRecvHandle(self, revData):
        self._recDataBuff = self._recDataBuff + revData
        index = self._recDataBuff.find("\r\n")
        if index >= 0:
            str_List = self._recDataBuff.split('\r')
            lenList = len(str_List)
            for i in range(lenList - 1):
                str_response = str_List[i]
                # print(str_response)
                self.handle_uart_response(str_response)
            self._recDataBuff = str_List[lenList - 1]  # 去最后一段

    def On_comboBox_Change(self, index):
        compnont = self.sender()
        if compnont == self.comboBox_Range00:  # 设置量程
            if compnont.count() >= 2:  # 避免第一次添加就触发
                str = (":SOUR:PRES:RANG \"{}\"".format(compnont.currentText()))
                self._setupdialog.SendDataByUart(str.encode())
                time.sleep(0.01)
                self._IsRefresh00 = True  # 如果需要更新基础数据，则逐个发送数据
        elif compnont == self.comboBox_Range01:
            if compnont.count() >= 2:  # 避免第一次添加就触发
                str = (":SOUR2:PRES:RANG \"{}\"".format(compnont.currentText()))
                self._setupdialog.SendDataByUart(str.encode())
                time.sleep(0.01)
                self._IsRefresh01 = True  # 如果需要更新基础数据，则逐个发送数据
        elif compnont == self.comboBox_rate_mode:
            self.currentModeIndex[0] = compnont.currentIndex()
            if self.currentModeIndex[0] == 0:
                self.lineEdit_output_rate.setDisabled(True)
            else:
                self.lineEdit_output_rate.setDisabled(False)
        elif compnont == self.comboBox_rate_mode_2:
            self.currentModeIndex[1] = compnont.currentIndex()
            if self.currentModeIndex[1] == 0:
                self.lineEdit_output_rate_2.setDisabled(True)
            else:
                (self.lineEdit_output_rate_2.setDisabled(False))
        elif compnont == self.comboBox_Unit00:
            if compnont.count() >= 2:  # 避免第一次添加就触发
                str = ("unit {}\r\n".format(compnont.currentText()))
                self._setupdialog.SendDataByUart(str.encode())
                time.sleep(0.01)
                self._IsRefresh01 = True  # 如果需要更新基础数据，则逐个发送数据

        elif compnont == self.comboBox_Unit01:
            if compnont.count() >= 2:  # 避免第一次添加就触发
                str = ("unit2 {}\r\n".format(compnont.currentText()))
                self._setupdialog.SendDataByUart(str.encode())
                time.sleep(0.01)
                self._IsRefresh01 = True  # 如果需要更新基础数据，则逐个发送数据


    def On_actionRecoder(self):
        if self._IsRecoder:
            self._IsRecoder = False
            self.actionRecoder.setText("Recoder")
            self._Savef.close()
        else:
            # self指向自身，"Open File"为文件名，"./"为当前路径，最后为文件类型筛选器
            fname, ok2 = QFileDialog.getSaveFileName(self,
                                                     "文件保存",
                                                     "./",
                                                     "Text Files (*.txt);;Bin (*.bin)")
            if fname:  # 判断路径非空
                # self._Savef = QFile(fname[0])
                self._Savef = open(fname, "w+")
                self._IsRecoder = True
                self.actionRecoder.setText("Stop")

    def closeEvent(self, event):  # 函数名固定不可变
        sys.exit(0)  # 状态码


if __name__ == "__main__":
    app = QApplication(sys.argv)
    sys.exit(app.exec_())
