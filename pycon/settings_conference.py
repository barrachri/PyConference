"""
Settings for the Conference.

"""

from datetime import timedelta

'''
This application can be MULTI CONFERENCE, you can run multiply istance
of this application with a shared database.

'''
CONFERENCE_CODE = False;


#######################
## PROPOSAL SETTINGS ##
#######################

#-------------------------------------------------------------------------------
# Proposal languages
#-------------------------------------------------------------------------------
PROPOSAL_LANGUAGES = (
    ('it', ('Italian')),
    ('en', ('English')),
)

#-------------------------------------------------------------------------------
# Proposal levels
#-------------------------------------------------------------------------------
PROPOSAL_LEVEL = (
    ('beginner',     ('Beginner')),
    ('intermediate', ('Intermediate')),
    ('advanced',     ('Advanced')),
)

#-------------------------------------------------------------------------------
# Proposal type
#-------------------------------------------------------------------------------
PROPOSAL_TYPE = (
    ('s', 'Talk'),
    ('i', 'Interactive'),
    ('t', 'Training'),
    ('p', 'Poster session'),
    ('h', 'Help desk'),
)

#-------------------------------------------------------------------------------
# Proposal status
#-------------------------------------------------------------------------------
PROPOSAL_STATUS = (
    ('proposed', ('Proposed')),
    ('accepted', ('Accepted')),
)
#-------------------------------------------------------------------------------
# Proposal duration
#-------------------------------------------------------------------------------
PROPOSAL_DURATION = (
    (timedelta(minutes=5),   ('5 minutes')),
    (timedelta(minutes=10),  ('10 minutes')),
    (timedelta(minutes=15),  ('15 minutes')),
    (timedelta(minutes=30),  ('30 minutes')),
    (timedelta(minutes=45),  ('45 minutes')),
    (timedelta(minutes=60),  ('1 hour')),
    (timedelta(minutes=90),  ('90 minutes')),
    (timedelta(minutes=120), ('2 hours')),
    (timedelta(minutes=180), ('3 hours')),
)

#######################
## TICKET SETTINGS ##
#######################

TICKET_CONFERENCE_SHIRT_SIZES = (
    ('fs', 'S (female)'),
    ('fm', 'M (female)'),
    ('fl', 'L (female)'),
    ('fxl', 'XL (female)'),
    ('fxxl', 'XXL (female)'),
    ('s', 'S (male)'),
    ('m', 'M (male)'),
    ('l', 'L (male)'),
    ('xl', 'XL (male)'),
    ('xxl', 'XXL (male)'),
)
TICKET_CONFERENCE_DIETS = (
    ('omnivorous', ('Omnivorous')),
    ('vegetarian', ('Vegetarian')),
    #('vegan', _('Vegan')),
    #('kosher', _('Kosher')),
)


VIDEO_TYPE = (
    ('viddler_oembed', 'oEmbed (Youtube, Vimeo, ...)'),
    ('download', 'Download'),
)
