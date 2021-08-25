from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Folder_Name = ""

# dosya konumu
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")

    else:
        locationError.config(test="dosya seç.",fg="red")


# video indirme
def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()
    
    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytdError.config(test="lütfen linki tekrar yapıştır.",fg="red")

    select.download(Folder_Name)
    ytdError.config(text="İndirme Tamamlandı!")






root = Tk()
root.title("Youtube downloader")
root.geometry("350x400")
root.columnconfigure(0,weight=1)
ytdLabel = Label(root, text="url giriniz")
ytdLabel.grid()


## box
ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()

## error
ytdError = Label (root,text="error msg", fg="red",font=("jost",10))
ytdError.grid()

## save
saveLabel = Label(root,text="kaydedilecek yeri seç", font=("jost",15,"bold"))
saveLabel.grid()
saveEntry = Button(root,width=10,bg="blue",fg="white",text="dosya seç",command=openLocation)
saveEntry.grid()

locationError = Label(root,text="", fg="red",font=("jost",10))
locationError.grid()

## kalite
ytdQuality = Label(root,text="Kaliteyi Seç", font=("jost",15))
ytdQuality.grid()

choices = ["720p","144p","ses dosyası"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.grid()

## download
downloadbtn = Button(root,text="Download",width=10,bg="red",fg="white",command=DownloadVideo)
downloadbtn.grid()










root.mainloop()