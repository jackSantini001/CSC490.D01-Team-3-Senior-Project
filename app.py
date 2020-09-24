import math
import toga
from toga.style.pack import COLUMN, LEFT, RIGHT, ROW, Pack
from toga.colors import WHITE, rgb
from toga.fonts import SANS_SERIF
import pygame
def button_handler(widget):
    print('Answer Received')


def level1(widget):
    print("Level 1")
    
def level2(widget):
    print("Level 2")
    
def level3(widget):
    print("Level 3")

def level4(widget):
    print("Level 4")

def level5(widget):
    print("Level 5")


def build(app):
    level1_icon = "icons/chicken-level1.png"
    level2_icon = "icons/cat-level2.png"
    level3_icon = "icons/fox-level3.png"
    level4_icon = "icons/lion-level4.png"
    level5_icon = "icons/tiger-level5.png"

    data = [
        ('Question1' , 'Points Receive: 3 ' , 'Which 100-mile long waterway links the Mediterranean and the Red Sea?'),
        ('Question2' , 'Points Receive: 5' , 'What is the capital of Kenya?'),
        ('Question3' , 'Points Receive: 7' , 'The average of first 50 natural numbers is?'),
        ('Question4' , 'Points Receive: 9' , 'The number of 3-digit numbers divisible by 6?'),
        ('Question5' , 'Points Receive: 11' , 'Which is the second longest river in Africa?')
    ]

    left_container = toga.Table(headings=['Questions', 'Points Per Question', 'Contents'], data = data)

    right_content = toga.Box(
        style=Pack(direction=COLUMN, padding_top=50)
    )
    for b in range(1, 6):
        right_content.add(
            toga.Button(
                'Answer %s' % b,
                on_press=button_handler,
                style=Pack(width=200, padding=20)
            )
        )
        print("Answer number", b, "is :")
    right_container = toga.ScrollContainer(horizontal=False)

    right_container.content = right_content

    split = toga.SplitContainer()

    split.content = [left_container, right_container]

    levels = toga.Group('Levels')

    cmd0 = toga.Command(
        level1,
        label='Level 1',
        tooltip='Perform level 0',
        icon=level1_icon,
        group=levels
    )
    cmd1 = toga.Command(
        level2,
        label='Level 2',
        tooltip='Perform level 1',
        icon=level2_icon,
        group=levels
    )
    cmd2 = toga.Command(
        level3,
        label='Level 3',
        tooltip='Perform level 2',
        icon=level3_icon,
        group=levels
    )
    cmd3 = toga.Command(
        level4,
        label='Level 4',
        tooltip='Perform level 3',
        shortcut=toga.Key.MOD_1 + 'k',
        icon=level4_icon
    )

    cmd4 = toga.Command(
        level5,
        label='Level 5',
        tooltip='Perform level 4',
        icon=level5_icon
    )

    app.commands.add(cmd1, cmd2, cmd3, cmd4)
    app.main_window.toolbar.add(cmd0, cmd1, cmd2, cmd3, cmd4)

    return split


def main():
    return toga.App('Math & History Learning', 'org.beeware.helloworld', startup=build)


if __name__ == '__main__':
    main().main_loop()
