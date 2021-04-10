import tkinter
from PIL import ImageTk, Image  

root = tkinter.Tk()
root.title('PoE Notes')

image1 = Image.open("lab.png")
image2 = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=image2)
label1.image=image2

label1.place(x=1, y=1)

root.mainloop()