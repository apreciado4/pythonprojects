import concurrent.futures
import sys
import codecs


def check_utf(path):
    """
    Tests provided file to check if it is utf-8 encoded
    """
    try:
        test = codecs.open(path, encoding='utf-8', errors='strict')
        test.readline()
        print(f'{path} is utf-8 encoded')
        pass
    except UnicodeDecodeError:
        print(f'SORRY {path} is NOT utf-8 encoded')


def threads(inputs):
    """
    Creates multiple threads based off of provided iterable to check_utf function
    """
    with concurrent.futures.ThreadPoolExecutor() as pool:
        pool.map(check_utf, inputs)


if __name__ == "__main__":
    # Create a list of filepaths from arguments
    args = []
    for i in range(len(sys.argv)):
        if i != 0:
            args.append(sys.argv[i])
    # Calls threads() with list of filepaths from arguments
    threads(args)
