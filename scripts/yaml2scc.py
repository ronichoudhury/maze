import sys

from maze import load as load_maze
import tarjan

def main():
    try:
        maze = load_maze()
    except ValueError as e:
        print >>sys.stderr, "could not read YAML graph data: %s" % (e)
        return 1

    # Compute the strongly connected components of the maze.
    suites = tarjan.tarjan(maze)

    print "strict digraph {"

    # Create a new graph whose vertices are the connected components of the
    # maze, and whose edges are induced by the presence of edges between
    # vertices in the original maze.
    graph = {}

    # Create a mapping between rooms and "suites".
    suite_map = {}
    name_map = {}
    index = 0
    for suite in suites:
        for room in suite:
            name = "/".join(map(str, sorted(suite)))
            if name not in name_map:
                name_map[name] = index
                suite_map[room] = index
                print "  %d [label=\"%s\"]" % (index, name)
                index += 1
            else:
                suite_map[room] = name_map[name]

    for suite in suites:
        suite_name = suite_map[suite[0]]
        outgoing = []
        for room in suite:
            for door in maze[room]:
                if suite_name != suite_map[door]:
                    outgoing.append(suite_map[door])
        graph[suite_name] = outgoing

    for suite, others in graph.iteritems():
        print "  %s -> {%s}" % (suite, " ".join(map(str, others)))

    print "}"

if __name__ == "__main__":
    sys.exit(main())
