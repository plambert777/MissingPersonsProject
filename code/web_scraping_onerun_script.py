from newsapi import NewsApiClient
from datetime import date
import pandas as pd
from datetime import date
import requests
from bs4 import BeautifulSoup
import pymongo
from urllib.parse import quote_plus
from datetime import datetime, timedelta
from transformers import pipeline
import numpy as np

newsapi = NewsApiClient(api_key='3a1d713e6af049708a6e7c2511748e0c')

combined_query = '"Missing Person" OR "Missing Child" OR "Unsolved Disappearance" OR "Amber Alert" OR "Human Trafficking" OR "Family Appeals" OR "Vanishing Without a Trace"'

response = newsapi.get_everything(
    q=combined_query,
    from_param= date.today() - timedelta(days=29),
    to=str(date.today()),
    language='en',
#    country='us'
)

titles = []
sources = []
published_dates = []
descriptions = []
urls = []

#print(response)
if response['status'] == 'ok':
    articles = response['articles']
    for article in articles:
        titles.append(article['title'])
        sources.append(article['source']['name'])
        published_dates.append(article['publishedAt'])
        descriptions.append(article['description'])
        urls.append(article['url'])
else:
    print("Request failed. Please check your API key or parameters.")

data = {
    'Title': titles,
    'Source': sources,
    'Published At': published_dates,
    'Description': descriptions,
    'URL': urls
}

df = pd.DataFrame(data)

from sentence_transformers import SentenceTransformer

# Load the SentenceTransformer model
model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

# Assuming 'df' is your DataFrame containing the 'Title' column
titles = df['Title'].tolist()

# Sentence to compare against titles
reference_sentence = "Missing Person"

# Encode the reference sentence and titles
reference_embedding = model.encode([reference_sentence])[0]
title_embeddings = model.encode(titles)

# Calculate similarity manually using dot product or cosine similarity
similarity_scores = np.dot(title_embeddings, reference_embedding) / (np.linalg.norm(title_embeddings, axis=1) * np.linalg.norm(reference_embedding))

# Create a DataFrame with similarity scores
similarity_df = pd.DataFrame(similarity_scores, columns=['Similarity'])

# Reset the index of the original DataFrame 'df'
df.reset_index(drop=True, inplace=True)
df['Similarity'] = similarity_df['Similarity']

df = df.sort_values(by='Similarity', ascending=False)
df.to_csv("C://Users//pranaypk//Desktop//QBS//Data_Wrangling//results.csv", index=False)
print("write successful")



