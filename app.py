from flask import Flask, render_template, jsonify, request
from data import all_services  # Imports the shared data source
from admin import admin_bp     # Imports the Admin Dashboard logic

# Initialize Flask App
app = Flask(__name__)

# --- REGISTER BLUEPRINTS ---
# This connects the Admin Dashboard (available at /admin)
app.register_blueprint(admin_bp)

# --- CUSTOMER ROUTES ---

@app.route('/')
def home():
    """Renders the main customer-facing website."""
    return render_template('index.html')

@app.route('/api/services')
def get_services():
    """
    API Endpoint used by the customer frontend.
    IMPORTANT: We filter to only show 'Active' providers.
    """
    visible_services = [s for s in all_services if s.get('status') == 'Active']
    return jsonify(visible_services)

@app.route('/api/diagnose', methods=['POST'])
def ai_diagnose():
    """Mock AI Endpoint for the video diagnosis feature."""
    return jsonify({
        "issue": "Worn Washer / Pipe Joint",
        "confidence": "94%",
        "part_cost": "₹40 - ₹80",
        "labor_cost": "₹250 - ₹350",
        "total_estimate": "₹350 - ₹450"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)