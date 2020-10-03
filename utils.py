import dateparser
import datetime
import logging
import string

_logger = logging.getLogger(__name__)


def parse_and_format_date(datestr, **kwargs):
    try:
        dt = dateparser.parse(datestr, **kwargs)
        fmtdate = dt.strftime("%Y-%m-%d")
        _logger.info("Parsing %s result %s", datestr, fmtdate)
        return fmtdate
    except:
        _logger.exception("Could not parse %s as date", datestr)
        return ""


def parse_and_format_month_year(datestr, **kwargs):
    try:
        dt = dateparser.parse(datestr, **kwargs)
        fmtdate = dt.strftime("%Y-%m")
        _logger.info("Parsing %s result %s", datestr, fmtdate)
        return fmtdate
    except:
        _logger.exception("Could not parse %s as date", datestr)
        return ""


def select_highest_amount(matches):
    maxval = 0.00
    for m in matches:
        val = float(m.replace(",", "."))
        if val > maxval:
            maxval = val
    _logger.info("selected %s out of %s", maxval, len(matches))
    return str(maxval)


def strip_spaces(matches):
    return matches.replace(" ", "")


def strip_empty_matches(matches):
    return filter(None, matches)


def format_property_address(matches):
    return string.capwords(list(strip_empty_matches(matches))[0]);


def info_dump(matches):
    _logger.error(":::: In Info Dump ::::")
    _logger.error("Processing matches which is of type %s", type(matches))
    _logger.error("Content of matches is %s", matches)
    for match in matches:
        _logger.error("match type: %s -> match value: %s", type(match), match)
    _logger.error(":::: Leaving Info Dump ::::")
    return matches

def selector_dump(matches):
    _logger.error(":::: In Selector Dump ::::")
    _logger.error("Processing matches which is of type %s", type(matches))
    _logger.error("Content of matches is %s", matches)
    for match in matches:
        _logger.error("match type: %s -> match value: %s", type(match), match)
    _logger.error(":::: Leaving Selector Dump ::::")
    return matches
