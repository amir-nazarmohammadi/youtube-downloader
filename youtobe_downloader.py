import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askdirectory
from pytube import YouTube

root = tk.Tk()
root.title("Youtube Downloader")
root.minsize(width=450, height=200)
root.config(bg="#FFFFFF")


def window_display():
    link_label = tk.Label(root, text="Link Video:",)
    link_label.grid(row=0, column=0, padx=20, pady=20)
    link_label.config(font=("None", 13), fg="#FF0063", bg="#FFFFFF")

    link_input = tk.Entry(root, width=40, border=1, textvariable=video_link)
    link_input.grid(row=0, column=1)
    link_input.config(bg="#EAF6F6")

    link_label2 = tk.Label(root, text="Browser:")
    link_label2.grid(row=1, column=0, padx=20, pady=20)
    link_label2.config(font=("None", 13), fg="#FF0063", bg="#FFFFFF")

    link_input2 = tk.Entry(root, width=30, border=1, textvariable=download_dir)
    link_input2.grid(row=1, column=1, sticky="w")
    link_input2.config(bg="#EAF6F6")

    btn_browse = tk.Button(root, text="open file:", command=open)
    btn_browse.grid(row=1, column=2, padx=15)
    btn_browse.config(height=1, width=10, bg="#5463FF", fg="#FFFFFF")

    btn_download = tk.Button(root, text="Download Now!", command=download)
    btn_download.grid(row=2, column=1)
    btn_download.config(font=("None", 10, "bold"), height=3,
                        width=20, bg="#FF0063", fg="#FFFFFF")


def open():

    directory = askdirectory(initialdir="YOUR DIRECTORY PATH", title="save")
    download_dir.set(directory)


def download():

    link = video_link.get()
    save_dir = download_dir.get()
    yt = YouTube(link)
    yt.streams.filter(res="720p").first().download(save_dir)
    messagebox.showinfo(title="success",message="Your video download successfuly!")

download_dir = tk.StringVar()
video_link = tk.StringVar()


window_display()
root.mainloop()
