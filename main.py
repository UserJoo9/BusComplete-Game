import threading
from customtkinter import *
from tkinter import messagebox

from BusComplete import BusComplete

bc = BusComplete()


def Window1():
    global MasterLitter, MasterLable, MasterButton
    MasterLable = CTkLabel(top, text='Master Litter', font=('arial', 18, 'bold'))
    MasterLable.pack(pady=5)
    MasterLitter = CTkEntry(top, width=200, font=('arial', 18, 'bold'))
    MasterLitter.pack(pady=8)
    MasterLitter.focus_set()
    MasterLitter.bind('<Return>', setMasterLitter)
    MasterButton = CTkButton(top, text='Continue', font=('arial', 12, 'bold'), command=setMasterLitter)
    MasterButton.pack(pady=5)
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
    MasterPlay = CTkLabel(top, text=f'The Master Litter: {bc.getMasterLitter()}', font=('arial', 14, 'bold'))
    MasterPlay.pack(pady=5)
    Separator = CTkLabel(top, text='-' * 100)
    Separator.pack(pady=5)
    BoyName = CTkLabel(top, text='Boy', font=('arial', 15, 'bold'))
    BoyName.pack(pady=5)
    BoyEntry = CTkEntry(top, font=('arial', 14), width=200)
    BoyEntry.pack(pady=5)
    BoyEntry.bind('<Return>', revision)
    BoyEntry.bind('<Escape>', BackToMain)
    BoyEntry.focus_set()
    GirlName = CTkLabel(top, text='Girl', font=('arial', 15, 'bold'))
    GirlName.pack(pady=5)
    GrilEntry = CTkEntry(top, font=('arial', 14), width=200)
    GrilEntry.pack(pady=5)
    GrilEntry.bind('<Return>', revision)
    GrilEntry.bind('<Escape>', BackToMain)
    PlantName = CTkLabel(top, text='Plant', font=('arial', 15, 'bold'))
    PlantName.pack(pady=5)
    PlantEntry = CTkEntry(top, font=('arial', 14), width=200)
    PlantEntry.pack(pady=5)
    PlantEntry.bind('<Return>', revision)
    PlantEntry.bind('<Escape>', BackToMain)
    Inanimate = CTkLabel(top, text='Inanimate', font=('arial', 15, 'bold'))
    Inanimate.pack(pady=5)
    InanimateEntry = CTkEntry(top, font=('arial', 14), width=200)
    InanimateEntry.pack(pady=5)
    InanimateEntry.bind('<Return>', revision)
    InanimateEntry.bind('<Escape>', BackToMain)
    Animal = CTkLabel(top, text='Animal', font=('arial', 15, 'bold'))
    Animal.pack(pady=5)
    AnimalEntry = CTkEntry(top, font=('arial', 14), width=200)
    AnimalEntry.pack(pady=5)
    AnimalEntry.bind('<Return>', revision)
    AnimalEntry.bind('<Escape>', BackToMain)
    Country = CTkLabel(top, text='Country', font=('arial', 15, 'bold'))
    Country.pack(pady=5)
    CountryEntry = CTkEntry(top, font=('arial', 14), width=200)
    CountryEntry.pack(pady=5)
    CountryEntry.bind('<Return>', revision)
    CountryEntry.bind('<Escape>', BackToMain)
    RevisionButton = CTkButton(top, text='Continue', font=('arial', 15, 'bold'), command=revision)
    RevisionButton.pack(pady=5)
    RevisionButton.bind('<Return>', revision)
    BackButton = CTkButton(top, text='Back', font=('arial', 15, 'bold'), command=BackToMain)
    BackButton.pack(pady=10)
    BackButton.bind('<Escape>', BackToMain)


def revision(*args):
    global MasterPlay, BackButton, RevisionButton, Separator, BoyName, BoyEntry, GirlName, GrilEntry
    global PlantName, PlantEntry, Animal, AnimalEntry, Inanimate, InanimateEntry, Country, CountryEntry
    global score, totalScore, ModifyButton, ModifyButton1, FinishButton
    global boyLable, girlLable, plantLable, animalLable, inanimateLable, countryLable
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

    score = CTkLabel(top, text=f'Score: {bc.getScore()}', font=('arial', 15, 'bold'))
    score.pack(pady=5)
    bc.sumTotal(bc.getScore())
    totalScore = CTkLabel(top, text=f'Total Score: {bc.getTotalScore()}', font=('arial', 18, 'bold'))
    totalScore.pack(pady=5)
    ModifyButton = CTkButton(top, text='-5', font=('arial', 16, 'bold'), command=ModifyScore)
    ModifyButton.pack(pady=5)
    ModifyButton1 = CTkButton(top, text='+5', font=('arial', 16, 'bold'), command=ModifyScorePlus)
    ModifyButton1.pack(pady=5)
    FinishButton = CTkButton(top, text='Finish', font=('arial', 16, 'bold'), command=Home)
    FinishButton.pack(pady=5)
    FinishButton.focus_set()
    ModifyButton.bind('<Key-m>', ModifyScore)
    FinishButton.bind('<Return>', Home)

    boyLable = CTkLabel(top, text=f'Boy: {boy}', font=('arial', 14, 'bold'))
    boyLable.pack(pady=5)
    girlLable = CTkLabel(top, text=f'Girl: {girl}', font=('arial', 14, 'bold'))
    girlLable.pack(pady=5)
    plantLable = CTkLabel(top, text=f'Plant: {plant}', font=('arial', 14, 'bold'))
    plantLable.pack(pady=5)
    animalLable = CTkLabel(top, text=f'Animal: {animal}', font=('arial', 14, 'bold'))
    animalLable.pack(pady=5)
    inanimateLable = CTkLabel(top, text=f'Inanimate: {inanimate}', font=('arial', 14, 'bold'))
    inanimateLable.pack(pady=5)
    countryLable = CTkLabel(top, text=f'Country: {country}', font=('arial', 14, 'bold'))
    countryLable.pack(pady=5)


def Table():
    global score1, totalScore1
    toplivil = CTkToplevel(top)
    toplivil.geometry("400x100")
    toplivil.title('Score Table')
    toplivil.resizable(False, False)
    score1 = CTkLabel(toplivil, text=f'Score: {bc.getScore()}', font=('arial', 18, 'bold'))
    score1.pack(pady=10)
    totalScore1 = CTkLabel(toplivil, text=f'Total Score: {bc.getTotalScore()}', font=('arial', 20, 'bold'))
    totalScore1.pack(pady=10)


def UpdateTable():
    global score1, totalScore1
    score1.configure(text=f'Score: {bc.getScore()}')
    totalScore1.configure(text=f'Total Score: {bc.getTotalScore()}')


def ModifyScore(*args):
    global score, totalScore
    if bc.getScore() <= 0:
        messagebox.showerror('Error', "Score Can't Be Negative!")
    else:
        bc.modifyScoreMinus()
        bc.ModifyTotalScoreMinus()
        score.configure(text=f'Score: {bc.getScore()}')
        totalScore.configure(text=f'Total Score: {bc.getTotalScore()}')
        UpdateTable()


def ModifyScorePlus(*args):
    global score, totalScore
    bc.modifyScorePlus()
    bc.ModifyTotalScorePlus()
    score.configure(text=f'Score: {bc.getScore()}')
    totalScore.configure(text=f'Total Score: {bc.getTotalScore()}')
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


top = CTk()
top.title('Bus Complete')
top.resizable(False, False)
top.iconbitmap()

l1 = CTkLabel(top, text='Bus Complete', font=('arial', 25, 'bold'), width=400, fg_color="black")
l1.pack(ipady=15)

Window1()
TableThread = threading.Thread(target=Table)
TableThread.start()

top.mainloop()
