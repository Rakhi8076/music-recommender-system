# My ML-Powered Music Recommender 🎵

This is a Flask-based web application that provides song recommendations to users. The recommendation engine is built using a machine learning model that analyzes song data to find similar tracks.

## Features

- **Search Interface**: Users can search for a song to get recommendations.
- **Recommendation Engine**: The app uses a pre-trained model to provide song recommendations based on content-based filtering.
- **Clean UI**: A simple and intuitive user interface built with HTML and CSS.

## Project Structure

- **`run_flask.py`**: The main Flask application file that handles all the routing and logic.
- **`data/`**: Contains the dataset used for the recommendation engine (`spotify_finalDataset.csv`).
- **`model/`**: Stores the pre-trained machine learning model (`recommender_model.pkl`).
- **`templates/`**: Contains the HTML files (`index.html`, `results.html`) for the user interface.
- **`static/`**: Includes static files like CSS and images.
- **`requirements.txt`**: Lists all the Python dependencies required to run the application.
- **`start.sh`**: A simple shell script for starting the Flask application in a production environment.

**Note**: The `app.py` file in this repository was for a previous attempt at deploying on Hugging Face Spaces. It is not used for the Flask application.

## Getting Started

Follow these steps to set up and run the project on your local machine.

### Prerequisites

- Python 3.x
- Git

- # The Spotifier - Music Recommender System

## Live Demo
Check out the live website here: [https://the-spotifier.onrender.com/](https://the-spotifier.onrender.com/)

### Installation

### Installation

1.  **Clone the repository**:
    ```bash
    git clone [https://github.com/Rakhi8076/music-recommender-system.git](https://github.com/Rakhi8076/music-recommender-system.git)
    cd music-recommender-system
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv myenv
    source myenv/bin/activate  # On macOS/Linux
    myenv\Scripts\activate     # On Windows
    ```

3.  **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

To run the application, set the `FLASK_APP` environment variable to point to your main file and then run Flask.

```bash
# On Windows PowerShell
$env:FLASK_APP = "run_flask.py"
flask run

# On macOS/Linux
export FLASK_APP=run_flask.py
flask run
