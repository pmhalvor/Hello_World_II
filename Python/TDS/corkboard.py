import tkinter as tk
import os

"""
Working on:
-read from files
-save to files
-layout nicely
-switch from idea->task->working->complete
-graph showing how much of each task there is
-

"""

###################### GLOBAL VARIABLES ##########################
number_of_tasks = 0

######################### FUNCITONS ##############################
"""
Functions needed for working system:
v create files
v create lists  #done in scene setup
v update_list(fname):
	will update list from respective files w/ lists
- add_to_board(entry, boardname):
	will add task to specified board

- move(frm, to):
	will move selected item from one board to next
- save_data():
	will save all the lists to their respective file names
	might not need this if i update file every time new task is added to list
	but in good OO-nomenclature save_data should remain its own indvd. task


"""
# def save_data(fname):
# 	text = e.get().strip()
# 	if text: # checks for empty entries
# 		f = open(fname, 'a')
# 		f.write(text + '\n')
# 		f.close()
# 		#IDK IF THESE ARE NEEDED FOR MY NEW VERSION
# 		todos.insert(tk.END, text)
# 		e.delete(0, tk.END)

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

def add_to_board(fname, lstbx):
	input = entry.get() #entry defined globally in SET SCENE area
	print('valid input, now writing to file and listbox')
	# weird that this only calls when file first starts, but not throughout loop
	if input:
		f = open(fname, 'w')
		f.write(input + '\n')
		f.close()
		lstbx.insert(tk.END, input)


##################### SCENE SET ###########################
master = tk.Tk()

# Make sure files are in current directory
create_file('Idea')
create_file('ToDo')
create_file('Work')
create_file('Done')

# Create listboxes
idea = tk.Listbox(master)
idea.grid(row=3, column=0)
todo = tk.Listbox(master)
todo.grid(row=3, column=1)
work = tk.Listbox(master)
work.grid(row=3, column=2)
done = tk.Listbox(master)
done.grid(row=3, column=3)

# Update lists if files already exsisted
update_list('Idea.txt', idea)
update_list('ToDo.txt', todo)
update_list('Work.txt', work)
update_list('Done.txt', done)

#Label
l = tk.Label(master, text='Task:')
l.grid(row=1,column=0)

#Inbox
entry = tk.Entry(master)
entry.grid(row=1, column=1, columnspan=4)

#Buttons
Q = tk.Button(master, text='Quit', command=master.quit)
Q.grid(row=2, column=4, sticky=tk.E) #Adds to stage #sticky=tk.W---> west

I = tk.Button(master, text='Idea', command=add_to_board('Idea.txt', idea))
I.grid(row=2, column=0, sticky=tk.W) #adds to stage

T = tk.Button(master, text='Todo', command=add_to_board('ToDo.txt', todo))
T.grid(row=2, column=1, sticky=tk.W) #adds to stage

W = tk.Button(master, text='Work', command=add_to_board('Work.txt', work))
W.grid(row=2, column=2, sticky=tk.W) #adds to stage

D = tk.Button(master, text='Done', command=add_to_board('Done.txt', done))
D.grid(row=2, column=3, sticky=tk.W) #adds to stage



master.mainloop()
