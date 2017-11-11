
import datetime

from PIM_constants import DisplayParts, InfoSeverity


def get_info():
    build_1 = {
        'display_part': DisplayParts.QUARTER_TOP_LEFT,
        'info_severity': InfoSeverity.ERROR,
        'info': {
            'platform': 'mac',
            'build': 'Failed',
            'test': 'Error',
            'Summarize': 'Something went wrong :-(',
            'Report creation time': datetime.datetime.now().isoformat(),
        },
    }

    build_2 = {
        'display_part': DisplayParts.QUARTER_TOP_RIGHT,
        'info_severity': InfoSeverity.WARNING,
        'info': {
            'platform': 'linux',
            'build': 'OK',
            'test': 'Failed',
            'Summarize': 'We can do it better ;-)',
            'Report creation time': datetime.datetime.now().isoformat(),
        },
    }

    build_3 = {
        'display_part': DisplayParts.QUARTER_BOTTOM_LEFT,
        'info_severity': InfoSeverity.OK,
        'info': {
            'platform': 'windows',
            'build': 'OK',
            'test': 'Passed',
            'Summarize': 'Hurray good build',
            'Report creation time': datetime.datetime.now().isoformat(),
        },
    }

    build_4 = {
        'display_part': DisplayParts.QUARTER_BOTTOM_RIGHT,
        'info_severity': InfoSeverity.INFO,
        'info': {
            'number of bugs': 24,
            '<font color="red">critical</font>': '<font color="red">4</font>',
            '<font color="yellow">normal</font>': '<font color="yellow">15</font>',
            'low': '5',
            'current number of tasks to do in this sprint': 25,
            'Report creation time': datetime.datetime.now().isoformat(),
        },
    }

    info = [build_1, build_2, build_3, build_4, ]
    return info
