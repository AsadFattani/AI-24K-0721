from typing import List, Tuple, Dict
import heapq

class Job:
	def __init__(self, job_id: int, exec_time: int, priority: int):
		self.job_id = job_id
		self.exec_time = exec_time
		self.priority = priority

class Processor:
	def __init__(self, proc_id: int):
		self.proc_id = proc_id
		self.load = 0
		self.jobs = []

def beam_search_allocate(jobs: List[Job], num_processors: int, beam_width: int = 3) -> Dict[int, List[int]]:
	# Initial state: all jobs unassigned, all processors empty
	initial_state = ([[] for _ in range(num_processors)], [0]*num_processors, set(range(len(jobs))))
	# State: (job_assignments, processor_loads, remaining_jobs)
	# Use a min-heap for beam
	beam = [(score_state(initial_state, jobs), initial_state)]

	for _ in range(len(jobs)):
		next_beam = []
		for _, (assignments, loads, remaining) in beam:
			for job_idx in remaining:
				for proc_idx in range(num_processors):
					# Copy state
					new_assignments = [a.copy() for a in assignments]
					new_loads = loads[:]
					new_remaining = set(remaining)
					# Assign job
					new_assignments[proc_idx].append(job_idx)
					new_loads[proc_idx] += jobs[job_idx].exec_time
					new_remaining.remove(job_idx)
					new_state = (new_assignments, new_loads, new_remaining)
					heapq.heappush(next_beam, (score_state(new_state, jobs), new_state))
		# Keep only top beam_width states
		beam = heapq.nsmallest(beam_width, next_beam)

	# Choose the best allocation
	best_score, (best_assignments, _, _) = min(beam, key=lambda x: x[0])
	# Convert to job id lists
	allocation = {i: [jobs[j].job_id for j in best_assignments[i]] for i in range(num_processors)}
	return allocation

def score_state(state, jobs: List[Job]) -> float:
	assignments, loads, remaining = state
	# Minimize max load, but also consider priorities (lower is better)
	max_load = max(loads) if loads else 0
	# Penalize unassigned high-priority jobs
	priority_penalty = sum(jobs[j].priority for j in remaining)
	return max_load + 0.1 * priority_penalty

# Example usage
jobs = [Job(1, 5, 1), Job(2, 3, 2), Job(3, 2, 1), Job(4, 7, 3)]
num_processors = 2
allocation = beam_search_allocate(jobs, num_processors, beam_width=3)
print("Task allocation (processor: [job ids]):")
for proc, job_ids in allocation.items():
	print(f"Processor {proc}: {job_ids}")
