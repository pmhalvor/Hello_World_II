import tkinter as tk
import os


def save_data():
	text = e.get().strip()
	if text: # checks for empty entries
		f = open('tasks.txt', 'a')
		f.write(text + '\n')
		f.close()
		todos.insert(tk.END, text)
		e.delete(0, tk.END)

def start_task():
	if todos.curselection():
		task = todos.get(todos.curselection())
		if task:
			f = open('working.txt', 'a')
			f.write(task + '\n')
			f.close()
			wrkng.insert(tk.END, task)
			todos.delete(todos.curselection())
			# Need to update todo file when removed

def create_idea():
	idea = e.get()
	if idea:
		f = open('ideas.txt', 'w+')
		f.write(idea + '\n')
		f.close()
		ideas.insert(tk.END, idea)

# Checks if the files exist
# if not then create them and
# write the header '(Name) List'
if not os.path.exists('tasks.txt'):
	f = open('tasks.txt', 'w')
	f.write('Task List:\n')
	f.close()

if not os.path.exists('working.txt'):
	f = open('working.txt', 'w')
	f.write('Working on List:\n')
	f.close()


root = tk.Tk()

tk.Label(root, text = "Please Enter Task Here:").pack()

e = tk.Entry(root)
e.pack()

tk.Button(root, text= 'Idea', command = create_idea).pack({'side':'left'})
tk.Button(root, text = 'Save', command = save_data).pack({'side':'right'})
tk.Button(root, text = 'Work', command = start_task).pack({'side':'right'})
# tk.Button(root, text = 'Save', command = save_data).grid(row=0, column=0)

ideas = tk.Listbox(root)
ideas.pack({'side': 'left'})
ideas.insert(tk.END, "Ideas")

todos = tk.Listbox(root)
todos.pack({'side': 'left'})
todos.insert(tk.END, "To Dos")

wrkng = tk.Listbox(root)
wrkng.pack({'side':'right'})
wrkng.insert(tk.END, 'Working On')


root.mainloop()
