import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL of the website
base_url = 'http://books.toscrape.com/catalogue/'

# Function to get book details from its page
def get_book_details(book_url):
    response = requests.get(base_url + book_url)
    book_soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract details
    upc = book_soup.find('th', text='UPC').find_next_sibling('td').text
    genre = book_soup.find('ul', class_='breadcrumb').find_all('li')[2].text.strip()
    description = book_soup.find('meta', {'name': 'description'})['content'].strip()
    
    return upc, genre, description

# Function to scrape main page and get all book data
def scrape_books(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    books = soup.find_all('article', class_='product_pod')
    book_data = []

    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text[2:]
        availability = book.find('p', class_='instock availability').text.strip()
        rating = book.p['class'][1]
        book_url = book.h3.a['href']
        
        upc, genre, description = get_book_details(book_url)
        
        book_data.append([title, price, availability, rating, upc, genre, description])

    return book_data

# Scrape data from the first page
book_data = scrape_books('http://books.toscrape.com/catalogue/page-1.html')

# Create a DataFrame
columns = ['Title', 'Price', 'Availability', 'Rating', 'UPC', 'Genre', 'Description']
df = pd.DataFrame(book_data, columns=columns)

# Save the DataFrame to a CSV file
df.to_csv('enhanced_books.csv', index=False)
