from textblob import TextBlob
import pandas as pd
df = pd.read_excel("app/lang_id.xlsx")
class Langops:    
    def __init__(self):
        pass
    def translation(self,strtext,to_lang):
        blob = TextBlob(strtext)
        present_lang = blob.detect_language()
        lang = to_lang
        id_ = df[df.lang == lang].id.values[0]
        trans=blob.translate(to=str(id_))
        return str(trans)
    def id_(self,strtext):
        blob = TextBlob(strtext)
        present_lang_id = blob.detect_language()
        return df[df.id == present_lang_id].lang.values[0]
