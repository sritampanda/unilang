from gensim.summarization import summarize
class summary:
    def summarize_gensim(self,text):
        return str(summarize(text))

