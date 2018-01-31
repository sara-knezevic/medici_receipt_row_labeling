from tkinter import *
from PIL import ImageTk, Image
import os, shutil

def save_label(filename):
	filename = os.path.basename(filename)
	new_filename = filename[:-4] + ".txt"
	
	text = e.get()

	if (text == ""):
		Label(top, text = "No text.").grid(row = 3, columnspan = 2)
	else:
		labelled = open(os.path.join(path_saved, new_filename), "w")
		labelled.write(text)
		labelled.close() # writes to file the label text 

		shutil.move(os.path.join(path_load, filename), os.path.join(path_saved, filename))
		Label(top, text = "Labelled!").grid(row = 3, columnspan = 2)

	top.destroy()

def exit_window():
	quit()

path_load = '/home/saras/coding/medici/medici-labelling/Receipts/Unlabelled' # where the rows are stored, unlabelled ones
path_saved = '/home/saras/coding/medici/medici-labelling/Receipts/Labelled' # where labelled receipts are stored (txt and jpg)

for f in os.listdir(path_load):

	top = Tk()

	photo = f
	row = Image.open(os.path.join(path_load, photo))
	width_r, height_r = row.size
	new_width_r = int(width_r / 6)
	new_height_r = int(height_r / 6)

	row = row.resize((new_width_r, new_height_r), Image.ANTIALIAS)
	row = ImageTk.PhotoImage(row)

	e = Entry(top, bd = 2)
	s = e.get()

	Label(top).grid(row = 1, columnspan = 2)

	e.grid(row = 2, columnspan = 2)

	row_image = Label(top)
	row_image.configure(image = row)

	confirm = Button(top, text = "Confirm", command = lambda: save_label(os.path.join(path_load, f)))
	exit = Button(top, text = "Exit", command = exit_window)

	Label(top, text = "").grid(row = 3, columnspan = 2)

	row_image.grid(row = 0, columnspan = 2)
	confirm.grid(row = 4, column = 0)
	exit.grid(row = 4, column = 1)

	top.mainloop()