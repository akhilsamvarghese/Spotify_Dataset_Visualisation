<p align="center">
  <img src="https://storage.googleapis.com/pr-newsroom-wp/1/2018/11/Spotify_Logo_RGB_Green.png" alt="Spotify Logo" width="400"/>
</p>

# Spotify Data Visualization Dashboard

## Overview

This project presents an interactive dashboard for visualizing and analyzing Spotify's music data. It offers insights into popular songs, artists, and audio features using a variety of charts and filters. The dashboard is built using Python and Streamlit, providing an engaging and user-friendly interface for exploring music trends.

## Features

1. **Data Overview:** 
   - Display of the dataset's first few rows

2. **Top Charts:**
   - Top Artists by Stream Count (adjustable number of artists)
   - Top Most Streamed Songs (adjustable number of songs)

3. **Time-based Analysis:**
   - Average Streams by Release Month
   - Streams Over Time (yearly trend)

4. **Audio Feature Analysis:**
   - Correlation Heatmap of Audio Features
   - Distribution of Audio Features (interactive selection)

5. **Additional Insights:**
   - Popularity vs. Audio Features Scatter Plot
   - Audio Feature Comparison Box Plot

6. **Interactive Data Explorer:**
   - Custom column selection for detailed data view

## Filters

- Minimum Streams slider
- Artist selection multi-select

## Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- Matplotlib
- Seaborn

## How to Run

1. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
2. Run the Streamlit app:
   ```
   streamlit run spotify_dashboard.py
   ```

## Data Source

The dashboard uses a cleaned Spotify dataset (`cleaned_spotify_data.csv`). The data includes information about tracks, artists, stream counts, and various audio features.

## Creator

Created by Akhil Sam Varghese

