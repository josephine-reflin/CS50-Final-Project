import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os

def animate_hydrograph(df, title="Animated Hydrograph", observed_col="observed", simulated_col="simulated", datetime_col="datetime", output_path="outputs/hydrograph_animation.gif", file_format="gif"):
    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.set_xlabel("Datetime")
    ax.set_ylabel("Water Level (TMA)")
    ax.grid(True)

    # Data storage for animation
    x_data, y_obs_data, y_sim_data = [], [], []

    # Two lines of observed and simulated (returns a list)
    line_obs, = ax.plot([], [], label = "Observed", color = "green")
    line_sim, = ax.plot([], [], label = "Simulated", color = "red", linestyle = "--")

    def update(frame):
        # gets data from the current row
        current_time = df[datetime_col].iloc[frame]
        current_observed = df[observed_col].iloc[frame]
        current_simulated = df[simulated_col].iloc[frame]

        # append values to the lists
        x_data.append(current_time)
        y_obs_data.append(current_observed)
        y_sim_data.append(current_simulated)

        # updates the data shown
        line_obs.set_data(x_data, y_obs_data)
        line_sim.set_data(x_data, y_sim_data)

        #rescale
        ax.relim()
        ax.autoscale_view()

        return line_obs, line_sim

    # create animation object
    ani = FuncAnimation(
       fig,
       update,
       frames=len(df),
       interval=200,
       repeat=True
    )

    # save the animation
    ax.legend()
    plt.tight_layout()

    # make sure the folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    if file_format == "gif":
        ani.save(output_path, writer="pillow", fps=5)
    elif file_format == "mp4":
        ani.save(output_path.replace(".gif", ".mp4"), writer="ffmeg", fps=5)

    print(f"✅ Animation saved to: {output_path}")


