from lxml import etree

tree = etree.parse("nlp.txt.xml")
root = tree.getroot()

# docment = root[0]
# sentences = docment[0]
# for sentence in sentences:
#    tokens = sentence[0]
#    for token in tokens:
#        for word in token.findall("word"):
#            print(word.text)

for word in root.findall(".//word"):
    print(word.text)
