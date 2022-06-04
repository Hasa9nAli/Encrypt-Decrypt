from tkinter import S
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtGui import QCursor
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLineEdit, QFileDialog, QTextEdit
from rc4 import encryptRc4
from rc4 import decryptRc4
from rc5encryption import RC5
from rc5decryption import RC5D
from aes import AESCipher
from rc6encryption import *
from rc6decryption import *
from helpers import *
import string, random, subprocess,binascii, sys, os
from ECC0 import *


class WindowEnDc:
    def __init__(self, home): 
        self.file_name = None
        self.backButton = None 
        self.enDeWindow = None
        self.leftPhoto = None
        self.rightPhoto = None 
        self.uploadFileButton = None
        self.uploadFileLabel = None 
        self.rc4Button = None 
        self.rc5Button = None
        self.rc6Button = None
        self.aesButton = None
        self.eccButton = None
        self.encryptButton = None
        self.decryptButton = None
        self.home = home
        self.app = QtWidgets.QApplication(sys.argv)
        self.rc4Open = False
        self.rc5Open = False
        self.rc6Open = False
        self.aesOpen = False
        self.eccOpen = False
        self.path = None
        self.textFile = None
        """---setting of the window ---"""
        
    def upload_label(self):
       
        """label of upload file"""
        self.uploadFileLabel = QtWidgets.QLabel("Upload File", self.enDeWindow)
        self.uploadFileLabel.setStyleSheet("""
            font-size:22px ; 
            color:#ddd; 
            background-color:transparent; 
            
        """)
        self.uploadFileLabel.move(600,440)

    def _create_button(self, name, pos_x, pos_y, iPos_x=None, iPos_y=None, img_path = None):
        Button = QtWidgets.QPushButton(name,self.enDeWindow)
        Button.setStyleSheet("""
            QPushButton{
            background-color: #343436;
            padding:20px 100px 20px 60px;
            color:#FFF;
            font-size:22px ;
            font-weight:500;
            border-radius:10px ; 
            text-align:left;
            }
            QPushButton:hover{
                background:#4b4c4e;
            }
        """)
        Button.move(pos_x,pos_y)
        if img_path is not None:
            photo = QtWidgets.QLabel(self.enDeWindow)
            p = QPixmap(img_path)
            photo.setPixmap(p)
            photo.move(iPos_x, iPos_y)
            photo.setStyleSheet("""
                    background-color:transparent;
            """)
        Button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        return Button 
        
    def _back_button(self):
        self.backButton = QtWidgets.QPushButton("Back",self.enDeWindow)
        self.backButton.setStyleSheet("""
            background-color:#232323;
            color:#fff; 
            border:1px solid #77ff77; 
            padding : 5px 20px ; 
            border-radius :3px; 
            font-size :22px;
            font-weight:400;
        """)
        self.backButton.move(10,10)
        self.backButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.clicked.connect(lambda:[self.home.homeWindow.show(),self.enDeWindow.hide()])

    def _exit_button(self):
        exitButton = QtWidgets.QPushButton("Exit", self.enDeWindow)
        exitButton.setStyleSheet("""
                    QPushButton{
                    background-color:#232323;
                    color:#fff; 
                    border:1px solid #77ff77; 
                    padding : 5px 25px ; 
                    border-radius :3px; 
                    font-size :22px;
                    font-weight:400;
                    }
                    QPushButton:hover{
                        background-color:#ff7777;
                        border:none 

                    }
                """)
        exitButton.move(1250,10)
        exitButton.clicked.connect(exit)
        exitButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    def _create_file_button(self):
        self.uploadFileButton = QtWidgets.QPushButton("",self.enDeWindow)
        self.uploadFileButton.move(1365//2-90, 300)
        self.uploadFileButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.uploadFileButton.setStyleSheet("""
        QPushButton{
            background-image:url("img/folder-simple-plus.png");
            border-radius:12px;
            border:1px solid #CCC;}
        QPushButton:hover{
            background-color:#333

        }

        """)
        self.upload_label()
        self.uploadFileButton.resize(125,125)

    def browseFile(self):
        self.path = QFileDialog.getOpenFileName(self.enDeWindow,'Open file', f"{os.getcwd()}","text(*.txt *.py *.cpp *.js *.html *.css *.php )" )
         
    def _check_path(self,type, algorithm ):
        if self.path[0]:
            try:
                self.file = open(self.path[0])
                self.textFile = self.file.read()
                print(self.textFile)
                if type == "encrypt":
                    self.keyInput.clear()
                    self.confirmButtonDecrypt.hide()
                    self.confirmButton.show()
                elif type == "decrypt":
                    self.keyInput.clear()
                    self.confirmButton.hide()
                    self.confirmButtonDecrypt.show()
                if algorithm == "Rc4" or algorithm == "Rc5" or algorithm == "Rc6" or algorithm == "Aes" : 
                    self.keyLabel.show()
                    self.keyText.show()
                    self.keyInput.show()
                    self.correct_upload_file.show()
                elif algorithm == "Ecc" and type == "decrypt":
                    self.correct_upload_file.show()
                    self.keyLabel.show()
                    self.keyText.show()
                    self.keyInput.show()
                elif algorithm == "Ecc" and type != "decrypt":
                    self.correct_upload_file.show()

                    




            except: 
                self._error_message("please enter the correct file  ")

    def Rc4Encrypt(self):
        self.file_name_encrypt_rc4 = "encrypted by  Rc4 "+''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10))
        resultOFRc4Algorithm = open(f"{self.file_name_encrypt_rc4}.txt","w")
        key = self.keyInput.text()
        print(key)
        if len(key) > 4:
            try: 
                resultOFRc4Algorithm.write(encryptRc4(self.textFile, key))
                self.errorRc4.hide()
                self.placeOutPut.show()
                self.fileResult.show()
                self.openLabel.show()
                self.labelOutPut.show()
            except:
                self.errorRc4.setText("sorry there is error in the file ")
                self.errorRc4.show() 
        elif len(key) <= 4:
            self.errorRc4.show() 
                    
    def Rc4Decrypt(self):
        self.file_name_decrypt_Rc4 = "Decrypted by Rc4 "+''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10))
        key = self.keyInput.text()
        resultOFRc4Algorithm = open(f"{self.file_name_decrypt_Rc4}.txt", "w")
        if len(key) <= 4 : 
            self.errorRc4.show() 
        if len(key) > 4:
            try: 
                resultOFRc4Algorithm.write(decryptRc4(self.textFile, key))
                self.placeOutPut.show()
                self.fileResult.show()
                self.openLabel.show()
                self.labelOutPut.show()
            except:
                self.errorRc4.setText("sorry Error in the file or the file not encrypted by Rc4 ")
                self.errorRc4.show()

    def Rc5Encrypt(self):
        self.file_name_encrypt_rc5 = "Encrypted by Rc5 "+''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10))
        key = self.keyInput.text()
        resultOFRc5Algorithm = open(f"{self.file_name_encrypt_rc5}.txt", "w")
        rc5 = RC5(key)
        try:
            # rc5.encrypt_str(self.textFile)
            resultOFRc5Algorithm.write(rc5.encrypt_str(self.textFile))
            self.errorRc4.hide()
            self.placeOutPut.show()
            self.fileResult.show()
            self.openLabel.show()
            self.labelOutPut.show()
        except: 
            self.errorRc4.setText("sorry there is error in the file ")
            self.errorRc4.show()
    
    def Rc5Decrypt(self):
        self.file_name_decrypt_Rc5 =  "Decrypted by Rc5 "+''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10))
        key = self.keyInput.text() 
        resultOFRc4Algorithm = open(f"{self.file_name_decrypt_Rc5}.txt", "w")
        rc5 = RC5(key)
        try:
            resultOFRc4Algorithm.write(rc5.decrypt_str(self.textFile))
            self.errorRc4.hide()
            self.placeOutPut.show()
            self.fileResult.show()
            self.openLabel.show()
            self.labelOutPut.show()
        except:
            self.errorRc4.show()
            self.errorRc4.setText("sorry Error in the file or the file not encrypted by Rc5 ")


    def Rc6Encrypt(self): 
        self.file_name_encrypt_rc6 = "Encrypted by Rc6 "+''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10))
        key = self.keyInput.text()
        resultOFRc6Algorithm = open(f"{self.file_name_encrypt_rc6}.txt", "w")
        try:
            if len(key) < 16:
                key = key + " " * (16 - len(key))
            key = key[:16]
            s = generateKey(key)
            # sentence = 'I WORD IS A WORD'
            if len(text) < 16:
                text = text + " " * (16 - len(text))

            text = text[:16]
            orgi, cipher = encrypt(text, s)
            encrypted = deBlocker(cipher)
            # rc5.encrypt_str(self.textFile)
            resultOFRc6Algorithm.write(encrypted)
            self.errorRc4.hide()
            self.placeOutPut.show()
            self.fileResult.show()
            self.openLabel.show()
            self.labelOutPut.show()
        except: 
            self.errorRc4.setText("sorry the Rc6 under the maintains")
            self.errorRc4.show()
      
    def AesEncrypt(self):
        self.file_name_encrypt_Aes = "Encrypted by Aes  "+''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10))
        key = self.keyInput.text()
        resultOFAesAlgorithm = open(f"{self.file_name_encrypt_Aes}.txt", "w")
        aes = AESCipher(key)
        try:
            # rc5.encrypt_str(self.textFile)
            resultOFAesAlgorithm.write(aes.encrypt(self.textFile))
            self.errorRc4.hide()
            self.placeOutPut.show()
            self.fileResult.show()
            self.openLabel.show()
            self.labelOutPut.show()
        except: 
            self.errorRc4.setText("Sorry there is error in the file")
            self.errorRc4.show()
    
    def AesDecrypt(self):
        self.file_name_decrypt_Aes =  "Decrypted by AES "+''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10))
        key = self.keyInput.text() 
        resultOFAesAlgorithm = open(f"{self.file_name_decrypt_Aes}.txt", "w")
        aes = AESCipher(key)
        try:
            resultOFAesAlgorithm.write(aes.decrypt(self.textFile))
            self.errorRc4.hide()
            self.placeOutPut.show()
            self.fileResult.show()
            self.openLabel.show()
            self.labelOutPut.show()
        except:
            self.errorRc4.setText("the file not encrypted by Aes ")
            self.errorRc4.show()

    def eccEncrypt(self):
        self.file_name_encrypt_Ecc = "Encrypted by Ecc  "+''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10))
        resultOFEccAlgorithm = open(f"{self.file_name_encrypt_Ecc}.txt", "w")
        curve = registry.get_curve('brainpoolP256r1')
        try:
            msg = self.textFile
            privKey = secrets.randbelow(curve.field.n)
            self.keyInput.setText(hex(privKey)) 
            self.keyInput.setEchoMode(QLineEdit.Normal)

            # self.keyInput.setStyleSheet("""
            # font-size:16px ; 
            # padding:10px ; 
            # color: #777 ; 
            
            # """)
            print("private key:", hex(privKey))
            key = hex(privKey)
            aes = AESCipher(key)
            encryptedMsg = aes.encrypt(msg)
            print('encrypted text :', encryptedMsg)
            # rc5.encrypt_str(self.textFile)
            resultOFEccAlgorithm.write(encryptedMsg)
            self.errorRc4.hide()
            self.placeOutPut.show()
            self.fileResult.show()
            self.openLabel.show()
            self.labelOutPut.show()
            self.keyLabel.show()
            self.keyText.show()
            self.keyInput.show()
            self.copyButton.show()
            self.copyButton.clicked.connect(self.copy_Stuff)
        except: 
            self.errorRc4.setText("sorry there is error in the file".title())
            self.errorRc4.show()

    def eccDecrypt(self):
        self.file_name_decrypt_ecc =  "Decrypted by ECC "+''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10))
        key = self.keyInput.text() 
        resultOFAesAlgorithm = open(f"{self.file_name_decrypt_ecc}.txt", "w")
        aes = AESCipher(key)
        try:
            resultOFAesAlgorithm.write(aes.decrypt(self.textFile))
            self.errorRc4.hide()
            self.placeOutPut.show()
            self.fileResult.show()
            self.openLabel.show()
            self.labelOutPut.show()
        except:
            self.errorRc4.setText("the file not encrypted by Rc4".title()) 
            self.errorRc4.show()
    def copy_Stuff(self):
        self.keyInput.selectAll()
        self.keyInput.copy()

    def runProgramWindow(self, algorithm):
        self.enDeWindow = QtWidgets.QWidget()
        # window and style window 
        self.enDeWindow.setStyleSheet("""
            background-color:#232323; 
        """)
        
        self.copyButton = QtWidgets.QPushButton("",self.enDeWindow)
        self.copyButton.setStyleSheet("""
        QPushButton{
        background-image: url("img/copy.png");
        background-color:transparent; 
        padding-right:3px; 
        }
        QPushButton:hover{
            background-color:rgb(99, 99 , 99,0.5);
        }
      
        """)
        self.copyButton.resize(50,50)
        self.copyButton.move(800,550)
        self.copyButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.copyButton.hide()
        self.encryptButton = self._create_button("Encrypt",470,230)
        self.encryptButton.setStyleSheet("""
                QPushButton{
                padding:10px 50px;
                color:#000;
                background-color:#22ff88;
                font-size:22px;
                border-radius:8px;
                font-weight:400;
                }
                QPushButton:hover{
                    background-color:#22ff66;        
                    }
            """)
        self.textEdit = QTextEdit()
        self.textEdit.move(50,50)
        self.textEdit.resize(150,150)
        self.textEdit.setStyleSheet("""
            background:#fff
        """)

        self.confirmButtonDecrypt = self._create_button("Confirm",590,550)
        self.confirmButtonDecrypt.setStyleSheet("""
            background-color:#ff5544;
            padding:10px 30px ; 
            font-size:22px ;
            font-weight:400;
            border-radius:5px;

        """)
        self.encryptButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.decryptButton = self._create_button("Decrypt",670, 230)
        self.decryptButton.setStyleSheet("""
                QPushButton{
                padding:10px 50px;
                color:#000;
                background-color:#Ef6767;
                font-size:22px;
                border-radius:8px;
                font-weight:400;
                }
                QPushButton:hover{
                    background-color:#ee4567;
                    
                    }
            """)        
        # file upload encryption 
        self._create_file_button()
        self.uploadFileButton.close()
        self.uploadFileLabel.close()
        

        """key labels"""
        self.keyLabel = QtWidgets.QLabel("",self.enDeWindow)
        self.keyLabel.setStyleSheet("""
            background-color:#ee4567;
        """)
        self.keyLabel.resize(400, 40)
        self.keyLabel.move(460, 500)
        self.keyLabel.setStyleSheet("""
            background-color:#343436;
            border-radius:5px;
        """)
        """key text"""
        self.keyText = QtWidgets.QLabel("Key: ",self.enDeWindow)
        self.keyText.setStyleSheet("""
            background-color:transparent;
            font-size:24px; 
            font-weight:400;
            color:#22ff88;
            padding:10px;
            
        """)
        self.keyText.move(460,495)
        """button key text"""
        self.keyInput =  QLineEdit(self.enDeWindow)
        self.keyInput.setStyleSheet("""
        background-color:transparent;
        padding:1px 5px 1px 1px;
        font-size:18px;
        border-radius:5px;
        border:none; 
        color:#fcfcfc

        """)
        self.keyInput.setEchoMode(QLineEdit.Password)
        self.keyInput.move(523,500)
        self.keyInput.resize(340,40)
        self.keyInput.show()
        """button of confirm"""
        self.confirmButton = self._create_button("Confirm",590,550)
        self.confirmButton.setStyleSheet("""
            background-color:#ff7777;
            padding:10px 30px ; 
            font-size:22px ;
            font-weight:400;
            border-radius:5px;

        """)
        self.uploadFileDecryptLabel = QtWidgets.QPushButton("", self.enDeWindow)
        self.uploadFileDecryptLabel.setStyleSheet("""
        QPushButton{
            background-color: transparent;
            border-radius:12px ; 
            border:1px solid #ccc ; 
            background-image: url("img/folder-simple-plus-decrypt.png")
        }
        QPushButton:hover{
            background-color: #333

        }
          
        """)
        self.uploadFileDecryptLabel.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.uploadFileDecryptLabel.close()
        self.uploadFileDecryptLabel.resize(125,125)
        self.uploadFileDecryptLabel.move(1365//2-90, 300)

       
        self.correct_upload_file = QtWidgets.QLabel(self.enDeWindow)
        p = QPixmap("img/.png")
        self.correct_upload_file.setPixmap(p)
        self.correct_upload_file.move(550,380)
        self.correct_upload_file.setStyleSheet("""
                background-color:transparent;
        """)
    
        self.messageErrorRC4("please enter at lest 5 character ")
        self._place_output()
        # show the result of encrypt 
        # the file of result encryption 
        self.fileResult = QtWidgets.QPushButton("", self.enDeWindow)
        self.fileResult.setStyleSheet("""
        QPushButton{
        background-image: url("img/file-encrypted.png");
        border: 1px solid #ccc; 
        border-radius:12px;
        }
        QPushButton:hover{
            background-color:#474747;
        }
        """)
        self.fileResult.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.fileResult.resize(125,125)
        self.fileResult.move(980, 390)
        self.fileResult.clicked.connect(lambda:[subprocess.Popen(r'explorer /select,'+ os.getcwd())])

        self.openLabel = QtWidgets.QLabel("if you want to open the path file save\nclick here 👇",self.enDeWindow)
        self.openLabel.setStyleSheet("""
            font-size :16px ;
            color:#99ff99; 
            background-color :transparent; 


        """)
        self.openLabel.move(890, 310)

        self.rc4TextHead = QtWidgets.QLabel("welcome in RC4 encrypt & decrypt algorithm".title(),self.enDeWindow)
        self.rc4TextParagraph = QtWidgets.QLabel("this algorithm encrypt and decrypt Text,Html,Css,JS,Python,c++ file and more...",self.enDeWindow)
        self.rc4TextHead.setStyleSheet("""
            background-color :transparent;
            color: #A8FFB0;
            font-size:32px ; 
            font-weight:400;

        """)
        self.rc4TextParagraph.setStyleSheet("""
            background-color:transparent; 
            font-size:24px; 
            color:#C5FFCB; 
            font-weight:300;
        """)
        self.rc4TextHead.move(80, 80)
        self.rc4TextParagraph.move(90,135)
        """"""
        self.rc5TextHead = QtWidgets.QLabel("welcome in RC5 encrypt & decrypt algorithm".title(),self.enDeWindow)
        self.rc5TextParagraph = QtWidgets.QLabel("this algorithm encrypt and decrypt Text,Html,Css,JS,Python,c++ file and more...",self.enDeWindow)
        self.rc5TextHead.setStyleSheet("""
            background-color :transparent;
            color: #A8FFB0;
            font-size:32px ; 
            font-weight:400;

        """)
        self.rc5TextParagraph.setStyleSheet("""
            background-color:transparent; 
            font-size:24px; 
            color:#C5FFCB; 
            font-weight:300;
        """)
        self.rc5TextHead.move(80, 80)
        self.rc5TextParagraph.move(90,135)
        """"""
        self.rc6TextHead = QtWidgets.QLabel("welcome in RC4 encrypt & decrypt algorithm".title(),self.enDeWindow)
        self.rc6TextParagraph = QtWidgets.QLabel("this algorithm encrypt and decrypt short (just 16 character) Text,Html,Css,JS,Python,c++ file and more...",self.enDeWindow)
        self.rc6TextHead.setStyleSheet("""
            background-color :transparent;
            color: #A8FFB0;
            font-size:32px ; 
            font-weight:400;

        """)
        self.rc6TextParagraph.setStyleSheet("""
            background-color:transparent; 
            font-size:24px; 
            color:#C5FFCB; 
            font-weight:300;
        """)
        self.rc6TextHead.move(80, 80)
        self.rc6TextParagraph.move(90,135)
        """"""
        self.aesTextHead = QtWidgets.QLabel("welcome in AES encrypt & decrypt algorithm".title(),self.enDeWindow)
        self.aesTextParagraph = QtWidgets.QLabel("this algorithm encrypt and decrypt Text,Html,Css,JS,Python,c++ file and more...",self.enDeWindow)
        self.aesTextHead.setStyleSheet("""
            background-color :transparent;
            color: #A8FFB0;
            font-size:32px ; 
            font-weight:400;

        """)
        self.aesTextParagraph.setStyleSheet("""
            background-color:transparent; 
            font-size:24px; 
            color:#C5FFCB; 
            font-weight:300;
        """)
        self.aesTextHead.move(80, 80)
        self.aesTextParagraph.move(90,135)
        """"""
        self.eccTextHead = QtWidgets.QLabel("welcome in Ecc encrypt & decrypt algorithm".title(),self.enDeWindow)
        self.eccTextParagraph = QtWidgets.QLabel("this algorithm encrypt and decrypt Text,Html,Css,JS,Python,c++ file and more...\n and generate key ",self.enDeWindow)
        self.eccTextHead.setStyleSheet("""
            background-color :transparent;
            color: #A8FFB0;
            font-size:32px ; 
            font-weight:400;

        """)
        self.eccTextParagraph.setStyleSheet("""
            background-color:transparent; 
            font-size:24px; 
            color:#C5FFCB; 
            font-weight:300;
        """)
        self.eccTextHead.move(80, 80)
        self.eccTextParagraph.move(90,135)
      
        self.rc4TextHead.close()
        self.rc4TextParagraph.close()
        self.rc5TextHead.close()
        self.rc5TextParagraph.close()
        self.rc6TextHead.close()
        self.rc6TextParagraph.close()
        self.aesTextParagraph.close()
        self.aesTextHead.close()
        self.eccTextParagraph.close()
        self.eccTextHead.close()

        if algorithm == "Rc4":
            self.encryptButton.clicked.connect(lambda :[self.hide_all_decryption_content(),self.uploadFileButton.show(),self.uploadFileLabel.show()])
            self.uploadFileButton.clicked.connect(lambda :[self.browseFile(),self._check_path("encrypt","Rc4")])
            self.uploadFileDecryptLabel.clicked.connect(lambda:[self.browseFile(),self._check_path("decrypt","Rc4")])

            self.confirmButton.clicked.connect(lambda :[self.Rc4Encrypt()])
            self.decryptButton.clicked.connect(lambda:[self.hide_all_encryption_content(), self.uploadFileLabel.show(),self.uploadFileDecryptLabel.show()
            ])
            self.confirmButtonDecrypt.clicked.connect(lambda:[self.Rc4Decrypt()])
            self.rc4TextParagraph.show()
            self.rc4TextHead.show()


        elif algorithm == "Rc5":
            print("rc5")
            self.confirmButton.clicked.connect(lambda :[self.Rc5Encrypt()])
            self.encryptButton.clicked.connect(lambda :[self.hide_all_decryption_content(),self.uploadFileButton.show(),self.uploadFileLabel.show()])
            self.decryptButton.clicked.connect(lambda:[self.hide_all_encryption_content(), self.uploadFileLabel.show(),self.uploadFileDecryptLabel.show()])
            self.confirmButtonDecrypt.clicked.connect(lambda:[self.Rc5Decrypt()])
            self.uploadFileButton.clicked.connect(lambda :[self.browseFile(),self._check_path("encrypt","Rc5")])
            self.uploadFileDecryptLabel.clicked.connect(lambda:[self.browseFile(),self._check_path("decrypt","Rc5")])
            self.rc5TextHead.show()
            self.rc5TextParagraph.show()

        elif algorithm == "Rc6":
            self.confirmButton.clicked.connect(lambda :[self.Rc6Encrypt()])
            self.encryptButton.clicked.connect(lambda :[self.hide_all_decryption_content(),self.uploadFileButton.show(),self.uploadFileLabel.show()])
            self.decryptButton.clicked.connect(lambda:[self.hide_all_encryption_content(), self.uploadFileLabel.show(),self.uploadFileDecryptLabel.show()])
            self.confirmButtonDecrypt.clicked.connect(lambda:[self.Rc5Decrypt()])
            self.uploadFileButton.clicked.connect(lambda :[self.browseFile(),self._check_path("encrypt","Rc6")])
            self.uploadFileDecryptLabel.clicked.connect(lambda:[self.browseFile(),self._check_path("decrypt","Rc6")])
            self.rc6TextHead.show()
            self.rc6TextParagraph.show()
            print("rc6")
        elif algorithm == "Aes":
            self.confirmButton.clicked.connect(lambda :[self.AesEncrypt()])
            self.encryptButton.clicked.connect(lambda :[self.hide_all_decryption_content(),self.uploadFileButton.show(),self.uploadFileLabel.show()])
            self.decryptButton.clicked.connect(lambda:[self.hide_all_encryption_content(), self.uploadFileLabel.show(),self.uploadFileDecryptLabel.show()])
            self.confirmButtonDecrypt.clicked.connect(lambda:[self.AesDecrypt()])
            self.uploadFileButton.clicked.connect(lambda :[self.browseFile(),self._check_path("encrypt","Aes")])
            self.uploadFileDecryptLabel.clicked.connect(lambda:[self.browseFile(),self._check_path("decrypt","Aes")])
            self.aesTextHead.show()
            self.aesTextParagraph.show()
          

        elif algorithm == "Ecc":
            self.confirmButton.clicked.connect(lambda :[self.eccEncrypt()])
            self.encryptButton.clicked.connect(lambda :[self.hide_all_decryption_content(),self.uploadFileButton.show(),self.uploadFileLabel.show()])
            self.decryptButton.clicked.connect(lambda:[self.hide_all_encryption_content(), self.uploadFileLabel.show(),self.uploadFileDecryptLabel.show()])
            self.confirmButtonDecrypt.clicked.connect(lambda:[self.AesDecrypt()])
            self.uploadFileButton.clicked.connect(lambda :[self.browseFile(),self._check_path("encrypt","Ecc")])
            self.confirmButtonDecrypt.clicked.connect(lambda:[self.eccDecrypt()])
            self.uploadFileDecryptLabel.clicked.connect(lambda:[self.browseFile(),self._check_path("decrypt","Ecc")])

            self.eccTextHead.show()
            self.eccTextParagraph.show()
            
        
        # show

        
     
        
       
        self.correct_upload_file = QtWidgets.QLabel(self.enDeWindow)
        p = QPixmap("img/correct-upload.png")
        self.correct_upload_file.setPixmap(p)
        self.correct_upload_file.move(550,380)
        self.correct_upload_file.setStyleSheet("""
                background-color:transparent;
        """)
      
        """setting the exit button"""
        self._exit_button()
        """create the upload file """

        """-- the back button--"""
        self._back_button()
        self._close_()

        self.enDeWindow.showFullScreen()
        self.app.exec_()
    
    
    def _close_(self):
        self.errorRc4.close()    
        self.keyLabel.close()
        self.keyText.close()
        self.keyInput.close()
        self.confirmButton.close()
        self.correct_upload_file.close()
        self.placeOutPut.close()
        self.fileResult.close()
        self.openLabel.close()
        self.labelOutPut.close()
        self.confirmButtonDecrypt.close()
       

    def hide_all_encryption_content(self):
        self.uploadFileButton.hide()
        self.errorRc4.hide()
        self.placeOutPut.hide()
        self.labelOutPut.hide()
        self.openLabel.hide()
        self.keyLabel.hide()
        self.keyInput.hide()
        self.keyText.hide()
        self.confirmButton.hide()
        self.uploadFileLabel.hide()
        self.fileResult.hide()
        self.correct_upload_file.hide()
        self.copyButton.hide()

    def hide_all_decryption_content(self): 
        self.uploadFileDecryptLabel.hide()
        self.errorRc4.hide()
        self.placeOutPut.hide()
        self.labelOutPut.hide()
        self.openLabel.hide()
        self.confirmButtonDecrypt.hide()
        self.uploadFileLabel.hide()
        self.fileResult.hide()
        self.correct_upload_file.hide()
        self.keyLabel.hide()
        self.keyInput.hide()
        self.keyText.hide()
        

        
    
    def messageErrorRC4(self, massage):
        self.errorRc4 = QtWidgets.QLabel(massage.title(), self.enDeWindow)
        self.errorRc4.move(450, 620)   
        self.errorRc4.setStyleSheet("""
            color:#ff7777;
            background-color:#464646;
            padding :10px 50px 10px 50px; 
            font-size:22px ;
            border-radius:12px ; 
            

        """)

    def _place_output(self):
        
        self.placeOutPut = QtWidgets.QLabel("", self.enDeWindow)
        self.placeOutPut.setStyleSheet("""
            
            border-radius:4px ;
            border:1px solid #ccc; 
            background-color:#232323
        """)
        self.placeOutPut.move(880,250)
        self.placeOutPut.resize(350,400)
        
        
        self.labelOutPut = QtWidgets.QLabel("OutPut: the file is Encrypted... ",self.enDeWindow)
        self.labelOutPut.setStyleSheet("""
            font-size: 18px;
            color:#44dd44;
            font-weight:400
        """)
        self.labelOutPut.move(890, 270)
    


        
