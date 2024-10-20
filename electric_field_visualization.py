import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import matplotlib.cm as cm

# Constants
k = 8.99e9  # Coulomb's constant

# Function to calculate electric field due to a point charge
def electric_field(q, r0, x, y):
    rx = x - r0[0]
    ry = y - r0[1]
    r = np.sqrt(rx**2 + ry**2)
    Ex = k * q * rx / r**3
    Ey = k * q * ry / r**3
    return Ex, Ey

# Generate a grid of points
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Charge configuration
charges = [{'q': 1e-9, 'pos': [-2, 0]}, {'q': -1e-9, 'pos': [2, 0]}]

# Function to calculate the total electric field at each point
def total_electric_field(X, Y, charges):
    Ex_total, Ey_total = np.zeros(X.shape), np.zeros(Y.shape)
    for charge in charges:
        Ex, Ey = electric_field(charge['q'], charge['pos'], X, Y)
        Ex_total += Ex
        Ey_total += Ey
    return Ex_total, Ey_total

# Initial electric field calculation
Ex, Ey = total_electric_field(X, Y, charges)
magnitude = np.sqrt(Ex**2 + Ey**2)

# Create the plot
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.3)

# Quiver plot (color-coded by magnitude)
field = ax.quiver(X, Y, Ex, Ey, magnitude, cmap=cm.coolwarm, scale=5e9)
ax.set_title("Electric Field Visualization")

# Add color bar
plt.colorbar(field, ax=ax, label='Electric Field Magnitude')

# Add sliders for field line density and charge magnitudes
ax_density = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor='lightgray')
density_slider = Slider(ax_density, 'Density', 1, 10, valinit=5)

ax_q1 = plt.axes([0.2, 0.15, 0.65, 0.03], facecolor='lightgray')
q1_slider = Slider(ax_q1, 'Charge 1 (C)', 1e-9, 1e-8, valinit=1e-9)

ax_q2 = plt.axes([0.2, 0.2, 0.65, 0.03], facecolor='lightgray')
q2_slider = Slider(ax_q2, 'Charge 2 (C)', -1e-9, -1e-8, valinit=-1e-9)

# Function to update the plot when sliders are adjusted
def update(val):
    ax.clear()
    density = density_slider.val
    charges[0]['q'] = q1_slider.val
    charges[1]['q'] = q2_slider.val
    Ex, Ey = total_electric_field(X, Y, charges)
    magnitude = np.sqrt(Ex**2 + Ey**2)
    field = ax.quiver(X, Y, Ex, Ey, magnitude, cmap=cm.coolwarm, scale=5e9 * density)
    plt.colorbar(field, ax=ax, label='Electric Field Magnitude')
    ax.set_title("Electric Field Visualization")
    fig.canvas.draw_idle()

# Update function tied to the sliders
density_slider.on_changed(update)
q1_slider.on_changed(update)
q2_slider.on_changed(update)

plt.show()
