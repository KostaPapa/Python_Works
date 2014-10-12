import Tkinter
import tkMessageBox

class FirstWindow( object ):
    '''will create the first window'''

    def __init__( game, firstWindow = 0, title = 'WELCOME TO TABOO GAME' ):
        '''two variables'''

        game.__firstWindow              = firstWindow
        game.__title                    = title
                
        game.__firstWindow              = Tkinter.Tk(screenName=None, baseName=None, className = ' Taboo Game')
        game.__title                    = Tkinter.Label( game.__firstWindow, text = game.__title )

        game.__menuChoice_1             = Tkinter.Button( game.__firstWindow, text = '1\x11 PLAY GAME' )
        game.__menuChoice_2             = Tkinter.Button( game.__firstWindow, text = '2\x11 GAME RULES' )
        game.__menuChoice_3             = Tkinter.Button( game.__firstWindow, text = '3\x11 QUIT', command = game.__firstWindow.quit )      

        game.__title.pack()
        
        game.__menuChoice_1.pack()
        game.__menuChoice_2.pack()
        game.__menuChoice_3.pack()

        Tkinter.mainloop()
        
def firstWindow():
    '''will display the first window of game'''

    firstWindow = GuiInterFace()

def main():

    FirstWindow()

main()
