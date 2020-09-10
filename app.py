"""
1st Prototype
"""
import toga
from toga.style import Pack
from toga.style.pack import CENTER, COLUMN, ROW


class NetworkingGame(toga.App):

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))
        self.main_window = toga.MainWindow(title=self.formal_name)
        progress_label = toga.Label('Progress:', style=Pack(alignment=CENTER))
        progress = toga.ProgressBar(max=100, value=1)
        background = toga.ImageView(id='aerial field', image="icons/AerialFieldSample.jpg")
        main_box.add(progress_label)
        main_box.add(progress)
        main_box.add(background)
        self.main_window.content = main_box
        self.main_window.show()

        
        


def main():
    return NetworkingGame()
