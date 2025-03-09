# Job Scheduling Optimization

## Overview
This project implements **Job Scheduling** using various scheduling algorithms like **Johnson's Algorithm (for 2 & 3 machines)** and **Palmer's Heuristic** for optimizing job sequences. It provides an interactive **Streamlit-based web interface** for users to input job details and visualize the results.

## Features
- **Johnson's Algorithm for 2 Machines**: Determines an optimal sequence based on minimum processing times.
- **Johnson's Algorithm for 3 Machines**: Checks feasibility conditions and creates a virtual two-machine model if applicable.
- **Palmer's Heuristic**: Used for scheduling when jobs involve more than three machines.
- **Makespan Calculation**: Computes the total time required for job completion.
- **Streamlit Web Interface**: Allows users to enter job details and visualize optimized sequences.

## Project Structure
```
Job_Scheduling/
│── app.py  # Streamlit web application
│── schedule.py  # Core scheduling logic
│── requirements.txt  # Required dependencies
│── README.md  # Project documentation
```

## Installation
### Prerequisites
Ensure you have **Python 3.8+** and **pip** installed.

### Steps to Install and Run
```sh
# Clone the repository
git clone https://github.com/pylasandeep52/Job_Scheduling.git
cd Job_Scheduling

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

## API Workflow
1. **User Input**: The user provides job processing times.
2. **Algorithm Selection**: Based on the number of machines:
   - `Johnson's Algorithm` (for 2 or 3 machines, if conditions are met)
   - `Palmer's Heuristic` (for more than 3 machines or if Johnson's conditions fail)
3. **Makespan Calculation**: Computes the minimum completion time for the optimal sequence.
4. **Results Display**: Presents the optimized sequence and Gantt chart via Streamlit.

## Example Input (CLI Mode)
```
Enter the number of jobs: 4
Enter the number of machines: 3
Enter the processing times row-wise:
5 8 7
6 4 9
3 7 5
8 6 2
```

## Example Output
```
Optimal Job Sequence: J3 → J1 → J2 → J4
Total Makespan Time: 26
```

## Future Scope
- **Enhancing Visualization**: Add Gantt chart representations for better visualization.
- **Dynamic Algorithm Selection**: Implement AI-based scheduling optimization.
- **Cloud Integration**: Deploy as a full-fledged web service with database support.
- **Performance Optimization**: Improve the efficiency of job scheduling for larger datasets.

## Live Web App
🔗 **Try the Streamlit App:** [Job Scheduling App](https://jobscheduling-v5ddygocb7spmjehsegfy4.streamlit.app/)

