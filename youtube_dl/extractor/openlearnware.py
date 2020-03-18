# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor


class OpenLearnWareIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?openlearnware\.de/resource/-(?P<id>[0-9]+)(\?start=)?'
    _TESTS_ = [
        {
            'url': 'https://yourextractor.com/watch/42',
            'md5': 'TODO: md5 sum of the first 10241 bytes of the video file (use --test)',
            'info_dict': {
                'id': '42',
                'ext': 'mp4',
                'title': 'Video title goes here',
                'thumbnail': r're:^https?://.*\.jpg$',
                # TODO more properties, either as:
                # * A value
                # * MD5 checksum; start the string with md5:
                # * A regular expression; start the string with re:
                # * Any Python type (for example int or float)
            }
        },
        {
            'ur': 'https://www.openlearnware.de/resource/t0142-51-if-boolesche-funktionen-symbole-3663',
            'only_matching': True
        },
        {
            'ur': 'https://www.openlearnware.de/resource/untervektorraume-1189?start=0',
            'only_matching': True
        }
    ]

    def _real_extract(self, url):
        video_id = self._match_id(url)

        video_details = self._download_json(
            'https://www.openlearnware.de/olw-rest-db/api/resource-detailview/index/',
            display_id)
        webpage = self._download_webpage(url, video_id)

        # TODO more code goes here, for example ...
        title = self._html_search_regex(r'<h1>(.+?)</h1>', webpage, 'title')

        return {
            'id': video_id,
            'title': title,
            'description': self._og_search_description(webpage),
            'uploader': self._search_regex(r'<div[^>]+id="uploader"[^>]*>([^<]+)<', webpage, 'uploader', fatal=False),
            # TODO more properties (see youtube_dl/extractor/common.py)
        }
