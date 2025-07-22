import matplotlib.pyplot as plt
import os

def plot_hydrograph(df, title="Hydrograph", observed_col="observed", simulated_col="simulated", datetime_col="datetime", save_dir="outputs", save_name=None):
    """
    Plot a hydrograph comparing observed and simulated time series.

    Parameters:
    - df (pandas.DataFrame): Data includes datetime, observed, and simulated columns.
    - title (str): Title of the plot
    - observed_col (str): Column name for observed values.
    - simulated_col (str): Column name for simulated values.
    - datetime_col (str): Column name for datetime values.

    """
    # folder penyimpanan
    os.makedirs(save_dir, exist_ok=True)

    #normalize nama file
    if save_name:
        filename = f"{save_name}.png"
    else:
        safe_title = title.replace(" ", "_").replace("#","").replace(".","").replace("•","")
        filename = f"{safe_title}.png"

    filepath = os.path.join(save_dir, filename)

    plt.figure(figsize=(10, 5))
    plt.plot(df[datetime_col], df[observed_col], label="Observed", linewidth=2, color="green")
    plt.plot(df[datetime_col], df[simulated_col], label="Simulated",linewidth=2, linestyle="--", color="red")

    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Water Level")
    plt.legend()
    plt.grid(True)
    plt.tight_layout(pad=5)
    plt.xticks(rotation=45)
    plt.savefig(filepath)
    plt.close()

    print(f"🖼️ Saved plot to: {filepath}")
