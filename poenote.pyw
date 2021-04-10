import tkinter
from PIL import ImageTk,Image 

'''
To Do
-The Button Stuff- figure out how to make dynamic button lists--- maybe dont do this after all?
-Radio buttons for tabs
-customizeable tab names
'''


#setup our root process
root = tkinter.Tk()
root.title('PoE Notes')

#create our input field
userNote = tkinter.Entry(root, width=60, borderwidth=5)
userNote.pack()

#create our frame widget
frameWidget = tkinter.Frame(root)

#create function to call on launch- reads file, splits into array, creates text-fields for each line
def onStart():
	fileCreate = open('./one.txt', 'a')
	fileCreate.close()
	fileRead = open('./one.txt', 'r')
	fileArray = fileRead.read().split('\n')
	for x in fileArray:
		frameWidget.pack()
		w = tkinter.Text(frameWidget, height=1, width=40, borderwidth=0)
		w.configure(bg=root.cget('bg'), relief="flat", state='disabled')
		w.insert(1.0, x)
		w.pack()


#calls the startup function
onStart()

#create function to add user input to the end of the array and save it to the file. then adds a text-field with the user input to the end
def Save():
	userText = userNote.get()
	fileRead = open(f'./{tab}.txt', 'r')
	fileArray = fileRead.read().split('\n')
	if userText == "":
		pass
	else:
		fileArray.append(userText)
		arrayJoin = '\n'.join(fileArray)
		fileAppend = open(f'./{tab}.txt', 'w')
		fileAppend.write(arrayJoin)
		fileAppend.close
		frameWidget.pack()
		w = tkinter.Text(frameWidget, height=1, width=40, borderwidth=0)
		w.insert(1.0, userText)
		w.configure(bg=root.cget('bg'), relief="flat", state='disabled')
		w.pack()

#creates a function to remove a matching array object with a user input, then redeploys the text-fields
def Remove():
	userText = userNote.get()
	fileRead = open(f'./{tab}.txt', 'r')
	fileArray = fileRead.read().split('\n')
	w = tkinter.Text(frameWidget, height=1, width=40, borderwidth=0)
	if userText in fileArray:
		fileArray.remove(userText)
		arrayJoin = '\n'.join(fileArray)
		fileAppend = open(f'./{tab}.txt', 'w')
		fileAppend.write(arrayJoin)
		fileAppend.close
		packDelete = frameWidget.pack_slaves()
		for l in packDelete:
			l.destroy()
		for x in fileArray:
			frameWidget.pack()
			w = tkinter.Text(frameWidget, height=1, width=40, borderwidth=0)
			w.insert(1.0, x)
			w.configure(bg=root.cget('bg'), relief="flat", state='disabled')
			w.pack()

#creates a function that uses the value passed in from the lambda functions in the tabButtons to then set the tab global variable and then reset display
def TabSelect(value):
	global tab
	tab = value
	userText = userNote.get()
	fileCreate = open(f'./{tab}.txt', 'a')
	fileCreate.close()
	fileRead = open(f'./{tab}.txt', 'r')
	fileArray =  fileRead.read().split('\n')
	packDelete = frameWidget.pack_slaves()
	for l in packDelete:
		l.destroy()
	for x in fileArray:
		frameWidget.pack()
		w = tkinter.Text(frameWidget, height=1, width=40, borderwidth=0)
		w.insert(1.0, x)
		w.configure(bg=root.cget('bg'), relief="flat", state='disabled')
		w.pack()

#creates a function that deletes all previous texts and then creates a label with the supplied image
def ImageViewer(value):
	packDelete =  frameWidget.pack_slaves()
	for l in packDelete:
		l.destroy()
	nameImage = f'{value}.png'
	image1 = Image.open(nameImage)
	test = ImageTk.PhotoImage(image1)
	label1 = tkinter.Label(frameWidget, image=test)
	label1.image = test
	label1.pack()

	
	
	
#create frames for button positions
filler =  tkinter.Frame(root)
filler.pack(side='top')
filler2 = tkinter.Frame(root)
filler2.pack()
filler3 = tkinter.Frame(root)
filler3.pack()


#create our buttons 
saveButton = tkinter.Button(filler, width=50, borderwidth=5, text="Save", command=Save)
saveButton.pack()
removeButton = tkinter.Button(filler, width=50, borderwidth=5, text='Remove', command=Remove)
removeButton.pack()

tabOne = tkinter.Button(filler2, width=11, borderwidth=5, text="Page 1", command=lambda *args: TabSelect('one'))
tabOne.pack(side='left')
tabTwo = tkinter.Button(filler2, width=11, borderwidth=5, text="Page 2", command=lambda *args: TabSelect('two'))
tabTwo.pack(side='left')
tabThree = tkinter.Button(filler2, width=10, borderwidth=5, text="Page 3", command=lambda *args: TabSelect('three'))
tabThree.pack(side='left')
tabFour = tkinter.Button(filler2, width=11, borderwidth=5, text="Page 4", command=lambda *args: TabSelect('four'))
tabFour.pack(side='left')

imageTab1 = tkinter.Button(filler3, width=24, borderwidth=5, text="Uber Lab", command=lambda *args: ImageViewer('lab'))
imageTab1.pack(side='left')
imageTab2 = tkinter.Button(filler3, width=24, borderwidth=5, text="Leveling Crafts", command=lambda *args: ImageViewer('leveling'))
imageTab2.pack(side='left')

#create our mainloop
root.mainloop()