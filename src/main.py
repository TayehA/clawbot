#region VEXcode Generated Robot Configuration

from vex import *
from userInstance import user_control
from autonomous import autonomous

# Brain should be defined by default
brain=Brain()

# Robot configuration code
Arm = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
claw = Motor(Ports.PORT8, GearSetting.RATIO_18_1, True)
left_motor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
right_motor = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
controller_1 = Controller(PRIMARY)


# wait for rotation sensor to fully initialize
wait(30, MSEC)



# define variables used for controlling motors based on controller inputs
controller_1_left_shoulder_control_motors_stopped = True
controller_1_right_shoulder_control_motors_stopped = True

# define a task that will handle monitoring inputs from controller_1
def rc_auto_loop_function_controller_1():
    global controller_1_left_shoulder_control_motors_stopped, controller_1_right_shoulder_control_motors_stopped, remote_control_code_enabled
    # process the controller input every 20 milliseconds
    # update the motors based on the input values
    while True:
        if remote_control_code_enabled:
            # check the buttonL1/buttonL2 status
            # to control Arm
            if controller_1.buttonL1.pressing():
                Arm.spin(FORWARD)
                controller_1_left_shoulder_control_motors_stopped = False
            elif controller_1.buttonL2.pressing():
                Arm.spin(REVERSE)
                controller_1_left_shoulder_control_motors_stopped = False
            elif not controller_1_left_shoulder_control_motors_stopped:
                Arm.stop()
                # set the toggle so that we don't constantly tell the motor to stop when
                # the buttons are released
                controller_1_left_shoulder_control_motors_stopped = True
            # check the buttonR1/buttonR2 status
            # to control claw
            if controller_1.buttonR1.pressing():
                claw.spin(FORWARD)
                controller_1_right_shoulder_control_motors_stopped = False
            elif controller_1.buttonR2.pressing():
                claw.spin(REVERSE)
                controller_1_right_shoulder_control_motors_stopped = False
            elif not controller_1_right_shoulder_control_motors_stopped:
                claw.stop()
                # set the toggle so that we don't constantly tell the motor to stop when
                # the buttons are released
                controller_1_right_shoulder_control_motors_stopped = True
        # wait before repeating the process
        wait(20, MSEC)

# define variable for remote controller enable/disable
remote_control_code_enabled = True

rc_auto_loop_thread_controller_1 = Thread(rc_auto_loop_function_controller_1)
#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
# 	Project:clawbot autonomous/usercontrol for VRC tippingpoint
#	Author:Ameer Tayeh
#	Created:long time ago
#	Configuration:
# 
# ------------------------------------------

# Library imports
from vex import *

# Begin project code

class initMain:
    
    def getController():#type: ignore
        return controller_1

    def getClaw():#type: ignore
        return claw

    def getArm():#type: ignore
        return Arm

    def rightMotor():#type: ignore
        return right_motor

    def leftMotor():#type: ignore
        return left_motor

def pre_autonomous():
    # actions to do when the program starts
    brain.screen.clear_screen()
    brain.screen.print("pre auton code")
    wait(1, SECONDS)

                
         
# create competition instance
comp = Competition(user_control, autonomous)
pre_autonomous()

