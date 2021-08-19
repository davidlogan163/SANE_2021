import sys
from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *

# Function to quit the program
def Quit():
    App.quit()

# Function to calculate averages and display averages and assigments with grades
def calculate():
    # Calculating total grade average with weights
    total = ((UI.spinBox.value()*0.3) + (UI.spinBox_2.value()*0.1) + (UI.spinBox_3.value()*0.15) + (UI.spinBox_4.value()*0.1)
    + (UI.spinBox_5.value()*0.15) + (UI.spinBox_6.value()*0.2))

    # Logic for calculating grade letter
    if total >= 89.5: grade = "A"
    elif total >= 79.5: grade = "B"
    elif total >= 69.5: grade = "C"
    elif total >= 59.5: grade = "D"
    else: grade = "F"
 
    # Gathering the data from the labels and the spin boxes where the user enters the grade numbers
    # Also outputting the data in a neat format
    UI.label_3.setText(str(UI.label_5.text())  +  "  \t       |  " + "Grade: " + str(UI.spinBox.value())   + "\n"
                     + str(UI.label_6.text())  +  "  |  "          + "Grade: " + str(UI.spinBox_2.value()) + "\n"
                     + str(UI.label_7.text())  +  "  \t       |  " + "Grade: " + str(UI.spinBox_3.value()) + "\n"
                     + str(UI.label_8.text())  +  "  \t       |  " + "Grade: " + str(UI.spinBox_4.value()) + "\n"
                     + str(UI.label_9.text())  +  "  \t       |  " + "Grade: " + str(UI.spinBox_5.value()) + "\n"
                     + str(UI.label_10.text()) +  "  \t       |  " + "Grade: " + str(UI.spinBox_6.value()) + "\n")

    # Logic for the background color for each letter grade
    if grade ==   "A":
        BG_Color = UI.label_4.setStyleSheet("background-color: green")
    elif grade == "B":
        BG_Color = UI.label_4.setStyleSheet("background-color: cyan")
    elif grade == "C":
        BG_Color = UI.label_4.setStyleSheet("background-color: yellow")
    elif grade == "D":
        BG_Color = UI.label_4.setStyleSheet("background-color: orange")
    else:
        BG_Color = UI.label_4.setStyleSheet("background-color: red")

    # Outputting the grade average with the background color
    UI.label_4.setText("Average: " + grade + "  |  " + "%.2f" % total)
    UI.label_4.setStyleSheet("QLabel {background-color :" + BG_Color + "color : " )

App = QtWidgets.QApplication([])
UI=uic.loadUi("grade.ui")

# Push button to calculate and display the total average and display the assigment and its specific grade
UI.pushButton.clicked.connect(calculate)

# Button to quit the program
UI.actionQuit.triggered.connect(Quit)

UI.show()
sys.exit(App.exec_())