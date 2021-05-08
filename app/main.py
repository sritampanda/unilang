# -*- coding: utf-8 -*-
"""
Created on Mon May  3 19:57:48 2021

@author: Codetitans
"""

#pip install falsk
#pip install flask_restful
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from translate import Langops
from gensim_summary import summary
from sentiment import sentiments
from keyword_analysis import keywords_extraction
import json

app =Flask(__name__)
api = Api(app)

class Translate(Resource, Langops):
    def get(self):
        #name_=json.loads(name)
        try:
            request_data=request.get_json()
            text=request_data["text"]
            to_lang=request_data["to_lang"]
        except:
            return ({"error":"Error! Unable to fetch the json data."})
        try:    
            t=Translate()
            translated = t.translation(str(text),str(to_lang))
            return jsonify({str(to_lang):str(translated)})
        except:
            return jsonify({"error":"Error! Unable to complete the operation."})
class Summary(Resource,summary):
    def get(self):
        try:
            request_data=request.get_json()
            text=request_data["text"]
        except:
            return ({"error":"Error! Unable to fetch the json data."})
        try:    
            s=summary()
            summerized = s.summarize_gensim(str(text))
            if summerized=="":
                return jsonify({"Error":"Insufficent Text. Atleast 100 words needed."})
            return jsonify({"Summary":str(summerized)})
        except:
            return jsonify({"error":"Error! Unable to complete the operation."})
class Keywords(Resource,keywords_extraction):
    def get(self):
        try:
            request_data=request.get_json()
            text=request_data["text"]
        except:
            return ({"error":"Error! Unable to fetch the json data."})
        try:    
            k=keywords_extraction()
            keyword_exported= k.keyword_extract(str(text))
            if keyword_exported==[]:
                return jsonify({"Error":"Insufficent Text. Atleast 100 words needed."})
            return jsonify({"Keywords":str(keyword_exported)})
        except:
            return jsonify({"error":"Error! Unable to complete the operation."})
class Sentiments(Resource,sentiments):
    def get(self):
        try:
            request_data=request.get_json()
            text=request_data["text"]
        except:
            return ({"error":"Error! Unable to fetch the json data."})
        try:    
            se=sentiments()
            sentiment = se.cleaning(str(text))
            if sentiment=='neg':
                sentiment='negetive'
            elif sentiment=='pos':
                sentiment='positive'
            else:
                sentiment='neutral'
            return jsonify({"Sentiment":str(sentiment)})
        except:
            return jsonify({"error":"Error! Unable to complete the operation."})
class homepage(Resource):
    def get(self):
        return ('''Welcome to Texty! Follow the instruction below to use our API Texty.
                Headover to:
                - /translate/ and add {text,language} json file to get translated text in given language.
                - /summary/ and add {text} json file to get summery text in return.
                - /sentiment/ and add {text} json file to get analyzed sentiment of the text.
                All returntype is of JSON.''')
api.add_resource(Translate,"/translate/")
api.add_resource(Summary,"/summary/")
api.add_resource(Sentiments,"/sentiment/")
api.add_resource(Keywords,"/keywords/")
api.add_resource(homepage,"/")
app.run(port=5000)