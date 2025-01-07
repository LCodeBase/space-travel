# Space Travel Simulation

This project simulates the trajectory of a spacecraft traveling from Earth to a destination like the Moon or Mars, showcasing basic principles of orbital mechanics using Python. The simulation is visualized with an animated plot, and the user can interact with the program through a graphical interface to select the destination and duration of the journey.

## Features

- **Orbital Simulation:** Simulates the spacecraft's movement around Earth using gravitational forces.
- **Destination Selection:** Choose between the Moon and Mars for the journey.
- **Graphical User Interface (GUI):** A simple Tkinter-based interface allows the user to input simulation parameters.
- **Interactive Animation:** The trajectory and spacecraft position are dynamically displayed using Matplotlib animations.
- **Custom Icons:** Earth, Moon, and Mars icons are included to visually represent the bodies in space.
- **Real-time Data Display:** The current distance and simulation frame are displayed on the plot during the animation.

## Requirements

- Python 3.x
- Libraries: `numpy`, `scipy`, `matplotlib`, `tkinter`

You can install the necessary Python libraries using pip:

```bash
pip install numpy scipy matplotlib
```
## File Structure

- `space_travel_simulation.py`: The main script to run the simulation.
- `earth_icon.png`: Icon representing Earth.
- `moon_icon.png`: Icon representing the Moon.
- `mars_icon.png`: Icon representing Mars.
- `rocket_icon.png`: Icon representing the spacecraft.

## How It Works

### Initial Conditions:
The program uses predefined initial conditions for the spacecraft's position and velocity based on the selected destination:
- **Moon:** Distance = 384,400 km, Velocity = 1,022 m/s
- **Mars:** Distance = 78 million km, Velocity = 24,130 m/s

### Gravitational Force Calculation:
The gravitational force between Earth and the spacecraft is computed using Newton's law of universal gravitation. This force affects the spacecraft's acceleration and its subsequent trajectory.

### Orbit Simulation:
The simulation solves the differential equations of motion for the spacecraft using the `solve_ivp` function from SciPy.

### Visualization:
The trajectory is plotted, and the spacecraft's position is animated. The background simulates space with a black color, and grid lines are used to represent the coordinate system. Custom icons are used to represent Earth, the Moon, or Mars.

### Graphical User Interface (GUI):
The user selects the destination (Moon or Mars) and specifies the duration of the simulation (in seconds). A simple Tkinter interface is used to gather this input, and upon clicking the "Start Simulation" button, the animation is displayed.

## How to Run

1. Clone or download this repository to your local machine.
2. Ensure you have Python 3.x installed and the necessary libraries (`numpy`, `scipy`, `matplotlib`, `tkinter`).
3. Place the required icon images (`earth_icon.png`, `moon_icon.png`, `mars_icon.png`, `rocket_icon.png`) in the same directory as the Python script.
4. Run the script:

```bash
python space_travel_simulation.py
````

## Example Usage
1. Select the Moon as your destination.
2. Set the duration of the simulation to 259,200 seconds (3 days).
3. Click Start Simulation.
4. Watch the spacecraft's journey as it follows the calculated orbit around Earth.

:)
