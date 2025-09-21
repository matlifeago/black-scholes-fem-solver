import numpy as np

def linear_basis(i, nodes, S):
    """Evaluate the i-th linear hat function at point S.
    
    Args:
        i (int): Index of the basis function
        nodes (numpy.ndarray): Array of node coordinates
        S (float or numpy.ndarray): Point(s) to evaluate at
        
    Returns:
        float or numpy.ndarray: Value of the basis function at S
    """
    if i == 0:
        return np.where(S <= nodes[1], (nodes[1] - S) / (nodes[1] - nodes[0]), 0)
    elif i == len(nodes)-1:
        return np.where(S >= nodes[-2], (S - nodes[-2]) / (nodes[-1] - nodes[-2]), 0)
    else:
        return np.where(
            (S >= nodes[i-1]) & (S <= nodes[i]),
            (S - nodes[i-1]) / (nodes[i] - nodes[i-1]),
            np.where(
                (S >= nodes[i]) & (S <= nodes[i+1]),
                (nodes[i+1] - S) / (nodes[i+1] - nodes[i]),
                0
            )
        )

def linear_basis_derivative(i, nodes, S):
    """Evaluate the derivative of the i-th linear hat function at point S.
    
    Args:
        i (int): Index of the basis function
        nodes (numpy.ndarray): Array of node coordinates
        S (float or numpy.ndarray): Point(s) to evaluate at
        
    Returns:
        float or numpy.ndarray: Derivative of the basis function at S
    """
    if i == 0:
        return np.where(S <= nodes[1], -1/(nodes[1]-nodes[0]), 0)
    elif i == len(nodes)-1:
        return np.where(S >= nodes[-2], 1/(nodes[-1]-nodes[-2]), 0)
    else:
        return np.where(
            (S >= nodes[i-1]) & (S <= nodes[i]),
            1/(nodes[i] - nodes[i-1]),
            np.where(
                (S >= nodes[i]) & (S <= nodes[i+1]),
                -1/(nodes[i+1] - nodes[i]),
                0
            )
        )
