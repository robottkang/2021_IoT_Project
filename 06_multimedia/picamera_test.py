import picamera
import time

path = '/home/pi/src4/06_multimedia'

camera = picamera.PiCamera()

try:
    camera.resolution = (640, 480)
    camera.start_preview()
    time.sleep(3)
    camera.rotation = 180
    #camera.capture('%s/photo.jpg' % path)         #사진
    camera.start_recording('%s/video.h264' % path) #동영상
    time.sleep(10)
    camera.stop_recording()

finally:
    camera.stop_preview()