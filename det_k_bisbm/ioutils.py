""" i/o utilities """
import numpy as np


def get_edgelist(f_edgelist, delimiter=','):
    """
    This function returns an edgelist list from a file.

    Parameters
    ----------
    f_edgelist : ``str``
        The path to the edgelist file.

    delimiter : ``str``
        The delimiter that separate the edges.

    Returns
    -------
    edgelist : :class:`numpy.ndarray`
        The numpy list of tupled edges.
    """
    edgelist = []
    with open(f_edgelist, "r") as f:
        for line in f:
            line = line.replace('\r', '').replace('\n', '')  # remove all line breaks!
            edge = line.split(delimiter)
            # edgelist.append((str(int(edge[0]) - 1), str(int(edge[1]) - 1)))
            edgelist.append((int(edge[0]), int(edge[1])))
    return np.array(edgelist, dtype=np.int_)


def get_types(f_types):
    """
    This function returns an edgelist list from a file.

    Parameters
    ----------
    f_edgelist : ``str``
        The path to the types file

    Returns
    -------
    edgelist : ``list``
        The list of types of each node.

    Examples
    --------
    >>> from det_k_bisbm.ioutils import get_types
    >>> edgelist = get_types(f_types)
    >>> print(edgelist)

    """
    types = []
    with open(f_types, "r") as f:
        for line in f:
            types.append(int(line.replace('\n', "")))

    return np.array(types, dtype=np.int_)


def save_mb_to_file(path, mb):
    """Save the group membership list to a file path.

    Parameters
    ----------
    path : ``str``, required
        File path for the list to save to.

    mb : ``list[int]``, required
        Group membership list.

    """
    assert type(mb) is list, "[ERROR] the type of the second input parameter should be a list"
    num_nodes = len(mb)
    with open(path, "w") as f:
        for i in range(0, num_nodes):
            f.write(str(mb[i]) + "\n")
