class SmartLight:
	def __init__(self, room_name):
		self.room_name = room_name
		self.status = 'OFF'

	def turn_on(self):
		self.status = 'ON'
		print(f"{self.room_name} light turned ON.")

	def turn_off(self):
		self.status = 'OFF'
		print(f"{self.room_name} light turned OFF.")

	def display_status(self):
		print(f"{self.room_name} light is {self.status}.")


living_room = SmartLight("Living Room")
bedroom = SmartLight("Bedroom")

living_room.turn_on()
bedroom.turn_off()

living_room.display_status()
bedroom.display_status()
