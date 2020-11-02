import os
import sys



def get_first_exist_on_path(names, default):
    """
    Searches all files on sys.path for matches against names. If a matching file is not found,
    it returns the default value.
    """
    for p in sys.path:
        try:
            (_, _, filenames) = next(os.walk(p))
        except StopIteration as e:
            # StopIteration will be raised if the given directory is empty or does not exist
            break

        # Search for any of the given names on the path, returning the first one
        # that is found.
        for name in names:
            if name in filenames:
                return name
    return default




if __name__ == "__main__":
    print(f"System path: {sys.path}")

    # Tests are tuples of search items, and then the default
    tests = [
        (["com.example.my.jar", "do-not-exist.txt"], None),
        (["do-not-exist.txt", "com.example.my.jar"], None),
        (["test.txt"], None),
        ([], "default.txt"),
    ]

    for test in tests:
        first = get_first_exist_on_path(test[0], test[1])
        print("--------------------------------------------------")
        print(f"Searching for {test[0]} with default of {test[1]}")
        print(f"Return Value {first}")
