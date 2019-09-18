import tkinter as tk
import os

"""
Problems:
- Prioritize OO-design, or as few lines as possible


NOTES:
Button funcitons cannot have any parameters in order but be callable w/ button

Should be much easier to make as OO prog since each quad is doing the same thing
I just want to have a working prog before trying to build in java
"""

######################### FUNCITONS ##############################

def create_file(str):
	"""
	Creates file \'str.txt\' if not found in directory

	Parameters:

		str (string)
			String name of file
	"""
	if not os.path.exists(str+'.txt'): #broke up str and .txt to give list title
		f = open(str+'.txt', 'w')
		f.write(str+' List:\n') #list title
		f.close()

def update_list(fname, lstbx):
	"""
	Reads previously saved lists and loads data to respective listboxes

	Parameters:
		fname (string)
			name of file containing list

		lstbx (Listbox)
			list which will be updated

	"""
	f = open(fname, 'r')
	f.readline()
	for line in f:
		lstbx.insert(tk.END, line.strip('\n'))
	f.close()

def button_Idea(event=None):
	return 0

def add_Idea(event=None):
	"""
	Takes current entry box and inputs to Idea listbox and file

	"""
	input = entry.get().strip()
	if input:
		if is_repeat(input, Idea): #makes sure there are no repeats
			print("Found repeat")
			return
		f = open('Idea.txt', 'a')
		f.write(input+'\n')
		f.close()
		Idea.insert(tk.END, input)
		entry.delete(0, tk.END)

def add_ToDo():
	"""
	Takes current entry box and inputs to ToDo listbox and file

	"""
	input = entry.get().strip()
	if input:
		if is_repeat(input, ToDo): #makes sure there are no repeats
			print("Found repeat")
			return
		f = open('ToDo.txt', 'a')
		f.write(input+'\n')
		f.close()
		ToDo.insert(tk.END, input)
		entry.delete(0, tk.END)

def add_Work():
	"""
	Takes current entry box and inputs to Work listbox and file

	"""
	input = entry.get().strip()
	if input:
		if is_repeat(input, Work): #makes sure there are no repeats
			print("Found repeat")
			return
		f = open('Work.txt', 'a')
		f.write(input+'\n')
		f.close()
		Work.insert(tk.END, input)
		entry.delete(0, tk.END)

def add_Done():
	"""
	Takes current entry box and inputs to Done listbox and file

	"""
	input = entry.get().strip()
	if input:
		if is_repeat(input, Done): #makes sure there are no repeats
			print("Found repeat")
			return
		f = open('Done.txt', 'a')
		f.write(input+'\n')
		f.close()
		Done.insert(tk.END, input)
		entry.delete(0, tk.END)

def move_to_ToDo(event):
	"""
	Double click action that moves task from Idea to ToDo

	"""
	entry.insert(0, Idea.get(Idea.curselection())) #to avoid having to write new
	str = Idea.get(Idea.curselection())
	delete_from_file('Idea.txt', str)
	Idea.delete(Idea.curselection()) #deletes from previous list.
	add_ToDo() #calls same method as above

def move_to_Work(event):
	"""
	Double click action that moves task form ToDo to Work

	"""
	entry.insert(0, ToDo.get(ToDo.curselection())) #to avoid having to write new
	str = ToDo.get(ToDo.curselection())
	delete_from_file('ToDo.txt', str)
	ToDo.delete(ToDo.curselection()) #deletes from previous list.
	add_Work() #calls same method as above

def move_to_Done(event):
	"""
	Double click action that moves task from Work to Done

	"""
	entry.insert(0, Work.get(Work.curselection())) #to avoid having to write new
	str = Work.get(Work.curselection())
	delete_from_file('Work.txt', str)
	Work.delete(Work.curselection()) #deletes from previous list.
	add_Done() #calls same method as above

def delete_from_done(event):
	"""
	Double click action that just deletes from Done list and file

	"""
	str = Done.get(Done.curselection())
	delete_from_file('Done.txt', str)
	Done.delete(Done.curselection())

def delete_from_file(fname, remove_str):
	"""
	Helper function which removes one line containing remove_str. After the
	requested line to be removed is skipped, remove_str is changed so that the
	file will always match the Listbox.

	Parameters:
		fname (string)
			name of file to be changed

		remove_str (string)
			data which is supposed to be removed from file

	"""
	print('\nRemoving '+remove_str+' from '+fname+':\n')
	with open(fname, 'r') as f: #new formet. see how it works
		lines = f.readlines()
	with open(fname, 'w') as f:
		for line in lines:
			if line.strip() != remove_str.strip():
				print('rewriting: ' +line.strip('\n'))
				f.write(line)
			else:
				print('REMOVED: '+ line.strip('\n'))
				remove_str = '------------------' #cant make blank or null


def is_repeat(str, lstbx):
	"""
	Helper function that checks is current input is already in list

	Parameters:
		str (string)
			current input

		lstbx (Listbox)
			the list which needs to be checked fro repeats

	"""
	for i in range(lstbx.size()):
		if str.strip() == lstbx.get(i).strip():
			entry.delete(0, tk.END)
			return True
	return False


##################### SCENE SET ###########################
master = tk.Tk()

# Make sure files are in current directory
create_file('Idea')
create_file('ToDo')
create_file('Work')
create_file('Done')


#Label
l = tk.Label(master, text='Enter task in space below:')
l.grid(row=0,column=0)

xtra = tk.Label(master, text=' ')
xtra.grid(row=2,column=0)

#Buttons
Q = tk.Button(master, text='Quit', command=master.quit)
Q.grid(row=5, column=3, sticky=tk.E) #Adds to stage #sticky=tk.W---> west

I = tk.Button(master, text='Idea', command=add_Idea)
I.grid(row=3, column=0) #adds to stage

T = tk.Button(master, text='ToDo', command=add_ToDo)
T.grid(row=3, column=1) #adds to stage

W = tk.Button(master, text='Work', command=add_Work)
W.grid(row=3, column=2) #adds to stage

D = tk.Button(master, text='Done', command=add_Done)
D.grid(row=3, column=3) #adds to stage


#Inbox
entry = tk.Entry(master, width=100)
entry.grid(row=1, column=0, columnspan=4)
master.bind('<Return>', add_Idea)

def idea_to_taskbar(event):
	ind = tk.ACTIVE
	# if Idea.curselection() != ():
	# 	ind = Idea.curselection()
	# 	print(Idea.curselection())
	str = Idea.get(ind)
	entry.delete(0, tk.END)
	entry.insert(0, str)


def to_taskbar(lstbx):
	lstbx.get(tk.ACTIVE)

# Create listboxes and insert to scene
Idea = tk.Listbox(master, width=25, height=15)
Idea.grid(row=4, column=0, sticky=tk.N+tk.S)
Idea.bind('<Double-Button-1>', move_to_ToDo)
Idea.bind('<Button>', idea_to_taskbar)

ToDo = tk.Listbox(master, width=25, height=15)
ToDo.grid(row=4, column=1)
ToDo.bind('<Double-Button-1>', move_to_Work)

Work = tk.Listbox(master, width=25, height=15)
Work.grid(row=4, column=2)
Work.bind('<Double-Button-1>', move_to_Done)

Done = tk.Listbox(master, width=25, height=15)
Done.grid(row=4, column=3)
Done.bind('<Double-Button-1>', delete_from_done)


# Update lists if files already exsisted
update_list('Idea.txt', Idea)
update_list('ToDo.txt', ToDo)
update_list('Work.txt', Work)
update_list('Done.txt', Done)


# Start everything
master.mainloop()
