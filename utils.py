# utils.py

def get_percentage_increment(base: float, percent: float) -> float:
    """
    Adds a percentage to a given number and returns both the new total and the percentage value.

    :param base: The base number.
    :param percent: The percentage to add.
    :return: A tuple containing the new number with the percentage added and the percentage value.
    """
    total = base * (1 + percent / 100)
    increment = total - base
    return total, increment


def format_number(number: float) -> str:
    """
    Formats a given float number with thousand separators according to the French locale.
    It also ensures that the number is formatted with a specific number of decimal places.

    This function formats a float number by inserting thousand separators (using a space as a separator
    for the French locale), and ensures that a specified number of decimals is kept (default is 2 decimals).

    Args:
        number (float): The number to be formatted.
        decimal_places (int): The number of decimal places to retain (default is 2).

    Returns:
        str: The formatted number with 2 decimals as a string with thousand separators and specified decimal places. 

    Example:
        >>> format_number_with_locale(1232.34)
        '1 232,34'
        
        >>> format_number_with_locale(1384723.34)
        '1 384 723,34'
        
        >>> format_number_with_locale(2.34)
        '2,34'
        
        >>> format_number_with_locale(1234567.89, 1)
        '1 234 567,9'
    """
    x = f"{number:,.2f}"
    x = x.replace(',', ' ')
    x = x.replace('.', ',')
    return x