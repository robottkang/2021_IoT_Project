import picamera
import time

path = '/home/pi/src4/06_multimedia'
now_str = time.strftime("%Y%m%d_%H%M%S")

camera = picamera.PiCamera()

try:
    camera.resolution = (640, 480)
    camera.start_preview()
    camera.rotation = 180
    while True:
        cmd = input("photo:1, video:2, exit:9 > ")
        if cmd == '1':
            camera.capture('%s/%s.jpg' % (path, now_str))          #사진
        elif cmd == '2':
            camera.start_recording('%s/%s.h264' % (path, now_str)) #동영상
            stop = input("press enter to stop")
            camera.stop_recording()
        elif cmd == '9':
            break
        else:
            print('incorrect command')

finally:
    camera.stop_preview()