from tkinter import *
name="beautify"
import os,shutil
from datetime import datetime
myapp=Tk()	
myapp.resizable(0,0)
myapp.title("Beautify")
myapp.geometry("600x270+405+199")
myapp.configure(background="#136fd8")
font10 = "-family {Segoe UI} -size 18 -weight normal -slant "  \
            "italic -underline 0 -overstrike 0"
font12 = "-family {Bookman Old Style} -size 18 -weight normal "  \
            "-slant italic -underline 0 -overstrike 0"
font15 = "-family Arial -size 14 -weight normal -slant italic "  \
            "-underline 0 -overstrike 0"
font9 = "-family {Segoe UI Symbol} -size 18 -weight normal "  \
            "-slant italic -underline 0 -overstrike 0"
def update_file_name(temp):
	date=datetime.now()
	time=date.strftime("%H.%M.%S %p")
	temp=temp.split('.')
	temp=temp[0]+'.'+time+'.'+temp[-1]
	return(temp)
def undo_changes(directories,files,base_path):
	directories=set(directories)
	for _ in directories:
		try:
			hold=os.chdir(os.path.realpath(_))
		except:
			pass
		else:
			for file in os.listdir(hold):
				if file in files:
					file_path=os.path.realpath(file)
					try:
						shutil.move(file_path,base_path)
					except:
						temp=update_file_name(file)
						os.rename(file,temp)
						file_path=os.path.realpath(temp)
						shutil.move(file_path,base_path)
			else:
				os.chdir(base_path)
	try:
		for _ in directories:
			if os.listdir(_)==[]:
				os.rmdir(_)
	except:
		pass
def Beautify_Folder():
	directories=[]
	files=[]
	folder_path=path_text.get()
	Button(myapp,text="Undo",font=font9,background="#177f5c",foreground="#ffffff",relief=GROOVE,cursor="hand2",command=lambda:undo_changes(directories,files,folder_path)).place(relx=0.817, rely=0.812, height=34, width=87)
	myapp.update()
	try:
		os.chdir(folder_path)
		for _ in os.listdir():
			if '.' in _:
				ext=(_.split('.')[-1]).upper()
				try:
					os.makedirs(ext)
				except:
					pass
				finally:
					directories.append(ext)
					dst_path=os.path.realpath(ext)
					src_path=os.path.realpath(_)
				try:
					shutil.move(src_path,dst_path)
					files.append(_)
				except:
					temp=update_file_name(_)
					os.rename(_,temp)
					src_path=os.path.realpath(temp)
					shutil.move(src_path,dst_path)
					files.append(temp)
			else:
				if(os.path.isdir(os.path.realpath(_))):
					directories.append(_)
	except:
		emyapp=Tk()
		emyapp.geometry("398x177+490+225")
		emyapp.title("Invalid Path")
		emyapp.resizable(0,0)
		Label(emyapp,text="Error",font=30,relief=GROOVE).place(relx=0.13, rely=0.17, height=41, width=304)
		Label(emyapp,text="Please provide a valid path",font=30,relief=GROOVE).place(relx=0.13, rely=0.56, height=41, width=304)
		emyapp.mainloop()
	else:
		current_folder=os.getcwd()
		emyapp=Tk()
		emyapp.geometry("398x177+490+225")
		emyapp.title("Beautified")
		emyapp.resizable(0,0)
		Label(emyapp,text="Success",font=30,relief=GROOVE).place(relx=0.13, rely=0.17, height=41, width=304)
		Label(emyapp,text="Folder "+os.path.basename(folder_path)+" is Beautified",font=30,relief=GROOVE).place(relx=0.13, rely=0.56, height=41, width=304)
		emyapp.mainloop()
Label(myapp,text="Enter The Path",font=font12,background="#136fd8",foreground="#ffffff").place(relx=0.07, rely=0.19, height=31, width=174)
Entry(myapp,font=font15,background="#ffff30",foreground="#000000",relief=GROOVE).place(relx=0.37, rely=0.19,height=30, relwidth=0.61)
Button(myapp,text='Beautify',font=font9,command=Beautify_Folder,background="#177f5c",foreground="#ffffff",relief=GROOVE,cursor="hand2").place(relx=0.35, rely=0.59, height=44, width=177)
Label(myapp,text="Once exited action can't be undone",font=font10,background="#136fd8",foreground="#54ff54").place(relx=0.18, rely=0.37, height=31, width=394)
path_text=StringVar()
path_entry=Entry(myapp,font=font15,textvariable=path_text,background="#ffff30",foreground="#000000",relief=GROOVE).place(relx=0.37, rely=0.19,height=30, relwidth=0.61)
myapp.mainloop()