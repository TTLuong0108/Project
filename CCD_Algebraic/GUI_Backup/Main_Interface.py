
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinndesign.com
########################################################################

########################################################################
## IMPORTS
########################################################################
import sys
import os
from PySide2 import *


########################################################################
# IMPORT GUI FILE
from ui_MainGUI_v1 import *
########################################################################

########################################################################
# IMPORT Custom widgets
from Custom_Widgets.Widgets import *
########################################################################


########################################################################
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


########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  