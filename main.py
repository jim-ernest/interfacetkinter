from tkinter import*
import tkinter as tk
from PIL import ImageTk, Image
window =Tk()
#Define the geometry of the window
window.geometry("600x250")
frame_a = tk.Frame()
frame_a= Frame(window, highlightbackground="blue", highlightthickness=2)

label_a = tk.Label(frame_a, text="SITTING POSTURE RECOGNITION SYSTEM",
    fg="white",
    bg="black",
    width=90,
    height=2,
    font=('Helvetica 15 bold') )
border_effects = {
    "groove": tk.GROOVE,
   }
label_a.pack(pady=20)
label_b = tk.Label(frame_a, text="LIVE A HEALTHY LIFE BY ADJUSTING YOUR SITTING POSTURE",
font=('Helvetica 10 bold'))
label_b.pack()
frame_a.pack()
 #Load the image
image=Image.open('t.jpg')

# Resize the image in the given (width, height)
img=image.resize((700, 350))

# Convert the image in TkImage
my_img=ImageTk.PhotoImage(img)

# Display the image with label
label=Label(frame_a, image=my_img)
label.pack(pady=10)

button = Button(
	 frame_a, text = 'START DETECTION', command = "" ,
    fg= "WHITE", bg="#00008B",height= 2, width=15, font=('Helvetica 10 bold'))

button.pack(side=BOTTOM, padx=0, pady=10)

button.pack()


window.mainloop()