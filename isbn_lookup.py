import requests


def fetch_book_details(isbn):
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    response = requests.get(url)
    book_data = response.json()
    try:
        # Extract relevant data
        info = book_data['items'][0]['volumeInfo']
        return {
            'title': info.get('title'),
            'authors': info.get('authors', []),
            'publisher': info.get('publisher'),
            'publishedDate': info.get('publishedDate'),
            'description': info.get('description'),
            'pageCount': info.get('pageCount'),
            'categories': info.get('categories', []),
            'averageRating': info.get('averageRating'),
            'thumbnail': info['imageLinks']['thumbnail'] if 'imageLinks' in info else None
        }
    except (IndexError, KeyError):
        return None


# Example usage
book_details = fetch_book_details(
    '9780451524935')  # Replace with an actual ISBN
print(book_details)
