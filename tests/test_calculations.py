
from decimal import Decimal
import pytest
from calculator.calc import Calcs2
from calculator.calculations import Calcs
from calculator.ops import add, subtract

@pytest.fixture
def setup_calculations():
    """Clear history and add sample calculations for tests."""
    Calcs.clear_history()
    Calcs.add_calculation(Calcs2(Decimal('10'), Decimal('5'), add))
    Calcs.add_calculation(Calcs2(Decimal('20'), Decimal('3'), subtract))

def test_add_calculation(setup_calculations):
    """Test adding a calculation to the history."""
    calc = Calcs2(Decimal('2'), Decimal('2'), add)
    Calcs.add_calculation(calc)
    assert Calcs.get_latest() == calc, "Failed to add the calculation to the history"

def test_get_history(setup_calculations):
    """Test retrieving the entire calculation history."""
    history = Calcs.get_history()
    assert len(history) == 2, "History does not contain the expected number of calculations"

def test_clear_history(setup_calculations):
    """Test clearing the entire calculation history."""
    Calcs.clear_history()
    assert len(Calcs.get_history()) == 0, "History was not cleared"

def test_get_latest(setup_calculations):
    """Test getting the latest calculation from the history."""
    latest = Calcs.get_latest()
    assert latest.a == Decimal('20') and latest.b == Decimal('3'), "Did not get the correct latest calculation"

def test_find_by_operation(setup_calculations):
    """Test finding calculations in the history by operation type."""
    add_operations = Calcs.find_by_operation("add")
    assert len(add_operations) == 1, "Did not find the correct number of calculations with add operation"
    subtract_operations = Calcs.find_by_operation("subtract")
    assert len(subtract_operations) == 1, "Did not find the correct number of calculations with subtract operation"

def test_get_latest_with_empty_history():
    """Test getting the latest calculation when the history is empty."""
    Calcs.clear_history()
    assert Calcs.get_latest() is None, "Expected None for latest calculation with empty history"