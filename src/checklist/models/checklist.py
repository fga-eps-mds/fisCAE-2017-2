from django.db import models
from django.utils import timezone

from .school import School


class Checklist(models.Model):
    school = models.ForeignKey(
        School,
        related_name="checklists",
        on_delete=models.CASCADE
    )

    user = models.ForeignKey('auth.User')

    CHECKLIST_TYPE = (
        ('TA', 'Questões técnicas e administrativas'),
        ('HS', 'Questões Higiênico Sanitárias'),
        ('AL', 'Questões Alimentares'),
        ('D', 'Sobre a documentação'),
    )
    checklist_type = models.CharField(
        max_length=2,
        choices=CHECKLIST_TYPE,
        default=None,
    )

    created_date = models.DateTimeField(
            default=timezone.now)
