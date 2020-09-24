import toga
from random import randint
from toga.style.pack import COLUMN, LEFT, RIGHT, ROW, Pack

def button_handler(widget):
    print('button handler')
    for i in range(0, 10):
        print("hello", i)
        yield 1
    print("done", i)


def action0(widget):
    print("action 0")


def action1(widget):
    print("action 1")


def action2(widget):
    print("action 2")


def action3(widget):
    print("action 3")
    
def build(app):
    enc_box = toga.Box()
    hello_box = toga.Box()
    box = toga.Box()

    enc_input = toga.TextInput(readonly=True)
    hello_input = toga.TextInput()

    enc_label = toga.Label('when encrypted', style=Pack(text_align=LEFT))
    hello_label = toga.Label('Please type "hello"', style=Pack(text_align=LEFT))
    join_label = toga.Label('becomes ', style=Pack(text_align=RIGHT))

    def calculate(widget):
        try:
            enc_input.value = str(hello_input.value)
            key = randint(1, 10)
            ciphertext = ''
            for char in enc_input.value:
                unicode_a = ord(char)
                unicode_c = unicode_a + key
                new_letter = chr(unicode_c)
                ciphertext += new_letter
            enc_input.value = ciphertext
        except ValueError:
            enc_input.value = '???'

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

    enc_input.style.update(flex=1)
    hello_input.style.update(flex=1, padding_left=160)
    enc_label.style.update(width=100, padding_left=10)
    hello_label.style.update(width=100, padding_left=10)
    join_label.style.update(width=150, padding_right=10)

    button.style.update(padding=15, flex=1)
    '''brutus_icon = "icons/brutus"
    cricket_icon = "icons/cricket-72.png"

    data = [
        ('root%s' % i, 'value %s' % i)
        for i in range(1, 100)
    ]

    left_container = toga.Table(headings=['Hello', 'World'], data=data)

    right_content = toga.Box(
        style=Pack(direction=COLUMN, padding_top=50)
    )

    for b in range(0, 10):
        right_content.add(
            toga.Button(
                'Hello world %s' % b,
                on_press=button_handler,
                style=Pack(width=200, padding=20)
            )
        )

    right_container = toga.ScrollContainer(horizontal=False)

    right_container.content = right_content

    split = toga.SplitContainer()

    split.content = [left_container, right_container]

    things = toga.Group('Things')

    cmd0 = toga.Command(
        action0,
        label='Action 0',
        tooltip='Perform action 0',
        icon=brutus_icon,
        group=things
    )
    cmd1 = toga.Command(
        action1,
        label='Action 1',
        tooltip='Perform action 1',
        icon=brutus_icon,
        group=things
    )
    cmd2 = toga.Command(
        action2,
        label='Action 2',
        tooltip='Perform action 2',
        icon=toga.Icon.TOGA_ICON,
        group=things
    )
    cmd3 = toga.Command(
        action3,
        label='Action 3',
        tooltip='Perform action 3',
        shortcut=toga.Key.MOD_1 + 'k',
        icon=cricket_icon
    )

    def action4(widget):
        print("CALLING Action 4")
        cmd3.enabled = not cmd3.enabled

    cmd4 = toga.Command(
        action4,
        label='Action 4',
        tooltip='Perform action 4',
        icon=brutus_icon
    )

    app.commands.add(cmd1, cmd3, cmd4, cmd0)
    app.main_window.toolbar.add(cmd1, cmd2, cmd3, cmd4)

    #return split'''
    return box#, split


def main():
    return toga.App('CodeBreaker', 'com.project', startup=build)


if __name__ == '__main__':
    main().main_loop()
