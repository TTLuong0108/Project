
## IMPORTS
import sys
import os
from PySide2 import *
from ui_MainGUI_v1 import *
from Custom_Widgets.Widgets import *
import Test
import Forward_kinematic
## FUNCTION
###################################################################
def Update_slider(TextEdit,Slider):
    value = Slider.value()
    TextEdit.setText(str(value))


def Solve_FK(self):
    t1 = self.ui.slider_t1.value()
    t2 = self.ui.slider_t2.value()
    t3 = self.ui.slider_t3.value()
    t4 = self.ui.slider_t4.value()
    t5 = self.ui.slider_t5.value()
    t6 = self.ui.slider_t6.value()
    L1 = self.ui.textEdit_L1.toPlainText()
    L2 = self.ui.textEdit_L2.toPlainText()
    L3 = self.ui.textEdit_L3.toPlainText()
    L4 = self.ui.textEdit_L4.toPlainText()
    Px,Py,Pz = Forward_kinematic.run(t1,t2,t3,t4,t5,t6,int(L1),int(L2),int(L3),int(L4),"T07")
    self.ui.FK_Px.setText(str(Px))
    self.ui.FK_Py.setText(str(Py))
    self.ui.FK_Pz.setText(str(Pz))
    print(t1)
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self,self.ui)
        self.show()
        # EXPAND CENTER WIDGET SIZE
        self.ui.settingBtn.clicked.connect(lambda:self.ui.centerMenu.expandMenu())
        self.ui.aboutBtn.clicked.connect(lambda:self.ui.centerMenu.expandMenu())
        # ClOSE CENTER WIDGET SIZE
        self.ui.CloseMoreMenuBtn.clicked.connect(lambda:self.ui.centerMenu.collapseMenu())
        # ClOSE NOTIFICATION WIDGET SIZE
        self.ui.CloseNotificationBtn.clicked.connect(lambda:self.ui.popupNotification.collapseMenu())
        # SLIDER
        self.ui.slider_t1.valueChanged.connect(lambda: Update_slider(self.ui.textEdit_FK_t1,self.ui.slider_t1))
        self.ui.slider_t2.valueChanged.connect(lambda: Update_slider(self.ui.textEdit_FK_t2,self.ui.slider_t2))
        self.ui.slider_t3.valueChanged.connect(lambda: Update_slider(self.ui.textEdit_FK_t3,self.ui.slider_t3))
        self.ui.slider_t4.valueChanged.connect(lambda: Update_slider(self.ui.textEdit_FK_t4,self.ui.slider_t4))
        self.ui.slider_t5.valueChanged.connect(lambda: Update_slider(self.ui.textEdit_FK_t5,self.ui.slider_t5))
        self.ui.slider_t6.valueChanged.connect(lambda: Update_slider(self.ui.textEdit_FK_t6,self.ui.slider_t6))
        # BUTTON SOLVE FORWARD
        self.ui.Solve_FK.clicked.connect(lambda:Solve_FK(self))
        #########################
        self.ui.Connected.clicked.connect(lambda:Test.Hi(self.ui.textEdit_init_t1.toPlainText()))

      
## EXECUTE APP
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
