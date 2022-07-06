import pytube 

url = input("url here:")
path = "C:\\Users\\LENOVO\\Desktop"
pytube.YouTube(url).streams.get_highest_resolution().download(path)
