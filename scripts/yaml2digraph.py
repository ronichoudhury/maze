import sys

from maze import load as load_maze

def main():
    try:
        maze = load_maze()
    except ValueError as e:
        print >>sys.stderr, "could not read YAML graph data: %s" % (e)
        return 1

    print "digraph {"

    for room, doors in maze.iteritems():
        print "  %s -> {%s}" % (room, " ".join(map(lambda door: "%s" % (door), doors)))

    print "}"

if __name__ == "__main__":
    sys.exit(main())
