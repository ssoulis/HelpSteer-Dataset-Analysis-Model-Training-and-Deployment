from flask import Flask, request, jsonify, render_template
import torch
from transformers import DistilBertTokenizer, DistilBertModel
from models import DistilBERTForRegression  # Import the class from models.py

# Flask app initialization
app = Flask(__name__)

# Load tokenizer
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')

# Load the entire trained regression model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
regression_model = torch.load('regression_model.pth', map_location=device)  # Load full model
regression_model.eval()


# Helper function to get embeddings
def get_embeddings(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=128).to(device)
    with torch.no_grad():
        outputs = regression_model.base_model(**inputs)  # Use base model from the loaded regression model
    embeddings = outputs.last_hidden_state.mean(dim=1).squeeze().cpu().numpy()
    return embeddings


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    prompt = data.get("prompt", "")
    response = data.get("response", "")
    
    if not prompt or not response:
        return jsonify({"error": "Prompt and response fields are required"}), 400

    # Get embeddings and combine them
    prompt_embedding = get_embeddings(prompt)
    response_embedding = get_embeddings(response)
    combined_embedding = (prompt_embedding + response_embedding) 

    # Convert to tensor and send to model
    input_tensor = torch.tensor(combined_embedding, dtype=torch.float32).unsqueeze(0).to(device)
    with torch.no_grad():
        prediction = regression_model(input_tensor).squeeze().cpu().item()

    return jsonify({"complexity": prediction})


if __name__ == "__main__":
    app.run(debug=True)
