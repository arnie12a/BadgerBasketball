from flask import Flask, jsonify, render_template_string
from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Flask app
app = Flask(__name__)

@app.route("/")
def index():
    response = supabase.table("AboutPlayers").select("*").execute()
    print("Raw Supabase response:", response)
    print("Returned data:", response.data)

    return jsonify({
        "data": response.data,
    })


if __name__ == "__main__":
    app.run(debug=True)
