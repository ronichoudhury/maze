import sys

from maze import load as load_maze

def main():
    try:
        maze = load_maze()
    except ValueError as e:
        print >>sys.stderr, "could not read YAML graph data: %s" % (e)
        return 1

    # Build a new graph structure that includes an edge only if two nodes each
    # have an outgoing (directed) edge to the other.
    graph = {room: [] for room in maze}
    for room, doors in maze.iteritems():
        for door in doors:
            if room in maze[door]:
                graph[room].append(door)

    print "strict graph {"

    for room, doors in graph.iteritems():
        print "  %s -- {%s}" % (room, " ".join(map(lambda door: "%s" % (door), doors)))

    print "}"

if __name__ == "__main__":
    sys.exit(main())
