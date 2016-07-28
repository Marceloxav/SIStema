# -*- coding: utf-8 -*-

import djchoices
from django.db import models

import schools.models
import users.models


class Discount(models.Model):
    class Type(djchoices.DjangoChoices):
        SOCIAL = djchoices.ChoiceItem(1, 'Социальная скидка')
        PARTNER = djchoices.ChoiceItem(2, 'Скидка от партнёра')
        STATE = djchoices.ChoiceItem(3, 'Скидка от государства')
        OLYMPIADS = djchoices.ChoiceItem(4, 'Олимпиадная скидка')

    school = models.ForeignKey(schools.models.School, related_name='+')

    user = models.ForeignKey(users.models.User, related_name='discounts')

    type = models.PositiveIntegerField(choices=Type.choices, validators=[Type.validator])

    # If amount = 0, discount is considered now
    amount = models.PositiveIntegerField(
            help_text='Размер скидки. Выберите ноль, чтобы скидка считалась «рассматриваемой»')

    private_comment = models.TextField(blank=True, help_text='Не показывается школьнику')

    public_comment = models.TextField(blank=True, help_text='Показывается школьнику')

    @property
    def type_name(self):
        return self.Type.values[self.type]