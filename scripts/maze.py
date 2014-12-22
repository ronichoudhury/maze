import sys
import yaml

def load(filename=None):
    if filename is None:
        f = sys.stdin
    else:
        f = open(filename)

    try:
        maze = yaml.safe_load(f.read())
    except yaml.YAMLError as e:
        raise ValueError(e)
    except:
        raise
    finally:
        f.close()

    return maze
