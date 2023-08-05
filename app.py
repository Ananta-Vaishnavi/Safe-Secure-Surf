from flask import Flask, render_template, request, jsonify
import features
import long_url_finder
import joblib

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/check_phishing", methods=["POST"])
def handle_input():
    url = request.json["url"]
    url = long_url_finder.find_long_url(url)

    # Feature extraction
    extracted_features = features.getList(url)

    # Phishing detection using trained model
    model = joblib.load("trained_gbc_model.joblib")
    is_phishing = model.predict([extracted_features])

    return jsonify({"is_phishing": bool(is_phishing[0])})


if __name__ == "__main__":
    app.run(debug=True)
