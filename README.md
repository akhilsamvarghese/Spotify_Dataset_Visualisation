<p align="center">
  <img src="https://storage.googleapis.com/pr-newsroom-wp/1/2023/12/Generic-FTR-headers_V10-1920x733.jpg" alt="Spotify Dataset Cover" />
</p>

# Spotify Dataset Visualisation

## Overview

This project analyzes and visualizes data from Spotify's 2023 dataset. It explores various aspects of popular songs, including their audio features, streaming statistics, and artist information. The analysis is performed using Python, with libraries such as Pandas for data manipulation and Seaborn/Matplotlib for visualization.


# Basic info about the Dataset

The “Most Streamed Spotify Songs 2023” dataset provides comprehensive insights into the music tracks that dominated Spotify in 2023. Here’s a detailed analysis based on the features and their implications:

[**Read more ....**](https://fresh-operation-c28.notion.site/Spotify-Dataset-Visualisation-1032252b58d780b994faef50a17b6db3)
# Dataset used :

[https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023/data](https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023/data)

## Requirements

- Python 3.7+
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/spotify-data-visualization.git
   ```

2. Navigate to the project directory:
   ```
   cd spotify-data-visualization
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Open the Jupyter Notebook:
   ```
   jupyter notebook Spotify_Data_Visualization.ipynb
   ```

2. Run the cells in order to perform the analysis and generate visualizations.

## Data Processing

The notebook performs several data processing steps:

1. Importing the dataset
2. Exploring the dataset structure
3. Handling missing values
4. Removing unnecessary columns
5. Converting data types
6. Creating a release date column
7. Exporting the cleaned data to a CSV file

## Visualizations

The project includes various visualizations:

1. **Univariate Analysis:**
   - Distribution of streams, danceability, valence, energy, acousticness, instrumentalness, liveness, and speechiness

2. **Bivariate Analysis:**
   - Scatter plot of danceability vs. energy
   - Violin plot of valence for songs in/out of Spotify charts

3. **Top Charts:**
   - Top 10 artists by stream count
   - Top 10 most streamed songs
   - Top 10 artists by number of songs in the dataset

4. **Time-based Analysis:**
   - Average streams by release month

5. **Correlation Analysis:**
   - Heatmap of audio feature correlations


