"""
Database models for blogging_for_humans.
"""
from django.db import models
from model_utils.models import TimeStampedModel


# class Model01(TimeStampedModel):
class Model01(models.Model):
    model01_id = models.CharField(max_length=250, null=False, blank=False)
    field_01 = models.CharField(max_length=255)
    """
    TODO: replace with a brief description of the model.

    TODO: Add either a negative or a positive PII annotation to the end of this docstring.  For more
    information, see OEP-30:
    https://open-edx-proposals.readthedocs.io/en/latest/oep-0030-arch-pii-markup-and-auditing.html
    """

    # TODO: add field definitions

    def __str__(self):
        """
        Get a string representation of this model instance.
        """
        # TODO: return a string appropriate for the data fields
        # return '<Model_01, ID: {}>'.format(self.field_01)
        return 'juhuuu'
