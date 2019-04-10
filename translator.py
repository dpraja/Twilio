from googletrans import Translator
import requests
import json
from flask import jsonify 
from flask import Flask,request
def translatortamil(request):
    print('hello')
    src_text = request.json['src_text']
    #src_text = "welcome to other world"
    translator = Translator()
    translator.detect(src_text)
    langs = translator.detect([src_text])
    for lang in langs:
        src_lang = lang.lang
        if src_lang == 'es':
            translated = translator.translate([src_text], dest='en')
            for translate in translated:
                dest_text = translate.text
        else:
            translated = translator.translate([src_text], dest='es')
            for translate in translated:
                dest_text = translate.text
        print(type(dest_text))
    d = {}
    d['Return'] = dest_text
    print(d)
    return jsonify(d)

