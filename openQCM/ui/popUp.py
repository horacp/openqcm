from PyQt5 import QtWidgets

TAG = "[PopUp]"

###############################################################################
# Warning dialog module
###############################################################################
class PopUp:
    
    ###########################################################################
    # Shows a pop-up question dialog with yes and no buttons (unused)
    ###########################################################################
    @staticmethod
    def question_QCM(parent, title, message):
        """
        :param parent: Parent window for the dialog.
        :param title: Title of the dialog :type title: str.
        :param message: Message to be shown in the dialog :type message: str.
        :return: 1 if button1 was pressed, 0 if button2   :rtype: int.
        """
        #ans = QtWidgets.QMessageBox.question(parent, title, message, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        #if ans == QtWidgets.QMessageBox.Yes:
        #    print('Si')
        #    return True
        #elif ans == QtWidgets.QMessageBox.No:
        #    print('No')
        #    return False
        left = 700
        top = 400
        width = 340
        height = 220
        box = QtWidgets.QMessageBox(parent)
        box.setIcon(QtWidgets.QMessageBox.Question)
        box.setWindowTitle(title)
        box.setGeometry(left, top, width, height)
        box.setText(message)
        box.setStandardButtons(QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        button1 = box.button(QtWidgets.QMessageBox.Yes)
        button1.setText('@10MHz')
        button2 = box.button(QtWidgets.QMessageBox.No)
        button2.setText(' @5MHz')
        box.exec_()
        
        if box.clickedButton() == button1:
            print(TAG, 'Quartz Crystal Sensor installed on the openQCM Device: @10MHz')
            return 1
        elif box.clickedButton() == button2:
            print(TAG, 'Quartz Crystal Sensor installed on the openQCM Device: @5MHz')
            return 0

    ###########################################################################
    # Shows a Pop up warning dialog with a Ok buttons
    ###########################################################################
    @staticmethod
    def warning(parent, title, message):
        """
        :param parent: Parent window for the dialog.
        :param title: Title of the dialog :type title: str.
        :param message: Message to be shown in the dialog :type message: str.
        """
        QtWidgets.QMessageBox.warning(parent, title, message, QtWidgets.QMessageBox.Ok)
        #msgBox=QtWidgets.QMessageBox.warning(parent, title, message, QtWidgets.QMessageBox.Ok)
        #msgBox = QtWidgets.QMessageBox()
        #msgBox.setIconPixmap( QtWidgets.QPixmap("favicon.png"))
        #msgBox.exec_() 

    ###########################################################################
    # Shows a pop-up question dialog with yes and no buttons
    ###########################################################################
    @staticmethod
    def question(parent, title, message):
        """
        :param parent: Parent window for the dialog.
        :param title: Title of the dialog :type title: str.
        :param message: Message to be shown in the dialog :type message: str.
        :return: True if Yes button was pressed :rtype: bool.
        """
        ans = QtWidgets.QMessageBox.question(parent, title, message, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if ans == QtWidgets.QMessageBox.Yes:
            return True
        else:
            return False
