"""
test_gcn_requester.py
"""
from src.cargese.gcn_requester import get_circular_json, GcnRequester


def test_get_circular_json():
    data_json = get_circular_json(33764)
    assert data_json["createdOn"] == 1683789447191

    data_json = get_circular_json(10000000)
    assert data_json == {}


def test_gcn_requester():
    gcn_req = GcnRequester()
    gcn_req.fill_archive(31)
    gcn_req.format_time()
    assert len(gcn_req.archive) == 1
    assert "body" not in gcn_req.archive

    gcn_req.fill_archive(31, body=True)
    assert len(gcn_req.archive) == 1
    assert "body" in gcn_req.archive

    bad_id = 10000000
    gcn_req.fill_archive(bad_id, bad_id)
    assert len(gcn_req.archive) == 0
