from __future__ import print_function

import time
from sr.robot import *



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
	global next_marker
	distance=100
	'''when a marker is being released or when the simulation starts'''
	if next_marker==0:
		for token in R.see():
			'''check if the seen marker is already been moved'''
			if token.info.code not in moved_markers:
				'''choosing next marker as nearest unmoved 					marker'''
				if token.dist<distance:
					distance=token.dist
					angle=token.rot_y
					next_marker=token.info.code
					return distance, angle
		if distance==100:
			return -1,-1

	else:
		for token in R.see():
			if token.info.code==next_marker:
				distance=token.dist
				angle=token.rot_y
		if distance<100:
			return distance,angle
		else: 
			return -1,-1
def find_center():
	global center_code,next_marker,moved_markers
	distance=100
	print(center_code)
	if center_code==0:
		for token in R.see():
			if token.dist<distance:
				distance=token.dist
				angle=token.rot_y
				center_code=token.info.code
		if distance<100:
			moved_markers.append(center_code)
			return distance, angle
		else:
			return -1,-1
	else:
		for token in R.see():
			if token.info.code==center_code:
				distance=token.dist
				angle=token.rot_y
		if distance<100:
			return distance,angle
		else:
			return -1,-1
	
		
def move_to_marker(distance, angle):
	global status,moved_markers,next_marker,status
	if angle<-a_th:
		turn(-distance,0.5)
	if angle>a_th:
		turn(distance,0.5)
	else:
		'''if I have to drop a marker near the center block I can't 			use the regular threshold'''
		if distance>d_th+status*0.3:
			drive(30,1)
		else:
			if status==0:
				R.grab()
				drive(-20,2)
				status=1
				print(status)
			else:
				R.release()
				drive(-20,2)
				status=0
				print(status)
				moved_markers.append(next_marker)
				print(moved_markers)
				next_marker=0

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
			
def main():
	global status
	while True:
		while center_code==0:
			distance,angle=find_center()
			turn(20,1)
		if status==0:
			distance,angle=find_token()
		elif status==1:
			distance,angle=find_center()
		if distance==-1:
			turn(20,0.3)
		else:
			move_to_marker(distance,angle)
			
		
			
main()
		
		
	
	


    


