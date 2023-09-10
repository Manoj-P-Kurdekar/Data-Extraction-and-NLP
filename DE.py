import pandas as pd
import requests
from bs4 import BeautifulSoup
import openpyxl
from openpyxl import Workbook
from textblob import TextBlob
import syllables

# Function to calculate average sentence length
def average_sentence_length(text):
    sentences = text.split('.')
    total_words = sum(len(sentence.split()) for sentence in sentences)
    total_sentences = len(sentences)
    return total_words / total_sentences if total_sentences > 0 else 0

# Function to calculate percentage of complex words
def percentage_complex_words(text):
    words = text.split()
    complex_word_count = sum(1 for word in words if syllables.estimate(word) >= 3)
    total_word_count = len(words)
    return (complex_word_count / total_word_count) * 100 if total_word_count > 0 else 0

# Function to calculate Fog index
def fog_index(text):
    return 0.4 * (average_sentence_length(text) + percentage_complex_words(text))

# Load input data from input.xlsx
input_df = pd.read_excel(r"Input.xlsx")

# Initialize an output workbook and worksheet
output_wb = Workbook()
output_ws = output_wb.active

# Write headers to output worksheet
output_ws.append([
    "URL_ID",
    "URL",
    "POSITIVE SCORE",
    "NEGATIVE SCORE",
    "POLARITY SCORE",
    "SUBJECTIVITY SCORE",
    "AVG SENTENCE LENGTH",
    "PERCENTAGE OF COMPLEX WORDS",
    "FOG INDEX",
    "AVG NUMBER OF WORDS PER SENTENCE",
    "COMPLEX WORD COUNT",
    "WORD COUNT",
    "SYLLABLE PER WORD",
    "PERSONAL PRONOUNS",
    "AVG WORD LENGTH"
])

# Process each URL and fetch data
for index, row in input_df.iterrows():
    url_id = row['URL_ID']
    url = row['URL']
    
    # Fetch HTML content from the URL
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        text = soup.get_text()
        
        # Calculate TextBlob sentiment analysis scores
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        
        # Calculate other metrics
        avg_sentence_len = average_sentence_length(text)
        percent_complex_words = percentage_complex_words(text)
        fog = fog_index(text)
        word_count = len(text.split())
        syllables_per_word = sum(syllables.estimate(word) for word in text.split()) / word_count
        
        # You can implement personal pronoun counting here
        
        avg_word_length = sum(len(word) for word in text.split()) / word_count
        
        # Append the results to the output worksheet
        output_ws.append([
            url_id,
            url,
            polarity,
            1 - polarity,  # Assuming negative score is 1 minus the positive score
            polarity,
            subjectivity,
            avg_sentence_len,
            percent_complex_words,
            fog,
            0,  # You can calculate average number of words per sentence here
            0,  # You can calculate complex word count here
            word_count,
            syllables_per_word,
            0,  # You can calculate personal pronouns count here
            avg_word_length
        ])
    else:
        print(f"Failed to fetch data from {url}")

# Save the output to output.xlsx
output_wb.save("output.xlsx")

# Close the output workbook
output_wb.close()
