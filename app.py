# This imports all the necessary libraries.
import gradio as gr
import pickle
import pandas as pd

# Load the model and data. File paths should be correct.
# 'model/recommender_modelFin (1).pkl' and 'data/songs.csv'
# should be inside your project folder.
try:
    model = pickle.load(open('model/recommender_modelFin (1).pkl', 'rb'))
    data = pd.read_csv('data/songs.csv')
except FileNotFoundError as e:
    # If files are not found, print an error and stop the app.
    print(f"Error loading files: {e}")
    model = None
    data = None

# This function will run the recommendation logic.
def recommend_songs(song_name):
    if model is None or data is None:
        return "Model or data not loaded. Please check the logs."

    # Your recommendation logic goes here.
    # For now, it returns a sample list.
    return [
        f"1. Recommended Song for '{song_name}'",
        f"2. Another great song for you",
        f"3. A third recommendation"
    ]

# Create the Gradio interface.
# The inputs have a text box and the outputs have a text box.
iface = gr.Interface(
    fn=recommend_songs,
    inputs=gr.Textbox(label="Enter a song name"),
    outputs=gr.Textbox(label="Top Recommendations")
)

# Launch the app. Hugging Face will deploy this.
if __name__ == "__main__":
    iface.launch()