import pytube
from pytube import Search, Stream
import os

def _download_audio(link, path = None):
    #filters by audio and downloads it into the current path
    yt = pytube.YouTube(link)
    vid = yt.streams.filter(progressive=False, abr='160kbps').first()
    if vid is None:
        raise ValueError
    
    
    downloaded = vid.download(filename=yt.title+".mp3", output_path=path)
    
    print(vid)

    # vid = yt.streams.filter(abr = "160kbps", progressive= False).last().download()

def download_audio(link, max_tries, dir):
    curr = 0
    if max_tries > 0:
        max_tries = max_tries
    else:
        raise ValueError

    while curr < max_tries:
        try:
            _download_audio(link, dir)
            break
        except: 
            curr += 1
    

if __name__ == "__main__":
    link = "https://www.youtube.com/watch?v=MxEjnYdfLXU"
    dir = '\cool'
    curr_path = os.curdir + dir
    max_tries = 3
    download_audio(link, max_tries,curr_path)
   
    