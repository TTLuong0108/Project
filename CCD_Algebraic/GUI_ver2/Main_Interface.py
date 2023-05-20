from Draw import *
import time
## IMPORTS
import numpy as np
import sys
import os
from PySide2 import *
from ui_MainGUI_v1 import *
from Custom_Widgets.Widgets import *
import Forward_kinematic
from Inverse_Kinematic import *
from code_handle import MyFigureCanvas

from function_serial import Function_UI_Serial
import serial, serial.tools.list_ports
from PyQt5.QtCore import pyqtSlot
from itertools import count
from PyQt5 import QtCore
###
# Phân Luồng xử lý
class Worker(QtCore.QRunnable):

	def __init__(self,function,*args,**kwargs):
		super(Worker, self).__init__()
		self.function = function
		self.args = args
		self.kwargs = kwargs

	@pyqtSlot()
	def run(self): 
		self.function(*self.args,**self.kwargs)    
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self,self.ui)
        self.show()
        # ClOSE NOTIFICATION WIDGET SIZE
        self.ui.CloseNotificationBtn.clicked.connect(lambda:self.ui.popupNotification.collapseMenu())
        # SERIAL
        self.serial = Function_UI_Serial()
        self.serialPort = serial.Serial()
        self.ui.cbbBaudrate.addItems(self.serial.baudList)
        self.ui.cbbBaudrate.setCurrentText('115200')
        self.update_ports()
        #-----------------------------------------------------

        #region ---/////////// CONNECTED PAGE /////////--------------
            # CHECK BOX AND CONNECT BTN
        self.ui.ConnectedBtn.clicked.connect(self.connect_serial)
        self.ui.UpdatePortBtn.clicked.connect(self.update_ports)
        self.serial.data_available.connect(self.read_data)
        self.ui.CloseWinBtn.clicked.connect(lambda: self.stop_Threading())
        #endregion -----------------------------------------------------
        #region  ---/////////// KINEMATIC PAGE /////////--------------
            # SLIDER CHANGE
        self.ui.slider_t1.valueChanged.connect(lambda:self.Update_EditTextFromSlider(self.ui.textEdit_FK_t1,self.ui.slider_t1))
        self.ui.slider_t2.valueChanged.connect(lambda:self.Update_EditTextFromSlider(self.ui.textEdit_FK_t2,self.ui.slider_t2))
        self.ui.slider_t3.valueChanged.connect(lambda:self.Update_EditTextFromSlider(self.ui.textEdit_FK_t3,self.ui.slider_t3))
        self.ui.slider_t4.valueChanged.connect(lambda:self.Update_EditTextFromSlider(self.ui.textEdit_FK_t4,self.ui.slider_t4))
        self.ui.slider_t5.valueChanged.connect(lambda:self.Update_EditTextFromSlider(self.ui.textEdit_FK_t5,self.ui.slider_t5))
        self.ui.slider_t6.valueChanged.connect(lambda:self.Update_EditTextFromSlider(self.ui.textEdit_FK_t6,self.ui.slider_t6))
            # EDIT TEXT CHANGE
        self.ui.Solve_FK.clicked.connect(lambda: self.Update_SliderFromEditText_FK())
        self.ui.Solve_IK.clicked.connect(lambda: self.Update_SliderFromEditText_IK())
        # endregion -----------------------------------------------------
        #region  ---/////////// TRAJECTORY PAGE /////////--------------
        self.ui.Lines.clicked.connect(lambda: self.start_Trajectory(shape="Line",stime=20,tf=5,step=0.05))
        self.ui.Triangles.clicked.connect(lambda: self.start_Trajectory(shape="Triangle",stime=25,tf=5,step=0.05))
        self.ui.Circles.clicked.connect(lambda: self.start_Trajectory(shape="Circle",stime=20,tf=5,step=0.05))
        self.ui.Stop_draw.clicked.connect(lambda: self.stop_Threading())
        # endregion -----------------------------------------------------

        #region ---/////////// CHART PAGE /////////--------------
        self.mode = 0
        self.read_mode = 0
        self.ui.SignalOutputBtn.clicked.connect(lambda: self.draw_Signal_Output())
        self.ui.SignalErrorBtn.clicked.connect(lambda: self.draw_Signal_Error())
        self.ui.PositionOutputBtn.clicked.connect(lambda: self.draw_Position_Output())
        self.ui.PositionErrorBtn.clicked.connect(lambda: self.draw_Position_Error())
        self.threadpool = QtCore.QThreadPool()
        self.theta_1=[]
        self.theta_2=[]
        self.theta_3=[]
        self.theta_4=[]
        self.theta_5=[]
        self.theta_6=[]
        self.theta_1_Eror=[]
        self.theta_2_Error=[]
        self.theta_3_Error=[]
        self.theta_4_Error=[]
        self.theta_5_Error=[]
        self.theta_6_Error=[]
        self.X = []
        self.Y = []
        self.Z = []
        self.alpha = []
        self.beta = []
        self.gama = []
        self.X_Eror = []
        self.Y_Eror = []
        self.Z_Eror = []
        self.alpha_Eror = []
        self.beta_Eror = []
        self.gama_Eror = []
        self.time_draw = []
        # Output
        self.screen_XOY_Output = Display_demension_output('XOY demension',width=100, height=5, dpi=70,size=15)
        self.screen_XOY_Output.config_display_output(self.screen_XOY_Output,size=8,xlable='X', ylable='Y')
        self.ui.XOY_demension.addWidget(self.screen_XOY_Output)

        self.screen_XOZ_Output = Display_demension_output('XOZ demension',width=100, height=5, dpi=70,size=15)
        self.screen_XOZ_Output.config_display_output(self.screen_XOZ_Output,size=8,xlable='X', ylable='Z')
        self.ui.XOZ_demension.addWidget(self.screen_XOZ_Output)

        self.screen_YOZ_Output = Display_demension_output('YOZ demension',width=100, height=5, dpi=70,size=15)
        self.screen_YOZ_Output.config_display_output(self.screen_YOZ_Output,size=8,xlable='Y', ylable='Z')
        self.ui.YOZ_demension.addWidget(self.screen_YOZ_Output)
        # Signal Error
        self.screen_theta1_Error = Display_error('Theta1 Error',width=100, height=10, dpi=70,size=15)
        self.screen_theta1_Error.config_display_output(self.screen_theta1_Error,size=8)
        self.ui.Theta1Error.addWidget(self.screen_theta1_Error)

        self.screen_theta2_Error = Display_error('Theta2 Error',width=100, height=40, dpi=70,size=15)
        self.screen_theta2_Error.config_display_output(self.screen_theta2_Error,size=8)
        self.ui.Theta2Error.addWidget(self.screen_theta2_Error)

        self.screen_theta3_Error = Display_error('Theta3 Error',width=100, height=40, dpi=70,size=15)
        self.screen_theta3_Error.config_display_output(self.screen_theta3_Error,size=8)
        self.ui.Theta3Error.addWidget(self.screen_theta3_Error)

        self.screen_theta4_Error = Display_error('Theta4 Error',width=100, height=40, dpi=70,size=15)
        self.screen_theta4_Error.config_display_output(self.screen_theta4_Error,size=8)
        self.ui.Theta4Error.addWidget(self.screen_theta4_Error)

        self.screen_theta5_Error = Display_error('Theta5 Error',width=100, height=40, dpi=70,size=15)
        self.screen_theta5_Error.config_display_output(self.screen_theta5_Error,size=8)
        self.ui.Theta5Error.addWidget(self.screen_theta5_Error)

        self.screen_theta6_Error = Display_error('Theta6 Error',width=100, height=40, dpi=70,size=15)
        self.screen_theta6_Error.config_display_output(self.screen_theta6_Error,size=8)
        self.ui.Theta6Error.addWidget(self.screen_theta6_Error)

        # Position Output
        self.screen_X_Output = Display_position_output('X Position',width=100, height=10, dpi=70,size=15)
        self.screen_X_Output.config_display_output(self.screen_X_Output,size=8)
        self.ui.XOuput.addWidget(self.screen_X_Output)

        self.screen_Y_Output = Display_position_output('Y Position',width=100, height=10, dpi=70,size=15)
        self.screen_Y_Output.config_display_output(self.screen_Y_Output,size=8)
        self.ui.YOuput.addWidget(self.screen_Y_Output)

        self.screen_Z_Output = Display_position_output('Z Position',width=100, height=10, dpi=70,size=15)
        self.screen_Z_Output.config_display_output(self.screen_Z_Output,size=8)
        self.ui.ZOuput.addWidget(self.screen_Z_Output)

        self.screen_alpha_Output = Display_angle_output('alpha angle',width=100, height=10, dpi=70,size=15)
        self.screen_alpha_Output.config_display_output(self.screen_alpha_Output,size=8)
        self.ui.alphaOuput.addWidget(self.screen_alpha_Output)

        self.screen_beta_Output = Display_angle_output('beta angle',width=100, height=10, dpi=70,size=15)
        self.screen_beta_Output.config_display_output(self.screen_beta_Output,size=8)
        self.ui.betaOuput.addWidget(self.screen_beta_Output)

        self.screen_gama_Output = Display_angle_output('gama angle',width=100, height=10, dpi=70,size=15)
        self.screen_gama_Output.config_display_output(self.screen_gama_Output,size=8)
        self.ui.gamaOutput.addWidget(self.screen_gama_Output)
        # Position Error
        self.screen_X_Error = Display_error('X Error',width=100, height=10, dpi=70,size=15)
        self.screen_X_Error.config_display_output(self.screen_X_Error,size=8)
        self.ui.XError.addWidget(self.screen_X_Error)

        self.screen_Y_Error = Display_error('Y Error',width=100, height=10, dpi=70,size=15)
        self.screen_Y_Error.config_display_output(self.screen_Y_Error,size=8)
        self.ui.YError.addWidget(self.screen_Y_Error)

        self.screen_Z_Error = Display_error('Z Error',width=100, height=10, dpi=70,size=15)
        self.screen_Z_Error.config_display_output(self.screen_Z_Error,size=8)
        self.ui.ZError.addWidget(self.screen_Z_Error)

        self.screen_alpha_Error = Display_error('alpha Error',width=100, height=10, dpi=70,size=15)
        self.screen_alpha_Error.config_display_output(self.screen_alpha_Error,size=8)
        self.ui.alphaError.addWidget(self.screen_alpha_Error)

        self.screen_beta_Error = Display_error('beta Error',width=100, height=10, dpi=70,size=15)
        self.screen_beta_Error.config_display_output(self.screen_beta_Error,size=8)
        self.ui.betaError.addWidget(self.screen_beta_Error)

        self.screen_gama_Error = Display_error('gama Error',width=100, height=10, dpi=70,size=15)
        self.screen_gama_Error.config_display_output(self.screen_gama_Error,size=8)
        self.ui.gamaError.addWidget(self.screen_gama_Error)

        # Signal Output
        self.screen_theta1 = Display_angle_output('Theta1',width=100, height=10, dpi=70,size=15)
        self.screen_theta1.config_display_output(self.screen_theta1,size=8)
        self.ui.Theta1Output.addWidget(self.screen_theta1)

        self.screen_theta2 = Display_angle_output('Theta2',width=100, height=40, dpi=70,size=15)
        self.screen_theta2.config_display_output(self.screen_theta2,size=8)
        self.ui.Theta2Output.addWidget(self.screen_theta2)

        self.screen_theta3 = Display_angle_output('Theta3',width=100, height=40, dpi=70,size=15)
        self.screen_theta3.config_display_output(self.screen_theta3,size=8)
        self.ui.Theta3Output.addWidget(self.screen_theta3)

        self.screen_theta4 = Display_angle_output('Theta4',width=100, height=40, dpi=70,size=15)
        self.screen_theta4.config_display_output(self.screen_theta4,size=8)
        self.ui.Theta4Output.addWidget(self.screen_theta4)

        self.screen_theta5 = Display_angle_output('Theta5',width=100, height=40, dpi=70,size=15)
        self.screen_theta5.config_display_output(self.screen_theta5,size=8)
        self.ui.Theta5Output.addWidget(self.screen_theta5)

        self.screen_theta6 = Display_angle_output('Theta6',width=100, height=40, dpi=70,size=15)
        self.screen_theta6.config_display_output(self.screen_theta6,size=8)
        self.ui.Theta6Output.addWidget(self.screen_theta6)                                 
        #endregion ----------------------------------------------------- 
         
    ## FUNCTION
    ###################################################################
    def Update_EditTextFromSlider(self,TextEdit,Slider):
        TextEdit.setText("")
        value = Slider.value()
        value = round(value * 0.01,2)
        TextEdit.setText(str(value))

    def Update_SliderFromEditText_FK(self):
        value_text1 = self.ui.textEdit_FK_t1.toPlainText()
        value_text2 = self.ui.textEdit_FK_t2.toPlainText()
        value_text3 = self.ui.textEdit_FK_t3.toPlainText()
        value_text4 = self.ui.textEdit_FK_t4.toPlainText()
        value_text5 = self.ui.textEdit_FK_t5.toPlainText()
        value_text6 = self.ui.textEdit_FK_t6.toPlainText()

        if((value_text1 != "") and (value_text2 != "") and (value_text3 != "") and (value_text4 != "")
        and (value_text5 != "") and (value_text6 != "")):
            value1 = float(value_text1)*100
            value2 = float(value_text2)*100
            value3 = float(value_text3)*100
            value4 = float(value_text4)*100
            value5 = float(value_text5)*100
            value6 = float(value_text6)*100
            self.ui.slider_t1.setValue(value1)
            self.ui.slider_t2.setValue(value2)
            self.ui.slider_t3.setValue(value3)
            self.ui.slider_t4.setValue(value4)
            self.ui.slider_t5.setValue(value5)
            self.ui.slider_t6.setValue(value6)

        t1 = self.ui.slider_t1.value()
        t2 = self.ui.slider_t2.value()
        t3 = self.ui.slider_t3.value()
        t4 = self.ui.slider_t4.value()
        t5 = self.ui.slider_t5.value()
        t6 = self.ui.slider_t6.value()
        L1 = float(self.ui.Setting_L1.toPlainText())
        L2 = float(self.ui.Setting_L2.toPlainText())
        L3 = float(self.ui.Setting_L3.toPlainText())
        L4 = float(self.ui.Setting_L4.toPlainText())
        Px,Py,Pz = Forward_kinematic.run(t1/100.0,t2/100.0,t3/100.0,t4/100.0,t5/100.0,t6/100.0,L1,L2,L3,L4,"T07")
        self.ui.FK_Px.setText(str(Px))
        self.ui.FK_Py.setText(str(Py))
        self.ui.FK_Pz.setText(str(Pz))
        if(self.serial.serialPort.is_open):
            if(self.mode == 1):
                self.read_mode = 0
                self.mode = 0
            self.data_send = str(int(t1)) + ':'+ str(int(t2)) + ':'+ str(int(t3)) + ':'+ str(int(t4)) + ':'+ str(int(t5)) + ':'+str(int(t6)) + ':'+str(int(0))
            self.send_data(self.data_send)

    def Update_SliderFromEditText_IK(self):
        Px = float(self.ui.FK_Px.toPlainText())
        Py = float(self.ui.FK_Py.toPlainText())
        Pz = float(self.ui.FK_Pz.toPlainText())
        alpha = float(self.ui.alpha.toPlainText())
        beta = float(self.ui.beta.toPlainText())
        gama = float(self.ui.gama.toPlainText())
        L1 = float(self.ui.Setting_L1.toPlainText())
        L2 = float(self.ui.Setting_L2.toPlainText())
        L3 = float(self.ui.Setting_L3.toPlainText())
        L4 = float(self.ui.Setting_L4.toPlainText())
        theta_init1 = float(self.ui.Setting_Theta1_init.toPlainText())
        theta_init2 = float(self.ui.Setting_Theta2_init.toPlainText())
        theta_init3 = float(self.ui.Setting_Theta3_init.toPlainText())
        theta_init4 = float(self.ui.Setting_Theta4_init.toPlainText())
        theta_init5 = float(self.ui.Setting_Theta5_init.toPlainText())
        theta_init6 = float(self.ui.Setting_Theta6_init.toPlainText())
        theta_init = np.array([theta_init1,theta_init2,theta_init3,theta_init4,theta_init5,theta_init6])
        upper_limit = np.array([45,45,45,45,45,45])
        lower_limit = np.array([-45,-30,-45,-30,-45,-45])
        if((Px != "") and (Py != "") and (Pz != "") and (alpha != "")
        and (beta != "") and (gama != "")):
            theta = run(Px,Py,Pz,alpha,beta,gama,theta_init,L1,L2,L3,L4,upper_limit,lower_limit,precision=0.05,interation=700)
            value1 = float(round(theta[0],2))*100
            value2 = float(round(theta[1],2))*100
            value3 = float(round(theta[2],2))*100
            value4 = float(round(theta[3],2))*100
            value5 = float(round(theta[4],2))*100
            value6 = float(round(theta[5],2))*100
            self.ui.slider_t1.setValue(value1)
            self.ui.slider_t2.setValue(value2)
            self.ui.slider_t3.setValue(value3)
            self.ui.slider_t4.setValue(value4)
            self.ui.slider_t5.setValue(value5)
            self.ui.slider_t6.setValue(value6)
            self.ui.textEdit_FK_t1.setText(str(round(theta[0],2)))
            self.ui.textEdit_FK_t2.setText(str(round(theta[1],2)))
            self.ui.textEdit_FK_t3.setText(str(round(theta[2],2)))
            self.ui.textEdit_FK_t4.setText(str(round(theta[3],2)))
            self.ui.textEdit_FK_t5.setText(str(round(theta[4],2)))
            self.ui.textEdit_FK_t6.setText(str(round(theta[5],2)))

    def Trajectory(self,shape,stime,tf,step):
        self.read_mode = 1
        Px_home = float(self.ui.Setting_Px_Home.toPlainText())
        Py_home = float(self.ui.Setting_Py_Home.toPlainText())
        Pz_home = float(self.ui.Setting_Pz_Home.toPlainText())
        Home_theta = np.array([0,0,0,0,0,0])

        L1 = float(self.ui.Setting_L1.toPlainText())
        L2 = float(self.ui.Setting_L2.toPlainText())
        L3 = float(self.ui.Setting_L3.toPlainText())
        L4 = float(self.ui.Setting_L4.toPlainText())
        theta_init1 = float(self.ui.Setting_Theta1_init.toPlainText())
        theta_init2 = float(self.ui.Setting_Theta2_init.toPlainText())
        theta_init3 = float(self.ui.Setting_Theta3_init.toPlainText())
        theta_init4 = float(self.ui.Setting_Theta4_init.toPlainText())
        theta_init5 = float(self.ui.Setting_Theta5_init.toPlainText())
        theta_init6 = float(self.ui.Setting_Theta6_init.toPlainText())
        theta_init = np.array([theta_init1,theta_init2,theta_init3,theta_init4,theta_init5,theta_init6])
        upper_limit = np.array([45,45,45,45,45,45])
        lower_limit = np.array([-45,-30,-45,-30,-45,-45])
        times = np.arange(0,stime+step,step)
        if(shape == "Line"):
            Px1 = float(self.ui.Setting_Px1_Line.toPlainText())
            Py1 = float(self.ui.Setting_Py1_Line.toPlainText())
            Pz1 = float(self.ui.Setting_Pz1_Line.toPlainText())
            Px2 = float(self.ui.Setting_Px2_Line.toPlainText())
            Py2 = float(self.ui.Setting_Py2_Line.toPlainText())
            Pz2 = float(self.ui.Setting_Pz2_Line.toPlainText())
            Start_Point = np.array([Px1,Py1,Pz1])
            End_Point = np.array([Px2,Py2,Pz2])
            Start_theta = run(Px1,Py1,Pz1,0,0,0,np.array([45.0,-30.0,0.0,0.0,0.0,0.0]),L1,L2,L3,L4,upper_limit,lower_limit,precision=0.05,interation=700)
            for t in times:
                time.sleep(step)
                if(self.mode == 1):
                    t = round(t,2)                   
                    theta = lines_Home(Start_Point,End_Point,Home_theta,Start_theta,t,tf,L1,L2,L3,L4,theta_init,upper_limit,lower_limit)
                    theta_init = theta
                    self.Px,self.Py,self.Pz = Forward_kinematic.run(theta[0],theta[1],theta[2],theta[3],theta[4],theta[5],L1,L2,L3,L4,"T07")
                    if(self.serial.serialPort.is_open):
                        theta1 = round(theta_init[0],2)*100.0
                        theta2 = round(theta_init[1],2)*100.0
                        theta3 = round(theta_init[2],2)*100.0
                        theta4 = round(theta_init[3],2)*100.0
                        theta5 = round(theta_init[4],2)*100.0
                        theta6 = round(theta_init[5],2)*100.0
                        t = t*100.0
                        self.data_send = str(int(theta1)) + ':'+ str(int(theta2)) + ':'+ str(int(theta3)) + ':'+ str(int(theta4)) + ':'+ str(int(theta5)) + ':'+str(int(theta6))+ ':'+ str(int(t))
                        self.send_data(self.data_send)
                        
                    else:
                        FK = Forward_kinematic.run(theta[0],theta[1],theta[2],theta[3],theta[4],theta[5],L1,L2,L3,L4,"T07")
                        self.theta_1.append(theta_init[0])
                        self.theta_2.append(theta_init[1])
                        self.theta_3.append(theta_init[2])
                        self.theta_4.append(theta_init[3])
                        self.theta_5.append(theta_init[4])
                        self.theta_6.append(theta_init[5])

                        self.theta_1_Eror.append(0)
                        self.theta_2_Error.append(0)
                        self.theta_3_Error.append(0)
                        self.theta_4_Error.append(0)
                        self.theta_5_Error.append(0)
                        self.theta_6_Error.append(0)

                        self.X.append(FK[0])
                        self.Y.append(FK[1])
                        self.Z.append(FK[2])
                        self.alpha.append(0)
                        self.beta.append(0)
                        self.gama.append(0)

                        self.X_Eror.append(abs(FK[0]-self.Px))
                        self.Y_Eror.append(abs(FK[1]-self.Py))
                        self.Z_Eror.append(abs(FK[2]-self.Pz))
                        self.alpha_Eror.append(0)
                        self.beta_Eror.append(0)
                        self.gama_Eror.append(0)
                        
                        self.time_draw.append(t)
                        #print(t)
                else:
                    break
        elif(shape == "Triangle"):
            Px1 = float(self.ui.Setting_Px1_Triangle.toPlainText())
            Py1 = float(self.ui.Setting_Py1_Triangle.toPlainText())
            Pz1 = float(self.ui.Setting_Pz1_Triangle.toPlainText())
            Px2 = float(self.ui.Setting_Px2_Triangle.toPlainText())
            Py2 = float(self.ui.Setting_Py2_Triangle.toPlainText())
            Pz2 = float(self.ui.Setting_Pz2_Triangle.toPlainText())
            Px3 = float(self.ui.Setting_Px3_Triangle.toPlainText())
            Py3 = float(self.ui.Setting_Py3_Triangle.toPlainText())
            Pz3 = float(self.ui.Setting_Pz3_Triangle.toPlainText())
            Point1 = np.array([Px1,Py1,Pz1])
            Point2 = np.array([Px2,Py2,Pz2])
            Point3 = np.array([Px3,Py3,Pz3])
            Start_theta = run(Px1,Py1,Pz1,0,0,0,np.array([45.0,-30.0,0.0,0.0,0.0,0.0]),L1,L2,L3,L4,upper_limit,lower_limit,precision=0.05,interation=700)
            for t in times:
                time.sleep(step)
                if(self.mode == 1):
                    t = round(t,2)                   
                    theta = Triangle_Home(Point1,Point2,Point3,Home_theta,Start_theta,t,tf,L1,L2,L3,L4,theta_init,upper_limit,lower_limit)
                    theta_init = theta
                    self.Px,self.Py,self.Pz = Forward_kinematic.run(theta[0],theta[1],theta[2],theta[3],theta[4],theta[5],L1,L2,L3,L4,"T07")
                    if(self.serial.serialPort.is_open):
                        theta1 = round(theta_init[0],2)*100.0
                        theta2 = round(theta_init[1],2)*100.0
                        theta3 = round(theta_init[2],2)*100.0
                        theta4 = round(theta_init[3],2)*100.0
                        theta5 = round(theta_init[4],2)*100.0
                        theta6 = round(theta_init[5],2)*100.0
                        t = t*100.0
                        self.data_send = str(int(theta1)) + ':'+ str(int(theta2)) + ':'+ str(int(theta3)) + ':'+ str(int(theta4)) + ':'+ str(int(theta5)) + ':'+str(int(theta6))+ ':'+ str(int(t))
                        self.send_data(self.data_send)
                        
                    else:
                        FK = Forward_kinematic.run(theta[0],theta[1],theta[2],theta[3],theta[4],theta[5],L1,L2,L3,L4,"T07")
                        self.theta_1.append(theta_init[0])
                        self.theta_2.append(theta_init[1])
                        self.theta_3.append(theta_init[2])
                        self.theta_4.append(theta_init[3])
                        self.theta_5.append(theta_init[4])
                        self.theta_6.append(theta_init[5])

                        self.theta_1_Eror.append(0)
                        self.theta_2_Error.append(0)
                        self.theta_3_Error.append(0)
                        self.theta_4_Error.append(0)
                        self.theta_5_Error.append(0)
                        self.theta_6_Error.append(0)

                        self.X.append(FK[0])
                        self.Y.append(FK[1])
                        self.Z.append(FK[2])
                        self.alpha.append(0)
                        self.beta.append(0)
                        self.gama.append(0)

                        self.X_Eror.append(abs(FK[0]-self.Px))
                        self.Y_Eror.append(abs(FK[1]-self.Py))
                        self.Z_Eror.append(abs(FK[2]-self.Pz))
                        self.alpha_Eror.append(0)
                        self.beta_Eror.append(0)
                        self.gama_Eror.append(0)                  
                        self.time_draw.append(t)
                else:
                    break
        else:
            Px = float(self.ui.Setting_Px_Circle.toPlainText())
            Py = float(self.ui.Setting_PyCircle.toPlainText())
            Pz = float(self.ui.Setting_Pz_Circle.toPlainText())
            R = float(self.ui.Setting_Radius_Circle.toPlainText())
            Start_theta = run(Px,Py,Pz+R,0,0,0,np.array([45.0,-30.0,0.0,0.0,0.0,0.0]),L1,L2,L3,L4,upper_limit,lower_limit,precision=0.05,interation=700)
            Point1 = np.array([Px,Py,Pz])
            for t in times:
                time.sleep(step)
                if(self.mode == 1):
                    t = round(t,2)                   
                    theta = Circle_Home(Point1,R,Home_theta,Start_theta,t,tf,L1,L2,L3,L4,theta_init,upper_limit,lower_limit)
                    theta_init = theta
                    self.Px,self.Py,self.Pz = Forward_kinematic.run(theta[0],theta[1],theta[2],theta[3],theta[4],theta[5],L1,L2,L3,L4,"T07")
                    if(self.serial.serialPort.is_open):
                        theta1 = round(theta_init[0],2)*100.0
                        theta2 = round(theta_init[1],2)*100.0
                        theta3 = round(theta_init[2],2)*100.0
                        theta4 = round(theta_init[3],2)*100.0
                        theta5 = round(theta_init[4],2)*100.0
                        theta6 = round(theta_init[5],2)*100.0
                        t = t*100.0
                        self.data_send = str(int(theta1)) + ':'+ str(int(theta2)) + ':'+ str(int(theta3)) + ':'+ str(int(theta4)) + ':'+ str(int(theta5)) + ':'+str(int(theta6))+ ':'+ str(int(t))
                        self.send_data(self.data_send)
                        
                    else:
                        FK = Forward_kinematic.run(theta[0],theta[1],theta[2],theta[3],theta[4],theta[5],L1,L2,L3,L4,"T07")
                        self.theta_1.append(theta_init[0])
                        self.theta_2.append(theta_init[1])
                        self.theta_3.append(theta_init[2])
                        self.theta_4.append(theta_init[3])
                        self.theta_5.append(theta_init[4])
                        self.theta_6.append(theta_init[5])

                        self.theta_1_Eror.append(0)
                        self.theta_2_Error.append(0)
                        self.theta_3_Error.append(0)
                        self.theta_4_Error.append(0)
                        self.theta_5_Error.append(0)
                        self.theta_6_Error.append(0)

                        self.X.append(FK[0])
                        self.Y.append(FK[1])
                        self.Z.append(FK[2])
                        self.alpha.append(0)
                        self.beta.append(0)
                        self.gama.append(0)

                        self.X_Eror.append(abs(FK[0]-self.Px))
                        self.Y_Eror.append(abs(FK[1]-self.Py))
                        self.Z_Eror.append(abs(FK[2]-self.Pz))
                        self.alpha_Eror.append(0)
                        self.beta_Eror.append(0)
                        self.gama_Eror.append(0)                  
                        self.time_draw.append(t)
                else:
                    break
##########################################################################
    def connect_serial(self):
        #if(self.ui.ConnectedBtn.isChecked()):      
        if(self.ui.ConnectedBtn.text() == "Connected"):
            self.ui.ConnectedBtn.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.ui.ConnectedBtn.setText("Disconnected")
            if(self.ui.checkBox.isChecked()):
                port = self.ui.cbbCom.currentText()
                baud = self.ui.cbbBaudrate.currentText()
                self.serial.serialPort.port = port
                self.serial.serialPort.baudrate = baud
                self.serial.connect_serial()
                self.ui.lbl_DataStatus.setText("ON")
                self.ui.lbl_DataStatus.setStyleSheet("background-color: rgb(106, 157, 78);")
                self.ui.lbl_content_Notification.setText("Connected Success")
                self.ui.popupNotification.expandMenu()
            else:
                if(self.serial.serialPort.is_open):
                    self.serial.disconnect_serial()
                self.ui.lbl_DataStatus.setText("TESTING MODE")
                self.ui.lbl_DataStatus.setStyleSheet("background-color: rgb(255, 0, 0);")
                self.ui.lbl_content_Notification.setText("Testing mode success")
                self.ui.popupNotification.expandMenu()
        else:
            if(self.serial.serialPort.is_open):
                self.serial.disconnect_serial()
            self.ui.ConnectedBtn.setText("Connected")
            self.ui.ConnectedBtn.setStyleSheet("background-color: rgb(0, 0, 0);")
            self.ui.checkBox.setChecked(False)
            self.ui.lbl_DataStatus.setText("OFF")
            self.ui.lbl_DataStatus.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.ui.lbl_content_Notification.setText("Disconnected Success")
            self.ui.popupNotification.expandMenu()
            
    def update_ports(self):
        self.serial.update_port()
        self.ui.cbbCom.clear()
        self.ui.cbbCom.addItems(self.serial.portList)

    def send_data(self,datasend):
        if(self.serial.serialPort.is_open):
            self.serial.send_data(datasend)

    def read_data(self):
        data_receive = self.serial.data
        t =  int(data_receive[6])
        t1 = int(data_receive[0])
        t2 = int(data_receive[1])
        t3 = int(data_receive[2])
        t4 = int(data_receive[3])
        t5 = int(data_receive[4])
        t6 = int(data_receive[5])
        L1 = float(self.ui.Setting_L1.toPlainText())
        L2 = float(self.ui.Setting_L2.toPlainText())
        L3 = float(self.ui.Setting_L3.toPlainText())
        L4 = float(self.ui.Setting_L4.toPlainText())
        
        if(self.read_mode == 1):
            self.theta_1.append(t1/100.0)
            self.theta_2.append(t2/100.0)
            self.theta_3.append(t3/100.0)
            self.theta_4.append(t4/100.0)
            self.theta_5.append(t5/100.0)
            self.theta_6.append(t6/100.0)
            FK = Forward_kinematic.run(t1/100.0,t2/100.0,t3/100.0,t4/100.0,t5/100.0,t6/100.0,L1,L2,L3,L4,"T07")
            self.theta_1_Eror.append(0)
            self.theta_2_Error.append(0)
            self.theta_3_Error.append(0)
            self.theta_4_Error.append(0)
            self.theta_5_Error.append(0)
            self.theta_6_Error.append(0)

            self.X.append(FK[0])
            self.Y.append(FK[1])
            self.Z.append(FK[2])
            self.alpha.append(0)
            self.beta.append(0)
            self.gama.append(0)

            self.X_Eror.append(abs(FK[0]-self.Px))
            self.Y_Eror.append(abs(FK[1]-self.Py))
            self.Z_Eror.append(abs(FK[2]-self.Pz))
            self.alpha_Eror.append(0)
            self.beta_Eror.append(0)
            self.gama_Eror.append(0)       
            self.time_draw.append(t/100.0)
##########################################################
    def draw_(self): 
        while self.mode == 1:
            self.screen_XOY_Output.axes.clear()
            self.screen_XOY_Output.config_display_output(self.screen_XOY_Output,size=8,xlable='X', ylable='Y')  
            self.screen_XOY_Output.axes.plot(self.X, self.Y, linewidth=2)
            self.screen_XOY_Output.draw()

            self.screen_XOZ_Output.axes.clear()
            self.screen_XOZ_Output.config_display_output(self.screen_XOZ_Output,size=8,xlable='X', ylable='Z')  
            self.screen_XOZ_Output.axes.plot(self.X, self.Z, linewidth=2)
            self.screen_XOZ_Output.draw()

            self.screen_YOZ_Output.axes.clear()
            self.screen_YOZ_Output.config_display_output(self.screen_YOZ_Output,size=8,xlable='Y', ylable='Z')  
            self.screen_YOZ_Output.axes.plot(self.Y, self.Z, linewidth=2)
            self.screen_YOZ_Output.draw()

            len_t = len(self.time_draw)-1
            if(len_t < 0):
                len_t = 0
            ti = float(self.time_simulation/self.steps)
            percent = round((len_t/ti)*100,2)
            self.ui.label_14.setText(str(percent)+"%")

    def draw_Signal_Error(self):
        self.ui.SignalErrorBtn.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.ui.SignalOutputBtn.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.ui.PositionOutputBtn.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.ui.PositionErrorBtn.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.mode = 0
        self.screen_theta1_Error.axes.clear()
        self.screen_theta1_Error.config_display_output(self.screen_theta1_Error, size=8)    
        self.screen_theta1_Error.axes.plot(self.time_draw, self.theta_1_Eror, linewidth=2)
        self.screen_theta1_Error.draw()

        self.screen_theta2_Error.axes.clear()
        self.screen_theta2_Error.config_display_output(self.screen_theta2_Error, size=8)    
        self.screen_theta2_Error.axes.plot(self.time_draw, self.theta_2_Error, linewidth=2)
        self.screen_theta2_Error.draw()

        self.screen_theta3_Error.axes.clear()
        self.screen_theta3_Error.config_display_output(self.screen_theta3_Error, size=8)    
        self.screen_theta3_Error.axes.plot(self.time_draw, self.theta_3_Error, linewidth=2)
        self.screen_theta3_Error.draw()

        self.screen_theta4_Error.axes.clear()
        self.screen_theta4_Error.config_display_output(self.screen_theta4_Error, size=8)    
        self.screen_theta4_Error.axes.plot(self.time_draw, self.theta_4_Error, linewidth=2)
        self.screen_theta4_Error.draw()

        self.screen_theta5_Error.axes.clear()
        self.screen_theta5_Error.config_display_output(self.screen_theta5_Error, size=8)    
        self.screen_theta5_Error.axes.plot(self.time_draw, self.theta_5_Error, linewidth=2)
        self.screen_theta5_Error.draw()

        self.screen_theta6_Error.axes.clear()
        self.screen_theta6_Error.config_display_output(self.screen_theta6_Error, size=8)    
        self.screen_theta6_Error.axes.plot(self.time_draw, self.theta_6_Error, linewidth=2)
        self.screen_theta6_Error.draw()                

    def draw_Signal_Output(self):
        self.ui.SignalErrorBtn.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.ui.SignalOutputBtn.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.ui.PositionOutputBtn.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.ui.PositionErrorBtn.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.screen_theta1.axes.clear()
        self.screen_theta1.config_display_output(self.screen_theta1, size=8)    
        self.screen_theta1.axes.plot(self.time_draw, self.theta_1, linewidth=2)
        self.screen_theta1.draw()

        self.screen_theta2.axes.clear()
        self.screen_theta2.config_display_output(self.screen_theta2,size=8)    
        self.screen_theta2.axes.plot(self.time_draw, self.theta_2, linewidth=2)
        self.screen_theta2.draw()

        self.screen_theta3.axes.clear()
        self.screen_theta3.config_display_output(self.screen_theta3,size=8)    
        self.screen_theta3.axes.plot(self.time_draw, self.theta_3, linewidth=2)
        self.screen_theta3.draw()

        self.screen_theta4.axes.clear()
        self.screen_theta4.config_display_output(self.screen_theta4,size=8)    
        self.screen_theta4.axes.plot(self.time_draw, self.theta_4, linewidth=2)
        self.screen_theta4.draw()

        self.screen_theta5.axes.clear()
        self.screen_theta5.config_display_output(self.screen_theta5,size=8)    
        self.screen_theta5.axes.plot(self.time_draw, self.theta_5, linewidth=2)
        self.screen_theta5.draw()

        self.screen_theta6.axes.clear()
        self.screen_theta6.config_display_output(self.screen_theta6,size=8)    
        self.screen_theta6.axes.plot(self.time_draw, self.theta_6, linewidth=2)
        self.screen_theta6.draw()

    def draw_Position_Output(self):
        self.ui.SignalErrorBtn.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.ui.SignalOutputBtn.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.ui.PositionOutputBtn.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.ui.PositionErrorBtn.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.mode = 0
        self.screen_X_Output.axes.clear()
        self.screen_X_Output.config_display_output(self.screen_X_Output, size=8)    
        self.screen_X_Output.axes.plot(self.time_draw, self.X, linewidth=2)
        self.screen_X_Output.draw()

        self.screen_Y_Output.axes.clear()
        self.screen_Y_Output.config_display_output(self.screen_Y_Output, size=8)    
        self.screen_Y_Output.axes.plot(self.time_draw, self.Y, linewidth=2)
        self.screen_Y_Output.draw()

        self.screen_Z_Output.axes.clear()
        self.screen_Z_Output.config_display_output(self.screen_Z_Output, size=8)    
        self.screen_Z_Output.axes.plot(self.time_draw, self.Z, linewidth=2)
        self.screen_Z_Output.draw()

    def draw_Position_Error(self):
        self.ui.SignalErrorBtn.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.ui.SignalOutputBtn.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.ui.PositionOutputBtn.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.ui.PositionErrorBtn.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.mode = 0

        self.screen_X_Error.axes.clear()
        self.screen_X_Error.config_display_output(self.screen_X_Error, size=8)    
        self.screen_X_Error.axes.plot(self.time_draw, self.X_Eror, linewidth=2)
        self.screen_X_Error.draw()

        self.screen_Y_Error.axes.clear()
        self.screen_Y_Error.config_display_output(self.screen_Y_Error, size=8)    
        self.screen_Y_Error.axes.plot(self.time_draw, self.Y_Eror, linewidth=2)
        self.screen_Y_Error.draw()

        self.screen_Z_Error.axes.clear()
        self.screen_Z_Error.config_display_output(self.screen_Z_Error, size=8)    
        self.screen_Z_Error.axes.plot(self.time_draw, self.Z_Eror, linewidth=2)
        self.screen_Z_Error.draw()

        self.screen_alpha_Error.axes.clear()
        self.screen_alpha_Error.config_display_output(self.screen_alpha_Error, size=8)    
        self.screen_alpha_Error.axes.plot(self.time_draw, self.alpha_Eror, linewidth=2)
        self.screen_alpha_Error.draw()

        self.screen_beta_Error.axes.clear()
        self.screen_beta_Error.config_display_output(self.screen_beta_Error, size=8)    
        self.screen_beta_Error.axes.plot(self.time_draw, self.beta_Eror, linewidth=2)
        self.screen_beta_Error.draw()

        self.screen_gama_Error.axes.clear()
        self.screen_gama_Error.config_display_output(self.screen_gama_Error, size=8)    
        self.screen_gama_Error.axes.plot(self.time_draw, self.gama_Eror, linewidth=2)
        self.screen_gama_Error.draw()                

    # Hàm bắt đầu luồng vẽ đồ thị, được khởi động bằng nút nhấn
    def start_draw(self):
        self.worker = Worker(lambda: self.draw_())
        self.threadpool.start(self.worker)

    def stop_Threading(self):
        self.theta_1=[]
        self.theta_2=[]
        self.theta_3=[]
        self.theta_4=[]
        self.theta_5=[]
        self.theta_6=[]
        self.theta_1_Eror=[]
        self.theta_2_Error=[]
        self.theta_3_Error=[]
        self.theta_4_Error=[]
        self.theta_5_Error=[]
        self.theta_6_Error=[]
        self.X = []
        self.Y = []
        self.Z = []
        self.alpha = []
        self.beta = []
        self.gama = []
        self.X_Eror = []
        self.Y_Eror = []
        self.Z_Eror = []
        self.alpha_Eror = []
        self.beta_Eror = []
        self.gama_Eror = []
        self.time_draw = []
        self.ui.label_14.setText("0%")
        self.mode = 0

    def start_Trajectory(self,shape,stime,tf,step):
        self.stop_Threading()
        if(self.mode == 0):
            self.mode = 1
            self.start_draw()
        self.time_simulation = stime
        self.time_Pline = tf
        self.steps = step
        self.TrajectoryWorker = Worker(lambda: self.Trajectory(shape,stime=self.time_simulation,tf=self.time_Pline,step=self.steps))
        self.threadpool.start(self.TrajectoryWorker)

## EXECUTE APP
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
