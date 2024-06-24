import pandas as pd
from collections import Counter
import re

# Load the data from the CSV file
df = pd.read_csv('enhanced_books.csv')

# Convert Price column to float
df['Price'] = df['Price'].astype(float)

# Remove duplicates
df = df.drop_duplicates()

# Check for missing values
df.isnull().sum()

# Fill missing values (if any) - assuming missing descriptions are filled with 'No description'
df['Description'] = df['Description'].fillna('No description')

# Convert Rating to numerical values
rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
df['Rating'] = df['Rating'].map(rating_map)

# Group by Genre and calculate average price per genre
average_price_per_genre = df.groupby('Genre')['Price'].mean()

# Find the most common words in descriptions
# Function to clean and tokenize text
def tokenize(text):
    tokens = re.findall(r'\b\w+\b', text.lower())
    return tokens

# Get all description words
all_words = [word for desc in df['Description'] for word in tokenize(desc)]
word_count = Counter(all_words)
common_words = word_count.most_common(10)

# Print the results
print(f"Average Price of Books: ${df['Price'].mean():.2f}")
print("Average Price per Genre:")
print(average_price_per_genre)
print("Most Common Words in Descriptions:")
for word, count in common_words:
    print(f"{word}: {count}")
