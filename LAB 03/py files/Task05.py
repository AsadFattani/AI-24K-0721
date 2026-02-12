class HospitalEnvironment:
    def __init__(self, rooms, nurse_stations, medicine_storage, patient_schedule, staff_availability):
        self.rooms = rooms
        self.nurse_stations = nurse_stations
        self.medicine_storage = medicine_storage
        self.patient_schedule = patient_schedule
        self.staff_availability = staff_availability

class HospitalDeliveryRobot:
    def __init__(self, env):
        self.env = env
        self.location = 'medicine_storage'
        self.carrying_medicine = None

    def move_to(self, location):
        print(f"Moving to {location}")
        self.location = location

    def pick_up_medicine(self, medicine_type):
        if self.location == self.env.medicine_storage:
            print(f"Picking up medicine: {medicine_type}")
            self.carrying_medicine = medicine_type
        else:
            print("Robot must be at medicine storage to pick up medicine.")

    def scan_patient_id(self, patient_id):
        print(f"Scanning patient ID: {patient_id}")
        return True

    def deliver_medicine(self, room):
        if self.location == room and self.carrying_medicine:
            print(f"Delivering medicine to room {room}")
            self.carrying_medicine = None
        else:
            print("Robot must be at the correct room and carrying medicine to deliver.")

    def alert_staff(self, message):
        print(f"Alerting staff: {message}")

    def act(self):
        for room, deliveries in self.env.patient_schedule.items():
            for time, medicine_type, patient_id in deliveries:
                if self.location != self.env.medicine_storage:
                    self.move_to(self.env.medicine_storage)
                self.pick_up_medicine(medicine_type)
                self.move_to(room)
                if self.scan_patient_id(patient_id):
                    self.deliver_medicine(room)
                else:
                    self.alert_staff(f"Patient ID mismatch in room {room}")
            print()

rooms = ['101', '102', '103']
nurse_stations = ['NS1', 'NS2']
medicine_storage = 'medicine_storage'
patient_schedule = {
    '101': [('09:00', 'Painkiller', 'PID101')],
    '102': [('09:30', 'Antibiotic', 'PID102')],
}
staff_availability = {'Nurse1': True, 'Doctor1': True}

env = HospitalEnvironment(rooms, nurse_stations, medicine_storage, patient_schedule, staff_availability)
robot = HospitalDeliveryRobot(env)
robot.act()


