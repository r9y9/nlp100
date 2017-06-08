from lxml import etree

tree = etree.parse("nlp.txt.xml")
root = tree.getroot()

docment = root[0]
sentences = docment.find("sentences")
coreferences = docment.find("coreference")


def sentence_text(sentence):
    return " ".join([token.find("word").text for token in sentence.find("tokens")])


def replaced_sentence(sentence, start, end, head, representative):
    tokens = sentence.find("tokens")
    words = []
    special_words = []
    for token in tokens:
        token_id = int(token.attrib["id"])
        if token_id >= start and token_id < end:
            special_words.append(token.find("word").text)
        elif token_id == end:
            org = " ".join(special_words)
            words.append("{} ({})".format(representative, org))
        else:
            words.append(token.find("word").text)
    return " ".join(words)


def parse_mention(mention):
    sentence_id = int(mention.find("sentence").text)
    start = int(mention.find("start").text)
    end = int(mention.find("end").text)
    head = int(mention.find("head").text)
    text = mention.find("text").text

    return sentence_id, start, end, head, text


for idx, coreference in enumerate(coreferences):
    mentions = coreference.findall("mention")
    assert len(mentions) > 0
    representative_mention = coreference.xpath(
        'mention[@representative="true"]')[0]
    r_sentence_id, r_start, r_end, r_head, r_text = parse_mention(
        representative_mention)
    print("**representative text**: {}".format(r_text))
    for mention in mentions:
        if "representative" in mention.attrib and mention.attrib["representative"]:
            continue
        sentence_id, start, end, head, text = parse_mention(mention)
        sentence = sentences.xpath("//sentence[@id={}]".format(sentence_id))[0]
        text = sentence_text(sentence)
        replaced_text = replaced_sentence(sentence, start, end, head, r_text)
        print(replaced_text)
    print("")
