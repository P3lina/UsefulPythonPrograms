from pytube import YouTube
from sys import argv
import numpy as np

downloadFolder = ''
try:
    link = argv[1]
    video = YouTube(link)
    resolution = ''
    if(argv.__len__() > 2):
        resolution = argv[2]
    else:
        resolution = [int(i.split("p")[0]) for i in (list(dict.fromkeys([i.resolution for i in video.streams if i.resolution])))]
        resolution = str(np.sort(resolution)[-1]) + 'p'
    download = video.streams.filter(res=resolution).first()
    download.download(downloadFolder)
except: print('Usage of this program: python YoutubeDownloader [Link] ([Resolution (360p,720p, 1080p, ...)] \n Note that the resolution is optional. If it is not specified, the highest resolution is downloaded.')