import requests
import os

token = os.environ["UNTAPPD_TOKEN"]
username = os.environ["UNTAPPD_USERNAME"]


def get_checkins(username, token):
    results = []
    r_untappd = requests.get(
        f'https://api.untappd.com/v4/user/checkins/{username}?access_token={token}').json()
    checkins = r_untappd["response"]["checkins"]["items"]

    if not checkins:
        print(f"No checkins found for user: {username}")
        return

    results = results + checkins
    last_id = get_last_id(checkins)

    while last_id is not None:
        print(last_id)
        r_untappd = requests.get(
            f'https://api.untappd.com/v4/user/checkins/{username}?access_token={token}&max_id={last_id}').json()
        checkins = r_untappd["response"]["checkins"]["items"]

        if checkins:
            results = results + checkins

        last_id = get_last_id(checkins)

    return results


def get_last_id(checkins):
    if not checkins:
        return None

    last_checkin = checkins[len(checkins) - 1]
    return last_checkin.get("checkin_id", None)


checkins = get_checkins(username, token)
print(f"Retrieved {len(checkins)} checkins")
