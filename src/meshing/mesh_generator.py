import numpy as np

def generate_uniform_mesh(S_min, S_max, N_elements):
    """Generate a uniform mesh of node coordinates.
    
    Args:
        S_min (float): Minimum asset price
        S_max (float): Maximum asset price  
        N_elements (int): Number of elements
        
    Returns:
        numpy.ndarray: Array of node coordinates
    """
    nodes = np.linspace(S_min, S_max, N_elements + 1)
    return nodes

def generate_log_uniform_mesh(S_min, S_max, N_elements, density_around_K=None):
    """Generate a mesh with more points near a specific point.
    
    Args:
        S_min (float): Minimum asset price
        S_max (float): Maximum asset price
        N_elements (int): Number of elements
        density_around_K (float, optional): Point around which to add density (e.g., strike price)
        
    Returns:
        numpy.ndarray: Array of node coordinates
    """
    if density_around_K is None:
        return generate_uniform_mesh(S_min, S_max, N_elements)
    
    # For now, return uniform mesh. Can be enhanced later.
    return generate_uniform_mesh(S_min, S_max, N_elements)
