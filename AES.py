from tkinter import *
from tkinter import messagebox
import pybase64

window = Tk()

window.title('AES Encypt/Decrypt Application')
window.geometry("500x400")
window['bg'] = '#D9ECFC'

#Function to clear contents when clear button is clicked
def Clear():
    myText.delete(1.0, END)
    myKey.delete(0, END)

#Function to encrypt string
def Encrypt():
    #get string
    message = myText.get(1.0, END)
    myText.delete(1.0, END)
    #get key
    password = myKey.get()
    if len(password) >= 8:
        #if password is 5 characters or longer, encrypt the string
        message = message.encode("ascii")
        message = pybase64.b64encode(message)
        message = message.decode("ascii")
        myText.insert(END, message)
    else:
        messagebox.showwarning("Error", "Password length is too short")

def Decrypt():
    #get encrypted string
    message = myText.get(1.0, END)
    myText.delete(1.0, END)
    #get key
    password = myKey.get()
    if len(password) >= 8:
        #decode encrypted string
        message = message.encode("ascii")
        message = pybase64.b64decode(message)
        message = message.decode("ascii")
        myText.insert(END, message)
    else:
        messagebox.showwarning("Error", "Incorrect Password")

myFrame = Frame(window)
myFrame.pack(pady=20)

encryptButton = Button(myFrame, text = "Encrypt", font = ("MS UI Gothic", 12),bg = "#D9ECFC" , command=Encrypt)
encryptButton.grid(row=0, column=0)
decryptButton = Button(myFrame, text = "Decrypt", font = ("MS UI Gothic", 12), bg = "#D9ECFC" , command=Decrypt)
decryptButton.grid(row=0, column=1)
clearButton = Button(myFrame, text = "Clear", font = ("MS UI Gothic", 12), bg = "#D9ECFC", command=Clear)
clearButton.grid(row=0, column=2)

encryptLabel = Label(window, text="Text to Encrypt/Decrypt", font = ("MS UI Gothic", 14), bg = "#D9ECFC")
encryptLabel.pack()
myText = Text(window, width = 57, height = 10, bg = "#81AFCE", fg = "#FFFFFF")
myText.pack(pady=10)

keyLabel = Label(window, text="Enter your key", font = ("MS UI Gothic", 14), bg = "#D9ECFC")
keyLabel.pack()
myKey = Entry(window, font=("MS UI Gothic", 13), width = 35, show = "*", bg = "#81AFCE", fg = "#FFFFFF")
myKey.pack(pady=10)


window.mainloop()