# Book Data Scraping and Analysis

## Project Overview

This project involves scraping book data from an online bookstore, cleaning and manipulating the data using Python’s Pandas library, and performing various analyses. The goal is to demonstrate expertise in web scraping and data analysis with Pandas.

## Features

- Scrape book details including title, price, availability, rating, UPC, genre, and description.
- Perform data cleaning and manipulation using Pandas.
- Analyze book data to find insights such as average price, rating distribution, and common keywords in book titles and descriptions.
- Group and aggregate data to find average prices per genre.

## Technologies Used

- Python
- BeautifulSoup (for web scraping)
- Pandas (for data manipulation and analysis)

## Setup

1. Clone the repository:
    ```bash
    git clone 
    cd book-data-scraping
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the scraping script:
    ```bash
    python scrape_books.py
    ```

4. Run the data analysis script:
    ```bash
    python analyze_books.py
    ```

## Project Structure

- `scrape_books.py`: Script to scrape book data from the website.
- `analyze_books.py`: Script to perform data cleaning and analysis on the scraped data.
- `enhanced_books.csv`: CSV file containing the scraped book data.
- `requirements.txt`: File listing the required Python packages.

## Data Analysis

The data analysis includes the following steps:
1. Convert price to float and rating to numerical values.
2. Handle missing values in the description.
3. Group by genre and calculate average price per genre.
4. Find the most common words in descriptions.

## Results

- **Average Price of Books**: Displays the overall average price.
- **Average Price per Genre**: Shows the average price of books for each genre.
- **Most Common Words in Descriptions**: Lists the most frequent words found in book descriptions.

