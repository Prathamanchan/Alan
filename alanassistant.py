# Import library and create instance of REST client.
from gtts import gTTS
import datetime
import os
from time import sleep
from Adafruit_IO import Client

def talktome(audio):
        print(audio)
        tts=gTTS(text=audio,lang='en')
        tts.save('audiotwo.mp3') #install mpg123 Audio Player Software
        os.system('mpg123 audiotwo.mp3')

now = datetime.datetime.now()    
if now.hour <= 11:
        talktome("Good MOrning")
elif now.hour <=15:
        talktome("Good Afternoon")
elif now.hour <= 19:
        talktome("Good Evening")
else:
        talktome("Good Evening")

talktome("Hello I am ALan")


aio = Client('37ce7e77dad140a18e906a5cd48b6f07')   #Enter Your AIO Key HERE from Adafruit
prev_data="Nothing "    #Erase Previous Data
prev_data2="Nothing"
prev_data3="Nothing"
prev_data4="Nothing"
prev_data5="Nothing"

#Overite the Prev Data
aio.send('remainder',prev_data2)
sleep(1)
aio.send('hello',prev_data)
sleep(1)
aio.send('battery',prev_data3)
sleep(1)
aio.send('importantmail',prev_data4)
sleep(1)
aio.send('googlecal',prev_data5)
sleep(1)

# Get the last value of the hello and remainder feed.
data = aio.receive('hello')
sleep(1)
data2=aio.receive('remainder')
sleep(1)
data3=aio.receive('battery')
sleep(1)
data4=aio.receive('importantmail')

print data.value
print data2.value
print data3.value
print data4.value

# Print the value if there is a change Notice that the value is
# converted from string to int because it always comes back as a string from IO.
sleep(10)
while True:
	sleep(4)
	data = aio.receive('hello')
	sleep(1)
	data2=aio.receive('remainder')
	sleep(1)
	data3=aio.receive('battery')
	sleep(1)
	data4=aio.receive('importantmail')


	if data.value==prev_data:  #Call Remainder
		#Do Nothing
		i=10
	else:
		prev_data=data.value
		print data.value
		talktome("You missed a call from "+data.value)

	if data2.value==prev_data2:  #Calender Event Remainder
                #Do Nothing
                i=10
        else:
                prev_data2=data2.value
                print data2.value
                talktome("Remainder "+data2.value)

	if data3.value==prev_data3:   #Battery Status
		 #Do Nothing
                i=10
        else:
                prev_data3=data3.value
                print data3.value
                talktome("Your Battery is low, below "+data3.value)

        if data4.value==prev_data4:   #Battery Status
                 #Do Nothing
                i=10
        else:
                prev_data4=data4.value
                print data4.value
                talktome("You have received an important mail from Manager, Subject "+data4.value)

