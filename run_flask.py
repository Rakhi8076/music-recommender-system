# Import all the necessary libraries for the Flask application.
from flask import Flask, render_template, request
import pandas as pd
import pickle
import os

# Create the Flask application instance.
app = Flask(__name__)

# --- Load the model and data only once when the app starts ---
try:
    # Use os.path.join for correct file paths across different operating systems.
    # The .pkl file is assumed to contain the pre-processed data including the dataframe.
    model_file_name = 'recommender_modelFin (1).pkl'
    model_path = os.path.join(os.path.dirname(__file__), 'model', model_file_name)
    with open(model_path, 'rb') as f:
        data_to_load = pickle.load(f)
    
    songs_df = data_to_load['df']
    indices = data_to_load['indices']
    cosine_sim = data_to_load['cosine_sim']
    
    print("Model and data loaded successfully!")

    # --- Load the raw CSV file to check for consistency. ---
    # This is the line that caused the deployment error.
    # The path is corrected here to match your file name.
    csv_file_name = 'spotify_finalDataset.csv'
    csv_path = os.path.join(os.path.dirname(__file__), 'data', csv_file_name)
    
    # You may or may not need to load this file again,
    # depending on what is stored in your .pkl file.
    # This is for demonstration to show the corrected path.
    # raw_songs_df = pd.read_csv(csv_path)

except FileNotFoundError as e:
    # If files are not found, print a helpful error message.
    print(f"Error loading files: {e}. Please check your file paths and GitHub repository.")
    songs_df = None
    indices = None
    cosine_sim = None
    
# Recommendation function
def get_recommendations(song_title):
    if songs_df is not None and indices is not None and cosine_sim is not None:
        try:
            # Check if the song exists in the indices before proceeding.
            if song_title not in indices:
                print(f"Song '{song_title}' not found in the dataset.")
                return []
            
            idx = indices[song_title]
            sim_scores = list(enumerate(cosine_sim[idx]))
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            sim_scores = sim_scores[1:6]  # Get top 5 recommendations
            song_indices = [i[0] for i in sim_scores]
            
            recommended_songs_df = songs_df.iloc[song_indices]
            
            recommendations = []
            for _, row in recommended_songs_df.iterrows():
                recommendations.append({
                    'title': row['song_name'],
                    'artist': row['artist'],
                    'image_url': row['image_url'],
                    'spotify_link': row['spotify_url'],
                    'rating': row['rating']
                })
            return recommendations
            
        except KeyError:
            # This handles cases where a song might not be in the model's index.
            print(f"Song '{song_title}' not found in the dataset.")
            return []
    return []

# Remaining Flask routes and main block
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_song = request.form.get("song_name")
        if user_song:
            # The song name is converted to lowercase here before being used.
            user_song = user_song.lower()
            recommendations = get_recommendations(user_song)
            return render_template("results.html", recommendations=recommendations)
    
    return render_template("index.html")

if __name__ == '__main__':
    # This runs the app in debug mode locally.
    app.run(debug=True)
