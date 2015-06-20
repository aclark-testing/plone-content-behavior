from plone.supermodel import model
from zope import schema


class Thing(model.Schema):
    """A Thing"""


    title = schema.TextLine(title=u"Name of Thing")
