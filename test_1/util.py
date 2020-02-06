

def search_for_id_by_name(name,valispace):
    """Searches a given valispace for a name.
    If found, returns the ID. If not, returns a list of dictionaries describing the valis


    Args:
        name (str): `name` of valispace .
        valispace (type): Description of parameter `valispace`.

    Returns:
        type: Description of returned object.

    Examples
        Examples should be written in doctest format, and
        should illustrate how to use the function/class.
        >>>

    """
    """

    """
    valis = valispace.get_vali_list()
    filtered_valis = [v for v in valis if v['name'] == name]
    if len(filtered_valis) == 0:
        raise RuntimeError("No valis of this name found!")
    elif len(filtered_valis) == 1:
        return filtered_valis[0]['id']
    else:
        return filtered_valis
