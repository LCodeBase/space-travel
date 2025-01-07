import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import tkinter as tk
from tkinter import messagebox, simpledialog

# Constantes
G = 6.67430e-11  # Constante gravitacional, m³/kg/s²
M = 5.972e24  # Massa da Terra, kg
R = 6371e3  # Raio da Terra, m

def get_initial_conditions(destination):
    destinations = {
        "Lua": {"x": R + 384400e3, "y": 0, "vx": 0, "vy": 1022},
        "Marte": {"x": R + 78e9, "y": 0, "vx": 0, "vy": 24130},
    }
    if destination in destinations:
        data = destinations[destination]
        return data["x"], data["y"], data["vx"], data["vy"]
    else:
        raise ValueError(f"Destino desconhecido: {destination}")

def gravity(t, state):
    x, vx, y, vy = state
    r = np.sqrt(x ** 2 + y ** 2)
    ax = -G * M * x / r ** 3
    ay = -G * M * y / r ** 3
    return [vx, ax, vy, ay]

def simulate_orbit(pos_x, pos_y, vel_x, vel_y, duration):
    initial_state = [pos_x, vel_x, pos_y, vel_y]
    t_span = (0, duration)
    t_eval = np.linspace(*t_span, 1000)
    sol = solve_ivp(gravity, t_span, initial_state, t_eval=t_eval)
    return sol

def plot_orbit(simulation_result, destination):
    x_data = simulation_result.y[0] / 1e3  # Convertendo para km
    y_data = simulation_result.y[2] / 1e3

    # Criando a figura
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_aspect('equal', adjustable='box')
    ax.set_facecolor("black")  # Fundo preto para simular o espaço
    ax.set_title(f"Simulação de Órbita - Destino: {destination}", fontsize=16, color="white")
    ax.set_xlabel("Distância X (km)", fontsize=12, color="white")
    ax.set_ylabel("Distância Y (km)", fontsize=12, color="white")
    ax.tick_params(colors="white")  # Cor dos ticks
    ax.grid(color='gray', linestyle='--', linewidth=0.5)

    # Ajuste dos limites dos eixos para garantir visibilidade
    buffer = max(abs(x_data).max(), abs(y_data).max()) * 1.1  # Adicionar 10% extra como margem
    ax.set_xlim(-buffer, buffer)
    ax.set_ylim(-buffer, buffer)

    # Adicionando ícones dos corpos celestes
    def add_icon(ax, x, y, image_path, zoom):
        img = plt.imread(image_path)
        imagebox = OffsetImage(img, zoom=zoom)
        ab = AnnotationBbox(imagebox, (x, y), frameon=False)
        ax.add_artist(ab)

    add_icon(ax, 0, 0, "earth_icon.png", zoom=0.1)  # Terra
    if destination == "Lua":
        add_icon(ax, 384400, 0, "moon_icon.png", zoom=0.05)  # Lua
    elif destination == "Marte":
        add_icon(ax, 78e6, 0, "mars_icon.png", zoom=0.05)  # Marte

    # Linha da trajetória
    line, = ax.plot([], [], 'cyan', label="Trajetória", linewidth=2)
    ax.legend(loc="upper left", fontsize=10, facecolor="black", edgecolor="white", labelcolor="white")

    # Adicionando o ícone do foguete
    rocket_img = plt.imread("satellite_icon.png")
    rocket_imagebox = OffsetImage(rocket_img, zoom=0.05)
    rocket_ab = AnnotationBbox(rocket_imagebox, (x_data[0], y_data[0]), frameon=False)
    ax.add_artist(rocket_ab)

    # Informações dinâmicas
    info_text = ax.text(0.02, 0.95, "", transform=ax.transAxes, fontsize=12, verticalalignment='top',
                        bbox=dict(boxstyle="round", facecolor="white", alpha=0.8))

    # Função de atualização da animação
    def update(frame):
        # Atualizar a linha
        line.set_data(x_data[:frame + 1], y_data[:frame + 1])
        # Atualizar a posição do foguete
        rocket_ab.xy = (x_data[frame], y_data[frame])
        # Atualizar informações de texto
        distance = np.sqrt(x_data[frame] ** 2 + y_data[frame] ** 2)
        info_text.set_text(f"Frame: {frame}\nDistância: {distance:.2f} km")
        return line, rocket_ab, info_text

    # Criando animação
    ani = FuncAnimation(fig, update, frames=len(x_data), interval=50, blit=True)

    plt.show()



def run_simulation(destination, duration):
    try:
        init_x, init_y, init_vx, init_vy = get_initial_conditions(destination)
        simulation_result = simulate_orbit(init_x, init_y, init_vx, init_vy, duration)
        plot_orbit(simulation_result, destination)
    except Exception as e:
        messagebox.showerror("Erro na Simulação", str(e))

def main():
    def start_simulation():
        destination = destination_var.get()
        try:
            duration = int(duration_entry.get())
            if duration <= 0:
                raise ValueError("A duração deve ser um número positivo.")
            run_simulation(destination, duration)
        except ValueError as e:
            messagebox.showerror("Erro de Entrada", str(e))

    root = tk.Tk()
    root.title("Simulador de Viagens Espaciais")

    tk.Label(root, text="Simulador de Viagens Espaciais", font=("Arial", 16)).pack(pady=10)

    tk.Label(root, text="Selecione o destino:", font=("Arial", 12)).pack(pady=5)
    destination_var = tk.StringVar(value="Lua")
    tk.Radiobutton(root, text="Lua", variable=destination_var, value="Lua", font=("Arial", 12)).pack(anchor="w")
    tk.Radiobutton(root, text="Marte", variable=destination_var, value="Marte", font=("Arial", 12)).pack(anchor="w")

    tk.Label(root, text="Duração da simulação (em segundos):", font=("Arial", 12)).pack(pady=5)
    duration_entry = tk.Entry(root, font=("Arial", 12))
    duration_entry.insert(0, "259200")
    duration_entry.pack(pady=5)

    tk.Button(root, text="Iniciar Simulação", font=("Arial", 12), command=start_simulation).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
