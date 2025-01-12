from flask import Flask, render_template, jsonify, request
import requests
import json

app = Flask(__name__)

API_KEY = "your_api_key"
API_URL = "https://api.sportsdata.io/v4/sports/stats"
STATS_FILE = "player_stats.json"

def fetch_random_player_stats():
    """Fetch stats for 5 random players from the API."""
    response = requests.get(
        f"{API_URL}/players/random",
        headers={"Authorization": f"Bearer {API_KEY}"},
        params={"count": 5}
    )
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch stats: {response.status_code} {response.text}"}

@app.route("/")
def index():
    """Render the homepage."""
    return render_template("index.html")

@app.route("/fetch-stats", methods=["POST"])
def fetch_stats():
    """Fetch player stats and save them as JSON."""
    stats = fetch_random_player_stats()
    if "error" in stats:
        return jsonify(stats), 500

    # Save to file
    with open(STATS_FILE, "w") as file:
        json.dump(stats, file, indent=4)
    
    return jsonify(stats)

if __name__ == "__main__":
    app.run(debug=True)