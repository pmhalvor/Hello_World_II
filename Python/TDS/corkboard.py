import tkinter as tk

number_of_tasks = 0
def add_to_board(str):
	global number_of_tasks
	index = number_of_tasks + 2
	m = tk.Message(master, text=str)
	m.grid(row=index, column=0)
	number_of_tasks += 1

master = tk.Tk()

#Inbox
e = tk.Entry(master)
e.grid(row=1, column=1)

#Button
Q = tk.Button(master, text='Quit', command=master.quit)
Q.grid(row=0, column=3, sticky=tk.W) #Adds to stage

A = tk.Button(master, text='Add', command=add_to_board(e.get()))
A.grid(row=0, column=0, sticky=tk.W) #adds to stage

#Label
l = tk.Label(master, text='Task')
l.grid(row=1,column=0)

la = tk.Label(master, text='test')
la.grid(row=2,column=0)


tk.mainloop()
