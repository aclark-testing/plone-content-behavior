from plone.supermodel import model
from zope import schema


class IDoStuff(model.Schema):
    """
    """
    stuff = schema.TextLine(title=u"Do Stuff")
