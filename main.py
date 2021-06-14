from tkinter import *
from PIL import Image

root = Tk()
#specifying the title of the tkinter window within which the specified image is displayed
root.title("QUOTES")
#using image.open function and PhotoImage function to open the spcified image and display on the screen
img = PhotoImage(Image.open("lena_gray.jpeg"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()