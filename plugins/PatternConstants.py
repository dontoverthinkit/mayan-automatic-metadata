#
# Certain patterns will be used across multiple plugins.
#
# e.g. The subject of a document (for me at least) re-occurs across
# multiple utility bills - phone, water, electricity etc.
#
# Store these centrally for re-use.
#
# This of course assumes that the multiple documents represent the information
# being matched in in the same way across the documents.
#
SUBJECT_PROPERTY_ADDRESS_REGEX="(DARNUM\s*COURT) CORNUBIA|(JESSON) STREET ZILLLMERE|(?:28\s*(BRADLEY\s*AVENUE)\s*KEDRON)|(?:13\s*(Tolkien\s*Pl),\s*COOLUM)"