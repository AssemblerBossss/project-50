#!/usr/bin/env python3
from gendiff import generate_diff
from gendiff.cli import parse_arguments


def main():
    args = parse_arguments()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)
    print(generate_diff())


if __name__ == '__main__':
    main()
