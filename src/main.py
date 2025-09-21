#!/usr/bin/env python3
"""
Main script for running the Black-Scholes FEM solver.
"""

import numpy as np
import matplotlib.pyplot as plt
from src.meshing.mesh_generator import generate_uniform_mesh
from src.payoffs.european import call_payoff

def main():
    """Main function to demonstrate the FEM solver."""
    print("Black-Scholes FEM Solver")
    print("========================")
    
    # Example parameters
    K, T, r, sigma = 100, 1, 0.05, 0.2
    S_min, S_max, N_elements = 0, 200, 100
    
    # Generate mesh and initial condition
    nodes = generate_uniform_mesh(S_min, S_max, N_elements)
    payoff = call_payoff(nodes, K)
    
    print(f"Mesh generated with {len(nodes)} nodes")
    print(f"Strike price: {K}")
    print(f"Time to expiration: {T}")
    print(f"Risk-free rate: {r}")
    print(f"Volatility: {sigma}")
    
    # Plot the initial payoff
    plt.figure(figsize=(10, 6))
    plt.plot(nodes, payoff, 'b-', label='Call Option Payoff')
    plt.title('European Call Option Payoff')
    plt.xlabel('Asset Price S')
    plt.ylabel('Payoff')
    plt.grid(True)
    plt.legend()
    plt.savefig('payoff_plot.png')
    plt.show()
    
    print("Plot saved as 'payoff_plot.png'")

if __name__ == "__main__":
    main()
