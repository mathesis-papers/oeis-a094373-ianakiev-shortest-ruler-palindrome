import json
from itertools import permutations
from math import comb, factorial, prod
from pathlib import Path


def valuation(number):
    if number <= 0:
        raise ValueError('The valuation requires a positive integer')
    return (number & -number).bit_length() - 1


def sequence_a(index):
    return 1 if index == 0 else 2 ** (index - 1) + 1


def ruler(index):
    return 1 + valuation(index)


def divisor_quotient(index, power):
    divisors = [divisor for divisor in range(1, index + 1) if index % divisor == 0]
    odd_sum = sum(divisor ** power for divisor in divisors if divisor % 2)
    total_sum = sum(divisor ** power for divisor in divisors)
    assert total_sum % odd_sum == 0
    return total_sum // odd_sum


def additional_checks(minima):
    factor_checks = 0
    for start in range(1, 129):
        for length in range(1, 65):
            word = [ruler(index) for index in range(start, start + length)]
            actual = word == word[::-1]
            center = start + length // 2
            expected = length % 2 == 1 and length // 2 < 2 ** valuation(center)
            assert actual == expected
            factor_checks += 1

    for endpoint in range(1, 257):
        word = [ruler(index) for index in range(1, endpoint + 1)]
        lengths = [length for length in range(1, endpoint + 1)
                   if word[-length:] == word[-length:][::-1]]
        bits = [bit for bit in range(endpoint.bit_length()) if endpoint & (1 << bit)]
        expected = [1 + 2 * sum(1 << bit for bit in bits[:count])
                    for count in range(len(bits))]
        assert lengths == expected
        assert len(lengths) == endpoint.bit_count()

    quotient_checks = 0
    for index in range(1, 129):
        for power in range(6):
            assert divisor_quotient(index, power) == sum(2 ** (power * term)
                                                        for term in range(ruler(index)))
            quotient_checks += 1
    for height in range(1, 11):
        word = [(4 ** ruler(index) - 1) // 3 for index in range(1, 2 ** height)]
        assert word == word[::-1]
        assert sum(word) == (2 ** height - 1) * (2 ** (height + 1) - 1) // 3
        assert word[2 ** (height - 1) - 1] == (4 ** height - 1) // 3
    for power in range(4):
        word = [sum(2 ** (power * term) for term in range(ruler(index)))
                for index in range(1, 513)]
        for start in range(1, 129):
            minimum = 2 ** (valuation(start) + 1) + 1
            lengths = [length for length in range(2, minimum + 1)
                       if word[start - 1:start - 1 + length]
                       == word[start - 1:start - 1 + length][::-1]]
            assert lengths == [minimum]

    for endpoint in range(1, 513):
        assert sum(ruler(index) for index in range(1, endpoint + 1)) == 2 * endpoint - endpoint.bit_count()
        coincidences = {ruler(index) for index in range(1, endpoint)
                        if ruler(index) == ruler(endpoint - index)}
        assert coincidences == set(range(1, ruler(endpoint)))
    word = [ruler(index) for index in range(1, 257)]
    square_checks = 0
    for start in range(len(word)):
        for length in range(1, (len(word) - start) // 2 + 1):
            assert word[start:start + length] != word[start + length:start + 2 * length]
            square_checks += 1
    for index in range(1, 257):
        for smaller in range(1, ruler(index)):
            changed = word[:index - 1] + [smaller]
            length = 2 ** (smaller - 1)
            assert changed[-2 * length:-length] == changed[-length:]

    for index in range(61):
        transform = sum(comb(index, term) * sequence_a(term) for term in range(index + 1))
        inverse = sum((-1) ** (index - term) * comb(index, term) * sequence_a(term)
                      for term in range(index + 1))
        assert transform == 2 ** index + (3 ** index - 1) // 2
        assert inverse == (index == 0 or index % 2 == 1)
    degree = 128
    coefficients = [1] + [0] * degree
    weight = 1
    while weight <= degree:
        for index in range(degree, weight - 1, -1):
            coefficients[index] += coefficients[index - weight]
        weight = 2 * weight + 1
    for exponent in range(1, degree + 1):
        assert 2 * sum(coefficients[:exponent]) == minima[exponent]
    for exponent in range(8):
        for remainder in range(2 ** exponent):
            expected = (2 ** (exponent + 1) if remainder == 2 ** exponent - 1
                        else 2 ** exponent + minima[remainder + 1])
            assert minima[2 ** exponent + remainder] == expected
    jumps = {2 * index - index.bit_count() for index in range(1, 513)}
    for exponent in range(2, 513):
        assert (minima[exponent + 1] == minima[exponent] + 2) == (exponent in jumps)
    continued = [0] * 65
    for level in range(65, -1, -1):
        continued = [1] + [2 ** level + continued[0]] + continued[1:-1]
    assert continued == [sequence_a(index) for index in range(65)]
    for dimension in range(1, 8):
        original = [[-((row - column - 1) // dimension)
                     for column in range(1, dimension + 1)] for row in range(1, dimension + 1)]
        corrected = [[-((row - column - 2) // dimension)
                      for column in range(1, dimension + 1)] for row in range(1, dimension + 1)]
        original_sum = sum(prod(original[row][image[row]] for row in range(dimension))
                           for image in permutations(range(dimension)))
        corrected_sum = sum(prod(corrected[row][image[row]] for row in range(dimension))
                            for image in permutations(range(dimension)))
        assert original_sum == 1
        assert corrected_sum == 2 ** (dimension - 1) + 1
    for chosen_side in [1, 3, 5, 7]:
        adjacency = []
        for source in range(9):
            row = []
            for destination in range(9):
                if source == 4:
                    connected = destination == chosen_side
                else:
                    connected = (source != destination
                                 and abs(source // 3 - destination // 3)
                                 == abs(source % 3 - destination % 3))
                row.append(int(connected))
            adjacency.append(row)
        counts = [1] * 9
        for length in range(21):
            assert all(counts[corner] == sequence_a(length) for corner in [0, 2, 6, 8])
            assert counts[4] == (1 if length == 0 else 2 ** (length - 1))
            counts = [sum(adjacency[source][destination] * counts[destination]
                          for destination in range(9)) for source in range(9)]
    return {
        'all_factor_windows': factor_checks,
        'factor_start_positions': [1, 128],
        'factor_lengths': [1, 64],
        'suffix_prefix_lengths': [1, 256],
        'divisor_quotient_checks': quotient_checks,
        'divisor_inputs': [1, 128],
        'divisor_powers': [0, 5],
        'divisor_palindrome_powers': [0, 3],
        'divisor_palindrome_starts': [1, 128],
        'a296306_prefix_heights': [1, 10],
        'ruler_sum_and_coincidence_inputs': [1, 512],
        'square_tests': square_checks,
        'square_free_prefix_length': 256,
        'binomial_transform_indices': [0, 60],
        'factorial_generating_function_degree': degree,
        'factorial_recursion_dyadic_exponents': [0, 7],
        'factorial_jump_exponents': [2, 512],
        'continued_fraction_degree': 64,
        'permanent_matrix_dimensions': [1, 7],
        'elephant_walk_lengths': [0, 20],
        'elephant_center_side_choices': 4
    }


def main():
    factorial_limit = 4096
    current_factorial = 1
    least_index = 1
    minima = []
    for exponent in range(factorial_limit + 1):
        modulus = 1 << exponent
        while current_factorial % modulus:
            least_index += 1
            current_factorial *= least_index
        assert current_factorial == factorial(least_index)
        assert current_factorial % modulus == 0
        if least_index > 1:
            assert factorial(least_index - 1) % modulus != 0
        minima.append(least_index)
    boundaries = [0]
    for exponent in range(1, len(minima)):
        if minima[exponent] != minima[exponent - 1]:
            boundaries.append(exponent)
    runs = [right - left for left, right in zip(boundaries, boundaries[1:])]
    assert runs[0] == 1
    for position, length in enumerate(runs[1:], start=2):
        assert length == 1 + valuation(position - 1)
    for run_index, boundary in enumerate(boundaries[1:]):
        assert boundary == valuation(factorial(2 * run_index)) + 1
        assert minima[boundary] == 2 * (run_index + 1)

    position_limit = 257
    palindrome_lengths = [1]
    candidates = 0
    reflected_pairs = 0
    for position in range(2, position_limit + 1):
        predicted = 2 ** (valuation(position - 1) + 1) + 1
        assert position - 1 + predicted <= len(runs)
        observed = None
        for length in range(2, predicted + 1):
            candidates += 1
            block = runs[position - 1:position - 1 + length]
            if block == block[::-1]:
                observed = length
                break
        assert observed == predicted
        palindrome_lengths.append(observed)
        reflected_pairs += predicted // 2

    first_positions = []
    seen = set()
    for position, length in enumerate(palindrome_lengths, start=1):
        if length not in seen:
            first_positions.append(position)
            seen.add(length)
    expected_first = [sequence_a(index) for index in range(10)]
    assert first_positions == expected_first
    for index in range(2, 10):
        assert palindrome_lengths[sequence_a(index - 1) - 1] == sequence_a(index)
    count_checks = 0
    for prefix in range(1, position_limit + 1):
        for exponent in range(9):
            target = 2 ** (exponent + 1) + 1
            actual = palindrome_lengths[1:prefix].count(target)
            expected = (prefix - 1) // 2 ** exponent - (prefix - 1) // 2 ** (exponent + 1)
            assert actual == expected
            count_checks += 1
    for height in range(2, 11):
        prefix = [1 + valuation(index) for index in range(1, 2 ** (height - 1))]
        assert prefix == prefix[::-1]

    for index in range(101):
        assert sum(sequence_a(term) for term in range(index + 1)) == 2 ** index + index
        if index >= 2:
            assert sequence_a(index) == 2 * sequence_a(index - 1) - 1
        if index >= 3:
            assert sequence_a(index) == 3 * sequence_a(index - 1) - 2 * sequence_a(index - 2)
        if index >= 1:
            assert sequence_a(2 * index) == 2 * sequence_a(2 * index - 1) - 1
            assert sequence_a(index + 1) <= 2 * sequence_a(index)
    subset_sums = {0}
    for index in range(13):
        subset_sums |= {number + sequence_a(index) for number in subset_sums}
        assert len(subset_sums) == 2 ** index + index + 1
        assert min(subset_sums) == 0
        assert max(subset_sums) == 2 ** index + index

    extended = additional_checks(minima)
    output = {
        'status': 'pass',
        'arithmetic': 'exact integers',
        'factorial_exponents': [0, factorial_limit],
        'complete_run_count': len(runs),
        'last_complete_run_position': len(runs),
        'palindrome_start_positions': [2, position_limit],
        'candidate_blocks_tested': candidates,
        'attaining_reflected_pairs': reflected_pairs,
        'first_occurrence_positions': first_positions,
        'position_identity_indices': [2, 9],
        'occurrence_count_checks': count_checks,
        'ruler_prefix_heights': [2, 10],
        'sequence_identity_indices': [0, 100],
        'completeness_prefix_indices': [0, 12],
        'palindrome_prefix': palindrome_lengths[:17],
        'sibling_checks': extended,
        'scope': 'Finite consistency checks; note.tex supplies written proofs or cited results for the unbounded statements.'
    }
    Path(__file__).with_name('verification.json').write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
