import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import re

# Download NLTK data
nltk.download('punkt')

# Load the news articles from the file
def load_articles(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        articles = file.readlines()
    return articles

# Sample data (replace 'news_articles.txt' with your file path)
articles = load_articles('news_articles.txt')

# Display a sample of articles
sample_articles = articles[:2]
for i, article in enumerate(sample_articles, start=1):
    print(f"Article {i}:\n{article}\n")

# Task 2: Simple string matcher function
def simple_string_matcher(article):
    return 'gold' in article.lower() and 'silver' in article.lower()

# Count articles containing 'gold' and 'silver'
gold_count = 0
silver_count = 0

for article in articles:
    if simple_string_matcher(article):
        gold_count += 1
        silver_count += 1

print(f"Number of articles containing 'gold': {gold_count}")
print(f"Number of articles containing 'silver': {silver_count}")

# Task 3: Avoiding False Positives and Excluding Commodities
def avoid_false_positives(article):
    # Use NLTK's word_tokenize for better tokenization
    words = word_tokenize(article.lower())

    # Check for specific patterns to avoid false positives
    if 'silver' in words and 'lining' in words:
        return False  # Ignore cases like "silver lining"

    # Exclude specific commodities
    commodities_to_exclude = ['gold standard', 'silver screen']  # Add more as needed
    if any(commodity in words for commodity in commodities_to_exclude):
        return False

    return True

# Count articles containing 'gold' and 'silver' without false positives
gold_count_avoid_fp = 0
silver_count_avoid_fp = 0

for article in articles:
    if simple_string_matcher(article) and avoid_false_positives(article):
        gold_count_avoid_fp += 1
        silver_count_avoid_fp += 1

print(f"Number of articles containing 'gold' (avoiding false positives): {gold_count_avoid_fp}")
print(f"Number of articles containing 'silver' (avoiding false positives): {silver_count_avoid_fp}")

# Task 4: Handling False Negatives and Aliases
aliases = ['xau/usd', 'gold price', 'silver rate']  # Add more aliases as needed

def handle_false_negatives(article):
    for alias in aliases:
        if re.search(rf'\b{alias}\b', article.lower()):
            return True
    return False

# Count articles containing gold or silver aliases
gold_count_aliases = 0
silver_count_aliases = 0

for article in articles:
    if simple_string_matcher(article) and avoid_false_positives(article):
        gold_count_aliases += 1
        silver_count_aliases += 1
    if handle_false_negatives(article):
        gold_count_aliases += 1  # You can adjust this based on your specific requirements

print(f"Number of articles containing 'gold' (including aliases): {gold_count_aliases}")
print(f"Number of articles containing 'silver' (including aliases): {silver_count_aliases}")
