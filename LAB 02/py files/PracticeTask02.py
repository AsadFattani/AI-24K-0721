class Staff:
	def __init__(self, name, staff_id, department):
		self.name = name
		self.staff_id = staff_id
		self.department = department

	def display_info(self):
		print(f"Name: {self.name}\nStaff ID: {self.staff_id}\nDepartment: {self.department}")

class Teacher(Staff):
	def __init__(self, name, staff_id, department, courses, salary):
		super().__init__(name, staff_id, department)
		self.courses = courses  # list of courses
		self.salary = salary

	def teach_course(self):
		for course in self.courses:
			print(f"{self.name} is teaching {course}.")

	def display_info(self):
		super().display_info()
		print(f"Type: Teacher\nCourses: {', '.join(self.courses)}\nSalary: {self.salary}")

class AdminStaff(Staff):
	def __init__(self, name, staff_id, department, role, working_hours):
		super().__init__(name, staff_id, department)
		self.role = role
		self.working_hours = working_hours

	def perform_task(self, task):
		print(f"{self.name} ({self.role}) is performing task: {task}.")

	def display_info(self):
		super().display_info()
		print(f"Type: Admin Staff\nRole: {self.role}\nWorking Hours: {self.working_hours}")

class ResearchAssistant(Staff):
	def __init__(self, name, staff_id, department, research_topic, stipend):
		super().__init__(name, staff_id, department)
		self.research_topic = research_topic
		self.stipend = stipend

	def work_on_research(self):
		print(f"{self.name} is working on research topic: {self.research_topic}.")

	def display_info(self):
		super().display_info()
		print(f"Type: Research Assistant\nResearch Topic: {self.research_topic}\nStipend: {self.stipend}")

teacher = Teacher("Sherlock Holmes", "T123", "Literature", ["Detective Fiction", "Mystery Writing"], 5000)
admin = AdminStaff("dr. Watson", "A456", "Administration", "Registrar", "9 AM - 5 PM")
ra = ResearchAssistant("James Moriarty", "R789", "Criminology", "Advanced Crime Theories", 3000)

teacher.display_info()
teacher.teach_course()
print()
admin.display_info()
admin.perform_task("Process student applications")
print()
ra.display_info()
ra.work_on_research()
