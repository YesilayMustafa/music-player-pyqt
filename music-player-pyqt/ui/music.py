from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QListWidget, QListWidgetItem,
    QSlider, QLabel, QFileDialog, QMenu, QAction)
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import Qt, QUrl


class MusicPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        self.add_button = QPushButton("Add Music", self)
        self.add_button.clicked.connect(self.add_music)
        layout.addWidget(self.add_button)

        self.music_list = QListWidget(self)
        self.music_list.itemClicked.connect(self.select_music)
        layout.addWidget(self.music_list)

        self.seek_slider = QSlider(Qt.Horizontal, self)
        self.seek_slider.setMinimum(0)
        self.seek_slider.sliderMoved.connect(self.seek_music)
        self.seek_slider.sliderPressed.connect(self.slider_pressed)
        self.seek_slider.sliderReleased.connect(self.slider_released)
        layout.addWidget(self.seek_slider)

        self.volume_slider = QSlider(Qt.Horizontal, self)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setValue(50)
        self.volume_slider.valueChanged.connect(self.set_volume)
        layout.addWidget(self.volume_slider)

        self.volume_label = QLabel("Volume: 50", self)
        layout.addWidget(self.volume_label)

        self.duration_label = QLabel("00:00 / 00:00", self)
        layout.addWidget(self.duration_label)

        self.play_button = QPushButton("Play", self)
        self.play_button.clicked.connect(self.play_or_stop_music)
        layout.addWidget(self.play_button)

        self.player = QMediaPlayer()
        self.is_slider_pressed = False
        self.player.positionChanged.connect(self.update_duration_label)
        self.player.durationChanged.connect(self.update_slider_range)

        self.music_url = None

    def add_music(self):
        file_dialog = QFileDialog()
        file_path = file_dialog.getOpenFileName(self, "Select Music")[0]

        if file_path:
            self.music_url = QUrl.fromLocalFile(file_path)
            music_content = QMediaContent(self.music_url)
            self.player.setMedia(music_content)

            music_name = file_path.split("/")[-1]
            item = QListWidgetItem(music_name)
            item.setData(Qt.UserRole, file_path)
            self.music_list.addItem(item)

    def select_music(self, item):
        file_path = item.data(Qt.UserRole)
        if file_path:
            self.music_url = QUrl.fromLocalFile(file_path)
            music_content = QMediaContent(self.music_url)
            self.player.setMedia(music_content)

    def play_or_stop_music(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
            self.play_button.setText("Play")
        else:
            if self.player.mediaStatus() == QMediaPlayer.NoMedia and self.music_url:
                music_content = QMediaContent(self.music_url)
                self.player.setMedia(music_content)
            self.player.play()
            self.play_button.setText("Stop")

    def seek_music(self, position):
        if not self.is_slider_pressed:
            self.player.setPosition(position)

    def slider_pressed(self):
        self.is_slider_pressed = True

    def slider_released(self):
        self.is_slider_pressed = False
        self.player.setPosition(self.seek_slider.value())
        if self.player.state() == QMediaPlayer.PausedState:
            self.player.play()

    def set_volume(self, value):
        self.player.setVolume(value)
        self.volume_label.setText(f"Volume: {value}")

    def update_slider_range(self):
        duration = self.player.duration()
        self.seek_slider.setRange(0, duration)

    def update_duration_label(self, position):
        duration = self.player.duration()
        current_position = self.player.position()
        duration_text = self.format_time(duration)
        current_position_text = self.format_time(current_position)
        self.duration_label.setText(f"{current_position_text} / {duration_text}")
        self.seek_slider.setValue(position)

    def format_time(self, milliseconds):
        seconds = int((milliseconds / 1000) % 60)
        minutes = int((milliseconds / (1000 * 60)) % 60)
        return "{:02d}:{:02d}".format(minutes, seconds)
