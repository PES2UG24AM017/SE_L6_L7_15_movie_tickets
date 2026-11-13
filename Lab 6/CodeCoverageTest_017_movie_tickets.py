import pytest
from movie_tickets import ticket_price, group_discount, snack_combo

#Example test cases:
def test_regular_afternoon():
    assert ticket_price("regular", 25, 15, False) == 150

def test_small_group():
    assert group_discount(2, False) == 0

#Write the rest of the test cases so that the code is 90- 100% covered.
def test_invalid_seat():
    with pytest.raises(ValueError, match="unknown seat"):
        ticket_price("vip", 25, 15, False)

def test_invalid_show_hour():
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 25, 25, False)

def test_morning_weekend_child():
    # Base 250 - 50 (morning) + 40 (weekend) = 240; child (<=12) -> 240 // 2 = 120
    assert ticket_price("premium", 10, 10, True) == 120

def test_evening_infant():
    # Age < 3 returns 0
    assert ticket_price("recliner", 2, 19, False) == 0

def test_group_discount_lines():
    with pytest.raises(ValueError, match="no tickets"):
        group_discount(0, False)
    # Covers tickets >= 10 and student group bonus
    assert group_discount(10, True) == 20
    # Covers elif tickets >= 5
    assert group_discount(5, False) == 10

def test_snack_combo_lines():
    assert snack_combo("small", True) == 70
    assert snack_combo("medium", False) == 180
    assert snack_combo("large", False) == 250