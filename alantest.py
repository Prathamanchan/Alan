from gtts import gTTS
import datetime
import os
from time import sleep
from Adafruit_IO import Client

def talktome(audio):
        print(audio)
        tts=gTTS(text=audio,lang='en')
        tts.save('audiotwo.mp3') #install mpg123 Audio Player Software
        os.system('mpg123 audiotwo.mp3') # Change the location according to your System

now = datetime.datetime.now()          #Greetings
if now.hour <= 11:
        talktome("Good MOrning")
elif now.hour <=15:
        talktome("Good Afternoon")
elif now.hour <= 19:
        talktome("Good Evening")
else:
        talktome("Good Evening")

talktome("Hello Alan Here")


aio = Client('920a3cb78bbf47848fcc023c52b79969')   #Enter Your AIO Key HERE from Adafruit
prev_data="Nothing "    #Erase Previous Data

#Overite the Prev Data
aio.send('ImpEmailNotifer',prev_data)
sleep(1)

# Get the last value of the feed.
data = aio.receive('ImpEmailNotifer')
sleep(1)

# Print the value if there is a change Notice that the value is
# converted from string to int because it always comes back as a string from IO.
sleep(10)
while True:
	sleep(4)
	data = aio.receive('ImpEmailNotifer')
	sleep(1)

	#Email Remainder  
	if data.value==prev_data:  #Conccurrent Same Subject willbe ignored
                #Do Nothing
                i=10
        else:
                prev_data=data.value
                print data.value
                talktome(" Received Email "+data.value)

