import toga
from random import randint
from toga.style.pack import COLUMN, LEFT, RIGHT, ROW, Pack

def button_handler(widget):
    print('button handler')
    for i in range(1, 5):
        print("Word", i)
        yield 1
    print("done", i)


def level1(widget):
    print("Level 1")


def level2(widget):
    print("Level 2")


def level3(widget):
    print("Level 3")


def level4(widget):
    print("Level 4")
    
def build(app):
    brutus_icon = "icons/brutus"
    cricket_icon = "icons/cricket-72.png"

    data = [
        ('root%s' % i, 'value %s' % i)
        for i in range(1, 100)
    ]

    left_container = toga.Table(headings=['Original Word', 'Encrypted Word'], data=data)

    right_content = toga.Box(
        style=Pack(direction=COLUMN, padding_top=50)
    )

    for b in range(0, 10):
        right_content.add(
            toga.Button(
                'Level %s' % b,
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
        level1,
        label='Level 1',
        tooltip='Activate level 1',
        icon=brutus_icon,
        group=things
    )
    cmd1 = toga.Command(
        level2,
        label='Level 2',
        tooltip='Activate level 2',
        icon=brutus_icon,
        group=things
    )
    cmd2 = toga.Command(
        level3,
        label='Level 3',
        tooltip='Activate level 3',
        icon=toga.Icon.TOGA_ICON,
        group=things
    )
    cmd3 = toga.Command(
        level4,
        label='Level 4',
        tooltip='Activate level 4',
        shortcut=toga.Key.MOD_1 + 'k',
        icon=cricket_icon
    )

    def action4(widget):
        print("CALLING Action 4")
        cmd3.enabled = not cmd3.enabled

    cmd4 = toga.Command(
        action4,
        label='Level 4',
        tooltip='Perform action 4',
        icon=brutus_icon
    )

    app.commands.add(cmd1, cmd3, cmd4, cmd0)
    app.main_window.toolbar.add(cmd1, cmd2, cmd3, cmd4)

    return split


def main():
    return toga.App('CodeBreaker', 'com.project', startup=build)


if __name__ == '__main__':
    main().main_loop()
