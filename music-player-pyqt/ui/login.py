from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox

class LoginPage(QWidget):
    def __init__(self, db_manager, switch_to_music_callback):
        super().__init__()
        self.db_manager = db_manager
        self.switch_to_music = switch_to_music_callback
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        self.username_edit = QLineEdit(self)
        self.username_edit.setPlaceholderText("Username")
        layout.addWidget(self.username_edit)

        self.password_edit = QLineEdit(self)
        self.password_edit.setPlaceholderText("Password")
        self.password_edit.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_edit)

        login_button = QPushButton("Login", self)
        login_button.clicked.connect(self.login)
        layout.addWidget(login_button)

        signup_button = QPushButton("Sign Up", self)
        signup_button.clicked.connect(self.signup)
        layout.addWidget(signup_button)

    def login(self):
        username = self.username_edit.text()
        password = self.password_edit.text()

        if not username or not password:
            QMessageBox.warning(self, "Login Failed", "Username and password cannot be empty.")
            return

        user_data = self.db_manager.find_user(username, password)

        if user_data:
            QMessageBox.information(self, "Login Successful", f"Welcome, {username}")
            self.switch_to_music()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

    def signup(self):
        username = self.username_edit.text()
        password = self.password_edit.text()

        if not username or not password:
            QMessageBox.warning(self, "Sign Up Failed", "Username and password cannot be empty.")
            return

        if self.db_manager.user_exists(username):
            QMessageBox.warning(self, "Sign Up Failed", "Username already exists.")
        else:
            self.db_manager.create_user(username, password)
            QMessageBox.information(self, "Sign Up Successful", "User registered successfully.")
