import pytube   

download_location = './'
download_link = input("Youtube link: ")
yt = pytube.YouTube(download_link)
stream= yt.streams.get_highest_resolution()
stream.download(download_location)
