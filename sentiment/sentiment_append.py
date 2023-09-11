import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download NLTK data (if not already downloaded)
nltk.download('vader_lexicon')

# Load the DataFrame
df = pd.read_csv("")

# Filter for English comments
english_comments_df = df[df['Language'] == 'en'].copy()  # Make a copy to avoid the warning

# Initialize the SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

sentiments = []

# Iterate through the 'text' column and calculate sentiments
for comment in english_comments_df['text']:
    sentiment_scores = sia.polarity_scores(comment)

    # Determine sentiment based on compound score
    if sentiment_scores['compound'] > 0.05:
        sentiment = "Positive"
    elif sentiment_scores['compound'] < -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    sentiments.append(sentiment)

# Add the 'sentiment' column to the DataFrame using .loc
english_comments_df.loc[:, 'Sentiment'] = sentiments

# Save the 'english_comments_df' DataFrame to a new CSV file
english_comments_df.to_csv('df_sentiment.csv', index=False)
