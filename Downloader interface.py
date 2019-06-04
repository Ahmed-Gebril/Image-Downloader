## This GUI takes a user's request to download images from the internet with a number of images needed or within a given period of time.

from bs4 import BeautifulSoup
import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image
from io import BytesIO

HEIGHT = 700
WIDTH = 700

class Userinterface:

    def __init__(self):

        """
        constructor: creats windows both topframe and bottomframe, lables
        and scales the window.
        """

        self.__mainwindow = tk.Tk()

        canvas = tk.Canvas(self.__mainwindow, height=HEIGHT, width=WIDTH)
        canvas.pack()

        background_image = tk.PhotoImage(file="parrot_PNG726.png")
        background_label = tk.Label(self.__mainwindow, image=background_image)
        background_label.place(relwidth=2, relheight=2)

        frame = tk.Frame(self.__mainwindow, bg='#80c1ff', bd=5)
        frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

      ##  entry3 = tk.Entry(self.__mainwindow)  # create 3st entry box
      ## canvas.create_window(100, 240, window=entry3)  # create a canvas window to place the 3rd entry box on top of the background image

        button = tk.Button(frame, text="Download images", font=40, command= self.downloader)
        entry = tk.Entry(frame, font=40)
        entry.place(relwidth=0.65, relheight=1)


        self.__entry=entry.get()
        button.place(relx=0.7, relheight=1, relwidth=0.3)

        lower_frame = tk.Frame(self.__mainwindow, bg='#80c1ff', bd=10)
        lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

        label = tk.Label(lower_frame)
        label.place(relwidth=1, relheight=1)




    def start(self):


        self.__mainwindow.mainloop()

    def downloader(self):

        import http_request _scraper


def main():

    ui = Userinterface()
    ui.start()



if __name__ == '__main__':
        main()
