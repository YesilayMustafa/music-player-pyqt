import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from db.mongodb import MongoDBManager
from ui.login import LoginPage
from ui.music import MusicPage

class MusicApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Music Player")
        self.setGeometry(100, 100, 600, 400)

        self.db_manager = MongoDBManager()
        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        self.login_page = LoginPage(self.db_manager, self.show_music_page)
        self.music_page = MusicPage()

        self.stacked_widget.addWidget(self.login_page)
        self.stacked_widget.addWidget(self.music_page)

        self.stacked_widget.setCurrentWidget(self.login_page)

    def show_music_page(self):
        self.stacked_widget.setCurrentWidget(self.music_page)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MusicApp()
    window.show()
    sys.exit(app.exec_())
