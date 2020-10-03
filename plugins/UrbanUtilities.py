import mambase
import utils
import PatternConstants
# import fiscalyear

#
# Generally, the set of attributes below are the ones I capture for each
# finance related document.
#
# Each Metadata item can contain the following:
# - value: a literal value to use
# - regex: the regular expression to use to pull content out of the document
# - selector: name of a method called to narrow down the result??? not sure how differs from post
# - post: the name of a method called to post-process the content selected by the regex
#
#
#
#
# - [ ] issue date 
# - [ ] due date
# - [ ] subject
# - [ ] issuer
# - [ ] account_identifier      - usually an account number
# - [ ] invoice_identifier      - usually an invoice or bill number
# - [ ] reference_identifier    - usually a payment reference, or receipt id
# - [ ] amount
# - [ ] Financial Year - possibly will not store, instead generate dynamically 
#                           in Mayan Index

def parse_and_format_date_en_AU(datestr):
    return utils.parse_and_format_date(datestr, settings={'DATE_ORDER': 'DMY'})

class UrbanUtilities(mambase.RegexMetaDataCheck):
    __documentclass__ = "Invoice"
    __tags__ = ["UrbanUtilities", "MAM", "Tax"]
    __filter__ = lambda s, x: ("urbanutilities.com.au" in x)
    __meta__ = [
        # Issuer, and Subject are both metadata items that I use for 
        # grouping items (categorisation) - related too, but not necessarily
        # taken from the content of the document.
        {"metadata": "issuer", "value": "Urban Utilities"},
        {
            "metadata": "subject",
            "regex": PatternConstants.SUBJECT_PROPERTY_ADDRESS_REGEX,
            # "selector": utils.selector_dump,
            "post": utils.format_property_address,
        },
        {
            "metadata": "due_date",
            "regex": "Current\s*charges\s*due\s*date\s*([\d\/]+)",
            # "post": parse_and_format_date_en_AU,
            "post": parse_and_format_date_en_AU,
        },
        {
            "metadata": "issue_date",
            "regex": "Date issued\s*([\d\/]+)",
            "post": parse_and_format_date_en_AU,
        },
        {
            "metadata": "account_identifier",
            # Depending on OCR/Document parsing, there might be spaces between
            #  the numbers CRN should be 15 digits so look for 15 digits, 
            # that might have one or more spaces between them
            "regex": "Customer\s*[R|r]eference\s*[N|n]\w*\.*\s*((?: *\d){15})",
            "post": utils.strip_spaces,
        },
        {
            "metadata": "invoice_identifier",
            # Depending on OCR/Document parsing, there might be spaces between
            # the numbers bull number should be 10 digits so look for 10 
            # digits, that might have one or more spaces between them
            "regex": "Bill number((?: *\d){10})",
            "post": utils.strip_spaces,
        },        
        # {
        #     "metadata": "reference_identifier",
        #     "regex": "Payment reference[ ]*(\d+[ \d]*)",
        #     "post": utils.strip_spaces,
        # },
        # {
        #     # store the amount the item was for - if useful down the track
        #     "metadata": "amount",
        #     "regex": "Total due[ ]*\$(\d+\.\d{2})",
        # },
    ]

__plugin__ = [UrbanUtilities]
