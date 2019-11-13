import tkinter

top = tkinter.Tk()


def helloCallBack():
    tkinter..showinfo("Hello Python", "Hello World")


B = tkinter.Button(top, text="Hello", command=helloCallBack)

B.pack()
top.mainloop()
