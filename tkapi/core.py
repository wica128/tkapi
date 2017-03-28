import requests
from local_settings import USER, PASSWORD, API_ROOT_URL

import tkapi.util


class TKItem(object):
    def __init__(self, item_json):
        self.json = item_json

    @property
    def id(self):
        return self.get_property_or_empty_string('Id')

    def print_json(self):
        tkapi.util.print_pretty(self.json)

    def get_property_or_empty_string(self, property_key):
        if property_key in self.json and self.json[property_key]:
            return str(self.json[property_key])
        return ''

    def get_date_or_none(self, property_key):
        if property_key in self.json and self.json[property_key]:
            return tkapi.util.odatedatetime_to_datetime(self.json[property_key]).date()
        return None

    def get_datetime_or_none(self, property_key):
        if property_key in self.json and self.json[property_key]:
            return tkapi.util.odatedatetime_to_datetime(self.json[property_key])
        return None


def get_all_items(page, max_items=None):
    items = []
    for item in page['value']:
        items.append(item)
    while 'odata.nextLink' in page:
        page = request_json(page['odata.nextLink'])
        for item in page['value']:
            items.append(item)
        if max_items and len(items) >= max_items:
            break
    return items


def request_json(url, params=None, verbose=False):
    if not params:
        params = {}
    params['$format'] = 'json',
    r = requests.get(API_ROOT_URL + url, params=params, auth=(USER, PASSWORD))
    if verbose:
        print('url: ' + str(r.url))
    if r.status_code != 200:
        print(r.text)
    assert r.status_code == 200
    return r.json()