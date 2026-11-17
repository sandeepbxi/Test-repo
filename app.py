def calculate_total(price, quantity):
    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity must be non-negative")
    return price * quantity

def is_palindrome(s):
    cleaned = "".join(ch.lower() for ch in str(s) if ch.isalnum())
    return cleaned == cleaned[::-1]

def get_delivery_status(days):
    if days < 0:
        raise ValueError("Days cannot be negative")
    if days <= 2:
        return "On Time"
    elif days <= 5:
        return "At Risk"
    else:
        return "Delayed"

if __name__ == "__main__":
    print("Calculate Total (10, 5):", calculate_total(10, 5))
    print("Is 'racecar' palindrome?:", is_palindrome("racecar"))
    print("Delivery status (1 day):", get_delivery_status(1))
