
def tax_calculator(subtotal,tax_rate):
    """Takes a subtotal and a tax rate and returns the total invoice amount

    Args:
        subtotal (int): total amount pruchased - applicatable tax rate
        tax_rate (int): taxrate for location

    Returns:
        int : Total of tax and subtotal
    """
    tax = subtotal * tax_rate
    total = subtotal * + tax
    return total
