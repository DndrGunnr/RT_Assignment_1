from __future__ import print_function

import time
from sr.robot import *

a_th = 2.0
""" float: Threshold for the control of the orientation"""

d_th = 0.4
""" float: Threshold for the control of the linear distance"""

center_code=0
""" code of the center marker, initialized to zero"""

next_marker=0
"""code of the next marker to pick up"""

status=0
"""0=searching for a block,1=seraching for center"""

moved_markers=[]
"""list of moved markers"""

R = Robot()
""" instance of the class Robot"""

def drive(speed, seconds):
    """
    Function for setting a linear velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def turn(speed, seconds):
    """
    Function for setting an angular velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def find_token():
	distance=100
	elif next_marker==0:
		for token in R.see():
			if token.info.code not in moved_markers:
				if token.distance<distance:
					distance=token.dist
					angle=token.rot_y
					next_marker=token.info.code
	elif next_marker!=0
		for token in R.see():
			if token.info.code==next_token:
				distance=token.dist
				angle=token.rot_y
	elif distance==100:
		return -1,-1
	else:
		return distance,angle
def find_center():

	if center_code==0:
		distance=100
		for token in R.see():
			if token.dist<distance:
				distance=token.dist
				angle=token.rot_y
				center_marker=token.info.code
		if distance<100:
			moved_markers.append(center_code)
	elif center_code!=0:
		for token in R.see():
			if token.info.code==center_code:
				return distance,angle
	else :
		return -1,-1
		
def move_to_marker()
	if status==0
		while
	
		
while True
	while center_code==0:
		distance,angle=find_token()
		turn(20,1)
	if status==1
		
	
	


    


