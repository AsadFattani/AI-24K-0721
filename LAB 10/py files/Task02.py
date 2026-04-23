# Task 2: Bayesian Network for Student Exam Performance
# Dependencies: pip install pgmpy
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define the Bayesian Network structure
model = DiscreteBayesianNetwork([
	('Intelligence', 'Grade'),
	('StudyHours', 'Grade'),
	('Difficulty', 'Grade'),
	('Grade', 'Pass')
])

# CPD for Intelligence
cpd_intelligence = TabularCPD(
	variable='Intelligence',
	variable_card=2,
	values=[[0.7], [0.3]],  # [High, Low]
	state_names={'Intelligence': ['High', 'Low']}
)

# CPD for StudyHours
cpd_studyhours = TabularCPD(
	variable='StudyHours',
	variable_card=2,
	values=[[0.6], [0.4]],  # [Sufficient, Insufficient]
	state_names={'StudyHours': ['Sufficient', 'Insufficient']}
)

# CPD for Difficulty
cpd_difficulty = TabularCPD(
	variable='Difficulty',
	variable_card=2,
	values=[[0.4], [0.6]],  # [Hard, Easy]
	state_names={'Difficulty': ['Hard', 'Easy']}
)

# CPD for Grade (I, S, D) -> G
# Order: I=High, S=Sufficient, D=Hard; I=High, S=Sufficient, D=Easy; ...
# [A, B, C] for each combination
cpd_grade = TabularCPD(
	variable='Grade',
	variable_card=3,
	values=[
		# A
		[0.7, 0.8, 0.5, 0.6, 0.5, 0.6, 0.3, 0.4],
		# B
		[0.2, 0.15, 0.3, 0.25, 0.3, 0.25, 0.4, 0.4],
		# C
		[0.1, 0.05, 0.2, 0.15, 0.2, 0.15, 0.3, 0.2],
	],
	evidence=['Intelligence', 'StudyHours', 'Difficulty'],
	evidence_card=[2, 2, 2],
	state_names={
		'Grade': ['A', 'B', 'C'],
		'Intelligence': ['High', 'Low'],
		'StudyHours': ['Sufficient', 'Insufficient'],
		'Difficulty': ['Hard', 'Easy']
	}
)

# CPD for Pass (G) -> P
cpd_pass = TabularCPD(
	variable='Pass',
	variable_card=2,
	values=[
		# Yes, No
		[0.95, 0.8, 0.5],  # Yes: [A, B, C]
		[0.05, 0.2, 0.5],  # No: [A, B, C]
	],
	evidence=['Grade'],
	evidence_card=[3],
	state_names={
		'Pass': ['Yes', 'No'],
		'Grade': ['A', 'B', 'C']
	}
)

# Add CPDs to the model
model.add_cpds(cpd_intelligence, cpd_studyhours, cpd_difficulty, cpd_grade, cpd_pass)

# Check if the model is valid
assert model.check_model()

# Perform inference
infer = VariableElimination(model)

# Query 1: P(Pass | StudyHours=Sufficient, Difficulty=Hard)
result1 = infer.query(
	variables=['Pass'],
	evidence={'StudyHours': 'Sufficient', 'Difficulty': 'Hard'}
)
print('P(Pass | StudyHours=Sufficient, Difficulty=Hard):')
print(result1)

# Query 2: P(Intelligence=High | Pass=Yes)
result2 = infer.query(
	variables=['Intelligence'],
	evidence={'Pass': 'Yes'}
)
print('\nP(Intelligence=High | Pass=Yes):')
print(result2)
