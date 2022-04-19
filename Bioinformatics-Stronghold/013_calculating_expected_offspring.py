probs = {
    'AA-AA': 1,
    'AA-Aa': 1,
    'AA-aa': 1,
    'Aa-Aa': 0.75,
    'Aa-aa': 0.5,
    'aa-aa': 0
}


def calculate_expected_offspring(numbers, probs=probs, offspiring=2):
    expected_number = 0
    for prob, number in zip(probs, numbers):
        expected_number += offspiring * probs[prob] * int(number)
    return expected_number


if __name__ == '__main__':
    with open('./dataset/sample_rosalind_iev.txt') as f:
        numbers = f.read().strip().split(' ')
    expected_number = calculate_expected_offspring(numbers)
    print(expected_number)
    with open('./dataset/rosalind_iev.txt') as f:
        numbers = f.read().strip().split(' ')
    expected_number = calculate_expected_offspring(numbers)
    print(expected_number)
    with open('./submission/calculating_expected_offspring.txt', mode='w') as f:
        f.write(str(expected_number))
