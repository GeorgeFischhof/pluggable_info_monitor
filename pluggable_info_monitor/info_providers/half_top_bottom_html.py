
import datetime

from PIM_constants import DisplayParts, InfoSeverity


def get_info() -> list:
    citation = {
        'display_part': DisplayParts.HALF_TOP,
        'info_severity': InfoSeverity.INFO,
        'info': '<H1>Citation for today</H1>'
                'Lorem ipsum dolor sit amet, consectetur '
                'adipiscing elit, sed do eiusmod tempor '
                'occaecat cupidatat non proident, sunt in culpa '
                'qui officia deserunt mollit anim id est laborum.'
    }

    nameday = {
        'display_part': DisplayParts.HALF_BOTTOM,
        'info_severity': InfoSeverity.INFO,
        'info': '<H1>Nameday for today is John</H1>'
                'Lorem ipsum dolor sit amet, consectetur '
                'adipiscing elit, sed do eiusmod tempor '
                'occaecat cupidatat non proident, sunt in culpa '
                'qui officia deserunt mollit anim id est laborum.'
    }

    info = [citation, nameday,]
    return info
