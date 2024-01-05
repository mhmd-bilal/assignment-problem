# Assignment Problem Solver 

## Overview

This project is a web-based application that solves the Assignment Problem using the Hungarian Algorithm. The user can input the cost matrix, specify whether to maximize or minimize the total cost, and the application will provide the optimal assignment along with the total cost.
### [Click here](https://assignment-problem-solver.streamlit.app/)

## Technologies Used

- Python
- Streamlit
- NumPy
- Pandas

## Files

### 1. `main.py`

This file contains the main code for the Streamlit web application. Users can input the dimensions of the cost matrix and fill in the matrix entries interactively. The application then utilizes the `matcal` function from the `calc.py` module to solve the Assignment Problem and displays the results.

### 2. `calc.py`

The `calc.py` module provides the core functionality for solving the Assignment Problem. It includes functions for maximizing profit, balancing the matrix, row and column allocation, verification, diagonal allocation, manipulation, and calculating the final cost.

### 3. `requirements.txt`

This file lists all the dependencies required for running the project. You can install them using the following command:

```bash
pip install -r requirements.txt
```

## How to Run the Project

1. Ensure you have Python installed on your machine.
2. Install the required dependencies by running the command mentioned in `requirements.txt`.
3. Execute the `main.py` file using the following command:

```bash
streamlit run main.py
```

4. Access the application in your web browser at the provided URL.

## Usage Instructions

1. Open the web application in your browser.
2. Adjust the sliders to set the number of rows and columns for the cost matrix.
3. Input the cost matrix entries by filling in the interactive cells.
4. Choose whether to maximize or minimize the total cost.
5. Click the "Submit" button to view the optimal assignment and the total cost.

