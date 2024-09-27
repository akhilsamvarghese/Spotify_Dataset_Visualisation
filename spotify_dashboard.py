import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Set page configuration
st.set_page_config(page_title="Spotify Data Dashboard", layout="wide")

# Load the data
@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_spotify_data.csv")
    df['release_date'] = pd.to_datetime(df['release_date'])
    return df

df = load_data()

# Add a banner
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("https://storage.googleapis.com/pr-newsroom-wp/1/2018/11/Spotify_Logo_RGB_Green.png", width=400, use_column_width=True)


# Set page title and description
st.title("🎵 Spotify Data Visualization Dashboard")
st.markdown("Explore trends and insights from Spotify's music data.")

# Sidebar for filtering
st.sidebar.header("Filters")
min_streams = st.sidebar.slider("Minimum Streams", min_value=0, max_value=int(df['streams'].max()), value=0, format="%d")

selected_artists = st.sidebar.multiselect("Select Specific Artists", df['artists'].unique())

# Apply filters
filtered_df = df[df['streams'] >= min_streams]
if selected_artists:
    filtered_df = filtered_df[filtered_df['artists'].isin(selected_artists)]

# Main content
col1, col2 = st.columns(2)

# Data Overview
st.header("📊 Data Overview")
st.dataframe(filtered_df.head())

# Top Artists by Stream Count
st.header("🔝 Top Artists by Stream Count")
top_n_artists = st.slider("Number of Top Artists", min_value=5, max_value=50, value=10)
top_artists = filtered_df.groupby('artists')['streams'].sum().sort_values(ascending=False).head(top_n_artists)
fig = px.bar(x=top_artists.values, y=top_artists.index, orientation='h',
             labels={'x': 'Total Streams', 'y': 'Artists'},
             title=f'Top {top_n_artists} Artists by Stream Count',
             color=top_artists.values,
             color_continuous_scale='RdBu',
             height=600,
             width=1000)
fig.update_layout(yaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True)

# Top Most Streamed Songs
st.header("🎶 Top Most Streamed Songs")
top_n_songs = st.slider("Number of top songs to display", min_value=5, max_value=50, value=10)
top_songs = filtered_df.sort_values('streams', ascending=False).head(top_n_songs)

fig = px.bar(top_songs, x='streams', y='track_name', orientation='h',
             labels={'streams': 'Streams', 'track_name': 'Song'},
             title=f'Top {top_n_songs} Most Streamed Songs',
             color='streams',
             color_continuous_scale='RdBu',
             height=600,
             width=1000)
fig.update_layout(yaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig, use_container_width=True)

# Average Streams by Release Month
st.header("📅 Average Streams by Release Month")
filtered_df['release_month'] = filtered_df['release_date'].dt.month
monthly_streams = filtered_df.groupby('release_month')['streams'].mean().reset_index()

fig = px.line(monthly_streams, x='release_month', y='streams', markers=True,
              labels={'release_month': 'Month', 'streams': 'Average Streams'},
              title='Average Streams by Release Month',
              color_discrete_sequence=['#4CAF50'])
fig.update_xaxes(tickmode='linear', tick0=1, dtick=1)
st.plotly_chart(fig)

# Streams Over Time
st.header("🪩 Streams Over Time")
yearly_streams = filtered_df.groupby(filtered_df['release_date'].dt.year)['streams'].mean().reset_index()
fig = px.line(yearly_streams, x='release_date', y='streams', 
              title='Average Streams by Release Year',
              labels={'release_date': 'Year', 'streams': 'Average Streams'},
              color_discrete_sequence=['#FF9800'])
st.plotly_chart(fig)

# Correlation Heatmap
st.header("🔗 Correlation Heatmap of Audio Features")
corr_features = ['danceability_%', 'valence_%', 'energy_%', 'acousticness_%', 'instrumentalness_%', 'liveness_%', 'speechiness_%']
correlation_matrix = filtered_df[corr_features].corr()

fig = px.imshow(correlation_matrix, text_auto=True, aspect="auto",
                title='Correlation Heatmap of Audio Features',
                color_continuous_scale='RdBu_r',
                width=800, height=900)
st.plotly_chart(fig, use_container_width=True)

# Distribution plots
st.header("📈 Distribution of Audio Features")

col1, col2 = st.columns(2)
with col1:
    feature = st.selectbox("Select Audio Feature", ['danceability_%', 'valence_%', 'energy_%', 'acousticness_%', 'instrumentalness_%', 'liveness_%', 'speechiness_%'])
with col2:
    bin_count = st.slider("Number of bins", min_value=10, max_value=100, value=50)

# Create the histogram using Plotly Express
fig = px.histogram(filtered_df, x=feature, nbins=bin_count, marginal='box',
                   title=f'Distribution of {feature}',
                   color_discrete_sequence=['#FF6B6B'])

# Update the trace to add borders to the bars
fig.update_traces(marker=dict(line=dict(width=1, color='black')))

# Update the layout for better visibility
fig.update_layout(
    plot_bgcolor='white',
    xaxis=dict(showline=True, linewidth=2, linecolor='black', mirror=True),
    yaxis=dict(showline=True, linewidth=2, linecolor='black', mirror=True)
)

# Display the plot
st.plotly_chart(fig)

# Additional Insights
st.header("🔍 Additional Insights")

# Popularity vs. Audio Features
st.subheader("Popularity vs. Audio Features")
feature_for_scatter = st.selectbox("Select Audio Feature for Scatter Plot", corr_features)
fig = px.scatter(filtered_df, x=feature_for_scatter, y='streams', 
                 hover_data=['track_name', 'artists'],
                 labels={'streams': 'Streams', feature_for_scatter: feature_for_scatter.capitalize()},
                 title=f'Relationship between {feature_for_scatter} and Popularity',
                 color=feature_for_scatter,
                 color_continuous_scale='twilight')
st.plotly_chart(fig)

# Audio Feature Comparison
st.subheader("Audio Feature Comparison")
features_to_compare = st.multiselect("Select Features to Compare", corr_features, default=corr_features[:3])
fig = px.box(filtered_df, y=features_to_compare, 
             title="Comparison of Audio Features",
             labels={'variable': 'Feature', 'value': 'Percentage'},
             color_discrete_sequence=px.colors.qualitative.Set3)
st.plotly_chart(fig)

# Interactive data explorer
st.header("🔍 Interactive Data Explorer")
selected_columns = st.multiselect("Select columns to display", df.columns.tolist(), default=["artists", "track_name", "streams", "release_date"])
st.dataframe(filtered_df[selected_columns])

# Add a footer
st.markdown("---")
st.markdown("Created by Akhil Sam Varghese")