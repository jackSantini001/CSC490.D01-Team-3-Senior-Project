"""
Network mini game for 2020 senior project
"""
import toga
from toga.colors import WHITE, rgb
from toga.style import Pack
from toga.style.pack import CENTER, COLUMN, ROW


def tower_action(widget):
    print('Tower')

def tower1(widget):
    print('Tower 1')

#def instructions(self, widget):
    #self.main_window.info_dialog(
    #    'Instructions:',
    #    "Hello, and welcome to Clear the Paths!  This is a mini"
    #    "game that intends to show the very basics of what networking"
    #    "is all about.  Castles and towers represent computers and"
    #    "routers, while bridges represent the connections between"
    #    "them.  Your job is to make sure the bridges stay open so"
    #    "that supplies can be transported between locations safely."
    #    "Bridges will periodically be raised, and will require you to"
    #    "press a button to lower it again.  Additionally, bandits will"
    #    "appear on the paths to block the transports.  You will need to"
    #    "click on them to get rid of them before the shipment is lost."
    #    "If you have any more questions, you can go to the help menu for"
    #    "more details.",)
    

class NetworkGame(toga.App):

    
    def startup(self):
        n = 0
        main_box = toga.Box(style=Pack(direction=COLUMN))
        self.main_window = toga.MainWindow(title=self.formal_name)
        button_box = toga.Box()

        #instruction_button = toga.Button('Instructions',
        #                               on_press=instructions)
        progress_label = toga.Label('Progress: ', style=Pack(alignment=CENTER))
        progress = toga.ProgressBar(max=100, value=1)
        tower_buttons = toga.Box(style=Pack(direction=ROW))
        for b in range(1, n+1):
            tower_buttons.add(
                toga.Button(
                    'Tower %s' % b,
                    on_press=tower_action
                ))
        background = toga.ImageView(id='green field', image="icons/GreenField1.jpg")
        #button_box.add(instruction_button)
        button_box.add(progress_label)
        button_box.add(progress)
        button_box.add(tower_buttons)
        main_box.add(button_box)
        main_box.add(background)
        
        

        
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return NetworkGame('Clear the Paths!')
