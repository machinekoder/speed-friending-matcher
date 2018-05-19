#!/usr/bin/env python
import argparse
import sys
from application import Application


def main():
    parser = argparse.ArgumentParser(description="""
    Matchmaking application for speed friending events
    """)
    parser.add_argument('-i', '--input', help='Input plugin and parameters e.g. csv:somefile.csv', required=True)
    parser.add_argument('-o', '--output', help='Output plugins and parameters e.g. todo:mytodo.txt', required=True)
    parser.add_argument('-m', '--matchmaker', help='Matchmaker, simple or clique', default='simple')
    args = parser.parse_args()

    app = Application(
        input_plugin=args.input,
        output_plugin=args.output,
        matchmaker=args.matchmaker,
    )
    app.process()

    sys.exit(0)


if __name__ == '__main__':
    main()
