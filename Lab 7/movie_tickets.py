def parse_seat(seat):
    if not isinstance(seat, str):
        return None
    seat = seat.strip()
    if len(seat) < 2 or not seat[0].isalpha() or not seat[1:].isdigit():
        return None
    seat_num = int(seat[1:])
    if seat_num <= 0:
        return None
    return seat[0].upper(), seat_num


def total_price(prices_csv):
    if not isinstance(prices_csv, str) or not prices_csv.strip():
        return 0.0
    prices = []
    for item in prices_csv.split(','):
        item = item.strip()
        if not item:
            continue
        try:
            val = int(item)
            if val < 0:
                return 0.0
            prices.append(val)
        except ValueError:
            return 0.0
    if not prices:
        return 0.0
    return round(sum(prices) * 1.18, 2)


def average_rating(ratings):
    if not isinstance(ratings, str) or not ratings.strip():
        return 0.0
    values = []
    for item in ratings.split():
        try:
            val = int(item)
            if val < 0:
                return 0.0
            values.append(val)
        except ValueError:
            return 0.0
    if not values:
        return 0.0
    return round(sum(values) / len(values), 1)


def main():
    print("==== Running parse_seat ====")
    user_input = input("Enter a seat number (e.g. H12): ")
    result = parse_seat(user_input)
    print("Row and Seat:", result)

    print("\n==== Running total_price ====")
    user_input = input("Enter ticket prices as CSV (e.g. 150,250,400): ")
    result = total_price(user_input)
    print("Total with GST:", result)

    print("\n==== Running average_rating ====")
    user_input = input("Enter ratings separated by spaces (e.g. 4 5 3): ")
    result = average_rating(user_input)
    print("Average Rating:", result)


if __name__ == "__main__":
    main()
