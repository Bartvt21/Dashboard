from Reisplanner.reisFuncties import *


def planAndDraw():
    'takes the stations and draws the reismogelijkheden'
    travelList = []  # list for storing all the reismogelijkheden
    beginStation = station1.get()  # getting the begin station
    eindStation = station2.get()  # getting the end station
    response = reisPlannen(beginStation, eindStation)

    # loops over every reisMogelijkheid and writes it to its own class
    for index in response["ReisMogelijkheden"]["ReisMogelijkheid"]:
        travelList.append(ReisInfo(beginStation, eindStation, index["GeplandeVertrekTijd"][11:16],
                                   index["GeplandeAankomstTijd"][11:16], index["AantalOverstappen"],
                                   index["GeplandeReisTijd"]))
    # loops over every object and print its own frame with info
    for reis in travelList[0:5]:
        reis.writeInfo(reisAdviezen1)


# Drawing the Main GUI
root = Tkint.Tk()
root.title('NS | Reisplanner')  # titel venster
root.config(width=1200, height=750)  # formaat venster
root.config(background="#FFC917")  # gele achtergrond van ns.nl

frameHeader = Frame(master=root,  # hoofd frame
                    width=1050,
                    height=690,
                    background="#FFC917")
frameHeader.place(x=70, y=10)

frameHeader1 = Frame(master=frameHeader,  # frame voor logo en tekst
                     width=1050,
                     height=90,
                     background="#FFC917")
frameHeader1.place(x=0)

imgpath = 'images/logo.png'  # NS logo
img = PhotoImage(file=imgpath)
img = img.zoom(4)
img = img.subsample(35)
panel = Label(frameHeader1,
              image=img,
              background="#FFC917")
panel.place(x=0, y=20)

logoText = Label(master=frameHeader1,  # Reisplanner
                 text='Reisplanner',
                 foreground='#003067',
                 background="#FFC917",
                 font=('Helvetica', 16, 'bold'),
                 width=10,
                 height=3)
logoText.place(x=85, y=5)

frameHeader2 = Frame(master=frameHeader,  # hoofd frame(Plan hier uw reis), zoekbalk en de reisadviezen
                     width=1050,
                     height=600,
                     background="white")
frameHeader2.place(x=0, y=90)

subFrameHeader = Frame(master=frameHeader2,
                       # sub frame waar alles komt te staan (Plan hier uw reis), zoekbalk en de reisadviezen
                       width=940,
                       height=550,
                       background="white")
subFrameHeader.place(x=54, y=25)

text = Label(master=subFrameHeader,  # Plan hier uw reis
             text='Plan hier uw reis',
             background="white",
             foreground='#003067',
             font=('Helvetica', 23),
             height=2)
text.place(x=0, y=0)

reisAdviezen = Frame(master=subFrameHeader,  # hoofd frame voor reisadviezen en ernaast
                     width=940,
                     height=400,
                     background="white")
reisAdviezen.place(x=0, y=145)

reisAdviezen1 = Frame(master=reisAdviezen,  # frame voor waar de reisadviezen komen te staan
                      width=470,
                      height=400,
                      background="white")
reisAdviezen1.place(x=0)

reisAdviezen2 = Frame(master=reisAdviezen,  # frame voor overige informatie naast reisadviezen
                      width=470,
                      height=400,
                      background="white")
reisAdviezen2.place(x=470)

invoerFrame = Tkint.Frame(master=subFrameHeader)  # begin en eindstation invullen
invoerFrame.place(width=940, x=0, y=80)

symbol = Label(text='>',
               foreground='#003067',
               font=('Helvetica', 19))
symbol.place(x=545, y=213)

zoekButton = Tkint.Button(master=invoerFrame,  # button for activating searching
                          text="Plannen",
                          command=planAndDraw)
zoekButton.pack(padx=10, pady=5, side="right")

station1 = Tkint.Entry(master=invoerFrame, width=53)  # beginstation
station2 = Tkint.Entry(master=invoerFrame, width=53)  # eindstation

station1.pack(padx=50, pady=17, side="left")
station2.pack(padx=50, pady=17, side="right")

root.mainloop()