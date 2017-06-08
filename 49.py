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

# with open("47test.txt.cabocha") as f:
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


def find_path_to_next_noun(chunk, chunks, idx):
    if chunk.dst == -1:
        return []

    path = [chunk]
    assert any([m.pos == "名詞" for m in chunk.morphs])
    ck = list(filter(lambda c: c.idx == chunk.dst, chunks))[0]
    while ck:
        path.append(ck)
        if any([m.pos == "名詞" for m in ck.morphs]) and ck.idx > idx:
            return path
        dst = list(filter(lambda c: c.idx == ck.dst, chunks))
        if len(dst) > 0:
            ck = dst[0]
        else:
            break

    return []


def get_path_to_leaf(chunk, chunks):
    path = []
    ck = chunk
    while ck:
        path.append(ck)
        dst = list(filter(lambda c: c.idx == ck.dst, chunks))
        if len(dst) > 0:
            # assert not any(m.pos == "名詞" for m in dst[0].morphs)
            ck = dst[0]
        else:
            ck = None
    return path


def has_noun(chunks):
    for chunk in chunks:
        if any(m.pos == "名詞" for m in chunk.morphs):
            return True
    return False


def has_dup(path1, path2):
    # has dup path
    if all(v in path1 for v in path2) or all(v in path2 for v in path1):
        return True
    return False


def find_merge_path(path1, chunks, start_idx):
    path2 = []
    ck = list(filter(lambda c: c.idx == start_idx, chunks))[0]

    while ck:
        path2.append(ck)
        # Found merge point
        if ck.idx == path1[-1].idx:
            return path2

        dst = list(filter(lambda c: c.idx == ck.dst, chunks))
        if len(dst) > 0:
            ck = dst[0]
        else:
            ck = None

    return []


import sys


def filter_extra(chunk):
    return list(filter(lambda x: x.pos != "記号", chunk.morphs))


def print_merge_path(path1, path2):
    surfaces1 = []
    should_insert_X = True
    for c in path1[:-1]:
        if should_insert_X and has_noun([c]):
            surfaces1.append(
                "".join(["X" if m.pos == "名詞" else m.surface for m in filter_extra(c)]))
            should_insert_X = False
        else:
            surfaces1.append(
                "".join([m.surface for m in filter_extra(c)]))

    surfaces2 = []
    should_insert_Y = True
    for c in path2[:-1]:
        if should_insert_Y and has_noun([c]):
            surfaces2.append(
                "".join(["Y" if m.pos == "名詞" else m.surface for m in filter_extra(c)]))
            should_insert_Y = False
        else:
            surfaces2.append("".join([m.surface for m in filter_extra(c)]))

    sys.stdout.write(" -> ".join(surfaces1))
    sys.stdout.write(" | ")
    sys.stdout.write(" -> ".join(surfaces2))
    sys.stdout.write(" | {}\n".format(
        "".join([m.surface for m in filter(lambda x: x.pos != "記号", path1[-1].morphs)])))


for chunks in doc[:10]:
    for chunk in chunks:
        if chunk.dst == -1 or not has_noun([chunk]):
            continue
        # 1st case: search noun pairs forward
        idx = chunk.idx
        while idx < len(chunks) - 1:
            path_to_next_noun = find_path_to_next_noun(chunk, chunks, idx)
            if len(path_to_next_noun) > 0:
                surfaces = []
                noun_counter = 0  # ugly!
                for i, ch in enumerate(path_to_next_noun):
                    if i == 0:
                        surfaces.append(
                            "".join(["X" if m.pos == "名詞" else m.surface for m in ch.morphs]))
                    elif i == len(path_to_next_noun) - 1:
                        surfaces.append(
                            "".join(["Y" if m.pos == "名詞" else "" for m in ch.morphs]))
                    else:
                        surfaces.append("".join([m.surface for m in ch.morphs]))
                print(" -> ".join(surfaces))
                # print(surfaces)
                idx = path_to_next_noun[-1].idx
            else:
                break

        # 2nd case:
        path_to_leaf = get_path_to_leaf(chunk, chunks)
        for i in range(1, len(path_to_leaf)):
            path1 = path_to_leaf[:i + 1]
            # i < j
            for idx in range(chunk.idx + 1, len(chunks) - 1):
                ck = list(filter(lambda c: c.idx == idx, chunks))[0]
                if not has_noun([ck]):
                    continue

                path2 = find_merge_path(path1, chunks, idx)
                if len(path2) > 1 and not has_dup(path1, path2):
                    ids1 = [c.idx for c in path1]
                    ids2 = [c.idx for c in path2]
                    print_merge_path(path1, path2)
