import wpilib
from wpilib import Talon


class Intake:

	power = 1.0

	def __init__(self,left_cim, right_cim):

		self.left_cim = left_cim
		self.right_cim = right_cim

	def drive_cim(self, left_output, right_output):

		left_output *= self.power
		right_output *= self.power

		self.left_cim.set(-left_output)
		self.right_cim.set(right_output)

	def vision_based_drive(self,left_output, right_output)
		if Vision.identifiy_object='baseball detected'
			Intake.drive_cim

	def vision_based_pickeup(self,left_output,right_output,Vision)
		if Vision.identifiy_object='baseball'

			Intake

			


 