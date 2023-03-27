from pytube import Playlist

p = Playlist('https://www.youtube.com/playlist?list=PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n')
for videos in p.videos:
    try :
        print(videos.title) 
        # videos.streams.get_highest_resolution().download('./')
    except Exception as e:
        print(e)
        continue