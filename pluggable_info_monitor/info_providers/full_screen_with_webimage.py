
import base64
import datetime

import requests

from PIM_constants import DisplayParts, InfoSeverity


def get_info() -> list:
    image_url = 'https://www.python.org/static/community_logos/python-logo.png'
    image = requests.get(image_url).content
    image_base64 = (base64.b64encode(image)).decode('ascii')

    python = {
        'display_part': DisplayParts.FULL_SCREEN,
        'info_severity': InfoSeverity.INFO,
        'info': {
            'Language name': 'Python',
            'first released': 1991,
            'language type': 'scripting language',
            'current time': datetime.datetime.now().isoformat(),
            'icon': f'<img src="data:image/png;base64,{image_base64}" align="middle">'
        },
    }
    info = [python,]
    return info


# list of MIME types for images:
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Complete_list_of_MIME_types

# requests is a http library
# https://pypi.python.org/pypi/requests/
