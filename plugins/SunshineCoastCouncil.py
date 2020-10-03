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
# - selector: name of a method called to narrow down when more than one match returned
# - post: the name of a method called to post-process the content selected by the regex
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

class SunshineCoastCouncil(mambase.RegexMetaDataCheck):
    __documentclass__ = "Invoice"
    __tags__ = ["SunshineCoastCouncil", "MAM", "Tax"]
    __filter__ = lambda s, x: ("sunshinecoast.qld.gov.au" in x)
    __meta__ = [
        {"metadata": "issuer", "value": "Sunshine Coast Council"},
        {
            "metadata": "subject",
            "regex": PatternConstants.SUBJECT_PROPERTY_ADDRESS_REGEX,
            "post": utils.format_property_address,
        },
        {
            "metadata": "due_date",
            "regex": "Ref[\w\s\:]*Due date\s*(.*)\n",
            "post": parse_and_format_date_en_AU,
        },
        {
            "metadata": "issue_date",
            "regex": "Issue date[ ]*([\d\w ]+)",
            "post": parse_and_format_date_en_AU,
        },
        {
            "metadata": "account_identifier",
            "regex": "PROPERTY NO\.\s*((?: *\d){6})",
        },
        {
            "metadata": "invoice_identifier",
            "regex": "PAYMENT REFERENCE NO\.\s*((?: *\d){9})",
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

__plugin__ = [SunshineCoastCouncil]
