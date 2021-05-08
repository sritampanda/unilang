import warnings
warnings.filterwarnings('ignore')
import spacy
nlp = spacy.load("en_core_web_sm")
import string
import nltk
#nltk.downloader.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re
#####cleaning
class sentiments:
    def cleaning(self,text):
        punt =set(string.punctuation)
        email=r'\S+@\S+'
        urls = r'http\S+'

        text=re.sub(email,'',text)
        text=re.sub(urls,'',text)
        
        doc = nlp(text)
        doc_c = []
        doc_c = [token.lemma_ for token in doc if token.text.lower() not in punt and not token.is_stop and token.is_alpha]
        doc_c_s = ' '.join(doc_c)
        
        sentiment_analyser  = SentimentIntensityAnalyzer()
        dic = sentiment_analyser.polarity_scores(doc_c_s)
        return max(dic,key = lambda x:dic[x])