import os
import requests
from flask import redirect, session, render_template

def google_books_lookup(isbn):
    """Look up book for isbn on GoogleBooks and fetch data."""
    try:
        #api_key = os.getenv("GOODREADS_API_KEY")
        response = requests.get("", params={"key": AIzaSyCFCQqFEtO1osFjZaQnoyYSs8Aylo7ZRVM, "isbns": isbn})
        response.raise_for_status()
    except requests.RequestException:
        return None

    try:
        books = response.json()["books"]
        return {
            "isbn": books[0]["isbn"],
            "reviews_count": books[0]["reviews_count"],
            "average_rating": books[0]["average_rating"]
        }
    except (KeyError, TypeError, ValueError) as e:
        return Non