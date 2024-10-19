import numpy as np
k_e = 8.99e9
class PointCharge:
    def __init__(self, q, position):
        """
        Initialize the point charge with a charge value and a position in 2D space.
        :param q: Charge in Coulombs (C)
        :param position: Position as a tuple (x, y)
        """
        self.q = q
        self.position = np.array(position)

    def electric_field(self, x, y):
        """
        Calculate the electric field vector at a point (x, y) due to this charge.
        :param x: x-coordinate of the point
        :param y: y-coordinate of the point
        :return: Electric field vector (Ex, Ey) at point (x, y)
        """
        r_vector = np.array([x, y]) - self.position
        r_magnitude = np.linalg.norm(r_vector)  # Distance from charge to point
        if r_magnitude == 0:
            return np.array([0.0, 0.0])  # To avoid division by zero at the charge's position
        
        E_vector = k_e * self.q * r_vector / r_magnitude**3
        return E_vector

    def potential(self, x, y):
        """
        Calculate the electric potential at a point (x, y) due to this charge.
        :param x: x-coordinate of the point
        :param y: y-coordinate of the point
        :return: Electric potential V at point (x, y)
        """
        r_vector = np.array([x, y]) - self.position
        r_magnitude = np.linalg.norm(r_vector)
        if r_magnitude == 0:
            return 0.0  # Avoid division by zero
        return k_e * self.q / r_magnitude

def total_electric_field(charges, x, y):
    """
    Calculate the total electric field at a point (x, y) due to multiple charges.
    :param charges: List of PointCharge objects
    :param x: x-coordinate of the point
    :param y: y-coordinate of the point
    :return: Total electric field vector (Ex, Ey) at point (x, y)
    """
    E_total = np.array([0.0, 0.0])
    for charge in charges:
        E_total += charge.electric_field(x, y)
    return E_total

def total_potential(charges, x, y):
    """
    Calculate the total electric potential at a point (x, y) due to multiple charges.
    :param charges: List of PointCharge objects
    :param x: x-coordinate of the point
    :param y: y-coordinate of the point
    :return: Total electric potential at point (x, y)
    """
    V_total = 0.0
    for charge in charges:
        V_total += charge.potential(x, y)
    return V_total

if __name__ == "__main__":
    num_charges = int(input("Enter the number of charges: "))

    charges = []
    for i in range(num_charges):
        q = float(input(f"Enter charge {i+1} value (in Coulombs): "))
        x_pos = float(input(f"Enter x-coordinate of charge {i+1}: "))
        y_pos = float(input(f"Enter y-coordinate of charge {i+1}: "))
        charges.append(PointCharge(q, (x_pos, y_pos)))

    # Input for the point where electric field and potential will be calculated
    x_point = float(input("Enter the x-coordinate of the point where the field and potential are calculated: "))
    y_point = float(input("Enter the y-coordinate of the point where the field and potential are calculated: "))

    # Calculate the total electric field and potential at the user-specified point
    E_field = total_electric_field(charges, x_point, y_point)
    V_potential = total_potential(charges, x_point, y_point)

    print(f"\nElectric Field at ({x_point}, {y_point}): {E_field} N/C")
    print(f"Electric Potential at ({x_point}, {y_point}): {V_potential} V")