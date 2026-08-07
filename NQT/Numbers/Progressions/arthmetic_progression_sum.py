# find the sum of the first n terms of an arithmetic progression

# Using the formula for the sum of an arithmetic progression
def arithmetic_progression_sum(first_term, common_difference, number_of_terms):
    """
    Calculate the sum of the first n terms of an arithmetic progression.

    Parameters:
    first_term (float): The first term of the arithmetic progression.
    common_difference (float): The common difference between consecutive terms.
    number_of_terms (int): The number of terms to sum.

    Returns:
    float: The sum of the first n terms of the arithmetic progression.
    """
    sum_n = number_of_terms / 2 * (2 * first_term + (number_of_terms - 1) * common_difference)
    return sum_n

# Using the for loop to calculate the sum of the first n terms of an arithmetic progression
def arithmetic_progression_sum_loop(first_term, common_difference, number_of_terms):
    """
    Calculate the sum of the first n terms of an arithmetic progression using a loop.

    Parameters:
    first_term (float): The first term of the arithmetic progression.
    common_difference (float): The common difference between consecutive terms.
    number_of_terms (int): The number of terms to sum.

    Returns:
    float: The sum of the first n terms of the arithmetic progression.
    """
    sum_n = 0
    for i in range(number_of_terms):
        sum_n += first_term + i * common_difference
    return sum_n

# Example usage
if __name__ == "__main__":
    first_term = 2
    common_difference = 3
    number_of_terms = 5

    sum_formula = arithmetic_progression_sum(first_term, common_difference, number_of_terms)
    sum_loop = arithmetic_progression_sum_loop(first_term, common_difference, number_of_terms)

    print(f"Sum of the first {number_of_terms} terms (using formula): {sum_formula}")
    print(f"Sum of the first {number_of_terms} terms (using loop): {sum_loop}")