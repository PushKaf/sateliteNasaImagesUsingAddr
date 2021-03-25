import requests
import ctypes


apiKey = "DEMO_KEY" #ENTER YOUR API KEY HERE | this one will work, but you'll get limited after some pulls
link =f"https://api.nasa.gov/planetary/apod?api_key={apiKey}"
out = requests.get(link)
texts = out.text

#extracts the link of the image returned
imgLink = texts.split("\"")[-2]
#gets the typoe of file -> sometimes it might be videos so gotta check
imgType = imgLink.split(".")[-1]
#img name formatted with img type
imgName = f"nasaBackground.{imgType}"

#open the file with imgname in write binary format as write the content to save it
with open(imgName, "wb") as f:
    f.write(requests.get(imgLink).content)

#check if the type is actually an image 
if imgType in ["jpg", "png"]:
    #using ctypes set the walpaper of the sys to the img
    ctypes.windll.user32.SystemParametersInfoW(20,0,imgName,0)
else:
    #lmaooooooooo
    print("lmao")
