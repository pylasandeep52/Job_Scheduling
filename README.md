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

## 1️⃣ Installation

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

## 2️⃣ Running the Application

### Run Flask API (app.py)
```sh
python app.py
```
API will run at `http://127.0.0.1:5000/`.

### Run Job Scheduling Script (schedule.py)
```sh
python schedule.py
```
This script asks for user input and calculates the optimal job sequence.

---

## 3️⃣ API Endpoints

### `POST /schedule`
- **Description**: Accepts job processing times and returns an optimal job sequence and makespan.
- **Request JSON Format:**
```json
{
  "processing_times": [
    [5, 8, 7],
    [3, 6, 9],
    [4, 5, 8]
  ]
}
```
- **Response JSON Format:**
```json
{
  "sequence": ["J2", "J1", "J3"],
  "makespan": 20,
  "schedule": [[5, 13, 20], [8, 14, 23], [12, 19, 28]]
}
```

---

## 4️⃣ Workflow

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

## 5️⃣ Future Scope 🚀
- ✅ Implement **NEH Heuristic Algorithm** for flow shop scheduling.
- ✅ Optimize job sequences using **Genetic Algorithm**.
- ✅ Extend to **Dynamic Job Scheduling** with real-time job insertion.
- ✅ Provide **Graphical Visualization** for schedules.

---

## 6️⃣ Contributing
Feel free to contribute to this project! Open an issue or submit a pull request.

---

## 7️⃣ Author
👤 **Pyla Sandeep**  
📧 [GitHub](https://github.com/pylasandeep52)

---

## 8️⃣ License
This project is licensed under the MIT License.

