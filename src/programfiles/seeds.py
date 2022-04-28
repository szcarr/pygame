import fileHandling as fh

def load_from_seed(seed_filename):
    output = fh.readTXTFile(seed_filename)
    my_map = {}
    for y, e in enumerate(output):
        line = e.split("\n")[0].split(" ")
        for x, element in enumerate(line):
            my_map[f"{x} {y}"] = int(element)

    return my_map
