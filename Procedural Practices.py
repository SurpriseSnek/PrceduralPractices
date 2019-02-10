from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
import sys
import random
import keyboard
import os
import time


def getName():
    firstName = ["Liam","Emma","Noah","Olivia","William","Ava","James","Isabella","Logan","Sophia","Benjamin","Mia","Mason","Charlotte","Elijah","Amelia","Oliver","Evelyn","Jacob","Emily"]
    lastName = ["Smith","Johnson","Williams","Jones","Brown","Davis","Miller","Wilson","Moore","Taylor"]
    firstNum = random.randint(0, 19)
    lastNum = random.randint(0, 9)
    return (firstName[firstNum] + " " + lastName[lastNum])

def getSurgery():
    diseaseName = ["Appendicitis", "Tuberculosis", "Frostbite", "Crippling Debt", "Heat Exhaustion","Shark Attack","Fortnitis","Alien Hand Syndrome","Boanthropy","Cotard Disorder"]
    diseaseNum = random.randint(0, len(diseaseName) - 1)
    return (diseaseName[diseaseNum])

def getMod():
    chance = random.randint(0,5)
    if chance == 0:
        return "Moving Vehicle"
    elif chance == 1:
        return "Friday The 13th"
    elif chance == 2:
        return "Blood Moon"
    elif chance == 3:
        return "Close To Death"
    elif chance == 4:
        return "College Practice"
    elif chance == 5:
        return "Minor Injury"

class Ui_MainWindow(object):
    global surgeriesComplete
    surgeriesComplete = 0

    global patientStatus
    patientStatus = ""

    global stepCounter
    stepCounter = 0

    global surgeryPattern
    surgeryPattern = []

    global surgerySteps
    surgerySteps = []

    global workingOnPatient
    workingOnPatient = False
    def commandCheck(self, commandInput):
        global workingOnPatient, surgerySteps
        if workingOnPatient == True:
            if commandInput == "Cut":
                surgerySteps.append('0')
                return "You cut into the patient."
            elif commandInput == "Move":
                surgerySteps.append('1')
                return "You move organs and tissue out of the way."
            elif commandInput == "Stitch":
                surgerySteps.append('2')
                return "You artfully stitch the patient."
            elif commandInput == "Fasten":
                surgerySteps.append('3')
                return "You fasten down part of the body."
            elif commandInput == "Transplant":
                surgerySteps.append('4')
                return "You transplant the organ safely"
            elif commandInput == "Savings":
                surgerySteps.append('5')
                return "You teach your patient the art of saving money."
            elif commandInput == "Fan":
                surgerySteps.append('6')
                return "You fan your patient to cool them off."
            elif commandInput == "Anesthetic":
                surgerySteps.append('7')
                return "You inject anesthetic into the patient."
            elif commandInput == "Hypnosis":
                surgerySteps.append('8')
                return "You dafely hypnotize the patient."
            elif commandInput == "Finish":
                return self.checkIfCured()
                
            elif commandInput == "Wolf":
                if self.PetientLayout.item(0,2) == "Blood Moon":
                    if self.TableStats.item(3,1) >= 15:
                        mod = self.PetientLayout.item(0,2)
                        acc = self.TableStats.item(0,1)
                        pwr = self.TableStats.item(1,1)
                        lck = self.TableStats.item(2,1)
                        snt = self.TableStats.item(3,1)
                        dgr = self.TableStats.item(4,1)
                        randStatNum = random.randint(0,3)
                        if randStatNum == 0:
                            self.TableStats.setItem(0,1, QtWidgets.QTableWidgetItem(acc + 1))
                        if randStatNum == 1:
                            self.TableStats.setItem(1,1, QtWidgets.QTableWidgetItem(pwr + 1))
                        if randStatNum == 2:
                            self.TableStats.setItem(2,1, QtWidgets.QTableWidgetItem(lck + 1))
                        if randStatNum == 3:
                            self.TableStats.setItem(4,1, QtWidgets.QTableWidgetItem(dgr + 1))
                    else:
                        return "You're not ready"
                else:
                    return "It's not time yet"
            else:
                return "You can't do that."
        elif commandInput == "Help":
            return '''
Handbook - Lists how to complete the surgeries (only accessible between surgeries).
Help - Gets you here.
Start - Enters the most recent surgery

- In-Surgery ACtions -
Cut - Cuts into the patient.
Move - Moves aside internal objects.
Fasten - Tightens down part of the patient's body.
Transplant - Replaces cut body part(s).
Savings - Teaches the patient about saving money with Dave Ramsey.
Fan - Cool down patient's body temp.
Anis
Finish  - Finish Surgery and clean things up.
Wolf - ?????
'''
            
        elif commandInput == 'Start':
            workingOnPatient = True
            stepCounter = 0
            patientStatus = "InProgress"
            procOne = ""
            procTwo = ""
            if (int(self.TableStats.item(3,1).text()) * 15) >= random.randint(30,75):
                procOne = surgeryPattern[0]
                if (int(self.TableStats.item(3,1).text()) * 15) >= random.randint(60,75):
                    procTwo = surgeryPattern[1]
            return '''Bringing in your patient!
''' + procOne + '''
''' + procTwo
        elif commandInput == 'Handbook':
            if workingOnPatient == False:
                return '''
AP - Cut, Move, Fasten, Cut, Fasten, Move, Stitch
TB - Cut, Move, Cut, Move, Fasten, Cut, Transplant, Move, Stitch, Stitch
FB - Fasten, Cut, Cut, Fasten, Stitch
CD - Savings, Savings, Savings, Stitch
HE - Fan, Cut, Fasten, Fan
SA - Anisthetic, Stitches, Transplant, Stitches
F - Fasten, Hypnosis, Savings
AHS - Anisthetic, Cut, Stitches
B - Fasten, Hypnosis, Hypnosis
CD - Fan, Hypnosis, Fasten, Hypnosis

0 - Cut
1 - Move
2 - Stitch
3 - Fasten
4 - Transplant
5 - Savings
6 - Fan
7 - Anesthetic
8 - Hypnosis
'''
            else:
                return "You're busy with the patient."
        else:
            return "You can't do that."

            
    def randomizeStats():
        stats = []
        for i in range(5):
            num = random.randint(0,5)
        if num == 5:
            random.randint(0,5)
            stats.append(num)
            self.TableStats.setItem((i),1, num)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(821, 615)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("LCD Solid")
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 550, 821, 21))
        self.plainTextEdit.setAutoFillBackground(False)
        self.plainTextEdit.setStyleSheet("background-color: rgb(20, 20, 20);\n"
"color: rgb(255, 255, 255);")
        self.plainTextEdit.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.plainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.PrevActionList = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.PrevActionList.setGeometry(QtCore.QRect(0, 330, 821, 221))
        self.PrevActionList.setStyleSheet("background-color: rgb(5, 5, 5);\n"
"color: rgb(255, 255, 255);")
        self.PrevActionList.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.PrevActionList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.PrevActionList.setObjectName("PrevActionList")
        self.TableStats = QtWidgets.QTableWidget(self.centralwidget)
        self.TableStats.setGeometry(QtCore.QRect(0, 180, 201, 151))
        font = QtGui.QFont()
        font.setFamily("LCD Solid")
        self.TableStats.setFont(font)
        self.TableStats.setAutoFillBackground(False)
        self.TableStats.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.TableStats.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.TableStats.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.TableStats.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.TableStats.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.TableStats.setShowGrid(True)
        self.TableStats.setRowCount(5)
        self.TableStats.setColumnCount(2)
        self.TableStats.setObjectName("TableStats")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("LCD Solid")
        item.setFont(font)
        self.TableStats.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("LCD Solid")
        item.setFont(font)
        self.TableStats.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("LCD Solid")
        item.setFont(font)
        self.TableStats.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("LCD Solid")
        item.setFont(font)
        self.TableStats.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("LCD Solid")
        item.setFont(font)
        self.TableStats.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("LCD Solid")
        item.setFont(font)
        self.TableStats.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("LCD Solid")
        item.setFont(font)
        self.TableStats.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("LCD Solid")
        item.setFont(font)
        self.TableStats.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("LCD Solid")
        item.setFont(font)
        self.TableStats.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("LCD Solid")
        item.setFont(font)
        self.TableStats.setItem(4, 1, item)
        self.TableStats.horizontalHeader().setVisible(False)
        self.TableStats.verticalHeader().setVisible(False)
        self.PetientLayout = QtWidgets.QTableWidget(self.centralwidget)
        self.PetientLayout.setGeometry(QtCore.QRect(200, 0, 621, 331))
        font = QtGui.QFont()
        font.setFamily("LCD Solid")
        self.PetientLayout.setFont(font)
        self.PetientLayout.setAutoFillBackground(False)
        self.PetientLayout.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.PetientLayout.setLineWidth(1)
        self.PetientLayout.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.PetientLayout.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.PetientLayout.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.PetientLayout.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.PetientLayout.setShowGrid(True)
        self.PetientLayout.setCornerButtonEnabled(False)
        self.PetientLayout.setRowCount(10)
        self.PetientLayout.setColumnCount(3)
        self.PetientLayout.setObjectName("PetientLayout")
        item = QtWidgets.QTableWidgetItem()
        self.PetientLayout.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.PetientLayout.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.PetientLayout.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.PetientLayout.setItem(1, 2, item)
        self.PetientLayout.horizontalHeader().setVisible(True)
        self.PetientLayout.horizontalHeader().setDefaultSectionSize(198)
        self.PetientLayout.horizontalHeader().setMinimumSectionSize(15)
        self.PetientLayout.verticalHeader().setVisible(True)
        self.PetientLayout.verticalHeader().setDefaultSectionSize(31)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 201, 181))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Doctor.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.enterButton = QtWidgets.QPushButton(self.centralwidget)
        self.enterButton.setGeometry(QtCore.QRect(764, 550, 61, 23))
        self.enterButton.setObjectName("enterButton")
        self.plainTextEdit.raise_()
        self.PrevActionList.raise_()
        self.label.raise_()
        self.TableStats.raise_()
        self.PetientLayout.raise_()
        self.enterButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 821, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Precedural Practices"))
        __sortingEnabled = self.TableStats.isSortingEnabled()
        self.TableStats.setSortingEnabled(False)
        item = self.TableStats.item(0, 0)
        item.setText(_translate("MainWindow", "Accuracy"))
        item = self.TableStats.item(1, 0)
        item.setText(_translate("MainWindow", "Strength"))
        item = self.TableStats.item(2, 0)
        item.setText(_translate("MainWindow", "Luck"))
        item = self.TableStats.item(3, 0)
        item.setText(_translate("MainWindow", "Insanity"))
        item = self.TableStats.item(4, 0)
        item.setText(_translate("MainWindow", "Degree"))

        stats = []
        for i in range(5):
            num = random.randint(0,5)
            if num == 5:
                random.randint(0,5)
            stats.append(num)
            self.TableStats.setItem((i),1, QtWidgets.QTableWidgetItem(str(num)))
        while sum(stats) < 10:
            stats = []
            for i in range(5):
                num = random.randint(0,5)
                if num == 5:
                    random.randint(0,5)
                stats.append(num)
                self.TableStats.setItem((i),1, QtWidgets.QTableWidgetItem(str(num)))
        
        self.TableStats.setSortingEnabled(__sortingEnabled)
        item = self.PetientLayout.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Patient Name"))
        item = self.PetientLayout.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Surgery"))
        item = self.PetientLayout.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Modifier"))

        for i in range(10):
            name = getName()
            surgery = getSurgery()
            if (random.randint(1,10)) <= 4:
                mod = getMod()
            else:
                mod = 'None'
            self.PetientLayout.setItem((i),0, QtWidgets.QTableWidgetItem(str(name)))
            self.PetientLayout.setItem((i),1, QtWidgets.QTableWidgetItem(str(surgery)))
            self.PetientLayout.setItem((i),2, QtWidgets.QTableWidgetItem(str(mod)))

        __sortingEnabled = self.PetientLayout.isSortingEnabled()
        self.PetientLayout.setSortingEnabled(False)
        self.PetientLayout.setSortingEnabled(__sortingEnabled)
        self.enterButton.setText(_translate("MainWindow", "Enter"))
        self.enterButton.clicked.connect(lambda val: self.textEval())

    def textEval(self):
        global surgeriesComplete
        global surgeryPattern
        global stepCounter
        commandText = ""
        commandText = str(self.plainTextEdit.toPlainText())
        commandResponse = self.commandCheck(str(commandText))
        self.PrevActionList.setPlainText(str(self.plainTextEdit.toPlainText()) + '''
> ''' + commandText + '''
''' + commandResponse)
        if workingOnPatient == True:
            if self.PetientLayout.item(0, 1) == 'Appendicitis':
                surgeryPattern = ['0','1','3','0','3','0','2']
                if surgerySteps[:(stepCounter)] != surgeryPattern[:(stepCounter)]:
                    if (self.TableStats.item(2,1)) * 5 >= random.randint(10,20):
                        surgerySteps[:(stepCounter)] = surgeryPattern[:(stepCounter)]
                    else:
                        self.PrevActionList.setPlainText(str(self.plainTextEdit.toPlainText()) + '''
> ''' + "You're patient has died. You're fired!")
                        time.sleep(5)
                        self.close()
            elif self.PetientLayout.item(0, 1) == 'Tuberculosis':
                surgeryPattern = ['0','1','0','1','3','0','4','0','2','2']
                if surgerySteps[:(stepCounter)] != surgeryPattern[:(stepCounter)]:
                    if (self.TableStats.item(2,1))*5 >= random.randint(10,20):
                        surgerySteps[:(stepCounter)] = surgeryPattern[:(stepCounter)]
                    else:
                        self.PrevActionList.setPlainText(str(self.plainTextEdit.toPlainText()) + '''
> ''' + "You're patient has died. You're fired!")
                        time.sleep(5)
                        self.close()
            elif self.PetientLayout.item(0, 1) == 'Frostbite':
                surgeryPattern = ['3','0','0','3','2']
                if surgerySteps[:(stepCounter)] != surgeryPattern[:(stepCounter)]:
                    if (self.TableStats.item(2,1))*5 >= random.randint(10,20):
                        surgerySteps[:(stepCounter)] = surgeryPattern[:(stepCounter)]
                    else:
                        self.PrevActionList.setPlainText(str(self.plainTextEdit.toPlainText()) + '''
> ''' + "You're patient has died. You're fired!")
                        time.sleep(5)
                        self.close()
            elif self.PetientLayout.item(0, 1) == 'Crippling Debt':
                surgeryPattern = ['0','1','3','0','3','0','2']
                if surgerySteps[:(stepCounter)] != surgeryPattern[:(stepCounter)]:
                    if (self.TableStats.item(2,1))*5 >= random.randint(10,20):
                        surgerySteps[:(stepCounter)] = surgeryPattern[:(stepCounter)]
                    else:
                        self.PrevActionList.setPlainText(str(self.plainTextEdit.toPlainText()) + '''
> ''' + "You're patient has died. You're fired!")
                        time.sleep(5)
                        self.close()
            elif self.PetientLayout.item(0, 1) == 'Heat Exhaustion':
                surgeryPattern = ['0','1','3','0','3','0','2']
                if surgerySteps[:(stepCounter)] != surgeryPattern[:(stepCounter)]:
                    if (self.TableStats.item(2,1))*5 >= random.randint(10,20):
                        surgerySteps[:(stepCounter)] = surgeryPattern[:(stepCounter)]
                    else:
                        self.PrevActionList.setPlainText(str(self.plainTextEdit.toPlainText()) + '''
> ''' + "You're patient has died. You're fired!")
                        time.sleep(5)
                        self.close()
            elif self.PetientLayout.item(0, 1) == 'Shark Attack':
                surgeryPattern = ['7','2','4','2']
                if surgerySteps[:(stepCounter)] != surgeryPattern[:(stepCounter)]:
                    if (self.TableStats.item(2,1))*5 >= random.randint(10,20):
                        surgerySteps[:(stepCounter)] = surgeryPattern[:(stepCounter)]
                    else:
                        self.PrevActionList.setPlainText(str(self.plainTextEdit.toPlainText()) + '''
> ''' + "You're patient has died. You're fired!")
                        time.sleep(5)
                        self.close()
            elif self.PetientLayout.item(0, 1) == 'Fortnitis':
                surgeryPattern = ['3','8','5']
                if surgerySteps[:(stepCounter)] != surgeryPattern[:(stepCounter)]:
                    if (self.TableStats.item(2,1))*5 >= random.randint(10,20):
                        surgerySteps[:(stepCounter)] = surgeryPattern[:(stepCounter)]
                    else:
                        self.PrevActionList.setPlainText(str(self.plainTextEdit.toPlainText()) + '''
> ''' + "You're patient has died. You're fired!")
                        time.sleep(5)
                        self.close()
            elif self.PetientLayout.item(0, 1) == 'Alien Hand Syndrome':
                surgeryPattern = ['7','0','2']
                if surgerySteps[:(stepCounter)] != surgeryPattern[:(stepCounter)]:
                    if (self.TableStats.item(2,1))*5 >= random.randint(10,20):
                        surgerySteps[:(stepCounter)] = surgeryPattern[:(stepCounter)]
                    else:
                        self.PrevActionList.setPlainText(str(self.plainTextEdit.toPlainText()) + '''
> ''' + "You're patient has died. You're fired!")
                        time.sleep(5)
                        self.close()
            elif self.PetientLayout.item(0, 1) == 'Boanthropy':
                surgeryPattern = ['3','8','8']
                if surgerySteps[:(stepCounter)] != surgeryPattern[:(stepCounter)]:
                    if (self.TableStats.item(2,1))*5 >= random.randint(10,20):
                        surgerySteps[:(stepCounter)] = surgeryPattern[:(stepCounter)]
                    else:
                        self.PrevActionList.setPlainText(str(self.plainTextEdit.toPlainText()) + '''
> ''' + "You're patient has died. You're fired!")
                        time.sleep(5)
                        self.close()
            elif self.PetientLayout.item(0, 1) == 'Cotard Disorder':
                surgeryPattern = ['6','8','3','8']
                if surgerySteps[:(stepCounter)] != surgeryPattern[:(stepCounter)]:
                    if (self.TableStats.item(2,1))*5 >= random.randint(10,20):
                        surgerySteps[:(stepCounter)] = surgeryPattern[:(stepCounter)]
                    else:
                        self.PrevActionList.setPlainText(str(self.plainTextEdit.toPlainText()) + '''
> ''' + "You're patient has died. You're fired!")
                        time.sleep(5)
                        self.close()

        self.plainTextEdit.setPlainText('')


    def checkMod(self):
        if self.PetientLayout.item(0,2) != 'None':
            mod = self.PetientLayout.item(0,2)
            acc = self.TableStats.item(0,1)
            pwr = self.TableStats.item(1,1)
            lck = self.TableStats.item(2,1)
            snt = self.TableStats.item(3,1)
            dgr = self.TableStats.item(4,1)
            if mod == "Moving Vehicle":                    
                self.TableStats.setItem(0,1, QtWidgets.QTableWidgetItem(acc - 1))
                self.TableStats.setItem(4,1, QtWidgets.QTableWidgetItem(dgr + (0.5 * acc)))

            if mod == "Friday The 13th":
                self.TableStats.setItem(2,1, QtWidgets.QTableWidgetItem(lck - (10 - acc)))

            if mod == "Blood Moon":
                self.TableStats.setItem(3,1, QtWidgets.QTableWidgetItem(snt + (0.5 * acc)))
                self.TableStats.setItem(1,1, QtWidgets.QTableWidgetItem(pwr + (0.5 * acc)))
                self.TableStats.setItem(4,1, QtWidgets.QTableWidgetItem(dgr - (10 - acc)))

            if mod == "Close To Death":
                self.TableStats.setItem(0,1, QtWidgets.QTableWidgetItem(acc + (0.5 * acc)))
                self.TableStats.setItem(3,1, QtWidgets.QTableWidgetItem(snt + (0.5 * acc)))

            if mod == "College Practice":
                self.TableStats.setItem(3,1, QtWidgets.QTableWidgetItem(snt - (10 + acc)))
                self.TableStats.setItem(4,1, QtWidgets.QTableWidgetItem(dgr - (10 - acc)))

            if mod == "Minor Injury":
                self.TableStats.setItem(2,1, QtWidgets.QTableWidgetItem(lck + (0.5 * acc)))
                self.TableStats.setItem(3,1, QtWidgets.QTableWidgetItem(snt - (10 + acc)))
                self.TableStats.setItem(0,1, QtWidgets.QTableWidgetItem(acc + 2))
                self.TableStats.setItem(1,1, QtWidgets.QTableWidgetItem(pwr + (0.5 * acc)))


    def checkIfCured(self):
        global surgerySteps, surgeriesComplete, workingOnPatient
        surgeryPattern = []
        if (self.PetientLayout.item(0, 1).text()) == 'Appendicitis':
            surgeryPattern = ['0','1','3','0','3','1','2']
        elif (self.PetientLayout.item(0, 1).text()) == 'Tuberculosis':
            surgeryPattern = ['0','1','0','1','3','0','4','0','2','2']
        elif (self.PetientLayout.item(0, 1).text()) == 'Frostbite':
            surgeryPattern = ['3','0','0','3','2']
        elif (self.PetientLayout.item(0, 1).text()) == 'Crippling Debt':
            surgeryPattern = ['0','1','3','0','3','0','2']
        elif (self.PetientLayout.item(0, 1).text()) == 'Heat Exhaustion':
            surgeryPattern = ['0','1','3','0','3','0','2']
        elif (self.PetientLayout.item(0, 1).text()) == 'Shark Attack':
            surgeryPattern = ['7','2','4','2']
        elif (self.PetientLayout.item(0, 1).text()) == 'Fortnitis':
            surgeryPattern = ['3','8','5']
        elif (self.PetientLayout.item(0, 1).text()) == 'Alien Hand Syndrome':
            surgeryPattern = ['7','0','2']
        elif (self.PetientLayout.item(0, 1).text()) == 'Boanthropy':
            surgeryPattern = ['3','8','8']
        elif (self.PetientLayout.item(0, 1).text()) == 'Cotard Disorder':
            surgeryPattern = ['6','8','3','8']

        for i in range(9):
            movePerson = self.PetientLayout.item((i+1),0).text()
            moveIllness = self.PetientLayout.item((i+1),1).text()
            moveMod = self.PetientLayout.item((i+1),2).text()
            self.PetientLayout.setItem((i),0, QtWidgets.QTableWidgetItem(str(movePerson)))
            self.PetientLayout.setItem((i),1, QtWidgets.QTableWidgetItem(str(moveIllness)))
            self.PetientLayout.setItem((i),2, QtWidgets.QTableWidgetItem(str(moveMod)))


        name = getName()
        surgery = getSurgery()
        if (random.randint(1,10)) <= 4:
            mod = getMod()
        else:
            mod = 'None'
        self.PetientLayout.setItem(9,0, QtWidgets.QTableWidgetItem(str(name)))
        self.PetientLayout.setItem(9,1, QtWidgets.QTableWidgetItem(str(surgery)))
        self.PetientLayout.setItem(9,2, QtWidgets.QTableWidgetItem(str(mod)))

        if surgeryPattern == surgerySteps:
            surgeriesComplete += 1
            workingOnPatient = False
            return('''Congratulations! You just saved a life!
You have completed %s operations! Keep it up!''' % surgeriesComplete)
        else:
            return('''You let a patient die!
Commit feel bad.''')
        
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())
