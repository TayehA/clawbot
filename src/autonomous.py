from vex import *
from main import initMain





Arm=initMain.getArm() 
claw=initMain.getClaw() 
left_motor=initMain.leftMotor() 
right_motor=initMain.rightMotor() 
controller_1=initMain.getController()  


brain= Brain()
def autonomous():
    brain.screen.clear_screen()
    brain.screen.print("autonomous code")
    # place automonous code here
    #speed

    left_motor.set_velocity(70, PERCENT)
    right_motor.set_velocity(70, PERCENT)
    Arm.set_velocity(70,PERCENT)
    claw.set_velocity(60, PERCENT)

    #Force control 
    #KELVIN IF FOR SOME REASON YOU SEE THIS DO NOT TOUCH BEFORE READING WHAT THIS FUNCTION DOES



    #plan
    #Put the preoaded ring in the allince goal
    #get another ring
    #put that ring in the other goal
    #simple


    #movements
    
    claw.spin_for(REVERSE, 0.5, TURNS, wait=False)
    wait(0.4, SECONDS)
    Arm.spin_for(FORWARD, 1, TURNS, wait=True)
    wait(0.4, SECONDS)
    left_motor.spin_for(FORWARD, 4, TURNS, wait=True)
    wait(0.5, SECONDS)
    claw.spin_for(FORWARD, 0.5, TURNS, wait=True)

    
    #GOAL 1 COMPLETE


    wait(0.1, SECONDS)
