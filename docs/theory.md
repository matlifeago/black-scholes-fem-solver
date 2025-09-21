# Theoretical Background

## Finite Element Method for Black-Scholes PDE

The Black-Scholes PDE is given by:

$$
\\frac{\partial V}{\partial t} + \\frac{1}{2} \sigma^2 S^2 \\frac{\partial^2 V}{\partial S^2} + rS \\frac{\partial V}{\partial S} - rV = 0
$$

### Weak Formulation

The weak form is obtained by multiplying by a test function $\phi(S)$ and integrating by parts:

$$
\int_{\Omega} \\frac{\partial V}{\partial t} \phi  dS - \int_{\Omega} \\frac{1}{2} \sigma^2 S^2 \\frac{\partial V}{\partial S} \\frac{\partial \phi}{\partial S}  dS + \int_{\Omega} rS \\frac{\partial V}{\partial S} \phi  dS - \int_{\Omega} rV \phi  dS = 0
$$

### Spatial Discretization

Using linear basis functions $N_i(S)$, we approximate:

$$
V(S, t) \approx \sum_{j=1}^{N} V_j(t) N_j(S)
$$

### Time Discretization

Using the theta-method:

$$
\left[ \mathbf{M} + \theta \Delta t \mathbf{A} \right] \vec{V}^{n+1} = \left[ \mathbf{M} - (1-\theta) \Delta t \mathbf{A} \right] \vec{V}^{n}
$$
