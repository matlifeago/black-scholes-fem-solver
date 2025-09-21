# Black-Scholes PDE Solver using the Finite Element Method

A Python implementation for solving the Black-Scholes partial differential equation for option pricing using the Finite Element Method (FEM).

## Features

*   Solves European call and put options.
*   Modular code for easy extension (e.g., American options, exotics).
*   Includes both uniform and non-uniform meshing.
*   Theta-method for time discretization (Crank-Nicolson, Implicit Euler).
*   Jupyter notebook examples.

## Installation

1.  Clone the repo:
    ```bash
    git clone https://github.com/your-username/black-scholes-fem-solver.git
    cd black-scholes-fem-solver
    ```

2.  Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

See the Jupyter notebooks in the `examples/` directory.

`examples/01_European_Call.ipynb` - Pricing a European call option and comparing it to the analytical solution.

You can also run the main script:
```bash
python src/main.py
