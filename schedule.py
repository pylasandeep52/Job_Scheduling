import numpy as np

# Johnson's Algorithm for 2 Machines
def johnsons_algorithm_2_machines(jobs, machine1, machine2):
    sequence = []
    job_data = list(zip(jobs, machine1, machine2))

    list1 = []  # Jobs where machine1 time <= machine2 time
    list2 = []  # Jobs where machine1 time > machine2 time

    for job in job_data:
        if job[1] <= job[2]:
            list1.append(job)
        else:
            list2.append(job)

    # Sort list1 in increasing order of machine1 time
    list1.sort(key=lambda x: x[1])
    # Sort list2 in decreasing order of machine2 time
    list2.sort(key=lambda x: x[2], reverse=True)

    # Combine the two lists
    sequence = [job[0] for job in list1 + list2]

    return sequence


# Johnson's Algorithm for 3 Machines
def johnsons_algorithm_3_machines(jobs, machine1, machine2, machine3):
    if min(machine1) >= max(machine2) or min(machine3) >= max(machine2):
        machine_g = [machine1[i] + machine2[i] for i in range(len(jobs))]
        machine_h = [machine2[i] + machine3[i] for i in range(len(jobs))]
        return johnsons_algorithm_2_machines(jobs, machine_g, machine_h)
    else:
        return None  # Condition not satisfied


# Palmer's Heuristic
def palmer_algorithm(processing_times):
    num_jobs, num_machines = len(processing_times), len(processing_times[0])
    weights = [-(num_machines - 1 - 2 * i) for i in range(num_machines)]
    slope_indices = [sum(p * w for p, w in zip(job, weights)) for job in processing_times]
    job_order = sorted(range(num_jobs), key=lambda j: slope_indices[j], reverse=True)
    return job_order


# Calculate Makespan
def calculate_makespan(sequence, processing_times):
    num_jobs, num_machines = len(sequence), len(processing_times[0])
    schedule = np.zeros((num_jobs, num_machines))

    for j_index, job in enumerate(sequence):
        for machine in range(num_machines):
            if machine == 0:
                schedule[j_index][machine] = (
                    schedule[j_index-1][machine] if j_index > 0 else 0
                ) + processing_times[job][machine]
            else:
                schedule[j_index][machine] = max(
                    schedule[j_index-1][machine] if j_index > 0 else 0,
                    schedule[j_index][machine-1]
                ) + processing_times[job][machine]

    makespan = schedule[-1][-1]
    return makespan, schedule


# Main Function
def main():
    num_jobs = int(input("Enter the number of jobs: "))
    num_machines = int(input("Enter the number of machines (2, 3, or more): "))

    processing_times = []
    print("Enter the processing times row-wise (space-separated values):")
    for i in range(num_jobs):
        row = input().split()
        if len(row) != num_machines or not all(val.isdigit() for val in row):
            print(f"Invalid input for Job {i+1}. Please enter {num_machines} space-separated integers.")
            return
        processing_times.append(list(map(int, row)))

    processing_times = np.array(processing_times)

    if num_machines == 2:
        sequence = johnsons_algorithm_2_machines(range(num_jobs), processing_times[:, 0], processing_times[:, 1])
    elif num_machines == 3:
        sequence = johnsons_algorithm_3_machines(range(num_jobs), processing_times[:, 0], processing_times[:, 1], processing_times[:, 2])
        if sequence is None:
            print("Johnson's algorithm conditions not satisfied. Using Palmer's heuristic.")
            sequence = palmer_algorithm(processing_times)
    else:
        sequence = palmer_algorithm(processing_times)

    makespan, schedule = calculate_makespan(sequence, processing_times)

    print("\nOptimal Job Sequence:", [f"J{i+1}" for i in sequence])
    print("\nSchedule Matrix:\n", schedule)
    print(f"\nTotal Makespan Time: {makespan}")

if __name__ == "__main__":
    main()
