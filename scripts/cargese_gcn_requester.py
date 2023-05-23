"""
App to request gcn
"""
import sys
import argparse
import logging

from cargese.gcn_requester import get_circular_json
from cargese.tools import timestamp_to_datetime

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - [%(name)s] - %(message)s",
)


def get_parser():
    """Method to generate command parser"""
    parser = argparse.ArgumentParser()
    parser.add_argument("circularId", type=str, help="ID of the GCN circular")
    return parser


def main():
    """Main method"""
    parser = get_parser()
    args = parser.parse_args(sys.argv[1:])
    circ = get_circular_json(args.circularId)
    if circ != {}:
        print(circ["subject"])
        print(circ["submitter"])
        print(timestamp_to_datetime(circ["createdOn"] / 1000))
        print(circ["body"])
