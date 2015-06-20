from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope import schema
from zope.interface import alsoProvides


class IDoStuff(model.Schema):
    """
    """
    stuff = schema.TextLine(title=u"Do Stuff")


alsoProvides(IDoStuff, IFormFieldProvider)


