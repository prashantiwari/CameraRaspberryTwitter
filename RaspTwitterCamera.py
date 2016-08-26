import time
from picamera import Picamera
from time import sleep
from twython import TwythonStreamer
from datetime import datetime


APP_KEY = 'TwjyVF0Elh2uAr8JNTQeJQdK6'
APP_SECRET = '5NUizxk8g8JaCjZuTHNakHXwdFpVy40OIXgDG1Vf8uQAnoQZOK'
OAUTH_TOKEN = '760761114334523392-yPZOICLEEinxjnDXDIAWMILPVyBn5qA'
OAUTH_TOKEN_SECRET = 'ujwt9LxRfmJ1oB24WW8lZGFmX6eUwuxPND46RdM9VGeJX'

TERM = '#TakePicture'
FOLLOW = '2851590678'

timeasofnow = str(datetime.now())
timeasofnow = timeasofnow.replace(":", "_")
timeasofnow = timeasofnow.replace("-","_")
picturelocation = /Home/pi/PicturesByRasp/image
picturelocation = picturelocation + timeasofnow



mycamera = PiCamera()

class BotStreamer(TwythonStreamer):
        def on_success(self, data):
                if 'text' in data:
                        print data['text'].encode('utf-8')
                        print
                        
                        
                        timeasofnow = str(datetime.now())
                        timeasofnow = timeasofnow.replace(":", "_")
                        timeasofnow = timeasofnow.replace("-","_")
                        picturelocation = /Home/pi/PicturesByRasp/image
                        picturelocation = picturelocation + timeasofnow

                        camera.start_preview()
                        sleep(5)
                        camera.capture('picturelocation')
                        camera.stop_preview()
                        
                        


try:
        stream = BotStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        stream.statuses.filter(track=TERM), follow=FOLLOW)

except KeyboardInterrupt:
	print 'end'
