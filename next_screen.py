from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title('Hospital')
window.config(bg='yellow')
window.geometry('300x350')

canvas = Canvas(window, width=300, height=300, bg="Yellow", borderwidth=0, highlightthickness=0)
canvas.place(x=0, y=0)
img = ImageTk.PhotoImage(Image.open('doctor-shake-hand-hello-patient-260nw-1185982159.jpg'))
canvas.create_image(0, 0, anchor=NW, image=img)


def exiting():
    window.destroy()


exit_btn = Button(window, text='Exit', fg='red', command=exiting)
exit_btn.place(x=220, y=300)
window.mainloop()
