import tkinter

#setup our root process
root = tkinter.Tk()
root.title('PoE Notes')

#create our input field
userNote = tkinter.Entry(root, width=50, borderwidth=5)
userNote.pack()

#create our frame widget
frameWidget = tkinter.Frame(root)

#create function to call on launch- reads file, splits into array, creates labels for each line
def onStart():
	fileRead = open('./notes.txt', 'r')
	fileArray = fileRead.read().split('\n')
	for x in fileArray:
		frameWidget.pack()
		tkinter.Label(frameWidget, text=x).pack()

#calls the startup function
onStart()

#create function to add user input to the end of the array and save it to the file. then adds a label with the user input to the end
def Save():
	userText = userNote.get()
	fileRead = open('./notes.txt', 'r')
	fileArray = fileRead.read().split('\n')
	if userText == "":
		pass
	else:
		fileArray.append(userText)
		arrayJoin = '\n'.join(fileArray)
		fileAppend = open('./notes.txt', 'w')
		fileAppend.write(arrayJoin)
		fileAppend.close
		frameWidget.pack()
		tkinter.Label(frameWidget, text=userText).pack()

#creates a function to remove a matching array object with a user input, then redeploys the labels
def Remove():
	userText = userNote.get()
	fileRead = open('./notes.txt', 'r')
	fileArray = fileRead.read().split('\n')
	if userText in fileArray:
		fileArray.remove(userText)
		arrayJoin = '\n'.join(fileArray)
		fileAppend = open('./notes.txt', 'w')
		fileAppend.write(arrayJoin)
		fileAppend.close
		packDelete = frameWidget.pack_slaves()
		for l in packDelete:
			l.destroy()
		for x in fileArray:
			frameWidget.pack()
			tkinter.Label(frameWidget, text=x).pack()

#create our buttons 
saveButton = tkinter.Button(root, width=40, borderwidth=5, text="Save", command=Save)
saveButton.pack()
removeButton = tkinter.Button(root, width=40, borderwidth=5, text='Remove', command=Remove)
removeButton.pack()

#create our mainloop
root.mainloop()