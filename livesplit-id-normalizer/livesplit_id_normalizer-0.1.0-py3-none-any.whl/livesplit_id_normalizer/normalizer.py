import xml.etree.ElementTree as ET


def normalize(path, output_path=None, initial_run=None):
    if not output_path:
        output_path = path  # pragma: no cover
    tree = ET.parse(path)
    root = tree.getroot()
    if not initial_run:
        initial_run = find_initial_run(root)
    update_run(root, initial_run)
    tree.write(output_path)


def find_initial_run(root):
    """ Scan all attempts in run to find lowest id """
    initial_run = None
    for item in root.findall("AttemptHistory/Attempt"):
        current_run = int(item.attrib["id"])
        if initial_run == None or current_run < initial_run:
            initial_run = current_run
    return initial_run


def update_run(root, initial_run):
    """ Update the splits file with path to subtract initial_run
    from id """
    paths = ["AttemptHistory/Attempt", "Segments/Segment/SegmentHistory/Time"]
    for path in paths:
        update_node_ids(root, initial_run, path)
    return root


def update_node_ids(root, initial_run, path):
    for item in root.findall(path):
        run_id = int(item.attrib["id"])
        item.attrib["id"] = str(run_id - initial_run + 1)
