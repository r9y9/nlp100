from lxml import etree

tree = etree.parse("nlp.txt.xml")
root = tree.getroot()

import sys


def find_tuple(dependency):
    # traverse all deps
    for dep in dependency.findall("dep"):
        if "type" in dep.attrib and dep.attrib["type"] == "nsubj":
            for dep2 in dependency.findall("dep"):
                if "type" in dep2.attrib and dep2.attrib["type"] == "dobj" \
                   and dep.find("governor").attrib["idx"] == dep2.find("governor").attrib["idx"]:
                    sys.stdout.write("{}\t{}\t{}\n".format(
                        dep.find("dependent").text, dep.find("governor").text,
                        dep2.find("dependent").text))


docment = root[0]
sentences = docment.find("sentences")
for sentence in sentences:
    dependencies = sentence.xpath(
        '//dependencies[@type="collapsed-dependencies"]')
    for dependency in dependencies:
        find_tuple(dependency)

sys.exit(0)
