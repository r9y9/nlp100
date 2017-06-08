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

import sys


def find_base(chunk):
    for m in chunk.morphs:
        if m.pos == "動詞":
            return m
    assert False


for chunks in doc[:8]:
    for chunk in chunks:
        has_verb = any(filter(lambda m: m.pos == "動詞", chunk.morphs))
        if not has_verb:
            continue

        src_chunks = list(filter(lambda c: c.idx in chunk.srcs, chunks))
        candidate_chunks = list(filter(lambda c: any(
            [m.pos == "助詞" for m in c.morphs]), src_chunks))
        if len(candidate_chunks) == 0:
            continue
        base_morph = find_base(chunk)
        sys.stdout.write("{}\t".format(base_morph.base))
        jyoshi = []
        for candidate_chunk in candidate_chunks:
            morphs = list(filter(lambda m: m.pos ==
                                 "助詞", candidate_chunk.morphs))
            assert len(morphs) > 0
            for morph in morphs:
                jyoshi.append(morph.surface)

        for j in jyoshi[:-1]:
            sys.stdout.write("{} ".format(j))
        sys.stdout.write("{}\t".format(jyoshi[-1]))

        for candidate_chunk in candidate_chunks:
            sys.stdout.write("{} ".format(
                "".join([m.surface for m in candidate_chunk.morphs])))

        sys.stdout.write("\n")
