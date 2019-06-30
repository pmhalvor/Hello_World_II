import tkinter as tk
import os

def save_data():
    text = name.get().strip()
    if text: # checks for empty entries
        f = open('names.txt', 'a')
        f.write(text + '\n')
        f.close()
        name.delete(0, tk.END)

# Checks if the file exists
# if not then create it and
# write the header 'Name List'
if not os.path.exists('names.txt'):
    f = open('names.txt', 'w')
    f.write('Name_List:\n')
    f.close()

root = tk.Tk()

tk.Label(root, text = "Please Enter Name Here:").pack()

name = tk.Entry(root)
name.pack()

tk.Button(root, text = 'Save', command = save_data).pack()

root.mainloop()
