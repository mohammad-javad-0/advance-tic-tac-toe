from PyQt6 import QtCore, QtGui, QtWidgets
from tic_tac_toe import *


class UiMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(600, 600)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ForbiddenCursor))
        MainWindow.setStyleSheet("background-color:black;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # create header app
        self.header_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.header_label.setGeometry(QtCore.QRect(0, 15, 600, 50))
        self.header_label.setStyleSheet("color:gold;")
        font = QtGui.QFont()
        font.setFamily("Script")
        font.setBold(True)
        font.setItalic(True)
        self.header_label.setFont(font)
        self.header_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.header_label.setObjectName("header_label")

        # create font
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)

        # create label and combo box for number of player
        self.number_player_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.number_player_label.setGeometry(QtCore.QRect(135, 110, 200, 30))
        self.number_player_label.setFont(font)
        self.number_player_label.setObjectName("number_player_label")

        self.player_number_comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.player_number_comboBox.setGeometry(QtCore.QRect(330, 110, 150, 25))
        self.player_number_comboBox.setFont(font)
        self.player_number_comboBox.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.player_number_comboBox.addItem("1 player")
        self.player_number_comboBox.addItem("2 player")
        self.player_number_comboBox.setObjectName("player_number_comboBox")

        # create label to show who is player turn
        self.turn_player_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.turn_player_label.setGeometry(QtCore.QRect(200, 110, 200, 30))
        font.setBold(True)
        self.turn_player_label.setFont(font)
        self.turn_player_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.turn_player_label.setStyleSheet("color:red;border:3px dashed blue;")
        self.turn_player_label.setHidden(True)
        self.turn_player_label.setObjectName("turn_player_label")

        # create game button for start and reset game
        self.game_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.game_pushButton.setGeometry(QtCore.QRect(245, 520, 110, 40))
        self.game_pushButton.setFont(font)
        self.game_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.game_pushButton.setObjectName("start")
        self.game_pushButton.clicked.connect(self.game_function)

        # create font for game board
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        font.setBold(True)

        # create game board
        self.list_of_board_button = list()
        for n in range(9):
            btn = Button(
                parent=self.centralwidget,
                other=self,
                geometry=[165+((n%3)*90), 190+((n//3)*90), 90, 90],
                objectname=str(n),
                font=font
            )
            self.list_of_board_button.append(btn)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.turn_player_label.setText(_translate("MainWindow", "Turn player 1     O"))
        self.number_player_label.setText(_translate("MainWindow", "Chooce number of player"))
        self.header_label.setText(_translate("MainWindow", "Tic Tac Toe"))
        self.game_pushButton.setText(_translate("MainWindow", "start"))

    def start_game(self, number_of_player):
        if number_of_player == "1 player":
            self.game = Game(1, self)
        else:
            self.game = Game(2, self)

        self.game.play()

    def game_function(self):
        if self.game_pushButton.objectName() == "start":
            for btn in self.list_of_board_button:
                btn.setEnabled(True)
            self.game_pushButton.setObjectName("reset")
            self.game_pushButton.setText("Reset")
            self.number_player_label.setHidden(True)
            self.player_number_comboBox.setHidden(True)
            self.turn_player_label.setHidden(False)
            self.start_game(self.player_number_comboBox.currentText())
        else:
            for btn in self.list_of_board_button:
                btn.setText("")
                btn.setStyleSheet("background-color: white;")
            self.game_pushButton.setObjectName("start")
            self.game_pushButton.setText("Start")
            self.number_player_label.setHidden(False)
            self.player_number_comboBox.setHidden(False)
            self.turn_player_label.setHidden(True)
            style = "color: green;background-color:white"
            self.end_game("Reset", "The game was reset", style)


    def end_game(self, title, message, style):
        for btn in self.list_of_board_button:
            btn.setEnabled(False)
        msg = QtWidgets.QMessageBox()
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.setStyleSheet(style)
        msg.exec()


class Button(QtWidgets.QPushButton):
    def __init__(self, parent, other, geometry, objectname, font):
        super().__init__(parent=parent)
        self.setGeometry(QtCore.QRect(geometry[0], geometry[1], geometry[2], geometry[3]))
        self.setFont(font)
        self.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.setStyleSheet("background-color: white;")
        self.setObjectName(objectname)
        self.setEnabled(False)
        self.clicked.connect(lambda: self.clicked_board(other))

    def clicked_board(self, other: UiMainWindow, winner: bool = False):
        Board.remaining_button_num -= 1
        if other.turn_player_label.text() == "Turn player 1     O":
            other.turn_player_label.setText("Turn player 2     X")
            other.turn_player_label.setStyleSheet("color: blue;border:3px dashed red;")
            self.setText("O")
            self.setStyleSheet("background-color: red;")
            winner, _ = other.game.game_board(int(self.objectName()), "O")
            if winner:
                style = "color:red;background-color:white"
                message = "Player 1 : O\nis Winner..."
        else:
            if not other.game.player2.user_name == "Computer":
                winner, _ = other.game.game_board(int(self.objectName()), "X")
            if winner:
                style = "color: blue;background-color:white"
                message = f"{other.game.player2.user_name} : X\nis Winner..."

            other.turn_player_label.setText("Turn player 1     O")
            other.turn_player_label.setStyleSheet("color: red;border:3px dashed blue;")
            self.setText("X")
            self.setStyleSheet("background-color: blue;")

        self.setEnabled(False)
        if winner:
            other.end_game("End game", message, style)
        elif Board.remaining_button_num == 0:
            style = "color:purple;background-color:white"
            other.end_game("End game", "No one won. The game was tied...", style)
        else:
            other.game.play()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
