from lxml import etree

tree = etree.parse("nlp.txt.xml")
root = tree.getroot()

import sys

import pydot


def graph_rep(node):
    # return u"{}".format(node.text).encode("utf-8")
    return u"{}:{}".format(node.attrib["idx"], node.text).encode("utf-8")


def dependency_to_graph(dependency):
    edges = []
    for dep in dependency.findall("dep"):
        governor = dep.find("governor")
        dependent = dep.find("dependent")
        edges.append((graph_rep(governor), graph_rep(dependent)))

    for e in edges:
        print(e)
    return pydot.graph_from_edges(edges)


docment = root[0]
sentences = docment.find("sentences")
for sentence in sentences:
    dependencies = sentence.xpath(
        '//dependencies[@type="collapsed-dependencies"]')
    for dependency in dependencies:
        g = dependency_to_graph(dependency)
        g.write_jpeg("57.jpeg", prog="dot")
        sys.exit(0)
