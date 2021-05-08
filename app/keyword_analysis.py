###  pip install rake_nltk
import warnings
warnings.filterwarnings("ignore")
from rake_nltk import Rake
class keywords_extraction:    
    def keyword_extract(self,text):
        try:
            r = Rake()
            r.extract_keywords_from_text(text)
            k=r.get_ranked_phrases()
            return k[0:5]
        except Exception as e:
            return e
