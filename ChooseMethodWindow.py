"""
SPT_Tool 2021
Antonio Brito @ BCB lab ITQB
"""

import tkinter as tk
from EllipseGUI import ellipseGUI
from loadGUI import loadNPY
from BatchGUI import batchNPY


# Class that inherits root window class from tk
class ChooseWindow(tk.Tk):
    """
    GUI window responsible for the choosing what input method to use
     - .csv predrawn ellipse from fiji
     - draw ellipses in-situ
     - load previous analyzed data to compare or reanalyze
     - batch load npys for several analysis
    """
    def __init__(self):
        super().__init__()  # init of tk.Tk

        self.wm_title("Methods")
        self.title("Methods")
        self.geometry('250x180')

        status_text = tk.Label(master=self, text="Choose how to input ellipse data")
        status_text.pack(side='top', fill='both')

        ELLIPSE_button = tk.Button(master=self, text="Draw Ellipses (xml + tif)", command=self.ellipse)
        ELLIPSE_button.pack(side='top', fill='both')

        LOAD_button = tk.Button(master=self, text="Load single .npy data)", command=self.loadnpy)
        LOAD_button.pack(side='top', fill='both')

        BATCH_button = tk.Button(master=self, text="Batch analysis of .npy files", command=self.batchnpy)
        BATCH_button.pack(side='top', fill='both')

    def ellipse(self):
        """
        Open next GUI window for inputting xml and drawing ellipse
        """
        self.destroy()
        gui = ellipseGUI()
        gui.mainloop()

    def loadnpy(self):
        """
        Open next GUI window for inputting one or more .npy files of previously loaded data
        """
        self.destroy()
        gui = loadNPY()
        gui.mainloop()

    def batchnpy(self):
        """
        Opens next GUI window for batch analysis of several npys
        """

        self.destroy()
        gui = batchNPY()
        gui.mainloop()



if __name__ == '__main__':
    app = ChooseWindow()
    app.mainloop()
