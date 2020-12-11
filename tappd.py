import requests
import os
from elasticsearch import Elasticsearch

token = os.environ["UNTAPPD_TOKEN"]
username = os.environ["UNTAPPD_USERNAME"]
es_host = os.environ["ES_HOST"]
es_port = os.environ["ES_PORT"]
index = os.getenv("ES_INDEX") or "untappd_checkins"


def get_checkins(username, token):
    results = []
    n_requests = 0
    r_untappd = requests.get(
        f'https://api.untappd.com/v4/user/checkins/{username}?access_token={token}').json()
    checkins = r_untappd["response"]["checkins"]["items"]

    n_requests += 1
    if not checkins:
        print(f"No checkins found for user: {username}")
        return

    results = results + checkins
    last_id = get_last_id(checkins)

    while last_id is not None:
        r_untappd = requests.get(
            f'https://api.untappd.com/v4/user/checkins/{username}?access_token={token}&max_id={last_id}').json()
        n_requests += 1
        checkins = r_untappd["response"]["checkins"]["items"]

        if checkins:
            results = results + checkins

        last_id = get_last_id(checkins)

    print(
        f"Retrieved {len(results)} checkins from Untappd API, {n_requests} requests made.")
    return results


def get_last_id(checkins):
    if not checkins:
        return None

    last_checkin = checkins[len(checkins) - 1]
    return last_checkin.get("checkin_id", None)


def setup_elastic():
    es = Elasticsearch([{'host': es_host, 'port': es_port}])

    if not es.indices.exists(index=index):
        es.indices.create(index=index)

    return es


es = setup_elastic()
checkins = get_checkins(username, token)
inserted = 0
for checkin in checkins:
    es.index(index=index, body=checkin, id=checkin['checkin_id'])
    inserted += 1

print(f"Inserted {len(checkins)} documents into index: {index}")
