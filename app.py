import streamlit as st
import numpy as np
import schedule

st.title("Job Scheduling Optimization")

# Input: Number of Jobs and Machines
num_jobs = st.number_input("Enter the number of jobs:", min_value=1, step=1, value=3)
num_machines = st.number_input("Enter the number of machines:", min_value=2, step=1, value=3)

# Input: Processing Times
processing_times = []
st.subheader("Enter Processing Times:")
for i in range(num_jobs):
    row = st.text_input(f"Processing times for Job {i+1} (space-separated)", value=" ".join(["0"] * num_machines))
    try:
        row_values = list(map(int, row.split()))
        if len(row_values) != num_machines:
            st.error(f"❌ Job {i+1}: Please enter exactly {num_machines} numbers.")
            st.stop()
        processing_times.append(row_values)
    except ValueError:
        st.error(f"❌ Job {i+1}: Invalid input. Please enter only integers.")
        st.stop()

processing_times = np.array(processing_times)

# Run Scheduling Algorithms
if st.button("Compute Optimal Job Sequence"):
    sequence = None

    if num_machines == 2:
        sequence = schedule.johnsons_algorithm_2_machines(
            range(num_jobs), processing_times[:, 0], processing_times[:, 1]
        )
        st.success("✅ Using Johnson's Algorithm (2 Machines)")
    elif num_machines == 3:
        sequence = schedule.johnsons_algorithm_3_machines(
            range(num_jobs), processing_times[:, 0], processing_times[:, 1], processing_times[:, 2]
        )
        if sequence is None:
            st.warning("⚠️ Johnson's Algorithm conditions not met. Using Palmer's heuristic.")
            sequence = schedule.palmer_algorithm(processing_times)
    else:
        st.info("ℹ️ More than 3 machines detected. Using Palmer's heuristic.")
        sequence = schedule.palmer_algorithm(processing_times)

    if sequence is not None:
        st.subheader("🔢 Optimal Job Sequence:")
        sequence_labels= [f"J{i+1}" for i in sequence]

        # Compute Makespan
        makespan, job_schedule = schedule.calculate_makespan(sequence, processing_times)
        st.success(f"✅ Optimal Sequence: {' → '.join(sequence_labels)}")
        st.subheader("⏳ Makespan Time:")
        st.write(f"Total Makespan: {makespan}")

        st.subheader("📊 Schedule Matrix:")
        st.write(job_schedule)
    else:
        st.error("❌ Unable to compute job sequence.")
