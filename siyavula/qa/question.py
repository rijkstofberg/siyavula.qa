from five import grok
from plone.directives import dexterity, form

from zope import schema
from plone.app.textfield import RichText

from siyavula.qa import MessageFactory as _


class IQuestion(form.Schema, IImageScaleTraversable):
    """
    A question for an expert
    """
    question = RichText(
        title = _(u'Question'),
        required = True,
        )

    answer = RichText(
        title = _(u'Answer'),
        required = True,
        )

# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class Question(dexterity.Item):
    grok.implements(IQuestion)
    # Add your class methods and properties here

