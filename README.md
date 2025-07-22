    # SimuFlow
    #### Video Demo:  https://youtu.be/vtn365gVjq0
    #### Description: SimuFlow is a Python-based tool that animates hydrographs and evaluates hydrological model performance using metrics like NSE, BIAS, and PBIAS.


# 💧 SimuFlow

SimuFlow i a Python-based tool to evaluate and visualize the accuracy of hydrological model outputs. It is comparing observed and simulated water level data, ranks model performance, and generates summary statistics, static plots, and animated hydrographs.

# 🎯 Purpose

Metrics like NSE, RMSE, Bias are common but they dont always intuitively enganging. SimuFlow creates an automation process that offer visual feeback, making model comparison easier and more accessible.

# 🧩 Features

- Batch processes single or multiple ".csv" simulation files
- Calculates:
    - NSE (Nash–Sutcliffe Efficiency)
    - RMSE (Root Mean Square Error)
    - Bias and Percent Bias (PBias)
- Ranks models by NSE
- Saves hydrographs plots (observed vs simulated)
- Creates animated ".gif" from the best performing model
- Output filenames include rank and performance score

# 📁 Project Structure

simuflow/
- project.py        # Main script
- plotter.py        # Static plot
- animator.py       # GIF creation
- sample_runs/      # Folder for input CSVs
- outputs/          # Folder of all generated plots and GIFs

# 📥 Input Format

Each CSV file must follow this structure:

column1,column2,column3

example:

    datetime,observed,simulated
    2025-01-01,5.1,5.0
    2025-01-02,5.3,5.2
    ...
    
# How to Run
    1. Add one or more '.csv' files to 'sample_runs/'
    2. Run the script:
        ^for single file^
        python project.py sample_runs/(name of the file).csv

        ^for multiple scripts (all) in sample_runs folder
        python project.py

    3. View outputs in 'outputs/':
        - Ranked plots: "1_modelname(NSE=...).PNG
        - Animated GIF: 'modelname_animation.gif'


# 🖥️ Terminal Output Example

📊 Summary:
🏆 (model_A).csv: NSE = 0.92, RMSE = 0.45, Bias = 0.03, PBias = 1.8%
-(model_A).csv: NSE = 0.78, RMSE = 0.5, Bias = 0.02, PBias = -2.5%
-(model_A).csv: NSE = 0.36, RMSE = 0.4, Bias = 0.01, PBias = -8.2%

# 🧠 What Each File Does

- `project.py`: Controls file scanning, ranking,, output naming, summary printing.
- `plotter.py`: Plots single/ top models into ranked `.png` files.
- `animator.py`: Creates `.gif` animation from the best model.
- `sample_runs/`: Puts your CSV files here
- `outputs/`: All saved images and animations go here

# ⚙️ Tools Used

- `pandas` : CSV reading and processing
- `matplotlib`: make plots
- `imageio`: creates GIF animation
- `os`/`sys` : File handling and CLI execution

# 💡 Design Highlights

- The project is split into separate files so that each part is easier to read, use, and update
- Automatic file naming using rank and NSE score
- Only top 3 models are plotted for focus and speed
- Friendly CLI messages and emojis for usability







