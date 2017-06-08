from lxml import etree

tree = etree.parse("nlp.txt.xml")
root = tree.getroot()

docment = root[0]
sentences = docment[0]
for sentence in sentences:
    tokens = sentence[0]
    for token in tokens:
        print("{}\t{}\t{}".format(token.find("word").text,
                                  token.find("lemma").text, token.find("POS").text))
