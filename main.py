from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import *
import shutil


def get_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)


def download():
    video_path = url_entry.get()
    file_path = path_label.cget("text")
    print('Downloading....')
    mp4 = YouTube(video_path).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(mp4)
    # code for mp3
    audio_file = video_clip.audio
    audio_file.write_audiofile('audio.mp3')
    audio_file.close()
    shutil.move('audio.mp3', file_path)
    # code for mp3
    video_clip.close()
    shutil.move(mp4, file_path)
    print('Download Complete')


root = Tk()

root.title('Video Downloader')
canvas = Canvas(root, width=800, height=600)
canvas.pack()

# app lable
app_label = Label(root, text="Video Downloader", fg='blue', font=('Arial', 30))
canvas.create_window(400, 20, window=app_label)

# entry to accept video url
url_label = Label(root, text="Enter video URL")
url_entry = Entry(root)
canvas.create_window(400, 80, window=url_label)
canvas.create_window(400, 100, window=url_entry)

# path to download video
path_label = Label(root, text="Select path to download")
path_button = Button(root, text="Select", command=get_path)
canvas.create_window(400, 150, window=path_label)
canvas.create_window(400, 170, window=path_button)

# download button
download_butto = Button(root, text="Download", command=download)
canvas.create_window(400, 250, window=download_butto)


root.mainloop()
