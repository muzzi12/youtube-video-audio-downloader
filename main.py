from tkinter import *
from pytube import YouTube
from tkinter.messagebox import showerror as error, askquestion as ask, showinfo as info
import os
from humanfriendly import format_timespan

class youtube_downloader:
    def __init__(self,master):

        def other_details():
            raw = self.stringvar.get()
            file = YouTube(raw).length
            if file <= 60:
                self.label5.config(text='Length: {} {}'.format(file,'secs'))
            else:
                new_length = format_timespan(file)
                self.label5.config(text='Length: {}'.format(new_length))

            file1 =YouTube(raw).video_id
            self.id.config(text='Id: {}'.format(file1))

            file2 = YouTube(raw).age_restricted
            self.age_restriction.config(text='Age Restricted: {}'.format(file2))

            file3 = YouTube(raw).views
            self.label6.config(text='Views: {}'.format(file3))

        def credits():
            info('YouTube Downloader','YouTube Video/Audio Downloader developed by Muhammad Muzammil Alam')

        def title():
            raw = self.stringvar.get()
            file = YouTube(raw).title
            if file=='':
                self.label4.config('This video has no title')
            else:
                final_text = ""
                for i in range(0,len(file)):
                    final_text+=file[i]
                    if i%24==0 and i!=0:
                        final_text+='\n'
                self.label4.config(text=final_text)
                self.under_label.config(text='The Title of the video')

        def description():
            raw = self.stringvar.get()
            file = YouTube(raw).description
            if file=='':
                self.textbox.delete(1.0,END)
                self.textbox.insert(END,'This video has no description')
            else:
                self.textbox.delete(1.0,END)
                self.textbox.insert(END,file)
                self.label3.config(text='The Description of the video')
                self.scroll.config(text='(you can scroll down)')

        def download():
            if self.intvar.get() == 1:
                url = self.stringvar.get()
                file = YouTube(url)
                download = file.streams.filter(only_audio=True).all()
                final_file = download[1].download('E:/downloaded_youtube_videos_and_audios')
                choice =  ask('YouTube Downloader','Your Audio has been downloaded. Do you want to play the audio?')
                if choice=='yes':
                    os.startfile(final_file)
                else:
                    info('YouTube Downloader','Ok Sir!')

            elif self.intvar.get() == 2:
                url = self.stringvar.get()
                file = YouTube(url)
                download = file.streams.first()
                final_file = download.download('E:/downloaded_youtube_videos_and_audios')
                choice = ask('YouTube Downloader','Your Video hass been downloaded. Do you want to play the video?')
                if choice=='yes':
                    os.startfile(final_file)

                else:
                    info('YouTube Downloader','Ok Sir')
            else:
                error('YouTube Downloader','Invalid Choice!')

        def enterbtn(event):
            self.btn1.config(bg='grey',fg='black',relief=GROOVE)

        def leavebtn(event):
            self.btn1.config(bg='red',fg='black',relief=RAISED)

        def enteraudio(event):
            self.audio.config(bg='black', fg='grey')

        def leaveaudio(event):
            self.audio.config(bg='black', fg='red')

        def entervideo(event):
            self.video.config(bg='black', fg='grey')

        def leavevideo(event):
            self.video.config(bg='black', fg='red')

        def enterthumbnail(event):
            self.btn2.config(bg='grey',fg='black',relief=GROOVE)

        def leavethumbnail(event):
            self.btn2.config(bg='red',fg='black',relief=RAISED)

        def enterdescription(event):
            self.btn3.config(bg='grey', fg='black', relief=GROOVE)

        def leavedescription(event):
            self.btn3.config(bg='red', fg='black', relief=RAISED)

        def enterdetails(event):
            self.other_details.config(bg='grey', fg='black', relief=GROOVE)

        def leavedetails(event):
            self.other_details.config(bg='red', fg='black', relief=RAISED
                                      )
        self.master = master
        self.title = master.title('Youtube Downloader')
        self.geometry = master.geometry('600x500')
        self.background = self.master.config(background='black')
        self.resizable = master.resizable(0,0)

        self.label_1 = Label(master,text='Welcome To The YouTube Video/Audio Downloader',font='cursive 15 bold italic'
                             ,bg='black',fg='yellow').pack()
        self.label_2 = Label(master,text='Enter the url of the video: ',font='cursive 14 bold italic',fg='yellow'
                             ,bg='black').place(x=20,y=70)
        self.stringvar = StringVar()
        self.entry = Entry(master,textvariable=self.stringvar,bg='grey',fg='red',font='cursive 10 bold italic',
                           width=43)
        self.entry.place(x=280,y=75)
        self.btn1 = Button(master,borderwidth=6,text='DOWNLOAD',font='cursive 10 bold italic',bg='red',fg='black'
                           ,activeforeground='red',activebackground='yellow',command=download)
        self.btn1.bind('<Enter>',enterbtn)
        self.btn1.bind('<Leave>',leavebtn)
        self.btn1.place(x=490,y=110)
        self.intvar = IntVar()
        self.audio = Radiobutton(master,variable=self.intvar,text='AUDIO',font='Arial 12 bold italic',fg='red',bg='black'
                                 ,value=1,activebackground='black',activeforeground='yellow')
        self.audio.place(x=275,y=110)
        self.audio.bind('<Enter>', enteraudio)
        self.audio.bind('<Leave>', leaveaudio)
        self.video = Radiobutton(master,variable=self.intvar,text='VIDEO',font='Arial 12 bold italic',fg='red'
                                 ,bg='black',value=2,activebackground='black',activeforeground='yellow')
        self.video.place(x=370,y=110)
        self.video.bind('<Enter>',entervideo)
        self.video.bind('<Leave>',leavevideo)

        self.image_label = Label(master,bg='black').place(x=380,y=320)
        self.under_label = Label(master,bg='black',fg='red',text='',font='cursive 8 bold italic')
        self.under_label.place(x=410,y=480)
        self.btn2 = Button(master,borderwidth=6,text='The Title',font='cursive 10 bold italic',bg='red',fg='black'
                           ,activeforeground='red',activebackground='yellow',command=title)
        self.btn2.place(x=445,y=260)
        self.btn2.bind('<Enter>',enterthumbnail)
        self.btn2.bind('<Leave>',leavethumbnail)
        self.label4 = Label(master, text='', font='cursive 13 bold italic', bg='black', fg='yellow')
        self.label4.place(x=372, y=327)

        self.textbox = Text(master,width=40,height=9,bg='black',fg='yellow',font='cursive 9 bold italic',border=NO)
        self.textbox.place(x=50,y=327)

        self.btn3 = Button(master,text='Description',font='cursive 10 bold italic',bg='red',fg='black'
                           ,command=description,activeforeground='red',activebackground='yellow',borderwidth=6)
        self.btn3.place(x=150,y=260)
        self.btn3.bind('<Enter>',enterdescription)
        self.btn3.bind('<Leave>',leavedescription)

        self.label3 = Label(master,text='',font='cursive 8 bold italic',bg='black',fg='red')
        self.label3.place(x=110,y=480)

        self.label5 = Label(master,text='',font='helvictia 12 bold italic',bg='black',fg='yellow')
        self.label5.place(x=200,y=160)

        self.label6 = Label(master,text='',font='helvictia 12 bold italic',bg='black',fg='yellow')
        self.label6.place(x=198,y=190)

        self.other_details = Button(master,text='Other Details',font='cursive 10 bold italic',bg='red',fg='black'
                           ,activeforeground='red',activebackground='yellow',borderwidth=6,command=other_details)
        self.other_details.place(x=20,y=120)
        self.age_restriction = Label(master,text='',font='cursive 12 bold italic',fg='yellow',bg='black')
        self.age_restriction.place(x=20,y=160)

        self.id = Label(master,text='',font='cursive 12 bold italic',bg='black',fg='yellow')
        self.id.place(x=20,y=190)

        self.other_details.bind('<Enter>',enterdetails)
        self.other_details.bind('<Leave>',leavedetails)

        self.menubar = Menu(master)
        self.menu = Menu(master,tearoff=0)
        self.menu.add_command(label='Credits',command=credits,foreground='red',background='black',font='cursive 8 bold italic',activeforeground='black',activebackground='red')
        self.menubar.add_cascade(label='Help',menu=self.menu)
        master.config(menu=self.menubar)

        self.scroll = Label(master,text='',font='cursive 7 bold italic',bg='black',fg='yellow')
        self.scroll.place(x=268,y=482)

window = Tk()
youtube_downloader(window)
window.mainloop()
