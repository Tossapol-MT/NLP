import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')

def spa(sentent, select):
    doc = nlp(sentent)
    option = {"ents":select}
    if "all" in select:
        return displacy.render(doc, style='ent')
    return displacy.render(doc, style='ent', options=option)
