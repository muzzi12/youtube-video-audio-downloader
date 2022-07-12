from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from pytube import YouTube
from tkinter.messagebox import showinfo as info, showerror as error, askquestion as ask
import os
from humanfriendly import format_timespan
import random
import pytube.exceptions
import urllib
import instalooter
from threading import Thread


class you_tube:

    def __init__(self, master):

        def thread_pre_download():
            thread = Thread(target=download)
            thread.start()

        def change_color():
            random_colors = ['red', 'green', 'blue', 'aqua', 'yellow', 'cyan', 'pink', 'purple', 'orange', 'black',
                             'maroon', 'grey', 'maroon', 'violet', 'brown', 'green']
            color = random.choice(random_colors)
            self.label1.config(fg=color)
            self.label1.after(100, change_color)

        def exit():
            c = ask('M-YT', 'Do you want to exit')
            if c == 'yes':
                quit()
            else:
                pass

        def show_details_thread():
            thread = Thread(target=show_details)
            thread.start()

        def show_details():

            try:
                self.label5.config(text='Fetching Details...')
                raw = self.stringvar.get()
                file = YouTube(raw).title
                self.title.config(text='TITLE:')
                self.line_between.config(
                    text='=====================================================================================')
                if file == '':
                    self.label4.config(text='This video has no title')
                else:
                    final_text = ""
                    for i in range(0, len(file)):
                        final_text += file[i]
                        if i % 22 == 0 and i != 0:
                            final_text += '\n'
                    self.label4.config(text=final_text)

                file1 = YouTube(raw).length
                self.Length_label.config(text='LENGTH:')
                if file1 <= 60:
                    self.length.config(text=(file1, 'secs'))
                else:
                    new_length1 = format_timespan(file1)
                    new_length2 = new_length1.replace('hours', 'hrs')
                    new_length3 = new_length2.replace('minutes', 'mins')
                    new_length4 = new_length3.replace('seconds', 'secs')
                    self.length.config(text=new_length4)

                file2 = YouTube(raw).video_id
                self.video_id_Label.config(text='ID:')
                self.video_id.config(text=file2)

                file3 = YouTube(raw).age_restricted
                self.age_restriction_label.config(text='AGE RESTRICTED:')
                if file3 == 0:
                    self.age_restriction.config(text='NO')
                else:
                    self.age_restriction.config(text='YES')

                file4 = YouTube(raw).views
                self.video_views_label.config(text='VIEWS:')
                self.video_views.config(text=file4)

                file5 = YouTube(raw).description
                self.description_label.config(text='DESCRIPTION:')
                if file5 == '':
                    self.description.delete(1.0, END)
                    self.description.insert(END, 'This video has no description')
                else:
                    self.description.delete(1.0, END)
                    self.description.insert(END, file5)
                self.label5.config(text='Waiting...')

            except pytube.exceptions.RegexMatchError:
                self.label5.config(text='Waiting...')
                error('M-YT', 'Please enter a valid URL!')

            except pytube.exceptions.VideoUnavailable:
                self.label5.config(text='Waiting...')
                error('M-YT', 'This video is unavailable!')

            except urllib.error.URLError:
                self.label5.config(text='Waiting...')
                error('M-YT', 'Please Check Your Internet Connection!')

            except ConnectionResetError:
                error('M-YT','A network error occure, try again later.')

        def hide_details():
            self.title.config(text='')
            self.label4.config(text='')
            self.description_label.config(text='')
            self.description.delete(1.0, END)
            self.Length_label.config(text='')
            self.length.config(text='')
            self.video_id_Label.config(text='')
            self.video_id.config(text='')
            self.video_views_label.config(text='')
            self.video_views.config(text='')
            self.age_restriction_label.config(text='')
            self.age_restriction.config(text='')
            self.line_between.config(text='')

        def download():
            if self.intvar.get() == 1:
                try:
                    if self.entry2.get() == '':
                        error('M-YT', 'Please select a destination for the file')
            #
                    else:
            #
                        url = self.stringvar.get()
                        file = YouTube(url)
                        self.label5.config(text='Downloading...')
                        download = file.streams.filter(only_audio=True).all()
                        download[1].download(self.entry2.get())
                        file_name = self.entry2.get()+'/'+os.listdir(self.entry2.get())[0]
                        new_file = self.entry2.get()+'.mp4'
                        os.rename(file_name,new_file)
                        os.system(f'rmdir /s /q \"{self.entry2.get()}\"')
                        os.system(f"ffmpeg -i \"{new_file}\" \"{str(new_file.replace('.mp4','.mp3'))}")
                        os.remove(new_file)
                        self.label5.config(text='Waiting...')
                        choice = ask('YouTube Downloader',
                                     'Your File has been downloaded. Do you want to play the File?')
                        if choice == 'yes':
                            os.startfile(self.entry2.get()+'.mp3')
                        else:
                            pass

                except pytube.exceptions.RegexMatchError:
                    error('M-YT', 'Please enter a valid URL!')

                except pytube.exceptions.VideoUnavailable:
                    error('M-YT', 'This video is unavailable!')

                except urllib.error.URLError:
                    error('M-YT', 'Please Check Your Internet Connection!')

                except ConnectionResetError:
                    error('M-YT','A network error occurred, try again later.')

                except:
                    error('M-YT', 'Invalid Destination for the file.')


            elif self.intvar.get() == 2:
                try:
                    if self.entry2.get() == '':
                        error('M-YT', 'Please select a destination for the file')

                    else:
                        self.label5.config(text='Downloading...')
                        url = self.stringvar.get()
                        file = YouTube(url)
                        download = file.streams.get_highest_resolution()
                        download.download(self.entry2.get())
                        file_name = self.entry2.get() + '/' + os.listdir(self.entry2.get())[0]
                        new_file = self.entry2.get() + '.mp4'
                        os.rename(file_name, new_file)
                        os.system(f'rmdir /s /q \"{self.entry2.get()}\"')
                        self.label5.config(text='Waiting...')
                        choice = ask('YouTube Downloader',
                                     'Your File has been downloaded in. Do you want to play the File?')
                        if choice == 'yes':
                            os.startfile(new_file)
                        else:
                            pass

                except pytube.exceptions.RegexMatchError:
                    error('M-YT', 'Please enter a valid URL!')

                except pytube.exceptions.VideoUnavailable:
                    error('M-YT', 'This video is unavailable!')

                except urllib.error.URLError:
                    error('M-YT', 'Please Check Your Internet Connection!')

                except ConnectionResetError:
                    error('M-YT','A network error occure, try again later.')

                except:
                    error('M-YT', 'Invalid Destination for the file.')

            else:
                error('M-YT', 'Invalid File Type!')

        def credits():
            info('M-YT', 'Youtube Audio/Video downloader made by Muhammad Muzammil Alam')

        def enterdownload(event):
            self.download.config(bg='grey', fg='black', relief=GROOVE)

        def leavedownload(event):
            self.download.config(fg='white', bg='black', relief=RAISED)

        def enteraudio(event):
            self.audio.config(fg='grey')

        def leaveaudio(event):
            self.audio.config(fg='green')

        def entervideo(event):
            self.video.config(fg='grey')

        def leavevideo(event):
            self.video.config(fg='green')

        def entershow_detalis(event):
            self.show_details.config(bg='black', fg='white', relief=GROOVE)

        def leaveshow_details(event):
            self.show_details.config(bg='red', fg='black', relief=RAISED)

        def enterhide_details(event):
            self.hide_details.config(bg='black', fg='white', relief=GROOVE)

        def leavehide_details(event):
            self.hide_details.config(bg='red', fg='black', relief=RAISED)

        def enterselect(event):
            self.select.config(bg='grey', fg='black', relief=GROOVE)

        def leaveselect(event):
            self.select.config(fg='white', bg='black', relief=RAISED)

        def enterexit(event):
            self.exit_button.config(fg='black', bg='grey', relief=GROOVE)

        def leaveexit(event):
            self.exit_button.config(fg='white', bg='black', relief=RAISED)

        def e():
            q = ask('M-YT', 'Do you want to exit?')
            if q:
                sys.exit()
            else:
                pass

        def set_path():
            path = filedialog.asksaveasfilename()
            self.entry2.delete(0,END)
            self.entry2.insert(END, path)

        self.master = master
        self.geometry = master.geometry('700x600')
        self.background = master.config(background='white')
        self.resize = master.resizable(0, 0)
        self.title = master.title('M-YT')

        self.label1 = Label(master, text='Welcome To The Youtube Video/Audio Downloader', font='chiller 25 bold italic',
                            fg='red', bg='white')
        self.label1.pack()
        self.label2 = Label(master, text='Enter The URL Of The Video:', font='cursive 14 bold italic', fg='blue',
                            bg='white').place(x=10, y=60)
        self.label3 = Label(master, text='Destination for Downloaded File:', font='cursive 14 bold italic', bg='white',
                            fg='blue').place(x=10, y=170)
        self.label3 = Label(master, text='Status : ', font='curisve 12 bold italic', bg='white', fg='blue').place(x=0,
                                                                                                                  y=570)
        self.label5 = Label(master, text='Waiting...', font='curisve 12 bold italic', bg='white', fg='black')
        self.label5.place(x=65, y=570)

        self.stringvar = StringVar()
        self.entry = Entry(master, width=45, border=3, font='cursive 10 bold italic', textvariable=self.stringvar)
        self.entry.place(x=320, y=64)
        self.entry2 = Entry(master, width=45, border=3, font='cursive 10 bold italic')
        self.entry2.place(x=320, y=174)

        self.download = Button(master, command=thread_pre_download, borderwidth=4, relief=RAISED, text='DOWNLOAD',
                               font='lorem 12 bold italic', fg='white', bg='black', activeforeground='white',
                               activebackground='red', cursor='hand2')
        self.download.place(x=525, y=90)
        self.download.bind('<Enter>', enterdownload)
        self.download.bind('<Leave>', leavedownload)
        self.select = Button(master, text='Select', command=set_path, font='lorem 12 bold italic', fg='white',
                             bg='black', activeforeground='white', activebackground='red', cursor='hand2',
                             borderwidth=4, relief=RAISED)
        self.select.place(x=576, y=200)
        self.select.bind('<Enter>', enterselect)
        self.select.bind('<Leave>', leaveselect)

        self.filetypes = Label(master, text='File Type : ', fg='black', font='cursive 12 bold italic',
                               bg='white').place(x=316, y=100)
        self.intvar = IntVar()
        self.audio = Radiobutton(master, text='Audio', font='cursive 10 bold italic', fg='green', variable=self.intvar,
                                 value=1, activeforeground='red', bg='white', activebackground='white', cursor='hand2')
        self.audio.place(x=420, y=102)
        self.audio.bind('<Enter>', enteraudio)
        self.audio.bind('<Leave>', leaveaudio)

        self.video = Radiobutton(master, text='Video', font='cursive 10 bold italic', fg='green', variable=self.intvar,
                                 value=2, activeforeground='red', bg='white', activebackground='white', cursor='hand2')
        self.video.place(x=420, y=130)
        self.video.bind('<Enter>', entervideo)
        self.video.bind('<Leave>', leavevideo)

        self.menubar = Menu(master)
        self.menu = Menu(master, tearoff=0)
        self.menu.add_command(label='Credits', command=credits, foreground='red', background='black',
                              font='cursive 8 bold italic', activeforeground='black', activebackground='red')
        self.menubar.add_cascade(label='Help', menu=self.menu)
        master.config(menu=self.menubar)

        self.show_details = Button(master, text='SHOW DETAILS', bg='red', fg='black', font='cursive 12 bold italic',
                                   borderwidth=4, relief=RAISED, activebackground='grey', activeforeground='black',
                                   command=show_details_thread, cursor='hand2')
        self.show_details.place(x=285, y=280)
        self.show_details.bind('<Enter>', entershow_detalis)
        self.show_details.bind('<Leave>', leaveshow_details)

        self.hide_details = Button(master, text='HIDE DETAILS', fg='black', bg='red', font='cursive 12 bold italic',
                                   borderwidth=4, relief=RAISED, activebackground='grey', activeforeground='black',
                                   command=hide_details, cursor='hand2')
        self.hide_details.place(x=290, y=220)
        self.hide_details.bind('<Enter>', enterhide_details)
        self.hide_details.bind('<Leave>', leavehide_details)

        self.line_between = Label(master, text='', bg='white', fg='blue')
        self.line_between.place(x=8, y=315)

        self.description = Text(master, font='cursive 9 bold italic', width=30, height=10, border=NO, )
        self.description.place(x=249, y=370)
        self.description_label = Label(master, text='', fg='blue', font='lorem 12 bold italic', bg='white')
        self.description_label.place(x=295, y=330)

        self.exit_button = Button(master, command=exit, text='EXIT', fg='white', bg='black',
                                  font='curive 12 bold italic', borderwidth=4, activeforeground='black',
                                  activebackground='red', relief=RAISED, cursor='hand2')
        self.exit_button.place(x=330, y=555)
        self.exit_button.bind('<Enter>', enterexit)
        self.exit_button.bind('<Leave>', leaveexit)

        self.title = Label(master, text='', font='curisve 12 bold italic', fg='blue', bg='white')
        self.title.place(x=80, y=332)

        self.label4 = Label(master, text='', font='cursive 11 bold italic', fg='black', bg='white')
        self.label4.place(x=10, y=370)

        self.Length_label = Label(master, text='', font='cursive 11 bold italic', bg='white', fg='blue')
        self.Length_label.place(x=485, y=332)

        self.length = Label(master, text='', font='cursive 8 bold italic', bg='white', fg='black')
        self.length.place(x=555, y=334)

        self.age_restriction_label = Label(master, text='', font='cursive 11 bold italic', bg='white', fg='blue')
        self.age_restriction_label.place(x=484, y=370)
        self.age_restriction = Label(master, text='', bg='white', fg='black', font='cursive 10 bold italic')
        self.age_restriction.place(x=630, y=371)

        self.video_id_Label = Label(master, text='', font='cursive 11 bold italic', bg='white', fg='blue')
        self.video_id_Label.place(x=484, y=410)
        self.video_id = Label(master, text='', font='cursive 10 bold italic', bg='white', fg='black')
        self.video_id.place(x=510, y=410)

        self.video_views_label = Label(master, text='', font='cursive 11 bold italic', bg='white', fg='blue')
        self.video_views_label.place(x=481, y=450)
        self.video_views = Label(master, text='', font='cursive 10 bold italic', bg='white', fg='black')
        self.video_views.place(x=540, y=451)

        self.master.protocol('WM_DELETE_WINDOW', e)

        change_color()


root = Tk()
you_tube(root)
root.mainloop()
