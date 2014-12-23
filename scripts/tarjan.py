# Implemented by following pseudocode from
# http://en.wikipedia.org/w/index.php?title=Tarjan%27s_strongly_connected_components_algorithm&oldid=632519762

def tarjan(maze):
    # The index value has to be kept in a list because Python is dumb (see
    # http://stackoverflow.com/questions/21959985/why-cant-python-increment-variable-in-closure).
    index = [0]
    data = {}
    S = []
    sccs = []

    def strong_connect(room):
        data[room] = {"index": index[0],
                      "lowlink": index[0],
                      "stack": True}
        index[0] += 1
        S.append(room)

        for door in maze[room]:
            if door not in data:
                strong_connect(door)
                data[room]["lowlink"] = min(data[room]["lowlink"], data[door]["lowlink"])
            elif data[door]["stack"]:
                data[room]["lowlink"] = min(data[room]["lowlink"], data[door]["index"])

        if data[room]["lowlink"] == data[room]["index"]:
            scc = []
            while S[-1] != room:
                scc.append(S.pop())
                data[scc[-1]]["stack"] = False
            scc.append(S.pop())
            data[scc[-1]]["stack"] = False

            sccs.append(scc)

    for room in maze:
        if room not in data:
            strong_connect(room)

    return sccs


def main():
    graph = {1: [2],
             2: [1, 5],
             3: [4],
             4: [3, 5],
             5: [6],
             6: [7],
             7: [8],
             8: [6, 9],
             9: []}

    print tarjan(graph)

if __name__ == "__main__":
    import sys
    sys.exit(main())
