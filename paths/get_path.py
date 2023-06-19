from os.path import abspath

def get_full_path(path):
    full_path = abspath(__file__ + '/../..') + f"/{path}"
    # full_path = os.path.join(os.path.abspath(__file__ + '/../..'), path)
    return full_path

