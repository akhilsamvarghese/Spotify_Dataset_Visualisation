<p align="center">
  <img src="https://storage.googleapis.com/pr-newsroom-wp/1/2023/12/Generic-FTR-headers_V10-1920x733.jpg" alt="Spotify Dataset Cover" />
</p>

# Spotify Dataset Visualisation

## Overview

This project analyzes and visualizes data from Spotify's 2023 dataset. It explores various aspects of popular songs, including their audio features, streaming statistics, and artist information. The analysis is performed using Python, with libraries such as Pandas for data manipulation and Seaborn/Matplotlib for visualization.


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


