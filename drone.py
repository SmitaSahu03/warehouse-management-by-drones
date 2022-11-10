from djitellopy import tello
import cv2
from time import sleep
 
tel = tello.Tello()
 
tel.connect()
 
print (tel.get_battery())

tel.takeoff()

tel.send_rc_control(0,80,0,0)
sleep(2)

tel.send_rc_control(-20,0,0,0)
sleep(2)

tel.send_rc_control(0,0,20,0)
sleep(2)

tel.rotate_counter_clockwise(90)
sleep(2)

tel.streamon()
frame_read = tel.get_frame_read()
cv2.imwrite("./picture.png", frame_read.frame)
sleep(2)

tel.rotate_counter_clockwise(90)
sleep(2)

tel.send_rc_control(0,70,0,0)
sleep(2)

tel.send_rc_control(0,0,0,0)
tel.land()

