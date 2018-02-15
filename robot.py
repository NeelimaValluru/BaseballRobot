import wpilib
from wpilib.drive import DifferentialDrive

class MyRobot(wpilib.IterativeRobot):
    
    def robotInit(self):
       
        
        self.frontLeftMotor = wpilib.Talon(1)
        self.rearLeftMotor = wpilib.Talon(12)
        self.frontRightMotor = wpilib.Talon(2)
        self.rearRightMotor = wpilib.Talon(5)

        self.left = wpilib.SpeedControllerGroup(self.frontLeftMotor, self.rearLeftMotor)
        self.right = wpilib.SpeedControllerGroup(self.frontRightMotor, self.rearRightMotor)

        self.myRobot = DifferentialDrive(self.left, self.right)
        self.myRobot.setExpiration(0.1)
        
        # joysticks 1 & 2 on the driver station
        self.leftStick = wpilib.Joystick(0)
        self.rightStick = wpilib.Joystick(1)
    
    def teleopInit(self):
        '''Executed at the start of teleop mode'''
        self.myRobot.setSafetyEnabled(True)

    def teleopPeriodic(self):
        '''Runs the motors with tank steering'''
        self.myRobot.tankDrive(self.leftStick.getY() * -1, self.rightStick.getY() * -1)
            
if __name__ == '__main__':
    wpilib.run(MyRobot)
