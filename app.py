import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import schedule  # Importing your existing job scheduling implementation

# Streamlit UI
st.set_page_config(page_title="Job Scheduling Optimization", layout="wide")

st.title("📊 Job Scheduling Optimization")
st.write("This app finds the optimal job sequence using Johnson's Algorithm or Palmer's Heuristic.")

# Input Section
num_jobs = st.number_input("Enter number of jobs:", min_value=1, max_value=50, step=1)
num_machines = st.number_input("Enter number of machines:", min_value=2, max_value=25, step=1)

if num_jobs and num_machines:
    st.subheader("📝 Enter Processing Times")
    processing_times = []

    for i in range(num_jobs):
        row = st.text_input(f"Job {i+1} (space-separated values)", value=" ".join(["0"] * num_machines))
        processing_times.append(list(map(int, row.split())))

    processing_times = np.array(processing_times)

    if st.button("Optimize Sequence"):
        jobs = list(range(num_jobs))

        if num_machines == 2:
            sequence = schedule.johnsons_algorithm_2_machines(jobs, processing_times[:, 0], processing_times[:, 1])
            method_used = "Johnson's Algorithm (2 Machines)"
        elif num_machines == 3:
            sequence = schedule.johnsons_algorithm_3_machines(jobs, processing_times[:, 0], processing_times[:, 1], processing_times[:, 2])
            if sequence is None:
                sequence = schedule.palmer_algorithm(processing_times)
                method_used = "Palmer's Heuristic (3 Machines - Condition not satisfied)"
            else:
                method_used = "Johnson's Algorithm (3 Machines)"
        else:
            sequence = schedule.palmer_algorithm(processing_times)
            method_used = "Palmer's Heuristic (More than 3 Machines)"

        sequence_labels = [f"J{i+1}" for i in sequence]
        makespan, schedule_matrix = schedule.calculate_makespan(sequence, processing_times)

        st.success(f"✅ Optimal Sequence: {' → '.join(sequence_labels)}")
        st.info(f"📌 Method Used: {method_used}")
        st.metric("⏳ Total Makespan", f"{makespan} units")

        # Display Schedule Table
        df_schedule = pd.DataFrame(schedule_matrix, index=sequence_labels, columns=[f"Machine {i+1}" for i in range(num_machines)])
        st.write("### 🔢 Processing Schedule")
        st.dataframe(df_schedule.style.format("{:.1f}"))

        # Gantt Chart
        gantt_data = []
        for j_index, job in enumerate(sequence):
            start_time = 0
            for machine in range(num_machines):
                start_time = max(start_time, schedule_matrix[j_index-1][machine] if j_index > 0 else 0)
                gantt_data.append(dict(Task=f"Job {job+1}", Start=start_time, Finish=start_time + processing_times[job][machine], Machine=f"Machine {machine+1}"))
                start_time += processing_times[job][machine]

        df_gantt = pd.DataFrame(gantt_data)

        # Plot Gantt Chart
        st.write("### 📊 Gantt Chart Visualization")
        fig = px.timeline(df_gantt, x_start="Start", x_end="Finish", y="Task", color="Machine", title="Job Scheduling Gantt Chart")
        fig.update_yaxes(categoryorder="total ascending")
        st.plotly_chart(fig, use_container_width=True)