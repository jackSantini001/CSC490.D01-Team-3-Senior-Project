"""
encryption decryption game
"""
import math
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, LEFT, RIGHT, ROW, Pack
from random import randint

class CodeBreaker(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        unencrypted_word = toga.Label(
            'Unencrypted Word: ',
            style=Pack(padding=(0, 5))
        )

        self.level_1 = toga.TextInput(style=Pack(flex=1))
        un_word_box = toga.Box(style=Pack(direction=ROW, padding=5))
        un_word_box.add(unencrypted_word)
        un_word_box.add(self.level_1)

        button = toga.Button(
            'Above, please type "hello"',
            on_press=self.say_hello,
            style=Pack(padding=5)
        )
        main_box.add(un_word_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def say_hello(self, widget):
        message = toga.value(self.level_1)
        self.key = randint(1, 104)
        while self.key > 26:
            self.key -=26

        ciphertext = ''
        for char in message:
            unicode_a = ord(char)
            unicode_c = unicode_a + key
            new_letter = chr(unicode_c)
            ciphertext += new_letter
        print("Hello", message)
            
def main():
    return CodeBreaker()
