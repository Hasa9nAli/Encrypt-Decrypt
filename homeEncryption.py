from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import QCursor
from PyQt5.QtGui import QPixmap
# connect with the command line
from windowEnDc import WindowEnDc 
from rc5encryption import RC5
"class for home window algorithm and design"

class Home:
    def __init__(self):
        self.homeWindow = None
        self.app = None
        self.imgHome = None
        self.iconHome = None
        
        # self.setting = Setting()
        # content of program
        self.secondWindow = WindowEnDc(self) 
        self.buttonRC4 = \
            self.buttonOfRc5 = \
            self.buttonOfRc6 = \
            self.buttonOfAes = \
            self.buttonOfAes = \
            self.buttonOfEcc = \
            self.exitBtn = \
            self.bodyText = \
            None
        

    def rc5Window(self):
        rc5 = RC5()
        self.secondWindow.runProgramWindow(rc5)
        
        """---function to open and close algorithms --- """

    def rc4Open(self):
        self.secondWindow.rc4Open = True

    def rc4Close(self):
        self.secondWindow.rc4Open = False

    def rc5Open(self):
        self.secondWindow.rc5Open = True

    def rc5Close(self):
        self.secondWindow.rc5Open = False

    # def rc6Open(self):
    #     self.secondWindow.rc6Open = True

    # def rc6Close(self):
    #     self.secondWindow.rc6Open = False

    # def aesOpen(self):
    #     self.secondWindow.aesOpen = True

    # def aesClose(self):
    #     self.secondWindow.aesOpen = False

    # def eccOpen(self):
    #     self.secondWindow.eccOpen = True

    # def eccClose(self):
    #     self.secondWindow.eccOpen = False

    """---end the open and close algorithms---"""
    """start Home window run"""
    def _rc4_create(self):
        self.buttonRC4 = QtWidgets.QPushButton("RC4 Algorithm", self.homeWindow)
        self.buttonRC4.setStyleSheet("""
            QPushButton{
            color:#fff; 
            width:400px; 
            height:501px;
            display:inline;
            font-size:24px; 
            border:1px solid #ccc;
            font-weight:500; 
            border-top-left-radius:12px;
            border-bottom-left-radius:12px;
            }
            QPushButton:hover{
                
                background-color:#393939;
                color:#ccc
            }            
        """)
        self.buttonRC4.setToolTip("""
        The RC4 algorithm encrypt texts
        How to use:
                1- Enter the text
                2- Type the key content from 5 letter of number
                3- Click on the Encrypt button
        A window will appear for the result of the encryption process,
        indicating that the text has been encrypted

        """)
        self.buttonRC4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonRC4.move(100, 120)
        textRc4 = QtWidgets.QLabel("""Private key security makes subscription payments, 
automated payments, and on chain reputations 
              extremely fraught with risk. """, self.homeWindow)
        textRc4.setStyleSheet("""
                    QLabel{
                    font-size:16px;
                    color:#fff;
                    background-color:transparent
                    }
                    QLabel:hover{
                    transition: 0.9s;
                    background-color:#FFF;
                    color:#000
                    }
                """)
        textRc4.move(130, 400)
        self.buttonRC4.clicked.connect(lambda:[self.secondWindow.runProgramWindow(),self.homeWindow.hide()])
        photo = QtWidgets.QLabel(self.homeWindow)
        p = QPixmap("img/lock1.png")
        photo.setPixmap(p)
        photo.move(270,280)
        photo.setStyleSheet("""
                background-color:transparent;
        """)

    def _rc5_create(self):
        self.buttonOfRc5 = QtWidgets.QPushButton("RC5 Algorithm", self.homeWindow)
        self.buttonOfRc5.setStyleSheet("""
            QPushButton{
            color:#fff; 
            width:400px; 
            height:248.5px;
            display:inline;
            font-size:24px; 
            border:1px solid #ccc;
            font-weight:500; 
            }
            QPushButton:hover{
                
                background-color:#393939;
                color:#ccc

            }            
        """)
        self.buttonOfRc5.setToolTip("""
        The RC5 algorithm encrypt texts
        How to use:
                1- Enter the text
                2- Type the key 
                3- Click on the Encrypt button
        A window will appear for the result of the encryption process,
        indicating that the text has been encrypted

        """)
        self.buttonOfRc5.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonOfRc5.move(503, 120)
        self.buttonOfRc5.clicked.connect(lambda:[self.secondWindow.runProgramWindow(),self.homeWindow.hide()])
        textRc5 = QtWidgets.QLabel("""Private key security makes subscription payments, 
automated payments, and on chain reputations 
                extremely fraught with risk. """, self.homeWindow)
        textRc5.setStyleSheet("""
                            QLabel{
                            font-size:16px;
                            color:#fff;
                            background-color:transparent
                            }
                            QLabel:hover{
                            transition: 0.9s;
                            background-color:#FFF;
                            color:#000
                            }
                        """)
        textRc5.move(530, 280)
        photo = QtWidgets.QLabel(self.homeWindow)
        p = QPixmap("img/keyhole.png")
        photo.setPixmap(p)
        photo.move(670,150)
        photo.setStyleSheet("""
                background-color:transparent;
        """)

    def _create_rc6(self):
        self.buttonOfRc6 = QtWidgets.QPushButton("RC6 Algorithm", self.homeWindow)
        self.buttonOfRc6.setStyleSheet("""
            QPushButton{
            color:#fff; 
            width:400px; 
            height:248.5px;
            display:inline;
            font-size:24px; 
            border:1px solid #ccc;
            font-weight:500; 
            
            }
            QPushButton:hover{
                
                background-color:#393939;
                color:#ccc

            }            
        """)
        self.buttonOfRc6.setToolTip("""
        The RC6 algorithm encrypt texts
        How to use:
                1- Enter the text
                2- Type the key 
                3- Click on the Encrypt button
        A window will appear for the result of the encryption process,
        indicating that the text has been encrypted

        """)
        self.buttonOfRc6.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonOfRc6.move(503, 372)
        self.buttonOfRc6.clicked.connect(lambda:[self.secondWindow.runProgramWindow(),self.homeWindow.hide()])
        textRc6 = QtWidgets.QLabel("""Private key security makes subscription payments, 
automated payments, and on chain reputations 
                extremely fraught with risk. """, self.homeWindow)
        textRc6.setStyleSheet("""
                                    QLabel{
                                    font-size:16px;
                                    color:#fff;
                                    background-color:transparent
                                    }
                                    QLabel:hover{
                                    transition: 0.9s;
                                    background-color:#FFF;
                                    color:#000
                                    }
                                """)
        textRc6.move(530, 520)
        photo = QtWidgets.QLabel(self.homeWindow)
        p = QPixmap("img/key.png")
        photo.setPixmap(p)
        photo.setStyleSheet("""
                background-color:transparent;
        """)
        photo.move(670, 410)

    def _create_aes(self):
        self.buttonOfAes = QtWidgets.QPushButton("AES Algorithm", self.homeWindow)
        self.buttonOfAes.setStyleSheet("""
            QPushButton{
            color:#fff; 
            width:380px; 
            height:248.5px;
            display:inline;
            font-size:24px; 
            border:1px solid #ccc;
            font-weight:500; 
            border-bottom-right-radius:12px
            }
            QPushButton:hover{
                
                background-color:#393939;
                color:#ccc
            }            
        """)
        self.buttonOfAes.setToolTip("""
        The RC6 algorithm encrypt texts
        How to use:
                1- Enter the text
                2- Type the key most bs 16 characters or number
                3- Click on the Encrypt button
        A window will appear for the result of the encryption process,
        indicating that the text has been encrypted

        """)
        self.buttonOfAes.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonOfAes.move(906, 372)
        self.buttonOfAes.clicked.connect(lambda:[self.secondWindow.runProgramWindow(),self.homeWindow.hide()])
        textAES = QtWidgets.QLabel("""Private key security makes subscription payments, 
automated payments, and on chain reputations 
                extremely fraught with risk. """, self.homeWindow)
        textAES.setStyleSheet("""
                                            QLabel{
                                            font-size:16px;
                                            color:#fff;
                                            background-color:transparent;
                                            }
                                            QLabel:hover{
                                            transition: 0.9s;
                                            background-color:#FFF;
                                            color:#000
                                            }
                                        """)
        textAES.move(920, 520)
        photo = QtWidgets.QLabel(self.homeWindow)
        p = QPixmap("img/lock-laminated.png")
        photo.setPixmap(p)
        photo.setStyleSheet("""
        background-color:transparent;
        """)
        photo.move(1060,410)

    def _ecc_create(self):
        self.buttonOfEcc = QtWidgets.QPushButton("ECC Algorithm", self.homeWindow)
        self.buttonOfEcc.setStyleSheet("""
            QPushButton{
            color:#fff; 
            width:379px; 
            height:248.5px;
            display:inline;
            font-size:24px; 
            border:1px solid #ccc;
            font-weight:500; 
            border-top-right-radius:12px;
            }
            QPushButton:hover{
                
                background-color:#393939;
                color:#ccc

            }            
        """)
        self.buttonOfEcc.setToolTip("""
        The RC5 algorithm encrypt texts
        How to use:
                1- Enter the text
                2- Type the key 
                3- Click on the Encrypt button
        A window will appear for the result of the encryption process,
        indicating that the text has been encrypted

        """)
        self.buttonOfEcc.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonOfEcc.move(907, 120)
        self.buttonOfEcc.clicked.connect(lambda:[self.secondWindow.runProgramWindow(),self.homeWindow.hide()])
        textECC = QtWidgets.QLabel("""Private key security makes subscription payments, 
automated payments, and on chain reputations 
                extremely fraught with risk. """, self.homeWindow)
        textECC.setStyleSheet("""
                                            QLabel{
                                            font-size:16px;
                                            color:#fff;
                                            background-color:transparent
                                            }
                                            QLabel:hover{
                                            transition: 0.9s;
                                            background-color:#FFF;
                                            color:#000
                                            }
                                        """)
        textECC.move(920, 280)
        photo = QtWidgets.QLabel(self.homeWindow)
        p = QPixmap("img/dontBroke.png")
        photo.setPixmap(p)
        photo.move(1060, 150)
        photo.setStyleSheet("""
                background-color:transparent;
        """)

    """---function to open and close algorithms --- """
    def runProgram(self): 
        self.app = QtWidgets.QApplication(sys.argv)
        self.homeWindow = QtWidgets.QWidget()

        self.homeWindow.resize(1360, 650)
        self.homeWindow.setWindowTitle("Encrypt and Decrypt")
        self.homeWindow.setWindowIcon(QtGui.QIcon("../img/eye.png"))
        self.homeWindow.setStyleSheet("""
            /* background-color: #413C48*/
            background-color: #252525;
        """)
        title = "Encrypt"
        logo = QtWidgets.QLabel(title, self.homeWindow)
        logo.setStyleSheet("""        
        QLabel {
        color:#55ff88; 
        font-size: 32px ; 
        font-weight: 400;
        padding:10px; 
            }
            QLabel:hover{
                color:#55ff88;
                display:inline;
                cursor:pointer;
            }
       
        """)
        logo.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self._rc4_create()
        self._rc5_create()
        self._create_rc6()
        self._create_aes()
        self._ecc_create()
        exitButton = QtWidgets.QPushButton("Exit", self.homeWindow)
        exitButton.setStyleSheet("""
            QPushButton{
            color:#fff; 
            display:inline;
            padding:10px 30px;
            font-size:16px; 
            border:1px solid #55fc32;
            border-radius:2px;
            font-weight:600;

            }
            QPushButton:hover{
                
                background-color:#FF6969;
                color:#fff;
                border:none;
                transition:5s all

            }            
        """)
        exitButton.setToolTip("""
            Go To Desktop 
        """)
       
        exitButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        exitButton.clicked.connect(exit)
        exitButton.move(1200, 12)
        self.homeWindow.showFullScreen()
        self.app.exec_()

# this is object from class to start programming run 
run = Home()
run.runProgram()
