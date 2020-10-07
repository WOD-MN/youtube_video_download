import pafy #import the library!!!

url = input("Enter the link of the video: ") #Enter the youtube video link here!!
video = pafy.new(url)

stream = video.streams
for a in stream:
    print(a)

best_res = video.getbest() #Get the best resolution

print(best_res.resolution, best_res.extension)

best_res.download() #Download the video!!

print("Video is downloaded successfully!!!")