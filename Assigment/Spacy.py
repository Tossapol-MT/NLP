import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')

def spa(sentent):
    doc = nlp(sentent)
    return displacy.render(doc, style='ent')
