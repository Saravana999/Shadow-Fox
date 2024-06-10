# Delhi AQI Analysis

## Overview

This project analyzes air quality in Delhi by examining the concentrations of various pollutants and calculating the Air Quality Index (AQI). It includes several visualizations to highlight trends and patterns in the data.

## Directory Structure

- `data/`: Contains the dataset file.
- `notebooks/`: Contains Jupyter notebooks for detailed analysis.
- `src/`: Contains Python scripts for data processing, AQI calculations, and visualizations.
- `README.md`: Project overview and instructions.
- `requirements.txt`: List of required Python packages.
- `LICENSE`: License information.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/saravana999/shadow Fox.git
    cd delhi_aqi_analysis
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Ensure the `delhiaqi.csv` file is in the `data/` directory.

2. Run the Jupyter notebook in the `notebooks/` directory to see the full analysis:
    ```sh
    jupyter notebook notebooks/analysis_notebook.ipynb
    ```

3. Alternatively, you can execute the scripts in the `src/` directory:
    ```sh
    python src/data_processing.py
    python src/aqi_calculations.py
    python src/visualizations.py
    ```

## Data

The dataset `delhiaqi.csv` contains the following columns:
- `date`: Date and time of the observation.
- `co`, `no`, `no2`, `o3`, `so2`, `pm2_5`, `pm10`, `nh3`: Concentrations of various pollutants.

## Analysis

- **Data Processing**: Convert `date` to datetime format and extract date and time components.
- **AQI Calculation**: Calculate AQI for each pollutant and determine the overall AQI.
- **Visualizations**: Generate scatter plots, line graphs, and bar charts to visualize pollutant concentrations and AQI trends.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
