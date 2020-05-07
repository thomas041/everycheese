import pytest

from ..models import Cheese

# Connects out tests with our Database
pytestmark = pytest.mark.django.db


def test__str__():
    cheese = Cheese.objects.create(
        name="Stracchino",
        description="Semi-Sweet cheese that goes well with Starches",
        firmness=Cheese.Firmness.SOFT,
    )
    assert cheese.__Str__() == "Stracchino"
    assert str(cheese) == "Stracchino"
