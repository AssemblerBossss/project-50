from gendiff.cli import parse_arguments
from gendiff.parser import parse_data, open_file


def main():
    arguments = parse_arguments()
    print(parse_data(*open_file(arguments.first_file)))
    # print(arguments)


if __name__ == '__main__':
    main()
