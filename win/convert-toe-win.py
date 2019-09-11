import sys, os, subprocess
from os.path import dirname, abspath
import shutil
import glob
import re
import tkinter
import tkinter.filedialog, tkinter.messagebox

root = tkinter.Tk()
root.withdraw()
iDir = os.path.abspath(os.path.expanduser('~/Desktop'))
input_file = ""
input_file = tkinter.filedialog.askopenfilename(filetypes=[('all files', '*'), ('toe to acsii','.toe'), ('ascii to toe', '.toc')], initialdir= iDir)

print("file: ", input_file)

folder = ""

td_path = "C:/Program Files/Derivative/TouchDesigner099/bin/"

if input_file != "":

	folder = dirname(input_file)
	print("folder: ",folder)
	if folder != "":
		folder = folder + "/"
	name, ext = os.path.splitext(os.path.basename(input_file))

	expand_script = td_path + "toeexpand"
	collapse_script = td_path + "toecollapse"

	if ext == ".toe":
		if os.path.exists(folder+"/"+name+".toe.toc"):
			os.remove(folder+"/"+name+".toe.toc")
		if os.path.exists(folder+"/"+name+".toe.dir"):
			shutil.rmtree(folder+"/"+name+".toe.dir")
		subprocess.call([expand_script, input_file])
	elif ext == ".toc":
		subprocess.call([collapse_script, folder+name+ext])

for p in glob.glob(folder+"*.bkp*"):
	if os.path.isfile(p):
		os.remove(p)
