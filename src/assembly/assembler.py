import numpy as np
from scipy import sparse

def assemble_system(nodes, r, sigma):
    """Assemble the FEM system matrices.
    
    Args:
        nodes (numpy.ndarray): Array of node coordinates
        r (float): Risk-free interest rate
        sigma (float): Volatility
        
    Returns:
        tuple: (Mass matrix M, Combined matrix A) as sparse matrices
    """
    N_nodes = len(nodes)
    M = sparse.lil_matrix((N_nodes, N_nodes))  # Mass matrix
    K = sparse.lil_matrix((N_nodes, N_nodes))  # Stiffness matrix
    C = sparse.lil_matrix((N_nodes, N_nodes))  # Convection matrix
    R = sparse.lil_matrix((N_nodes, N_nodes))  # Reaction matrix

    # Gaussian quadrature points and weights (2 points per element)
    gauss_points = [-1/np.sqrt(3), 1/np.sqrt(3)]
    gauss_weights = [1, 1]

    # Loop over each element
    for e in range(len(nodes)-1):
        S_left = nodes[e]
        S_right = nodes[e+1]
        jacobian = (S_right - S_left) / 2  # For mapping to [-1,1]

        # TODO: Implement the actual assembly with Gaussian quadrature
        # This is a placeholder structure
        pass

    # Convert to more efficient format for solving
    M = M.tocsc()
    K = K.tocsc()
    C = C.tocsc()
    R = R.tocsc()

    A = K + C - R  # Combine into the main matrix
    return M, A
