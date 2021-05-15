from tkinter import *
import random
from tkinter import messagebox

words=['the','apple', 'mango','tanish','be','to','have','not','about','would','which','time','know','our','people','just','look','after','fall','house', 'grapes', 'fan', 'laptop', 'mobile', 'hat', 'rat','boy','next','paper', 'follow', 'school', 'head', 'watch', 'wood','just','often', 'point','began','who', 'answer','year', 'mother', 'eat', 'are', 'could','song','put','air','study','before','study','car','through','pen','pencil','key','charger', 'keyboard', 'mouse', 'dell', 'mat', 'bottle', 'guitar', 'marker', 'plate', 'enter', 'return', 'band', 'airtel', 'two', 'hundred', 'intel', 'lenovo', 'track', 'right', 'write', 'left', 'coin', 'money', 'medal', 'whatsapp', 'facebook', 'bat', 'run', 'tools', 'navigate', 'view', 'edit', 'file', 'window', 'computer', 'help', 'india']
def labelSlider():
    global count, sliderWords
    text = 'Welcome To The Game - By Tanish Gupta'
    if(count>= len(text)):
        count = 0
        sliderWords = ''
    sliderWords += text[count]
    count += 1
    fontlabel.configure(text=sliderWords)
    fontlabel.after(150, labelSlider)

def time():
    global timeleft, score, miss
    if(timeleft>= 11):
        pass
    else:
        timerlabelcount.configure(fg='red')
    if(timeleft > 0):
        timeleft -= 1
        timerlabelcount.configure(text=timeleft)
        timerlabelcount.after(1000, time)
    else:
        gameplaydetaillabel.configure(text='Hit = {} | Miss = {} | Total Score = {}'.format(score,miss,score-miss))
        gameplaydetaillabel.place(x=100, y=450)
        rr = messagebox.askretrycancel('Notification', 'To play again, Hit retry button')
        if(rr == True):
            score = 0
            miss = 0
            timeleft = 60
            timerlabelcount.configure(text=timeleft)
            wordentry.configure(text=words[0])
            scorelabelcount.configure(text=score)
def startGame(eVent):
    if(wordentry.get() == wordlabel['text']):
        gameplaydetaillabel.configure(text='')
        if (timeleft == 60):
            time()
        global score,miss
        score += 1
        scorelabelcount.configure(text=score)
        print('SCORE:', score)
    else:
        miss += 1
    print(wordentry.get())
    wordentry.delete(0, END)
    random.shuffle(words)
    wordlabel.configure(text=words[0])

#----------Root Method--------------#
root = Tk()
root.geometry('800x600+300+100')
root.configure(bg='powder blue')
root.title("Typing Speed")
root.iconbitmap('icon.ico')
#----------variables--------------#
score = 0
timeleft= 60
count= 0
miss = 0
sliderWords = ''


#----------Label Methods--------------#
fontlabel = Label(root, text='', font=('arial', 25, 'italic bold'), bg='powder blue', fg='red', width=40)
fontlabel.place(x=40, y=10)
labelSlider()
random.shuffle(words)
wordlabel = Label(root, text=words[0], font=('arial', 35, 'italic bold'), bg='powder blue', fg='red')
wordlabel.place(x=340, y=200)

scorelabel= Label(root, text='Your Score:', font=('arial', 30, 'italic bold'), bg='powder blue', fg='blue')
scorelabel.place(x=40, y=100)

scorelabelcount= Label(root, text=score, font=('arial', 30, 'italic bold'), bg='powder blue', fg='yellow')
scorelabelcount.place(x=280, y=100)

timerlabel = Label(root, text='Time Left:', font=('arial', 30, 'italic bold'), bg='powder blue', fg='blue')
timerlabel.place(x=500, y=100)

timerlabelcount= Label(root, text=timeleft, font=('arial', 30, 'italic bold'), bg='powder blue', fg='blue')
timerlabelcount.place(x=700, y=100)

gameplaydetaillabel = Label(root, text ='Type word and Hit enter', font=('arial', 30, 'italic bold'), bg='powder blue', fg='dark grey')
gameplaydetaillabel.place(x=130, y=450)
#------------Entry Method-------------
wordentry= Entry(root, font=('arial', 25, 'italic bold'), bd=10, justify='center')
wordentry.place(x=230, y=300)
wordentry.focus_set()
#----------Mainloop------------------
root.bind('<Return>', startGame)
root.mainloop()