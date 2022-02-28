from tkinter import *
import tkinter.font as font

class Window:
    def __init__ (self, width = '750', height = '400', name = 'Weather Report'):
        self.width = width
        self.height = height
        self.name = name 

    def CreateWindow (self): 
        root = Tk ()

        root ['bg'] = "DeepSkyBlue2"
        root.title (self.name)
        root.geometry (str (self.width) + 'x' + str (self.height))
        root.resizable (width = False, height = False)
        root.iconbitmap ('materials/logo.ico')
        root.mainloop ()

    def CreateLabel (self, Text, lx = '10px', ly = '10px', FontType = 0, FontSize = 14):
        if FontType == 0:
            LabelFont = font.Font (family = 'Century Gothic', size = FontSize)

        Ll = Label (text = Text, font = LabelFont)
        Ll.place (x = lx, y = ly)
        Ll.pack ()
