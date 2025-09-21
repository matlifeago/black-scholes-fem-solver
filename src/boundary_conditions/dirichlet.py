import numpy as np

def apply_dirichlet_bc(A, b, node_indices, values):
    """Apply Dirichlet boundary conditions to the system.
    
    Args:
        A (scipy.sparse matrix): System matrix
        b (numpy.ndarray): Right-hand side vector
        node_indices (list): Indices of nodes with Dirichlet BC
        values (list): Values to enforce at those nodes
        
    Returns:
        tuple: (Modified A, Modified b)
    """
    # TODO: Implement Dirichlet BC application
    # This typically involves modifying the matrix and right-hand side
    return A, b
