from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

X_OFFSET = -25
Y_OFFSET = -25
RES = 0.05

if __name__ == "__main__":
    root = Tk()

    #setting up a tkinter canvas with scrollbars
    frame = Frame(root, bd=2, relief=SUNKEN)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    xscroll = Scrollbar(frame, orient=HORIZONTAL)
    xscroll.grid(row=1, column=0, sticky=E+W)
    yscroll = Scrollbar(frame)
    yscroll.grid(row=0, column=1, sticky=N+S)
    canvas = Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
    canvas.grid(row=0, column=0, sticky=N+S+E+W)
    xscroll.config(command=canvas.xview)
    yscroll.config(command=canvas.yview)
    frame.pack(fill=BOTH,expand=1)

    #adding the image
    File = askopenfilename(parent=root, initialdir="C:/",title='Choose an image.')
    img = ImageTk.PhotoImage(Image.open(File))
    canvas.create_image(0,0,image=img,anchor="nw")
    canvas.config(scrollregion=canvas.bbox(ALL))

    x_wps = []
    y_wps = []

    #function to be called when mouse is clicked
    def printcoords(event):
        canvas = event.widget
        x = canvas.canvasx(event.x)
        y = canvas.canvasy(event.y)
        r = 10
        canvas.create_oval(x-r, y-r, x+r, y+r)

        x_transform = (x)*(RES) + X_OFFSET
        y_transform = (y)*(RES) + Y_OFFSET

        x_wps.append(x_transform)
        y_wps.append(y_transform)

        print(str(x_transform), str(y_transform))

    canvas.bind("<Button 1>",printcoords)

    root.mainloop()

    f = open("waypointNodes.txt","w+")
    for i in range(len(x_wps)):
        f.write(str(x_wps[i]) + ", ")
    f.write("\n")
    for i in range(len(y_wps)):
        f.write(str(y_wps[i]) + ", ")
    f.close()
