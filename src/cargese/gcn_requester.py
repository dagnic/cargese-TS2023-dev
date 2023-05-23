"""
gcn_requester.py
"""
from urllib.request import urlopen
from urllib.error import HTTPError

import json
import logging
import pandas as pd

from cargese import tools

GCN_URL = "https://gcn.nasa.gov/circulars"

logger = logging.getLogger(__name__)


def get_circular_json(circ_id):
    """
    Get the circular in json for a given circular id
    :param circ_id: circular id
    """
    url = f"{GCN_URL}/{circ_id}/json"
    try:
        with urlopen(url) as response:
            data_json = json.loads(response.read())
            return data_json
    except HTTPError as err:
        if err.code == 404:
            logger.error("Circular not found")
            return {}
        raise


class GcnRequester:
    """
    Class to retrieve GCN info from https://gcn.nasa.gov/circulars
    """

    def __init__(self):
        self.archive = None

    def fill_archive(self, stop_id, start_id=31, body=False):
        """
        Fill an archive with all circular found in id range

        :param stop_id: Maximum id
        :param start_id: Minimum id
        :param body: If True, include circular body in archive
        """
        circulars = []
        for cir_id in range(start_id, stop_id + 1):
            circ_json = get_circular_json(cir_id)
            if circ_json != {}:
                logger.info("Found %s: %s", cir_id, circ_json["subject"])
            else:
                continue
            if not body:
                circ_json.pop("body")
            circulars.append(circ_json)
        self.archive = pd.DataFrame.from_records(circulars)

    def format_time(self):
        """
        Format the time info from circular `createdOn` field to regularr UTC date
        """
        time = [
            tools.timestamp_to_datetime(ts / 1000) for ts in self.archive["createdOn"]
        ]
        self.archive["createdOn"] = time
