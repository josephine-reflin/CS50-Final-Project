import os
import sys
import pandas as pd
import numpy as np
from plotter import plot_hydrograph
from animator import animate_hydrograph

DATA_DIR = "sample_runs"

def main(csv_path=None, output_filename=None):
    runs = []
    print(f"🔎 Scanning: {DATA_DIR}")

    if csv_path:

        if not os.path.isfile(csv_path):
            print(f"❌ File not found: {csv_path}")
            return

        print(f"🔎 Scanning file: {csv_path}")
        try:
            result = load_and_score(csv_path)
            runs.append(result)
            print(f"✅ NSE = {result['nse']:.3f}")
        except FileNotFoundError:
            print(f"⚠️ Error in {file}")

    else:

        for file in os.listdir("sample_runs"):
            if file.endswith(".csv"):
                full_path = os.path.join("sample_runs", file)
                try:
                    result = load_and_score(full_path)
                    runs.append(result)
                    print(f"✅ Loaded: {file} -> NSE = {result['nse']:.3f}")
                except:
                    print(f"⚠️ Error in {file}")

    if not runs:
        print("⚠️ No data loaded.")
        return

    ranked = sorted(runs, key=lambda x: x["nse"], reverse=True)

    print("\n📊 Summary:")
    print_summary(ranked)

    print("\n📈 Plotting Top Simulations..." )
    plot_top(ranked)

    df = ranked[0]["data"]

    # safely extract csv name, or fallback
    if csv_path:
        csv_name = os.path.splitext(ranked[0]["name"])[0]
    else:
        csv_name = "output"

    # if output_filename not given, use default name
    if not output_filename:
        output_filename = f"{csv_name}_animation.gif"
    else:
        csv_name = os.path.splitext(os.path.basename(output_filename))[0].replace("_animation", "")


    output_path = os.path.join("outputs", output_filename)

    print("\n🎞️ Saving animated Hydrograph to: {output_path}")
    animate_hydrograph(df, title=f"Hydrograph - {csv_name}", output_path=output_path)

    print("\n🎉 Done.")

def calculate_nse(observed, simulated):
    """Compute NSE. Returns 1 for a perfect match; values < 0 indicate poor performance. """

    observed = np.array(observed)
    simulated = np.array(simulated)

    numerator = np.sum((observed - simulated)**2)
    denominator = np.sum((observed - np.mean(observed))** 2)

    if denominator == 0:
        return np.nan # returns not a number
    return 1 - (numerator / denominator)

def calculate_rmse(observed, simulated):
    """ Compute RMSE. The lower the value the better the performance"""

    observed = np.array(observed)
    simulated = np.array(simulated)

    return np.sqrt(np.mean((observed - simulated)**2))

def calculate_bias(observed, simulated):
    """ compute mean bias (simulated - observed).
        positive bias = overestimation;
        negative bias = underestimation. """

    observed = np.array(observed)
    simulated = np.array(simulated)

    return np.mean(simulated - observed)

def calculate_pbias(observed, simulated):
    """ compute percent bias. Shows bias a percentage of total observed values """

    observed = np.array(observed)
    simulated = np.array(simulated)

    total_observed = np.sum(observed)
    if total_observed == 0:
        return np.nan # returns not a number
    return 100 * np.sum(simulated - observed) / total_observed


def load_and_score(file_path):
    """Load one CSV and compute metrics"""
    df = pd.read_csv(file_path, parse_dates=["datetime"])
    obs = df["observed"].values
    sim = df["simulated"].values

    return {
        "name": os.path.basename(file_path),
        "nse": calculate_nse(obs, sim),
        "rmse": calculate_rmse(obs, sim),
        "bias": calculate_bias(obs, sim),
        "pbias": calculate_pbias(obs, sim),
        "data": df
    }

def print_summary(results):
    """Print sorted summary of all simulations"""
    for i, r in enumerate(results):
        prefix = "🏆" if i == 0 else "-"
        print(f"-{prefix} {r['name']}: NSE = {r['nse']:.3f}, RMSE = {r['rmse']:.3f}, Bias = {r['bias']:.3f}, PBias = {r['pbias']:.2f}%")

def plot_top(results, top_k=3):
    """Plot top k results by NSE"""
    for i, res in enumerate(results[:top_k]):
        name = res["name"].replace(".csv", "")
        title = f"#{i+1} . {name} (NSE={res['nse']:.3f})"
        filename = f"#{i+1} . {name} (NSE={res['nse']:.3f})"
        plot_hydrograph(res["data"], title = title, save_name=filename)

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 2:
        main(args[0], args[1])
    elif len(args) == 1:
        main(args[0])
    else:
        main()
