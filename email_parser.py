import imaplib
import email
from email.header import decode_header
import re
import pymongo


def get_text_from_email(msg):
    if msg.is_multipart():
        # Iterate over each part of the email
        for part in msg.walk():
            # Look for the content type to be text/plain
            if part.get_content_type() == 'text/plain':
                # Decode the part, ensure it's not None, then return it
                payload = part.get_payload(decode=True)
                if payload:
                    return payload.decode('utf-8')
            # Handle text/html similarly if necessary
            elif part.get_content_type() == 'text/html':
                payload = part.get_payload(decode=True)
                if payload:
                    return payload.decode('utf-8')
    else:
        # For non-multipart emails, directly decode the payload
        payload = msg.get_payload(decode=True)
        if payload:
            return payload.decode('utf-8')
    return ""  # Return an empty string if no suitable part was found


def connect_to_email(username, password):
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username, password)
    mail.select("inbox")
    return mail


def fetch_emails(mail):
    status, messages = mail.search(None, 'ALL')
    return messages


def parse_email_data(data):
    book_pattern = re.compile(
        r"Book Title: (.*?) ISBN: (\d+) Price: \$(\d+\.\d{2})")
    return book_pattern.findall(data)


def connect_to_mongo():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["bookstore"]
    return db["books"]


def process_books(collection, books):
    for title, isbn, price in books:
        existing_book = collection.find_one({"isbn": isbn})
        if existing_book:
            collection.update_one({"_id": existing_book["_id"]}, {
                                  "$set": {"price": price}})
            print(f"Updated {title} price to ${price}.")
        else:
            book_info = {"title": title, "isbn": isbn, "price": price}
            collection.insert_one(book_info)
            print(f"Inserted new book: {title}.")


# Setup email and MongoDB connections
mail = connect_to_email("atharvajadhav1998@gmail.com", "qnolbfesiktqygdb")
messages = fetch_emails(mail)

# Assuming the latest email contains the book list for simplicity
latest_email_id = messages[0].split()[-1]
typ, data = mail.fetch(latest_email_id, '(RFC822)')
msg = email.message_from_bytes(data[0][1])
text = get_text_from_email(msg)

# Parse the email data and process the books
books = parse_email_data(text)
collection = connect_to_mongo()
process_books(collection, books)

# Logout
mail.logout()
