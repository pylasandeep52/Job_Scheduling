# Job Scheduling Optimization

## Overview
This project implements **Johnson's Algorithm** (for 2 & 3 machines) and **Palmer's Heuristic** (for more than 3 machines) to optimize job scheduling and minimize makespan. The project provides an API (`app.py`) and a scheduling module (`schedule.py`) to determine the optimal job sequence.

## Features
- **Johnson’s Algorithm** (2 & 3 Machines)
- **Palmer’s Heuristic** (More than 3 Machines)
- **Makespan Calculation** (Total Completion Time)
- **Flask API for Integration**
- **User Input Support** (Jobs & Machines Processing Time)

---

## 1) Installation

Clone the repository and navigate to the project folder:
```sh
# Clone the repository
git clone https://github.com/pylasandeep52/Job_Scheduling.git

# Navigate into the project folder
cd Job_Scheduling
```

Install dependencies:
```sh
pip install -r requirements.txt
```

---

## 2) Workflow

1. **User Inputs** number of jobs, machines, and processing times.
2. **Algorithm Selection**:
   - Johnson’s Algorithm for 2 & 3 machines.
   - Palmer’s Heuristic for more than 3 machines.
3. **Optimal Sequence Calculation**:
   - Orders jobs based on processing time constraints.
4. **Makespan Calculation**:
   - Determines the total completion time for all jobs.
5. **API Returns Results** (if using `app.py`).

---

## 3) Future Scope 🚀
- ✅ Implement **NEH Heuristic Algorithm** for flow shop scheduling.
- ✅ Optimize job sequences using **Genetic Algorithm**.
- ✅ Extend to **Dynamic Job Scheduling** with real-time job insertion.
- ✅ Provide **Graphical Visualization** for schedules.

---


## 4) Author
👤 **Pyla Sandeep**  
📧 [GitHub](https://github.com/pylasandeep52)

---



