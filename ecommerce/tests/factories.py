import factory
import pytest
from faker import Faker
from pytest_factoryboy import register

fake = Faker()

from ecommerce.inventory import models
class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    name = factory.Sequence(lambda n: "Simba's_database_%d" % n)
    slug = fake.lexify(text = "Simba's_database_??????")

register(CategoryFactory)