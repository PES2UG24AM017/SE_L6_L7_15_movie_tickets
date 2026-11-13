import pytest
from movie_tickets import ticket_price, group_discount, snack_combo

# Existing baseline tests
def test_regular_afternoon():
    assert ticket_price("regular", 25, 15, False) == 150

def test_small_group():
    assert group_discount(2, False) == 0

# Line & Branch coverage tests for ticket_price
def test_invalid_seat():
    with pytest.raises(ValueError, match="unknown seat"):
        ticket_price("vip", 25, 15, False)

def test_invalid_show_hour_branches():
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 25, -1, False)  # show_hour < 0 (True branch)
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 25, 24, False)  # show_hour > 23 (True branch)

def test_morning_weekend_child():
    assert ticket_price("premium", 10, 10, True) == 120

def test_evening_infant():
    assert ticket_price("recliner", 2, 19, False) == 0

def test_evening_senior_citizen():
    assert ticket_price("regular", 65, 20, False) == 90

# Line & Branch coverage tests for group_discount
def test_group_discount_branches():
    with pytest.raises(ValueError, match="no tickets"):
        group_discount(0, False)
    assert group_discount(10, True) == 20    
    assert group_discount(10, False) == 15   
    assert group_discount(5, False) == 10    
    assert group_discount(3, True) == 0      

def test_snack_combo_branches():
    assert snack_combo("small", True) == 70
    assert snack_combo("medium", False) == 180
    assert snack_combo("large", False) == 250
