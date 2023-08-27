# importing packages
from pytube import YouTube
import os
  
# url input from user
yt = YouTube(input("Enter the URL of the video you want to download: \n>> "))
  
# extract only audio
video = yt.streams.filter(only_audio=True).first()
  

# replace destination with the path where you want to save the downloaded file
destination = "/home/hamza/Desktop/Python scripts"
  
# download the file
out_file = video.download(output_path=destination)
  
# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
  