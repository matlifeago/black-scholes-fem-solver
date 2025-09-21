from scipy.sparse.linalg import spsolve
import scipy.sparse as sp

def theta_scheme(M, A, V_old, dt, theta=0.5):
    """Perform one time step of the theta-method.
    
    Args:
        M (scipy.sparse matrix): Mass matrix
        A (scipy.sparse matrix): Combined stiffness matrix
        V_old (numpy.ndarray): Solution vector at previous time step
        dt (float): Time step size
        theta (float): Theta parameter (0=explicit, 0.5=Crank-Nicolson, 1=implicit)
        
    Returns:
        numpy.ndarray: Solution vector at new time step
    """
    # Form the system matrices: B * V_new = F * V_old
    B = M + theta * dt * A
    F = M - (1 - theta) * dt * A

    # Solve the linear system
    V_new = spsolve(B, F.dot(V_old))
    return V_new
