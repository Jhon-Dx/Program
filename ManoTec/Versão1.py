from tkinter import *
from PIL import ImageTk, Image


Cor_de_Fundo = "#A9D2F6"
app = Tk()
app.title("Manotec Refrigeração")
app.geometry("900x600")
app.configure(background=Cor_de_Fundo)

#Setting it up
img = ImageTk.PhotoImage(Image.open("app.png"))

#Displaying it
imglabel = Label(app, image=img).grid(row=1, column=1)


app_root.mainloop()












app.mainloop()
