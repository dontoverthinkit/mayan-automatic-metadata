import mambase
import utils
import PatternConstants
# import fiscalyear

#
# Generally, the set of attributes below are the ones I capture for each
# finance related document.
#
# - [X] issue date 
# - [X] due date
# - [X] subject
# - [X] issuer
# - [X] account_identifier      - usually an account number
# - [X] invoice_identifier      - usually an invoice or bill number
# - [X] reference_identifier    - usually a payment reference, or receipt id
# - [X] amount
# - [ ] Financial Year - possibly will not store, instead generate dynamically 
#                           in Mayan Index

def parse_and_format_date_en_AU(datestr):
    return utils.parse_and_format_date(datestr, settings={'DATE_ORDER': 'DMY'})

class UnityWater(mambase.RegexMetaDataCheck):
    __documentclass__ = "Invoice"
    __tags__ = ["UnityWater", "MAM", "Tolkien", "Tax"]
    __filter__ = lambda s, x: ("unitywater.com" in x)
    __meta__ = [
        # Issuer, and Subject are both metadata items that I use for 
        # grouping items (categorisation) - related too, but not necessarily
        # taken from the content of the document.
        {"metadata": "issuer", "value": "Unity Water"},
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
            "regex": "Account number[ ]*(\d+)",
        },
        {
            "metadata": "invoice_identifier",
            "regex": "Bill number\s*(\d+)",
        },        
        {
            "metadata": "reference_identifier",
            "regex": "Payment reference[ ]*(\d+[ \d]*)",
            "post": utils.strip_spaces,
        },
        # {
        #     # store the amount the item was for - if useful down the track
        #     "metadata": "amount",
        #     "regex": "Total due[ ]*\$(\d+\.\d{2})",
        # },
    ]

__plugin__ = [UnityWater]
