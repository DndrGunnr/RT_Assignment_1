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
def count_tokens():
	global moved_markers
	seen_list=[]
	for i in range (1,8):
		for token in R.see():
			if token.info.code not in seen_list:
				#adding silver tokens to the moved list as to ignore them for the grabbing phase
				if token.info.marker_type==MARKER_TOKEN_SILVER:
					moved_markers.append(token.info.code)
				seen_list.append(token.info.code)
		turn(20,1)
	return seen_list

def find_token():
	global next_marker
	distance=100
	'''when a marker has been released or when the simulation starts'''
	if next_marker==0:
		for token in R.see():
			'''check if the seen marker is already been moved'''
			if token.info.code not in moved_markers:
				'''choosing next marker as nearest unmoved marker'''
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
	for token in R.see():
		if token.info.code==center_code:
			distance=token.dist
			angle=token.rot_y
	if distance<100:
		return distance,angle
	else:
		return -1,-1

def find_closest_silver():
	global center_code
	distance=100
	#make a full scan around robot
	for i in range(1,8):
		for token in R.see():
			if token.info.marker_type==MARKER_TOKEN_SILVER:
				if token.dist<distance:
					#the found token sets the lowest distance to robot
					distance=token.dist
					center_code=token.info.code
		turn(20,1)
	
	
		
def move_to_marker(distance, angle):
	global status,moved_markers,next_marker,status
	if angle<-a_th:
		turn(-2*distance,0.1)
	elif angle>a_th:
		turn(2*distance,0.1)
	else:
		'''status varible used to change threshold based on the target'''
		if distance>d_th+status*0.3:
			drive(100,0.02)
		else:
			#grab phase
			if status==0:
				R.grab()
				'''step back to avoid unnecesarely moving possible neighbour blocks'''
				drive(-75,0.3)
				#once the robot has grabbed a token, it starts looking for closest silver token
				find_closest_silver()
				status=1
				print("status= ",status)
			#group phase
			else:
				R.release()
				drive(-75,0.3)
				status=0
				print("status= ",status)
				moved_markers.append(next_marker)
				print("moved markers= ",moved_markers)
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
	seen_token=count_tokens()
	print("token list= ",seen_token)
	while len(moved_markers)<len(seen_token):
		if status==0:
			distance,angle=find_token()
		elif status==1:
			distance,angle=find_center()
		'''if nothing is in sight, turn slightly right'''
		if distance==-1:
			turn(40,0.05)
		else:
			move_to_marker(distance,angle)
	exit()
		
			
main()
		
		
	
	


    


