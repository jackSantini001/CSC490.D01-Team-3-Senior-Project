import toga
from random import randint
from toga.style.pack import COLUMN, LEFT, RIGHT, ROW, Pack


def build(app):
    enc_box = toga.Box()
    hello_box = toga.Box()
    box = toga.Box()

    enc_input = toga.TextInput(readonly=True)
    hello_input = toga.TextInput()

    end_label = toga.Label('when encrypted', style=Pack(text_align=LEFT))
    hello_label = toga.Label('Please type "hello"', style=Pack(text_align=LEFT))
    join_label = toga.Label('becomes ', style=Pack(text_align=RIGHT))

    def calculate(widget):
        try:
            message = str(hello_input.value)
            key = randint(1, 28)
            while key > 26:
                key -=26
            ciphertext = ''
            for char in message:
                unicode_a = ord(char)
                unicode_c = unicode_a + key
                new_letter = chr(unicode_c)
                ciphertext = += new_letter
            return ciphertext
        except ValueError:
            c_input.value = '???'

    button = toga.Button('Calculate', on_press=calculate)

    hello_box.add(hello_input)
    hello_box.add(hello_label)

    enc_box.add(join_label)
    enc_box.add(enc_input)
    enc_box.add(enc_label)

    box.add(hello_box)
    box.add(enc_box)
    box.add(button)

    box.style.update(direction=COLUMN, padding_top=10)
    hello_box.style.update(direction=ROW, padding=5)
    enc_box.style.update(direction=ROW, padding=5)

    c_input.style.update(flex=1)
    f_input.style.update(flex=1, padding_left=160)
    c_label.style.update(width=100, padding_left=10)
    f_label.style.update(width=100, padding_left=10)
    join_label.style.update(width=150, padding_right=10)

    button.style.update(padding=15, flex=1)

    return box


def main():
    return toga.App('CodeBreaker', 'com.project', startup=build)


if __name__ == '__main__':
    main().main_loop()
