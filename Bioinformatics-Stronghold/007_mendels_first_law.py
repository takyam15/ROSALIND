def calculate_dominant_probability(k, m, n):
    total = k + m + n
    p = k / total + (m / total) * ((k + 3*(m-1)/4 + n/2) / (total - 1)) + (n / total) * ((k + m/2) / (total - 1))
    return p


if __name__ == '__main__':
    with open('./dataset/sample_rosalind_iprb.txt') as f:
        k, m, n = f.read().strip().split(' ')
    p = calculate_dominant_probability(int(k), int(m), int(n))
    print(p)
    with open('./dataset/rosalind_iprb.txt') as f:
        k, m, n = f.read().strip().split(' ')
    p = calculate_dominant_probability(int(k), int(m), int(n))
    print(p)
    with open('./submission/mendels_first_law.py', mode='w') as f:
        f.write(str(p))
