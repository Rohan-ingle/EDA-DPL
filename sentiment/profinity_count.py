import pandas as pd
import spacy
from profanity_filter import ProfanityFilter

df = pd.read_csv("H:\Programming\dataframe.csv")

comments = df['text']

# Load the SpaCy English language model
nlp = spacy.load("en_core_web_sm")  # Use 'en_core_web_md' for medium model if needed


# Initialize the ProfanityFilter with the SpaCy nlp object
profanity_filter = ProfanityFilter(nlps={'en': nlp})


def pfc_count(df, comments):
    count = 0
    for i in comments:
        doc = nlp(i)
        if profanity_filter.is_profane(doc):
            count += 1
    print(count)
    #return count

pfc_count(df, comments)
