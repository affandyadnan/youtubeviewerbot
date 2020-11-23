import webbrowser
import time
import os

print ('\t\t\t ######################################')
print ('\t\t\t ## This is for educational purpose only ##')
print ('\t\t\t ## I am not responsible if any damage has been done while using this script ##')
print ('\t\t\t ## Author : Affandy  ##')
print ('\t\t\t ## Date   : 23th November 2020 ##')
print( '\t\t\t ######################################')




url = input("Enter YouTube URL : ")
refresh = input("Enter refresh rate(seconds) : ")
brow = input("Enter your default browser : ")

def OpenUrl():
	print("Successfully Viewed. ")
	os.system("taskkill /im msedge.exe /f")
	webbrowser.open(url)
	time.sleep(int(refresh))

for i in range(10):
	OpenUrl()
