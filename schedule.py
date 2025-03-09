import numpy as np

# Johnson's Algorithm for 2 Machines
def johnsons_algorithm_2_machines(jobs, machine1, machine2):
    sequence = []
    job_data = list(zip(jobs, machine1, machine2))

    # Separate jobs into two lists based on the minimum processing time
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
    # Check if the condition for Johnson's algorithm for 3 machines is satisfied
    if min(machine1) >= max(machine2) or min(machine3) >= max(machine2):
        # Create virtual machines G and H
        machine_g = [machine1[i] + machine2[i] for i in range(len(jobs))]
        machine_h = [machine2[i] + machine3[i] for i in range(len(jobs))]
        # Apply Johnson's algorithm for 2 machines
        return johnsons_algorithm_2_machines(jobs, machine_g, machine_h)
    else:
        return None  # Condition not satisfied


# Palmer's Heuristic
def palmer_algorithm(processing_times):
    num_jobs, num_machines = len(processing_times), len(processing_times[0])

    # Generate symmetric even weights
    weights = [-(num_machines - 1 - 2 * i) for i in range(num_machines)]

    # Compute slope index for each job
    slope_indices = [sum(p * w for p, w in zip(job, weights)) for job in processing_times]

    # Sort job order based on slope index values in descending order
    job_order = sorted(range(num_jobs), key=lambda j: slope_indices[j], reverse=True)

    return job_order


# Calculate Makespan
def calculate_makespan(sequence, processing_times):
    num_jobs, num_machines = len(sequence), len(processing_times[0])
    schedule = np.zeros((num_jobs, num_machines))

    for j_index, job in enumerate(sequence):
        for machine in range(num_machines):
            if machine == 0:
                # First machine: add to previous job's completion time
                schedule[j_index][machine] = (schedule[j_index-1][machine] if j_index > 0 else 0) + processing_times[job][machine]
            else:
                # Subsequent machines: wait for the current job's previous machine or the previous job's current machine
                schedule[j_index][machine] = max(schedule[j_index-1][machine], schedule[j_index][machine-1]) + processing_times[job][machine]

    makespan = schedule[-1][-1]
    return makespan, schedule


# Main Function
def main():
    # Input number of jobs and machines
    num_jobs = int(input("Enter the number of jobs: "))
    num_machines = int(input("Enter the number of machines (2, 3, or more): "))

    # Input processing times
    processing_times = []
    print("Enter the processing times row-wise (each job on a new line, space-separated values):")
    for i in range(num_jobs):
        processing_times.append(list(map(int, input().split())))

    # Convert processing times to a numpy array for easier manipulation
    processing_times = np.array(processing_times)

    # Apply Johnson's algorithm for 2 or 3 machines, otherwise Palmer's heuristic
    if num_machines == 2:
        machine1 = processing_times[:, 0]
        machine2 = processing_times[:, 1]
        sequence = johnsons_algorithm_2_machines(range(num_jobs), machine1, machine2)
        print("Optimal job sequence (Johnson's algorithm):", [f"J{i+1}" for i in sequence])
    elif num_machines == 3:
        machine1 = processing_times[:, 0]
        machine2 = processing_times[:, 1]
        machine3 = processing_times[:, 2]
        sequence = johnsons_algorithm_3_machines(range(num_jobs), machine1, machine2, machine3)
        if sequence is None:
            print("Johnson's algorithm conditions not satisfied. Using Palmer's heuristic.")
            sequence = palmer_algorithm(processing_times)
        else:
            print("Optimal job sequence (Johnson's algorithm):", [f"J{i+1}" for i in sequence])
    else:
        print("Using Palmer's heuristic for more than 3 machines.")
        sequence = palmer_algorithm(processing_times)
        print("Optimal job sequence (Palmer's heuristic):", [f"J{i+1}" for i in sequence])

    # Calculate makespan and schedule
    makespan, schedule = calculate_makespan(sequence, processing_times)
    print("\nDetailed Schedule:")
    print(schedule)
    print(f"\nTotal Makespan Time: {makespan}")


# Run the main function
if __name__ == "__main__":
    main()