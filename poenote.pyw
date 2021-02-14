import tkinter

#setup our root process
root = tkinter.Tk()
root.title('PoE Notes')

#create our input field
userNote = tkinter.Entry(root, width=55, borderwidth=5)
userNote.pack()

#create our frame widget
frameWidget = tkinter.Frame(root)

#create function to call on launch- reads file, splits into array, creates labels for each line
def onStart():
	fileCreate = open('./one.txt', 'a')
	fileCreate.close()
	fileRead = open('./one.txt', 'r')
	fileArray = fileRead.read().split('\n')
	for x in fileArray:
		frameWidget.pack()
		tkinter.Label(frameWidget, text=x).pack()

#calls the startup function
onStart()

#create function to add user input to the end of the array and save it to the file. then adds a label with the user input to the end
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
		tkinter.Label(frameWidget, text=userText).pack()

#creates a function to remove a matching array object with a user input, then redeploys the labels
def Remove():
	userText = userNote.get()
	fileRead = open(f'./{tab}.txt', 'r')
	fileArray = fileRead.read().split('\n')
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
			tkinter.Label(frameWidget, text=x).pack(side='bottom')

#creates a function that uses the value passed in from thr lambda functions in the tabButtons to then set the  tab global variable and then reset display
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
		tkinter.Label(frameWidget, text=x).pack(side='bottom')
	

#create our buttons 
saveButton = tkinter.Button(root, width=47, borderwidth=5, text="Save", command=Save)
saveButton.pack()
removeButton = tkinter.Button(root, width=47, borderwidth=5, text='Remove', command=Remove)
removeButton.pack()
tabOne = tkinter.Button(root, width=10, borderwidth=5, text="Page 1", command=lambda *args: TabSelect('one'))
tabOne.pack(side='left')
tabTwo = tkinter.Button(root, width=10, borderwidth=5, text="Page 2", command=lambda *args: TabSelect('two'))
tabTwo.pack(side='left')
tabThree = tkinter.Button(root, width=10, borderwidth=5, text="Page 3", command=lambda *args: TabSelect('three'))
tabThree.pack(side='left')
tabFour = tkinter.Button(root, width=10, borderwidth=5, text="Page 4", command=lambda *args: TabSelect('four'))
tabFour.pack(side='left')

#create our mainloop
root.mainloop()