from pytube import YouTube
import os

# create downloads folder if not exists
root = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(root, "downloads")
if not os.path.exists(path):
    os.mkdir(path)


def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(output_path=path)
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
Download(link)
