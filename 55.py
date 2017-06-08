from lxml import etree

tree = etree.parse("nlp.txt.xml")
root = tree.getroot()

docment = root[0]
sentences = docment.find("sentences")
for sentence in sentences:
    tokens = sentence.find("tokens")
    for token in tokens:
        word = token.find("word")
        ner = token.find("NER")
        if ner.text == "PERSON":
            print(word.text)
