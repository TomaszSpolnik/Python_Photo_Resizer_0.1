import cv2
import tkinter as tk
from tkinter.simpledialog import askstring
from tkinter import filedialog
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
import sys
import os

root = tk.Tk()  # Tkinter for user prompt
root.withdraw() # Hide deafult window
curr_dir = os.getcwd() # Assign path
correct_style_button = ("QPushButton {background-color: qlineargradient(spread:pad, x1:0.045, y1:0.886, x2:0.96, "
                        "y2:0.057, stop:0 rgba(56, 128, 140, 186), stop:0.495 rgba(85, 161, 167, 179), stop:1 rgba("
                        "149, 187, 189, 167));border:none;padding-top: 5px;color: rgb(255,255, 255);font: 900 9pt "
                        "\"Segoe UI\";border-radius: 5px;border-left: 1px solid rgb(0, 255, 127);border-right: 1px "
                        "solid rgb(0, 255, 127);border-top: 1px solid rgb(0, 255, 127);border-bottom: 1px solid rgb("
                        "0, 255, 127);border-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba("
                        "192, 253, 255, 255), stop:0.525 rgba(115, 233, 242, 238), stop:1 rgba(65, 173, 192, "
                        "238));}QPushButton:hover{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1,"
                        "y2:0,stop:0 rgba(192, 253, 255, 255), stop:0.525 rgba(115, 233, 242, 238), stop:1 rgba(65, "
                        "173, 192, 238));border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, "
                        "stop:0.005 rgba(69, 248, 255, 255), stop:0.525 rgba(76, 230, 242,255), stop:1 rgba(72, 192, "
                        "213, 255));}QPushButton:pressed{background-color: rgb(185, 185, 185);}")
                        # Graphical style for element
incorrect_style_button = ("QPushButton{background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, "
                          "stop:0 rgba(171, 0, 0, 162), stop:0.494382 rgba(169, 0, 0, 163), stop:0.98 rgba(72, 0, 0, "
                          "163), stop:1 rgba(0, 0, 0, 0));border: none;padding-top: 5px;color:rgb(200, 200, "
                          "200);border-radius: 5px;border-left: 1px solid rgb(0, 255, 127);border-right: 1px solid "
                          "rgb(0, 255, 127);border-top: 1px solid rgb(0, 255, 127);border-bottom: 1px solid rgb(0, "
                          "255, 127);border-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba("
                          "171, 0, 0, 162), stop:0.494382 rgba(169, 0, 0, 163), stop:0.98 rgba(72, 0, 0, 163), "
                          "stop:1 rgba(0, 0, 0, 0));font: 900 9pt \"Segoe UI\";}QPushButton:hover {background-color: "
                          "qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(215, 0, 0, 198), "
                          "stop:0.494382 rgba(189, 0, 0, 198), stop:0.983146 rgba(102, 0, 0, 198), stop:1 rgba(0, 0, "
                          "0, 0));border-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(215, "
                          "0, 0, 198), stop:0.494382 rgba(189, 0, 0, 198), stop:0.983146 rgba(102, 0, 0, 198), "
                          "stop:1 rgba(0, 0, 0, 0));}QPushButton:pressed {background-color: rgb(185, 185, 185);}")
                        # Graphical style for element
correct_style_viewer = ("color: rgb(255, 255, 255);background-color: qlineargradient(spread:pad, x1:0.045, y1:0.886, "
                        "x2:0.96, y2:0.057, stop:0 rgba(56, 128, 140, 186), stop:0.495 rgba(85, 161, 167, 179), "
                        "stop:1 rgba(149, 187, 189, 167));font: 900 9pt \"Segoe UI\";allign: center;border: "
                        "none;padding-top: 5px;color: rgb(200, 200, 200);border-radius: 5px;border-left: 1px solid "
                        "rgb(0, 255, 127);border-right: 1px solid rgb(0, 255, 127);border-top: 1px solid rgb(0, 255, "
                        "127);border-bottom: 1px solid rgb(0, 255, 127);border-color:qlineargradient(spread:pad, "
                        "x1:0, y1:0, x2:1, y2:0, stop:0 rgba(192, 253, 255, 255), stop:0.525 rgba(115, 233, 242, "
                        "238), stop:1 rgba(65, 173, 192, 238));")
                        # Graphical style for element
incorrect_style_viewer = ("color: rgb(255, 255, 255);background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, "
                          "y2:0, stop:0 rgba(171, 0, 0, 162), stop:0.494382 rgba(169, 0, 0, 163), stop:0.98 rgba(72, "
                          "0, 0, 163), stop:1 rgba(0, 0, 0, 0));font: 900 9pt \"Segoe UI\";allign: center;border: "
                          "none;padding-top: 5px;color: rgb(200, 200, 200);border-radius: 5px;border-left: 1px solid "
                          "rgb(0, 255, 127);border-right: 1px solid rgb(0, 255, 127);border-top: 1px solid rgb(0, "
                          "255, 127);border-bottom: 1px solid rgb(0, 255, 127);border-color: qlineargradient("
                          "spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(171, 0, 0, 162), stop:0.494382 rgba(169, "
                          "0, 0, 163), stop:0.98 rgba(72, 0, 0, 163), stop:1 rgba(0, 0, 0, 0));")
                        # Graphical style for element
correct_style_radio = ("QRadioButton {background-color: qlineargradient(spread:pad, x1:0.045, y1:0.886, x2:0.96, "
                       "y2:0.057, stop:0 rgba(56, 128, 140, 186), stop:0.495 rgba(85, 161, 167, 179), stop:1 rgba("
                       "149, 187, 189, 167));border: none;padding-top: 5px;color: rgb(255, 255, 255);font: 900 9pt "
                       "\"Segoe UI\";border-radius: 5px;border-left: 1px solid rgb(0, 255, 127);border-right: 1px "
                       "solid rgb(0, 255, 127);border-top: 1px solid rgb(0, 255, 127);border-bottom: 1px solid rgb(0, "
                       "255, 127);border-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(192, "
                       "253, 255, 255), stop:0.525 rgba(115, 233, 242, 238), stop:1 rgba(65, 173, 192, "
                       "238));}QRadioButton:hover {background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, "
                       "y2:0, stop:0 rgba(192, 253, 255, 255), stop:0.525 rgba(115, 233, 242, 238), stop:1 rgba(65, "
                       "173, 192, 238));border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.005 "
                       "rgba(69, 248, 255, 255), stop:0.525 rgba(76, 230, 242, 255),stop:1 rgba(72, 192, 213, "
                       "255));}QRadioButton:pressed {background-color: rgb(185, 185, 185);}")
                        # Graphical style for element
incorrect_style_radio = ("QRadioButton {background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, "
                         "stop:0 rgba(171, 0, 0, 162), stop:0.494382 rgba(169, 0, 0, 163), stop:0.98 rgba(72, 0, 0, "
                         "163), stop:1 rgba(0, 0, 0, 0));border: none;padding-top:5px;font: 900 9pt \"Segoe "
                         "UI\";border-radius: 5px;border-left: 1px solid rgb(0, 255, 127);border-right: 1px solid "
                         "rgb(0, 255, 127);border-top: 1px solid rgb(0, 255, 127);border-bottom: 1px solid rgb(0, "
                         "255, 127);border-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba("
                         "171, 0, 0, 162), stop:0.494382 rgba(169, 0, 0, 163), stop:0.98 rgba(72, 0, 0, 163), "
                         "stop:1 rgba(0, 0, 0, 0));}QRadioButton:hover {background-color: qlineargradient(spread:pad, "
                         "x1:0, y1:1, x2:1, y2:0, stop:0 rgba(215, 0, 0, 198), stop:0.494382 rgba(189, 0, 0, 198), "
                         "stop:0.983146 rgba(102, 0, 0, 198), stop:1 rgba(0, 0, 0, 0));border-color: qlineargradient("
                         "spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(215, 0, 0, 198), stop:0.494382 rgba(189, 0, "
                         "0, 198), stop:0.983146 rgba(102, 0, 0, 198), stop:1 rgba(0, 0, 0, 0));}QRadioButton:pressed "
                         "{background-color: rgb(185, 185, 185);}")
                        # Graphical style for element


class Ui(QtWidgets.QMainWindow):  # class for GUI
    global folder_dir # Declaring necessary variables
    global picture_dir # Declaring necessary variables
    global percent # Declaring necessary variables
    global new_vertical # Declaring necessary variables
    global new_horizontal # Declaring necessary variables
    new_vertical = "0" # Assigning value
    new_horizontal = "0" # Assigning value
    folder_dir = "" # Assigning value
    picture_dir = "" # Assigning value
    percent = "0" # Assigning value

    def __init__(self):  # initialise GUI function
        super().__init__()  # Call the inherited classes __init__ method
        uic.loadUi('main_window.ui', self)  # Load the .ui file

        self.Select_dir = self.findChild(QtWidgets.QPushButton, 'Select_dir')  # find button by name in GUI
        self.Select_dir.clicked.connect(self.select_directory)  # assign action to a button
        self.Folder_dir_view = self.findChild(QtWidgets.QTextBrowser, 'Folder_dir_view')  # Find the text browser
        self.Folder_dir_view.setHtml(folder_dir)  # Show the content of variable in html form
        self.Select_pic = self.findChild(QtWidgets.QPushButton, 'Select_pic')  # find button by name in GUI
        self.Select_pic.clicked.connect(self.select_picture)  # assign action to a button
        self.Picture_dir_view = self.findChild(QtWidgets.QTextBrowser, 'Picture_dir_view')  # Find the text browser
        self.Picture_dir_view.setHtml(picture_dir)  # Show the content of variable in html form
        self.Vertical = self.findChild(QtWidgets.QPushButton, 'Vertical')  # find button by name in GUI
        self.Vertical.clicked.connect(self.change_vertical)  # assign action to a button
        self.Horizontal = self.findChild(QtWidgets.QPushButton, 'Horizontal')  # find button by name in GUI
        self.Horizontal.clicked.connect(self.change_horizontal)  # assign action to a button
        self.Vertical_view = self.findChild(QtWidgets.QTextBrowser, 'Vertical_view')  # Find the text browser
        self.Vertical_view.setHtml(new_vertical)  # Show the content of variable in html form
        self.Horizontal_view = self.findChild(QtWidgets.QTextBrowser, 'Horizontal_view')  # find button by name in GUI
        self.Horizontal_view.setHtml(new_horizontal)  # assign action to a button
        self.Mono = self.findChild(QtWidgets.QCheckBox, 'Mono')  # Find the checkbox
        self.Mono.stateChanged.connect(self.monochromatic)  # call function
        self.Color = self.findChild(QtWidgets.QCheckBox, 'Color')  # Find the checkbox
        self.Color.stateChanged.connect(self.color)  # call function
        self.Ten = self.findChild(QtWidgets.QRadioButton, 'Ten')  # find button by name in GUI
        self.Ten.clicked.connect(self.percentage)  # assign action to a button
        self.Twenty = self.findChild(QtWidgets.QRadioButton, 'Twenty')  # find button by name in GUI
        self.Twenty.clicked.connect(self.percentage)  # assign action to a button
        self.Thirty = self.findChild(QtWidgets.QRadioButton, 'Thirty')  # find button by name in GUI
        self.Thirty.clicked.connect(self.percentage)  # assign action to a button
        self.Fourty = self.findChild(QtWidgets.QRadioButton, 'Fourty')  # find button by name in GUI
        self.Fourty.clicked.connect(self.percentage)  # assign action to a button
        self.Fifty = self.findChild(QtWidgets.QRadioButton, 'Fifty')  # find button by name in GUI
        self.Fifty.clicked.connect(self.percentage)  # assign action to a button
        self.Sixty = self.findChild(QtWidgets.QRadioButton, 'Sixty')  # find button by name in GUI
        self.Sixty.clicked.connect(self.percentage)  # assign action to a button
        self.Seventy = self.findChild(QtWidgets.QRadioButton, 'Seventy')  # find button by name in GUI
        self.Seventy.clicked.connect(self.percentage)  # assign action to a button
        self.Eighty = self.findChild(QtWidgets.QRadioButton, 'Eighty')  # find button by name in GUI
        self.Eighty.clicked.connect(self.percentage)  # assign action to a button
        self.Ninety = self.findChild(QtWidgets.QRadioButton, 'Ninety')  # find button by name in GUI
        self.Ninety.clicked.connect(self.percentage)  # assign action to a button
        self.Hundred = self.findChild(QtWidgets.QRadioButton, 'Hundred')  # find button by name in GUI
        self.Hundred.clicked.connect(self.percentage)  # assign action to a button
        self.Convert = self.findChild(QtWidgets.QPushButton, 'Convert')  # find button by name in GUI
        self.Convert.clicked.connect(self.convert)  # assign action to a button
        self.Convert_px = self.findChild(QtWidgets.QPushButton, 'Convert_px')  # find button by name in GUI
        self.Convert_px.clicked.connect(self.convert_px)  # assign action to a button
        self.Color.setCheckState(Qt.CheckState.Checked) # by default make this checked

    def clear(self): # clearing function
        global folder_dir # Declaring necessary variables
        global picture_dir # Declaring necessary variables
        global new_horizontal # Declaring necessary variables
        global new_vertical # Declaring necessary variables
        global percent # Declaring necessary variables
        folder_dir = "" # Assigning value
        picture_dir = "" # Assigning value
        new_horizontal = "0" # Assigning value
        new_vertical = "0" # Assigning value
        percent = "0" # Assigning value
        self.Folder_dir_view.setHtml("") # displaying empty string
        self.Picture_dir_view.setHtml("") # displaying empty string
        self.Horizontal_view.setHtml("") # displaying empty string
        self.Vertical_view.setHtml("") # displaying empty string
        self.w = Ui() # define window
        self.w.show() # Show window
        self.close() # close window

    def select_directory(self): # function for selecting directory
        global folder_dir # Declaring necessary variables
        folder_dir = filedialog.askdirectory(parent=root, initialdir=curr_dir,
                                             title='Please select a folder with pictures') # input from user
        if folder_dir == (): # If statement
            self.Folder_dir_view.setStyleSheet(incorrect_style_viewer) # change stylesheet
            self.Select_dir.setStyleSheet(incorrect_style_button) # change stylesheet
            self.clear() # call another function
            return
        else:
            self.Folder_dir_view.setStyleSheet(correct_style_viewer) # change stylesheet
            self.Select_dir.setStyleSheet(correct_style_button) # change stylesheet
            self.folder_dir_view() # call another function

    def folder_dir_view(self): # function to show folder directory
        self.Folder_dir_view.setHtml(folder_dir)  # Show the content of variable in html form
        self.Picture_dir_view.setHtml("") # show empty string in opposite view

    def select_picture(self):  # function for selecting picture
        global picture_dir # Declaring necessary variables
        picture_dir = filedialog.askopenfilename(parent=root, initialdir=curr_dir,
                                                 title='Please select a picture') # input from user
        if picture_dir == (): # If statement
            self.Picture_dir_view.setStyleSheet(incorrect_style_viewer) # change stylesheet
            self.Select_pic.setStyleSheet(incorrect_style_button) # change stylesheet
            self.clear() # call another function
            return
        else:
            self.Picture_dir_view.setStyleSheet(correct_style_viewer) # change stylesheet
            self.Select_pic.setStyleSheet(correct_style_button) # change stylesheet
            self.picture_dir_view() # call another function

    def picture_dir_view(self): # function to show picture directory
        self.Picture_dir_view.setHtml(picture_dir)  # Show the content of variable in html form
        self.Folder_dir_view.setHtml("") # show empty string in opposite view

    def change_vertical(self): # function to change vertical value
        global new_vertical # Declaring necessary variables
        self.Ten.setDisabled(True) # Disable procentage use
        self.Twenty.setDisabled(True) # Disable procentage use
        self.Thirty.setDisabled(True) # Disable procentage use
        self.Fourty.setDisabled(True) # Disable procentage use
        self.Fifty.setDisabled(True) # Disable procentage use
        self.Sixty.setDisabled(True) # Disable procentage use
        self.Seventy.setDisabled(True) # Disable procentage use
        self.Eighty.setDisabled(True) # Disable procentage use
        self.Ninety.setDisabled(True) # Disable procentage use
        self.Hundred.setDisabled(True) # Disable procentage use
        new_vertical = askstring("New vertical value", "Please type in new vertical value") # input from user
        self.Convert.setDisabled(True) # Disable converstion by percentage
        self.Convert_px.setEnabled(True) # Enable converstion by pixels
        self.vertical_view() # call another function

    def vertical_view(self): # function to show vertical value
        self.Vertical_view.setHtml(new_vertical)  # Show the content of variable in html form

    def change_horizontal(self): # function to change horizontal value
        global new_horizontal # Declaring necessary variables
        self.Ten.setDisabled(True) # Disable procentage use
        self.Twenty.setDisabled(True) # Disable procentage use
        self.Thirty.setDisabled(True) # Disable procentage use
        self.Fourty.setDisabled(True) # Disable procentage use
        self.Fifty.setDisabled(True) # Disable procentage use
        self.Sixty.setDisabled(True) # Disable procentage use
        self.Seventy.setDisabled(True) # Disable procentage use
        self.Eighty.setDisabled(True) # Disable procentage use
        self.Ninety.setDisabled(True) # Disable procentage use
        self.Hundred.setDisabled(True) # Disable procentage use
        new_horizontal = askstring("New horizontal value", "Please type in new horizontal value") # input from user
        self.Convert.setDisabled(True) # Disable conversion by percentage
        self.Convert_px.setEnabled(True) # Enable conversion by pixels
        self.horizontal_view() # call another function

    def horizontal_view(self): # function to show horizontal value
        self.Horizontal_view.setHtml(new_horizontal)  # Show the content of variable in html form

    def monochromatic(self): # function to select color conversion
        self.Color.setChecked(False) # change state of opposite button

    def color(self): # function to select mono conversion
        self.Mono.setChecked(False) # change state of opposite button

    def percentage(self): # function for conversion by percentage
        global percent # Declaring necessary variables
        signal_sender = self.sender()  # Assign sender to a var
        button_name = (signal_sender.objectName())  # Get the name of sender button
        caller = str(button_name)  # Assign the name of sender button as a string
        self.Vertical_view.setHtml("") # show empty string
        self.Horizontal_view.setHtml("") # show empty string
        self.Vertical.setDisabled(True) # disable vertical value
        self.Horizontal.setDisabled(True) # disable horizontal value
        self.Convert_px.setDisabled(True) # disable conversion by pixels
        self.Convert.setEnabled(True) # enable conversion by percentage
        if self.findChild(QtWidgets.QRadioButton, caller).isChecked(): # check if radio button is checked
            if str(caller) == "Ten": # nested if all the way
                percent = 0.1 # assign value
            elif str(caller) == "Twenty":
                percent = 0.2 # assign value
            elif str(caller) == "Thirty":
                percent = 0.3 # assign value
            elif str(caller) == "Fourty":
                percent = 0.4 # assign value
            elif str(caller) == "Fifty":
                percent = 0.5 # assign value
            elif str(caller) == "Sixty":
                percent = 0.6 # assign value
            elif str(caller) == "Seventy":
                percent = 0.7 # assign value
            elif str(caller) == "Eighty":
                percent = 0.8 # assign value
            elif str(caller) == "Ninety":
                percent = 0.9 # assign value
            elif str(caller) == "Hundred":
                percent = 1 # assign value
            else: # end of nested if
                percent = 0 # assign value

    def convert(self): # function to convert by percentage
        global x # Declaring necessary variables
        global percent # Declaring necessary variables

        if str(picture_dir) == "" and str(folder_dir) == "": # check if paths are selected
            self.Convert.setStyleSheet(incorrect_style_button) # change stylesheet
            self.Picture_dir_view.setStyleSheet(incorrect_style_viewer) # change stylesheet
            self.Select_pic.setStyleSheet(incorrect_style_button) # change stylesheet
            self.Folder_dir_view.setStyleSheet(incorrect_style_viewer) # change stylesheet
            self.Select_dir.setStyleSheet(incorrect_style_button) # change stylesheet
            return
        else:
            self.Picture_dir_view.setStyleSheet(correct_style_viewer) # change stylesheet
            self.Select_pic.setStyleSheet(correct_style_button) # change stylesheet
            self.Folder_dir_view.setStyleSheet(correct_style_viewer) # change stylesheet
            self.Select_dir.setStyleSheet(correct_style_button) # change stylesheet
            self.Convert.setStyleSheet(correct_style_button) # change stylesheet
        if percent == "0": # if statement
            self.Convert.setStyleSheet(incorrect_style_button) # change stylesheet
            self.Ten.setStyleSheet(incorrect_style_radio) # change stylesheet
            self.Twenty.setStyleSheet(incorrect_style_radio) # change stylesheet
            self.Thirty.setStyleSheet(incorrect_style_radio) # change stylesheet
            self.Fourty.setStyleSheet(incorrect_style_radio) # change stylesheet
            self.Fifty.setStyleSheet(incorrect_style_radio) # change stylesheet
            self.Sixty.setStyleSheet(incorrect_style_radio) # change stylesheet
            self.Seventy.setStyleSheet(incorrect_style_radio) # change stylesheet
            self.Eighty.setStyleSheet(incorrect_style_radio) # change stylesheet
            self.Ninety.setStyleSheet(incorrect_style_radio) # change stylesheet
            self.Hundred.setStyleSheet(incorrect_style_radio) # change stylesheet
            return
        else:
            self.Convert.setStyleSheet(correct_style_button) # change stylesheet
            self.Ten.setStyleSheet(correct_style_radio) # change stylesheet
            self.Twenty.setStyleSheet(correct_style_radio) # change stylesheet
            self.Thirty.setStyleSheet(correct_style_radio) # change stylesheet
            self.Fourty.setStyleSheet(correct_style_radio) # change stylesheet
            self.Fifty.setStyleSheet(correct_style_radio) # change stylesheet
            self.Sixty.setStyleSheet(correct_style_radio) # change stylesheet
            self.Seventy.setStyleSheet(correct_style_radio) # change stylesheet
            self.Eighty.setStyleSheet(correct_style_radio) # change stylesheet
            self.Ninety.setStyleSheet(correct_style_radio) # change stylesheet
            self.Hundred.setStyleSheet(correct_style_radio) # change stylesheet
        if self.findChild(QtWidgets.QCheckBox, "Color").isChecked(): # check if color is chosen
            x = 1 # assign value
        if self.findChild(QtWidgets.QCheckBox, "Mono").isChecked(): # check if mono is chosen
            x = 0 # assign value
        if str(folder_dir) != "" and str(picture_dir) == "" and percent != "0": # check if folder dir is not empty
            files = os.listdir(folder_dir) # assign paths
            for file_name in files: # for loop for each file
                img = cv2.imread(os.path.join(folder_dir, './' + file_name), x) # assign image to variable
                resized_image = cv2.resize(img, (int(img.shape[1] * percent), int(img.shape[0] * percent))) # convert image by percentage
                cv2.imwrite(os.path.join(folder_dir, "./" + file_name + "_resized"), resized_image) # write converted image
            self.clear() # call another function
            return

        if str(picture_dir) != "" and str(folder_dir) == "" and percent != "0": # check if picture dir is not empty
            file = picture_dir # assign path
            img = cv2.imread(file, x) # assign image to variable
            resized_image = cv2.resize(img, (int(img.shape[1] * percent), int(img.shape[0] * percent))) # convert image by percentage
            cv2.imwrite(file + "_resized", resized_image) # write converted image
            self.clear() # call another functiomn
            return

    def convert_px(self): # function to convert by pixels
        global y # Declaring necessary variables
        global new_horizontal # Declaring necessary variables
        global new_vertical # Declaring necessary variables

        if str(picture_dir) == "" and str(folder_dir) == "": # check if paths are selected
            self.Convert_px.setStyleSheet(incorrect_style_button) # change stylesheet
            self.Picture_dir_view.setStyleSheet(incorrect_style_viewer) # change stylesheet
            self.Select_pic.setStyleSheet(incorrect_style_button) # change stylesheet
            self.Folder_dir_view.setStyleSheet(incorrect_style_viewer) # change stylesheet
            self.Select_dir.setStyleSheet(incorrect_style_button) # change stylesheet
            return
        else:
            self.Picture_dir_view.setStyleSheet(correct_style_viewer) # change stylesheet
            self.Select_pic.setStyleSheet(correct_style_button) # change stylesheet
            self.Folder_dir_view.setStyleSheet(correct_style_viewer) # change stylesheet
            self.Select_dir.setStyleSheet(correct_style_button) # change stylesheet
            self.Convert_px.setStyleSheet(correct_style_button) # change stylesheet

        if str(new_horizontal) == "0" or str(new_vertical) == "0": # check if values are default
            self.Convert_px.setStyleSheet(incorrect_style_button) # change stylesheet
            self.Vertical_view.setStyleSheet(incorrect_style_viewer) # change stylesheet
            self.Vertical.setStyleSheet(incorrect_style_button) # change stylesheet
            self.Horizontal_view.setStyleSheet(incorrect_style_viewer) # change stylesheet
            self.Horizontal.setStyleSheet(incorrect_style_button) # change stylesheet
            return

        if self.findChild(QtWidgets.QCheckBox, "Color").isChecked(): # check if color is chosen
            y = 1 # assign value
        if self.findChild(QtWidgets.QCheckBox, "Mono").isChecked(): # check if color is chosen
            y = 0 # assign value

        if str(folder_dir) != "" and str(picture_dir) == "": # check if folder dir is not empty
            files = os.listdir(folder_dir) # assign paths
            for file_name in files: # for loop for each file
                img = cv2.imread(os.path.join(folder_dir, './' + file_name), y) # assign image to variable
                resized_image = cv2.resize(img, (int(new_horizontal), int(new_vertical))) # convert image by pixels
                cv2.imwrite(os.path.join(folder_dir, "./" + file_name + "_resized"), resized_image) # write converted image
            self.clear() # call another function
            return

        if str(picture_dir) != "" and str(folder_dir) == "": # check if picture dir is not empty
            file = picture_dir # assign path
            img = cv2.imread(file, y) # assign image to variable
            resized_image = cv2.resize(img, (int(new_horizontal), int(new_vertical))) # convert image by pixels
            cv2.imwrite(file + "_resized", resized_image) # write converted image
            self.clear() # call another function
            return


cv2.destroyAllWindows() # close all windows from CV2
app = QtWidgets.QApplication(sys.argv) # define widget as app
window = Ui() # define window
window.show() # show window
app.exec() # loop app
