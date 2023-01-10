from pytube import YouTube, Playlist
from pytube.cli import on_progress
import os
import sys

def download_video():
    video_url = input("Enter video url: \n");
    video = YouTube(video_url, on_progress_callback=on_progress)
    print(f"Video Name : {video.title}\n")
    download_path = input("Enter the path to save the files:")
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    
    stream = video.streams.filter(res='720p').first()
    if stream is not None:
        stream.download(output_path=download_path)
    else:
        print(f"No video found for {video.title}")

def download_audio():
    video_url = input("Enter video url: ");
    video = YouTube(video_url,on_progress_callback=on_progress)
    print(f"Video Name : {video.title}\n")
    download_path = input("Enter the path to save the files:")
    if not os.path.exists(download_path):
        os.makedirs(download_path)    
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    stream = video.streams.filter(only_audio=True, file_extension='mp4').first()
    if stream is not None:
        stream.download(output_path=download_path)
    else:
        print(f"No audio found for {video.title}")

def download_playlist_as_audio():
    link = input("Enter playlist link: ")
    playlist = Playlist(link)
    download_path = input("Enter the path to save the files:")
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    if not os.path.exists(download_path):   
        os.makedirs(download_path)
    download_path = os.path.join(download_path, playlist.title)
    for video in playlist.videos:
        video.register_on_progress_callback(on_progress)
        stream = video.streams.filter(only_audio=True, file_extension='mp4').first()
        if stream is None:
            stream = video.streams.filter(only_audio=True, file_extension='webm').first()
        if stream is not None:
            stream.download(output_path=download_path)
        else:
            print(f"No audio found for {video.title}")


def download_playlist_as_video():
    link = input("Enter playlist link: ")
    playlist = Playlist(link)
    download_path = input("Enter the path to save the files:")
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    download_path = os.path.join(download_path, playlist.title)
    for video in playlist.videos:
        video.register_on_progress_callback(on_progress)
        stream = video.streams.filter(res='720p').first()
        if stream is not None:
            stream.download(output_path=download_path)
        else:
            print(f"No video found for {video.title}")

def print_menu():
    print("Select the option you want to download\n")
    print("a - Download video\n")
    print("b - Download video format audio\n")
    print("c - Download playlist videos\n")
    print("d - Download playlist videos format audio \n")
    print("q - Quit\n")

def main():
    CHOICES = ["a", "b", "c", "d", "q"]
    choice = ""
    while (choice != "q") and (choice not in CHOICES):
        print_menu()
        choice = input("Enter your choice: ")
        if choice.lower() not in CHOICES:
            print("invalid choice. Try again!\n")

    match choice:
        case "a":
            download_video()
        case "b":
            download_audio()
        case "c":
            download_playlist_as_video()
        case "d":
            download_playlist_as_audio()
        case "q":
            print("Goodbye !!!\n")


main()