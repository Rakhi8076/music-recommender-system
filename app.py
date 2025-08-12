from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load the single .pkl file containing all the necessary data
try:
    with open('model/recommender_modelFin.pkl', 'rb') as f:
        data_to_load = pickle.load(f)
    
    songs_df = data_to_load['df']
    indices = data_to_load['indices']
    cosine_sim = data_to_load['cosine_sim']
    
except FileNotFoundError:
    print("Error: recommender_modelFin.pkl file not found. Please check your file paths.")
    songs_df = None
    indices = None
    cosine_sim = None

# Recommendation function
# app.py

# ... baaki code same rahega ...

def get_recommendations(song_title):
    if songs_df is not None and indices is not None and cosine_sim is not None:
        try:
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
                    'rating': row['rating']  # <-- Yahan rating add ki gayi hai
                })
            return recommendations
            
        except KeyError:
            print(f"Song '{song_title}' not found in the dataset.")
            return []
    return []

# ... baaki code same rahega ...

# Remaining Flask routes and main block
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_song = request.form.get("song_name")
        if user_song:
            recommendations = get_recommendations(user_song)
            return render_template("results.html", recommendations=recommendations)
    
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)