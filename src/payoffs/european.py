import numpy as np

def call_payoff(S, K):
    """Calculate European call option payoff.
    
    Args:
        S (numpy.ndarray): Asset prices
        K (float): Strike price
        
    Returns:
        numpy.ndarray: Payoff values
    """
    return np.maximum(S - K, 0)

def put_payoff(S, K):
    """Calculate European put option payoff.
    
    Args:
        S (numpy.ndarray): Asset prices
        K (float): Strike price
        
    Returns:
        numpy.ndarray: Payoff values
    """
    return np.maximum(K - S, 0)
