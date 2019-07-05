import tkinter as tk
import os

"""
Working on:
-write to files
-layout nicely
-switch from idea->task->working->complete
-graph showing how much of each task there is
-

Problems:
- Prioritize OO-design, or as few lines as possible

"""

###################### GLOBAL VARIABLES ##########################
number_of_tasks = 0
moving = False

######################### FUNCITONS ##############################
"""
NOTES:
Button funcitons cannot have any parameters in order but be callable w/ button


Functions needed for working system:
v create files
v create lists  #done in scene setup
v update_list(fname):
	will update list from respective files w/ lists
- add_to_board(entry, boardname):
	will add task to specified board
- delete:
	to delete from both list and file

- move(frm, to):
	will move selected item from one board to next
- save_data():
	will save all the lists to their respective file names
	might not need this if i update file every time new task is added to list
	but in good OO-nomenclature save_data should remain its own indvd. task
"""

def create_file(str):
	if not os.path.exists(str+'.txt'): #broke up str and .txt to give list title
		f = open(str+'.txt', 'w')
		f.write(str+' List:\n') #list title
		f.close()

def update_list(fname, lstbx):
	f = open(fname, 'r')
	f.readline()
	for line in f:
		lstbx.insert(tk.END, line)
	f.close()

def add_Idea():
	input = entry.get().strip()
	if input:
		f = open('Idea.txt', 'a')
		f.write(input+'\n')
		f.close()
		Idea.insert(tk.END, input)
		entry.delete(0, tk.END)

def add_ToDo():
	input = entry.get().strip()
	if input:
		f = open('ToDo.txt', 'a')
		f.write(input+'\n')
		f.close()
		ToDo.insert(tk.END, input)
		entry.delete(0, tk.END)

def add_Work():
	input = entry.get().strip()
	if input:
		f = open('Work.txt', 'a')
		f.write(input+'\n')
		f.close()
		Work.insert(tk.END, input)
		entry.delete(0, tk.END)

def add_Done():
	input = entry.get().strip()
	if input:
		f = open('Done.txt', 'a')
		f.write(input+'\n')
		f.close()
		Done.insert(tk.END, input)
		entry.delete(0, tk.END)

def move_to_ToDo(event):
	entry.insert(0, Idea.get(Idea.curselection())) #to avoid having to write new
	add_ToDo() #calls same method as above
	Idea.delete(Idea.curselection()) #deletes from previous list.

def delete(lstbox):
	#I dont have nay good way of deleting abstractly. Need to think a more here
	return 0

##################### SCENE SET ###########################
master = tk.Tk()

# Make sure files are in current directory
create_file('Idea')
create_file('ToDo')
create_file('Work')
create_file('Done')

#Label
l = tk.Label(master, text='Task:')
l.grid(row=1,column=0)

#Inbox
entry = tk.Entry(master)
entry.grid(row=1, column=1, columnspan=4)

# Create listboxes and insert to scene
Idea = tk.Listbox(master)
Idea.grid(row=3, column=0)
Idea.bind('<Double-Button-1>', move_to_ToDo)

ToDo = tk.Listbox(master)
ToDo.grid(row=3, column=1)
# ToDo.bind('<Double-Button-1>', move_to_Work)

Work = tk.Listbox(master)
Work.grid(row=3, column=2)
# Work.bind('<Double-Button-1>', move_to_Done)

Done = tk.Listbox(master)
Done.grid(row=3, column=3)

# Update lists if files already exsisted
update_list('Idea.txt', Idea)
update_list('ToDo.txt', ToDo)
update_list('Work.txt', Work)
update_list('Done.txt', Done)

#Buttons
Q = tk.Button(master, text='Quit', command=master.quit)
Q.grid(row=2, column=4, sticky=tk.E) #Adds to stage #sticky=tk.W---> west

I = tk.Button(master, text='Idea', command=add_Idea)
I.grid(row=2, column=0, sticky=tk.W) #adds to stage

T = tk.Button(master, text='Todo', command=add_ToDo)
T.grid(row=2, column=1, sticky=tk.W) #adds to stage

W = tk.Button(master, text='Work', command=add_Work)
W.grid(row=2, column=2, sticky=tk.W) #adds to stage

D = tk.Button(master, text='Done', command=add_Done)
D.grid(row=2, column=3, sticky=tk.W) #adds to stage

master.mainloop()
