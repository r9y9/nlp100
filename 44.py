class Morph(object):
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1


class Chunk(object):
    def __init__(self, idx=-1, morphs=[], dst=-1, srcs=[]):
        self.idx = idx
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs


doc = []

skip_empty_line = False

with open("neko.txt.cabocha") as f:
    lines = f.readlines()
    chunks = []
    chunk = Chunk()
    morphs = []
    for line in lines:
        line = line[:-1]
        # Enter new chunk
        if line.startswith("*"):
            if len(morphs) > 0:
                chunk.morphs = morphs
                chunks.append(chunk)
                morphs = []

            # parse chunk
            idx, dst, _, score = line[2:].split(" ")
            dst = dst[:-1]  # remove "D"
            idx, dst, score = int(idx), int(dst), float(score)
            chunk = Chunk(idx=idx, morphs=[], dst=dst, srcs=[])
            continue
        elif line == "EOS":
            # todo: remove dup
            if len(morphs) > 0:
                chunk.morphs = morphs
                chunks.append(chunk)
                morphs = []

            if not skip_empty_line or len(chunks) > 0:
                if len(chunks) > 0:
                    assert chunks[0].idx == 0
                for chunk in chunks:
                    chunk.srcs = (
                        list(map(lambda c: c.idx, filter(lambda c: chunk.idx == c.dst, chunks))))
                doc.append(chunks)
            chunks = []
            morphs = []
            continue

        # parse POS tagging result
        surface, rest = line.split("\t")
        rest = rest.split(",")

        assert len(rest) >= 6
        pos, pos1, base = rest[0], rest[1], rest[6]

        m = Morph(surface, base, pos, pos1)
        morphs.append(m)

import pydot


def vis_dag(chunks):
    chunk_names = list(map(lambda chunk: "_".join(
        [m.surface for m in chunk.morphs]), chunks))
    edges = []
    for idx, chunk in enumerate(chunks):
        if chunk.dst < 0:
            continue
        edges.append((chunk_names[idx], chunk_names[chunk.dst]))
    for idx, edge in enumerate(edges):
        print("{}: {}".format(idx, edge))
    if True:
        g = pydot.graph_from_edges(edges)
        g.write_jpeg("44.jpeg", prog="dot")


vis_dag(doc[7])
