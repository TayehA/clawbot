from vex import *
from main import initMain




Arm=initMain.getArm() 
claw=initMain.getClaw() 
left_motor=initMain.leftMotor() 
right_motor=initMain.rightMotor() 
controller_1=initMain.getController()  


brain= Brain()



def user_control():
    



    brain= Brain()
    brain.screen.clear_screen()
    # place driver control in this while loop
    while True:
        wait(20, MSEC)



        #speeded controls
        if controller_1.buttonUp.pressing()==True:
            left_motor.set_velocity(100, PERCENT)
            right_motor.set_velocity(100, PERCENT)
            left_motor.spin(FORWARD)
            right_motor.spin(FORWARD)

        elif controller_1.buttonDown.pressing()==True:
            left_motor.set_velocity(100, PERCENT)
            right_motor.set_velocity(100, PERCENT)
            left_motor.spin(REVERSE)
            right_motor.spin(REVERSE)
            

        elif controller_1.buttonLeft.pressing()==True:
            left_motor.set_velocity(100, PERCENT)
            left_motor.spin(FORWARD)
        elif controller_1.buttonRight.pressing()==True:
            right_motor.set_velocity(100, PERCENT)
            right_motor.spin(FORWARD)

        elif controller_1.buttonL1.pressing()==True:
            Arm.set_velocity(50, PERCENT) 
            Arm.spin(FORWARD)


        elif controller_1.buttonR1.pressing()==True:
            Arm.set_velocity(30, PERCENT)
            Arm.spin(REVERSE)

            Arm.set_stopping(HOLD)

        elif controller_1.buttonL2.pressing()==True:
            claw.set_velocity(100)
            claw.spin(FORWARD)


        elif controller_1.buttonR2.pressing()==True:
            claw.set_velocity(100)
            claw.spin(REVERSE)

            
        else:
            #joysticks
            left_motor.set_velocity(controller_1.axis3.position())
            right_motor.set_velocity(controller_1.axis2.position())
            left_motor.spin(FORWARD)
            right_motor.spin(FORWARD)
            claw.set_velocity(0,PERCENT)
            Arm.set_velocity(0, PERCENT)
            Arm.set_stopping(HOLD)
