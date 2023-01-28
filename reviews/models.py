from django.db import models
from accounts import models as user_models
from reviews import constants as review_constants


class Review(models.Model):
    """
    Model to store reviews details.
    """
    person = models.ForeignKey(
        user_models.Employee, default=None, null=True, blank=True,
        on_delete=models.CASCADE, related_name='reviewed_persons')
    reviewer = models.ForeignKey(
        user_models.Employee, default=None, null=True, blank=True,
        on_delete=models.CASCADE, related_name='reviewers')
    description = models.CharField(
        default='', max_length=2000, null=True, blank=True)
    rate = models.IntegerField(
        default=None, choices=review_constants.RateChoice.choice(),
        null=True, blank=True)
    feedback = models.CharField(
        default='', max_length=2000, null=True, blank=True)

    def __str__(self):
        """
        Object name in Django admin.
        """
        return f'{self.id} {self.description}'



