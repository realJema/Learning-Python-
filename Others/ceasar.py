'''
[Name]
Ceasar Encryption
[Summaru]
Program encrypts the the user input using the the ceasar encryption cipher 
'''
###########################################################
# imports 
###########################################################
from tkinter import * 

###########################################################
# Variables 
###########################################################
loremIpsum = 'Queries or modifies the desired attributes for the current font. If no option is specified,\
returns a dictionary describing all the options and their values for fontname. If a single\
option is specified with no value, then it returns the current value of that attribute. If one or\
more option-value pairs are specified, then the method modifies the given named font to have\
the given values; in this case, all widgets using that font will redisplay themselves using the\
new attributes for the font.' # sample text 

dftFont = ('calibri', 10) # default font
cipher  = 'abcdefghijklmnopqrstuvwxyz' # alphabet with lowercase
cipher2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # alphabet with uppercase
cipherNum = '0123456789' # numbers 
key = 3 # the key of the cipher
###########################################################
# functions 
###########################################################
def encryption(phrase):
    'This is used to encrypt the arguments passed on to it'
    encrypted = '' # stores the encrypted text
    for char in phrase:# goes through all the characters in the argument
        try:# used to catch characters not include in cipher such as spaces which can't be encrypted
            #if...else used to encrypt capital letters and numbers too
            if char in cipher:
                encrypted += cipher[(cipher.index(char) + key) % 26]
            elif char in cipher2:
                encrypted += cipher2[(cipher2.index(char) + key) % 26]
            else:
                encrypted += cipherNum[(cipherNum.index(char) + key) % 10]
        except:
            encrypted += char 
    # setting the text in the decrypt label area
    encrpytText.delete("1.0", END) # clears input 
    decryptText.delete('1.0', END)
    decryptText.insert(END, encrypted)

def decryption(encryptedPhrase):
    'This is used to decrypt the arguments passed on to it'
    decrypted = '' # stores the decrypted text 
    for char in encryptedPhrase: 
        try: 
            if char in cipher:
                decrypted += cipher[(cipher.index(char) - key) % 26]
            elif char in cipher2:
                decrypted += cipher2[(cipher2.index(char) - key) % 26]
            else:
                decrypted += cipherNum[(cipherNum.index(char) - key) % 10]
        except: 
            decrypted += char 
    # Replaces the text in the encrypt area
    decryptText.delete('1.0', END)
    encrpytText.delete("1.0", END)
    encrpytText.insert(END, decrypted)

###########################################################
# Windows 
###########################################################
window = Tk()
window.title('Ceasar Encryption')
# window.geometry('800x500+200+200')# size and position of window
window.resizable(0,0)

###########################################################
# window frame content 
###########################################################
lftFrame = Frame(window, width=400)
rhtFrame  = Frame(window, width=400)

# lftFrame
lfttitle   = Label(lftFrame,  text='DECRYPTED', font=('Palatino Linotype', 12, 'bold')).pack(side=TOP, pady=5)
# encrpytText = Label(lftFrame,  text=loremIpsum,  bg='#acffff', font=dftFont, wraplength=350, height=15, justify=LEFT, textvariable=encryptctn).pack(side=TOP, padx=10, ipadx=5)
encrpytText = Text(lftFrame, font=dftFont, borderwidth=1, bg='#acffff', width=50, height=20, relief=FLAT)
encrpytText.pack(side=TOP, padx=10)
encryptbtn = Button(lftFrame, text='Encrypt',   bg='gainsboro', font=dftFont, borderwidth=2, relief=FLAT, command=lambda: encryption(encrpytText.get("1.0","end-1c"))).pack(side=TOP, pady=30, ipady=2, ipadx=20)

# rhtFrame
lfttitle   = Label(rhtFrame,  text='ENCRYPTED', font=('Palatino Linotype', 12, 'bold')).pack(side=TOP, pady=5)
# decryptText = Label(rhtFrame,  text=loremIpsum,  bg='#ffbbbb', font=dftFont, wraplength=350, height=15, justify=LEFT, textvariable=decryptctn).pack(side=TOP, padx=10, ipadx=5)
decryptText = Text(rhtFrame, font=dftFont, borderwidth=1, bg='#ffbbbb', width=50, height=20, relief=FLAT)
decryptText.pack(side=TOP, padx=10)
decryptbtn = Button(rhtFrame, text='Decrypt',   bg='gainsboro', font=dftFont, borderwidth=2, relief=FLAT, command=lambda: decryption(decryptText.get("1.0","end-1c"))).pack(side=TOP, pady=30, ipady=2, ipadx=20)

lftFrame.pack(side=LEFT, fill=Y, padx=5, pady=5)
rhtFrame.pack(side=RIGHT, fill=Y, padx=5, pady=5)



###########################################################
# main 
###########################################################
window.mainloop()