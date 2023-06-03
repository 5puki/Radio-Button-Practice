from tkinter import *

socials = ["Instagram","Facebook","Youtube"]
def pick_social():
    if(x.get() == 0):
        print("You have posted on Instagram")
    elif(x.get() == 1):
        print("You have posted on Facebook")
    elif(x.get() == 2):
        print("You have posted on Youtube")
    else:
        print("You haven't posted today.")

window = Tk()

x = IntVar()

logo = PhotoImage(file="like.png")
window.iconphoto(True,logo)
window.title("Platform posting")

instagramlogo = PhotoImage(file="iglogo.png")
facebooklogo = PhotoImage(file="facebook.png")
youtubelogo = PhotoImage(file="ytlogo.png")
logo_picker = [instagramlogo,facebooklogo,youtubelogo]



for index in range(len(socials)):
    radiobutton = Radiobutton(window,
                              text = socials[index],
                              variable = x,
                              value = index,
                              command = pick_social,
                              padx = 30,
                              pady = 20,
                              indicatoron = 0,
                              width = 100,
                              image = logo_picker[index],
                              compound = CENTER)
    radiobutton.pack(anchor = W)

window.mainloop()