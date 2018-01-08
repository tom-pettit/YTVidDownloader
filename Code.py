from __future__ import unicode_literals
import youtube_dl
import urllib
import shutil
from Tkinter import *

def downloader():
    INPUT = entry.get()
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([INPUT])
        print 'Downloading Video...'
        print 'Video Downloaded'

def cancel():
    quit()
        
root = Tk()
root.title('YTDownloader')
root.geometry('250x100')
label = Label(root, text='Enter the Link of the Video: ')
entry = Entry(root)
button = Button(root, text='Download', command = downloader)
exitbutton = Button(root, text='Stop', command = cancel)
label.pack()
entry.pack()
button.pack()
exitbutton.pack()
mainloop()
