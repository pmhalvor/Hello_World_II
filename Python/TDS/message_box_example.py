# from tkinter import *
# from tkMessageBox import *
#
# def answer():
#     showerror("Answer", "Sorry, no answer available")
#
# def callback():
#     if askyesno('Verify', 'Really quit?'):
#         showwarning('Yes', 'Not yet implemented')
#     else:
#         showinfo('No', 'Quit has been cancelled')
#
# Button(text='Quit', command=callback).pack(fill=X)
# Button(text='Answer', command=answer).pack(fill=X)
# mainloop()


from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("100x100")
def hello():
   messagebox.showinfo("Title: Hello", "Hello World")

B1 = Button(top, text = "Say Hello", command = hello)
B1.place(x = 35,y = 50)

top.mainloop()
