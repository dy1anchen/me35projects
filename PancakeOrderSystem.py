from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # set the title
        self.setWindowTitle("Pancake Order")

        layout = QGridLayout()
        layout.setContentsMargins(100, 20, 20, 150) # Sets 20px left/right and 10px top/bottom margins

        # TITLE TEXT BOX
        title = QLabel("Welcome to the \nPokemon Pancake Cafe!")
        font = title.font()
        font.setPointSize(30)
        title.setFont(font)
        layout.addWidget(title, 0, 0)

        # PROMPT TEXT BOX
        prompt = QLabel("Select Pancake Options:")
        font = prompt.font()
        font.setPointSize(20)
        prompt.setFont(font)
        layout.addWidget(prompt, 1, 0)

        # POKEBALL IMAGE
        pokeball_image = QLabel(self)
        pixmap = QPixmap('pokeball.png')
        pokeball_image.setPixmap(pixmap) 
        pokeball_image.resize(pixmap.width(),
                     pixmap.height())
        layout.addWidget(pokeball_image, 0, 3)

        # CHOCO CHIPS IMAGE
        cc_image = QLabel(self)
        pixmap = QPixmap('chocolatechips.png')
        cc_image.setPixmap(pixmap) 
        cc_image.resize(pixmap.width(),
                     pixmap.height())
        layout.addWidget(cc_image, 2, 0)
 
        # CHOCOLATE CHIPS TOGGLE BUTTON
        self.cc_toggle = QPushButton("Chocolate Chips", self)
        self.cc_toggle.setGeometry(200, 150, 100, 40)
        self.cc_toggle.setCheckable(True)
        self.cc_toggle.clicked.connect(self.changeColor)
        self.cc_toggle.setStyleSheet("background-color : lightgrey")
        layout.addWidget(self.cc_toggle, 3, 0)

        # WHIPPED CREAM IMAGE
        wc_image = QLabel(self)
        pixmap = QPixmap('whippedcream.png')
        wc_image.setPixmap(pixmap) 
        wc_image.resize(pixmap.width(),
                     pixmap.height())
        layout.addWidget(wc_image, 2, 1)
 
        # WHIPPED CREAM TOGGLE BUTTON
        self.whipped_toggle = QPushButton("Whipped Cream", self)
        self.whipped_toggle.setGeometry(200, 200, 100, 40)
        self.whipped_toggle.setCheckable(True)
        self.whipped_toggle.clicked.connect(self.changeColor)
        self.whipped_toggle.setStyleSheet("background-color : lightgrey")
        layout.addWidget(self.whipped_toggle, 3, 1)

        # SPRINKLES IMAGE
        sprinkles_image = QLabel(self)
        pixmap = QPixmap('sprinkles.png')
        sprinkles_image.setPixmap(pixmap) 
        sprinkles_image.resize(pixmap.width(),
                     pixmap.height())
        layout.addWidget(sprinkles_image, 2, 2)

        # SPRINKLES TOGGLE BUTTON
        self.sprinkle_toggle = QPushButton("Sprinkles", self)
        self.sprinkle_toggle.setGeometry(200, 250, 100, 40)
        self.sprinkle_toggle.setCheckable(True)
        self.sprinkle_toggle.clicked.connect(self.changeColor)
        self.sprinkle_toggle.setStyleSheet("background-color : lightgrey")
        layout.addWidget(self.sprinkle_toggle, 3, 2)

        # CONFIRM BUTTON
        self.confirm = QPushButton("CONFIRM ORDER", self)
        self.confirm.setGeometry(200, 250, 100, 40)
        self.confirm.clicked.connect(self.confirmOrder)
        self.confirm.setStyleSheet("background-color : green")
        layout.addWidget(self.confirm, 4, 2)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # show all the widgets
        self.update()
        self.showMaximized()
 
    # method called by button
    def changeColor(self):

        # if button is checked
        if self.cc_toggle.isChecked():
            # setting background color to light-blue
            self.cc_toggle.setStyleSheet("background-color : lightblue")
 
        # if it is unchecked
        else:
            # set background color back to light-grey
            self.cc_toggle.setStyleSheet("background-color : lightgrey")

    # called when confirm order button is clicked
    def confirmOrder(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("CONFIRM ORDER")
        dlg.setText("Order Details: \n" 
                    + "Chocolate Chips: " + str(self.cc_toggle.isChecked()) + "\n" 
                    + "Whipped Cream: " + str(self.whipped_toggle.isChecked()) + "\n"
                    + "Sprinkles: " + str(self.sprinkle_toggle.isChecked()))
        dlg.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel
        )
        button = dlg.exec()
        if button == QMessageBox.StandardButton.Yes:
            print("-----------------------------------------------------------------")
            print("ORDER CONFIRMED")
            # prints out True if each button is pressed
            
            
            
            # UPLOAD INFO TO AIRTABLE HERE 
                # these three statements are True/False for the topping selections
                    # self.cc_toggle.isChecked() ---> chocolate chips
                    # self.whipped_toggle.isChecked() ---> whipped cream
                    # self.sprinkle_toggle.isChecked() ---> sprinkles



            print("Chocolate Chips: " + str(self.cc_toggle.isChecked()))
            print("Whipped Cream: " + str(self.whipped_toggle.isChecked()))
            print("Sprinkles: " + str(self.sprinkle_toggle.isChecked()))
            print("-----------------------------------------------------------------")
            self.close()

def main(args=None):
    # create pyqt5 app
    App = QApplication(sys.argv)
    
    # create the instance of our Window
    window = Window()
    
    # start the app
    sys.exit(App.exec())

if __name__ == '__main__':
    main()