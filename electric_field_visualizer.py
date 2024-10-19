import numpy as np
import matplotlib.pyplot as plt

k = 8.99e9  # Coulomb's constant in N m²/C²

def electric_field(q, r0, r):
    """Calculate the electric field due to a point charge."""
    r_vec = r - r0[:, np.newaxis, np.newaxis]  # Expand r0 to match r's shape
    r_magnitude = np.linalg.norm(r_vec, axis=0)  # Compute magnitude along the correct axis
    if np.any(r_magnitude == 0):
        return np.zeros_like(r_vec)  # Avoid division by zero
    return k * q * r_vec / r_magnitude**3  # Return the electric field vector

def potential(q, r0, r):
    """Calculate the electric potential due to a point charge."""
    r_vec = r - r0[:, np.newaxis, np.newaxis]  # Expand r0 to match r's shape
    r_magnitude = np.linalg.norm(r_vec, axis=0)  # Compute magnitude along the correct axis
    return np.where(r_magnitude == 0, np.inf, k * q / r_magnitude)  # Handle singularity

# Define the grid
x = np.linspace(-5, 5, 20)  # X-coordinates
y = np.linspace(-5, 5, 20)  # Y-coordinates
X, Y = np.meshgrid(x, y)    # Create a grid
r = np.array([X, Y])        # Combine X and Y into a single array for processing

# Define point charges
charges = [
    {'position': np.array([-2, 0]), 'magnitude': 1e-6},  # Positive charge
    {'position': np.array([2, 0]), 'magnitude': -1e-6}, # Negative charge
]

# Calculate the electric field and potential on the grid
Ex, Ey = np.zeros(X.shape), np.zeros(Y.shape)
V = np.zeros(X.shape)

for charge in charges:
    q = charge['magnitude']
    r0 = charge['position']
    
    Ex_charge, Ey_charge = electric_field(q, r0, r)  # Calculate electric field components
    Ex += Ex_charge
    Ey += Ey_charge
    V += potential(q, r0, r)  # Calculate potential

# Plotting electric field lines
plt.figure(figsize=(10, 8))
plt.quiver(X, Y, Ex, Ey, color='b', headlength=5)

# Contour for potential
contour = plt.contour(X, Y, V, levels=20, cmap='RdYlBu', alpha=0.5)
plt.colorbar(contour, label='Electric Potential (V)')

# Mark charges
for charge in charges:
    plt.plot(charge['position'][0], charge['position'][1], 'ro' if charge['magnitude'] > 0 else 'bo', markersize=12)

plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.xlabel('X-axis (m)')
plt.ylabel('Y-axis (m)')
plt.title('Electric Field and Potential Visualization')
plt.grid()
plt.show()
