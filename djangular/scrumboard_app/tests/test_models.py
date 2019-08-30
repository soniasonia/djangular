from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from scrumboard_app.models import Card, List
from unittest import skip


class CardModelTest(TestCase):

    def test_card_is_related_to_list(self):
        list_ = List.objects.create(name="Pierwsza lista")
        card = Card.objects.create(title="Pierwsza karta", list=list_)
        self.assertIn(card, list_.cards.all())

    def test_cannot_save_card_without_list(self):
        with self.assertRaises(IntegrityError):
            Card.objects.create(title="Pierwsza karta")

    def test_duplicate_card_is_invalid(self):
        list_ = List.objects.create(name="Pierwsza lista")
        Card.objects.create(title="Pierwsza karta", list=list_)
        with self.assertRaises(ValidationError):
            card = Card(title="Pierwsza karta", list=list_)
            card.full_clean()

    def test_can_save_card_to_different_list(self):
        list1 = List.objects.create(name="Pierwsza lista")
        list2 = List.objects.create(name="Druga lista")
        Card.objects.create(title="Pierwsza karta", list=list1)
        card = Card(title="Pierwsza karta", list=list2)
        card.full_clean()