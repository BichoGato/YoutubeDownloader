import youtube_dl
from tkinter import *
import tkinter.filedialog
import os


def getmp():
    global mp
    return mp.get()


def getdir():
    global userpath
    userpathtext = open('userpathtext.txt', 'w')
    diretorio = tkinter.filedialog.askdirectory()
    while diretorio == '':
        diretorio = tkinter.filedialog.askdirectory()
    userpathtext.write(diretorio + '\%(title)s.%(ext)s')
    userpathtext.close()


def downloadvideo():
    global videol, userpath

    if os.path.exists('userpathtext.txt'):
        userpathtext = open('userpathtext.txt', 'r')
        for i in userpathtext:
            userpath = i
    else:
        import ctypes.wintypes
        CSIDL_PERSONAL = 5
        SHGFP_TYPE_CURRENT = 0
        buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
        ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)
        userpath = buf.value + '\Youtube Downloader\%(title)s.%(ext)s'

    videolink = videol.get()
    if getmp() == 0:
        try:
            ydl_opts = {'outtmpl': userpath, 'format': '137+140', 'cachedir': False}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([str(videolink)])
        except:
            try:
                ydl_opts = {'outtmpl': userpath, 'format': '136+140', 'cachedir': False}
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([str(videolink)])
            except:
                try:
                    ydl_opts = {'outtmpl': userpath, 'format': '135+140', 'cachedir': False}
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([str(videolink)])
                except:
                    try:
                        ydl_opts = {'outtmpl': userpath, 'format': '134+140', 'cachedir': False}
                        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                            ydl.download([str(videolink)])
                    except:
                        try:
                            ydl_opts = {'outtmpl': userpath, 'format': '133+140', 'cachedir': False}
                            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                                ydl.download([str(videolink)])
                        except:
                            try:
                                ydl_opts = {'outtmpl': userpath, 'format': '160+140', 'cachedir': False}
                                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                                    ydl.download([str(videolink)])
                            except:
                                pass
    else:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': userpath,
            'cachedir': False,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]}

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([str(videolink)])


root = Tk()

root.iconbitmap('imagens/YoutubeDownloader_icon.ico')
root.geometry('800x700')
root.title("Youtube Downloader")
root.resizable(False, False)

#  TITULO
titulo_frame = Frame(root, bg='RED')
titulo_texto = Label(titulo_frame, text="Youtube Downloader", font=("Helvetica", 40), bg='RED')
titulo_texto.pack()
titulo_frame.pack(side=TOP, fill=X)

# botao diretorio
foto_path = PhotoImage(file='imagens/path_botao.png')
botao_path = Button(root,
                    text=' Escolher Diretorio  ',
                    font='Helvetica 9',
                    image=foto_path,
                    compound=TOP,
                    command=getdir)
botao_path.place(x=675, y=80)

# Link
link_label = Label(root, text='Link do video para fazer download', font=("Helvetica", 27))
link_label.place(x=350, y=150, anchor=CENTER)
link_label = Label(root, text='Ctrl C —— Ctrl V', font=("Helvetica", 9))
link_label.place(x=350, y=185, anchor=CENTER)

# inserir link
videol = Entry(root, bd='1.5', width=40, font="Helvetica 20")
videol.place(x=60, y=200, height=45)

# MP4 -- MP3
mp = IntVar()
Radiobutton(root,
            text="MP4",
            font="Helvetica 16",
            padx=20,
            variable=mp,
            value=0).place(x=270, y=265)

Radiobutton(root,
            text="MP3",
            font="Helvetica 16",
            padx=20,
            variable=mp,
            value=1).place(x=400, y=265)

# botao download
foto_download = PhotoImage(file='imagens/download_botao.png')
botao_download = Button(root,
                        text='  Download  ',
                        font="Helvetica 16",
                        image=foto_download,
                        compound=LEFT,
                        command=downloadvideo)
botao_download.place(x=305, y=340)

#  STATUS BARRA
status = Label(root,
               text='Youtube Downloader by BichoGato',
               bd=1,
               relief=SUNKEN,
               anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()
