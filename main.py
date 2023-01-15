import threading
from tkinter import *
from tkinter import messagebox

from BusComplete import BusComplete

bc = BusComplete()


def Window1():
    global MasterLitter, MasterLable, MasterButton
    top.geometry('400x250')
    MasterLable = Label(top, text='Master Litter', font=('arial 18 bold'))
    MasterLable.pack()
    MasterLitter = Entry(top, width=20, font=('arial 18 bold'))
    MasterLitter.pack(pady=8)
    MasterLitter.focus_set()
    MasterLitter.bind('<Return>', setMasterLitter)
    MasterButton = Button(top, text='Continue', width=10, font=('arial 12 bold'), pady=8, activebackground='gray',
                          activeforeground='#33e586', command=setMasterLitter)
    MasterButton.pack()
    MasterButton.bind('<Return>', setMasterLitter)


def setMasterLitter(*args):
    global MasterLitter, MasterLable, MasterButton, status
    ML = str(MasterLitter.get())
    if len(ML) > 1:
        messagebox.showerror('Error', 'Master Litter Must Be 1 Litter Only!', parent=top)
    elif len(ML) < 1:
        messagebox.showerror('Error', "Master Litter Can't Empty!", parent=top)
    elif not ML.isalpha():
        messagebox.showerror('Error', "Master Litter Must Be Char!", parent=top)
    else:
        bc.setMasterLitter(ML)
        MasterLitter.delete('0', 'end')
        MasterLable.destroy()
        MasterLitter.destroy()
        MasterButton.destroy()
        Window2()


def Window2():
    global MasterPlay, BackButton, RevisionButton, Separator, BoyName, BoyEntry, GirlName, GrilEntry
    global PlantName, PlantEntry, Animal, AnimalEntry, Inanimate, InanimateEntry, Country, CountryEntry
    top.geometry('400x600')
    MasterPlay = Label(top, text=f'The Master Litter: {bc.getMasterLitter()}', font=('arial 14 bold'))
    MasterPlay.pack()
    Separator = Label(top, text='-' * 100, font=('arial '))
    Separator.pack()
    BoyName = Label(top, text='Boy', font=('arial 12 bold'), pady=5)
    BoyName.pack()
    BoyEntry = Entry(top, font=('arial 14'), width=30)
    BoyEntry.pack(pady=5)
    BoyEntry.bind('<Return>', revision)
    BoyEntry.bind('<Escape>', BackToMain)
    BoyEntry.focus_set()
    GirlName = Label(top, text='Girl', font=('arial 12 bold'), pady=5)
    GirlName.pack()
    GrilEntry = Entry(top, font=('arial 14'), width=30)
    GrilEntry.pack(pady=5)
    GrilEntry.bind('<Return>', revision)
    GrilEntry.bind('<Escape>', BackToMain)
    PlantName = Label(top, text='Plant', font=('arial 12 bold'), pady=5)
    PlantName.pack()
    PlantEntry = Entry(top, font=('arial 14'), width=30)
    PlantEntry.pack(pady=5)
    PlantEntry.bind('<Return>', revision)
    PlantEntry.bind('<Escape>', BackToMain)
    Inanimate = Label(top, text='Inanimate', font=('arial 12 bold'), pady=5)
    Inanimate.pack()
    InanimateEntry = Entry(top, font=('arial 14'), width=30)
    InanimateEntry.pack(pady=5)
    InanimateEntry.bind('<Return>', revision)
    InanimateEntry.bind('<Escape>', BackToMain)
    Animal = Label(top, text='Animal', font=('arial 12 bold'), pady=5)
    Animal.pack()
    AnimalEntry = Entry(top, font=('arial 14'), width=30)
    AnimalEntry.pack(pady=5)
    AnimalEntry.bind('<Return>', revision)
    AnimalEntry.bind('<Escape>', BackToMain)
    Country = Label(top, text='Country', font=('arial 12 bold'), pady=5)
    Country.pack()
    CountryEntry = Entry(top, font=('arial 14'), width=30)
    CountryEntry.pack(pady=5)
    CountryEntry.bind('<Return>', revision)
    CountryEntry.bind('<Escape>', BackToMain)
    RevisionButton = Button(top, text='Continue', font='arial 12 bold', width=10, command=revision)
    RevisionButton.pack()
    RevisionButton.bind('<Return>', revision)
    BackButton = Button(top, text='Back', font='arial 12 bold', width=10, command=BackToMain)
    BackButton.pack(pady=10)
    BackButton.bind('<Escape>', BackToMain)


def revision(*args):
    global MasterPlay, BackButton, RevisionButton, Separator, BoyName, BoyEntry, GirlName, GrilEntry
    global PlantName, PlantEntry, Animal, AnimalEntry, Inanimate, InanimateEntry, Country, CountryEntry
    global score, totalScore, ModifyButton, ModifyButton1, FinishButton
    global boyLable, girlLable, plantLable, animalLable, inanimateLable, countryLable
    top.geometry('400x400')
    boy = BoyEntry.get()
    bc.setBoyName(boy)
    girl = GrilEntry.get()
    bc.setGirlName(girl)
    plant = PlantEntry.get()
    bc.setPlaneName(plant)
    animal = AnimalEntry.get()
    bc.setAnimal(animal)
    inanimate = InanimateEntry.get()
    bc.setInanimate(inanimate)
    country = CountryEntry.get()
    bc.setCountry(country)
    bc.Revision()

    MasterPlay.destroy()
    BackButton.destroy()
    RevisionButton.destroy()
    Separator.destroy()
    BoyName.destroy()
    BoyEntry.destroy()
    GirlName.destroy()
    GrilEntry.destroy()
    PlantName.destroy()
    PlantEntry.destroy()
    Animal.destroy()
    AnimalEntry.destroy()
    Inanimate.destroy()
    InanimateEntry.destroy()
    Country.destroy()
    CountryEntry.destroy()

    score = Label(top, text=f'Score: {bc.getScore()}', font=('arial 12 bold'), fg='red', pady=5)
    score.pack()
    bc.sumTotal(bc.getScore())
    totalScore = Label(top, text=f'Total Score: {bc.getTotalScore()}', font=('arial 15 bold'), fg='#33e586', pady=5)
    totalScore.pack()
    ModifyButton = Button(top, text='-5', width=25, font=('arial 12 bold'), command=ModifyScore)
    ModifyButton.pack(pady=5)
    ModifyButton1 = Button(top, text='+5', width=25, font=('arial 12 bold'), command=ModifyScorePlus)
    ModifyButton1.pack(pady=5)
    FinishButton = Button(top, text='Finish', width=25, font=('arial 12 bold'), command=Home)
    FinishButton.pack(pady=5)
    FinishButton.focus_set()
    ModifyButton.bind('<Key-m>', ModifyScore)
    FinishButton.bind('<Return>', Home)

    boyLable = Label(top, text=f'Boy: {boy}', font=('arial 10 bold'))
    boyLable.pack()
    girlLable = Label(top, text=f'Girl: {girl}', font=('arial 10 bold'))
    girlLable.pack()
    plantLable = Label(top, text=f'Plant: {plant}', font=('arial 10 bold'))
    plantLable.pack()
    animalLable = Label(top, text=f'Animal: {animal}', font=('arial 10 bold'))
    animalLable.pack()
    inanimateLable = Label(top, text=f'Inanimate: {inanimate}', font=('arial 10 bold'))
    inanimateLable.pack()
    countryLable = Label(top, text=f'Country: {country}', font=('arial 10 bold'))
    countryLable.pack()


def Table():
    global score1, totalScore1
    toplivil = Toplevel(top)
    toplivil.geometry('300x100')
    toplivil.title('Score Table')
    toplivil.resizable(False, False)
    score1 = Label(toplivil, text=f'Score: {bc.getScore()}', font=('arial 12 bold'), fg='red', pady=5)
    score1.pack()
    totalScore1 = Label(toplivil, text=f'Total Score: {bc.getTotalScore()}', font=('arial 15 bold'), fg='#33e586',
                        pady=5)
    totalScore1.pack()

    toplivil.mainloop()


def UpdateTable():
    global score1, totalScore1
    score1['text'] = f'Score: {bc.getScore()}'
    score1['font'] = 'arial 12 bold'
    totalScore1['text'] = f'Total Score: {bc.getTotalScore()}'
    totalScore1['font'] = 'arial 15 bold'


def ModifyScore(*args):
    global score, totalScore
    if bc.getScore() <= 0:
        messagebox.showerror('Error', "Score Can't Be Negative!")
    else:
        bc.modifyScoreMinus()
        bc.ModifyTotalScoreMinus()
        score['text'] = f'Score: {bc.getScore()}'
        score['font'] = 'arial 12 bold'
        totalScore['text'] = f'Total Score: {bc.getTotalScore()}'
        totalScore['font'] = 'arial 15 bold'
        UpdateTable()


def ModifyScorePlus(*args):
    global score, totalScore
    bc.modifyScorePlus()
    bc.ModifyTotalScorePlus()
    score['text'] = f'Score: {bc.getScore()}'
    score['font'] = 'arial 12 bold'
    totalScore['text'] = f'Total Score: {bc.getTotalScore()}'
    totalScore['font'] = 'arial 15 bold'
    UpdateTable()


def Home(*args):
    global score, totalScore, ModifyButton, ModifyButton1, FinishButton
    global boyLable, girlLable, plantLable, animalLable, inanimateLable, countryLable
    score.destroy()
    totalScore.destroy()
    ModifyButton.destroy()
    ModifyButton1.destroy()
    FinishButton.destroy()
    boyLable.destroy()
    girlLable.destroy()
    plantLable.destroy()
    animalLable.destroy()
    inanimateLable.destroy()
    countryLable.destroy()
    Window1()
    UpdateTable()


def BackToMain(*args):
    global MasterPlay, BackButton, RevisionButton, Separator, BoyName, BoyEntry, GirlName, GrilEntry
    global PlantName, PlantEntry, Animal, AnimalEntry, Inanimate, InanimateEntry, Country, CountryEntry
    MasterPlay.destroy()
    BackButton.destroy()
    RevisionButton.destroy()
    Separator.destroy()
    BoyName.destroy()
    BoyEntry.destroy()
    GirlName.destroy()
    GrilEntry.destroy()
    PlantName.destroy()
    PlantEntry.destroy()
    Animal.destroy()
    AnimalEntry.destroy()
    Inanimate.destroy()
    InanimateEntry.destroy()
    Country.destroy()
    CountryEntry.destroy()
    Window1()


top = Tk()
top.geometry('400x300')
top.title('Bus Complete')
top.resizable(False, False)
top.iconbitmap()

l1 = Label(top, text='Bus Complete', fg='#33e586', font=('arial 25 bold'), bg='gray', width=400)
l1.pack()

Window1()
TableThread = threading.Thread(target=Table)
TableThread.start()

top.mainloop()
