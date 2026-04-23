
# Task 3: Bayesian Network for Disease Prediction
# Reference: Lab09.ipynb Bayesian Network examples

from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define the structure: Disease influences all symptoms
model = DiscreteBayesianNetwork([
	('Disease', 'Fever'),
	('Disease', 'Cough'),
	('Disease', 'Fatigue'),
	('Disease', 'Chills')
])

# CPD for Disease (prior)
cpd_disease = TabularCPD(
	variable='Disease',
	variable_card=2,
	values=[[0.3], [0.7]],  # [Flu, Cold]
	state_names={'Disease': ['Flu', 'Cold']}
)

# CPD for Fever | Disease
cpd_fever = TabularCPD(
	variable='Fever',
	variable_card=2,
	values=[
		[0.9, 0.5],  # Fever=Yes | [Flu, Cold]
		[0.1, 0.5]   # Fever=No  | [Flu, Cold]
	],
	evidence=['Disease'],
	evidence_card=[2],
	state_names={
		'Fever': ['Yes', 'No'],
		'Disease': ['Flu', 'Cold']
	}
)

# CPD for Cough | Disease
cpd_cough = TabularCPD(
	variable='Cough',
	variable_card=2,
	values=[
		[0.8, 0.6],  # Cough=Yes | [Flu, Cold]
		[0.2, 0.4]   # Cough=No  | [Flu, Cold]
	],
	evidence=['Disease'],
	evidence_card=[2],
	state_names={
		'Cough': ['Yes', 'No'],
		'Disease': ['Flu', 'Cold']
	}
)

# CPD for Fatigue | Disease
cpd_fatigue = TabularCPD(
	variable='Fatigue',
	variable_card=2,
	values=[
		[0.7, 0.3],  # Fatigue=Yes | [Flu, Cold]
		[0.3, 0.7]   # Fatigue=No  | [Flu, Cold]
	],
	evidence=['Disease'],
	evidence_card=[2],
	state_names={
		'Fatigue': ['Yes', 'No'],
		'Disease': ['Flu', 'Cold']
	}
)

# CPD for Chills | Disease
cpd_chills = TabularCPD(
	variable='Chills',
	variable_card=2,
	values=[
		[0.6, 0.4],  # Chills=Yes | [Flu, Cold]
		[0.4, 0.6]   # Chills=No  | [Flu, Cold]
	],
	evidence=['Disease'],
	evidence_card=[2],
	state_names={
		'Chills': ['Yes', 'No'],
		'Disease': ['Flu', 'Cold']
	}
)

# Add CPDs to the model
model.add_cpds(cpd_disease, cpd_fever, cpd_cough, cpd_fatigue, cpd_chills)

# Check model validity
assert model.check_model(), "Model is incorrect"

# Inference engine
infer = VariableElimination(model)

# --- Inference Task 1 ---
# P(Disease | Fever=Yes, Cough=Yes)
result1 = infer.query(
	variables=['Disease'],
	evidence={'Fever': 'Yes', 'Cough': 'Yes'}
)
print("Task 1: P(Disease | Fever=Yes, Cough=Yes)")
print(result1)

# --- Inference Task 2 ---
# P(Disease | Fever=Yes, Cough=Yes, Chills=Yes)
result2 = infer.query(
	variables=['Disease'],
	evidence={'Fever': 'Yes', 'Cough': 'Yes', 'Chills': 'Yes'}
)
print("\nTask 2: P(Disease | Fever=Yes, Cough=Yes, Chills=Yes)")
print(result2)

# --- Inference Task 3 ---
# P(Fatigue=Yes | Disease=Flu)
result3 = infer.query(
	variables=['Fatigue'],
	evidence={'Disease': 'Flu'}
)
print("\nTask 3: P(Fatigue=Yes | Disease=Flu)")
print(f"P(Fatigue=Yes | Disease=Flu): {result3.values[0]:.2f}")
