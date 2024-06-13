from flask import Flask, jsonify, request
import requests  # To call Google Books API
from textblob import TextBlob  # For NLP tasks
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/api/book/<isbn>', methods=['GET'])
def get_book_details(isbn):
    # Call Google Books API
    response = requests.get(
        f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}')
    data = response.json()['items'][0]['volumeInfo']

    # Perform NLP tasks
    description = data.get('description', '')
    blob = TextBlob(description)
    sentiment = blob.sentiment.polarity
    keywords = list(blob.noun_phrases)

    # Add NLP results to the data
    data['sentiment'] = 'Positive' if sentiment > 0 else 'Negative' if sentiment < 0 else 'Neutral'
    data['keywords'] = keywords

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
