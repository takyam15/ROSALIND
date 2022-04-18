def transcribe(t):
    u = t.strip().replace('T', 'U')
    return u


if __name__ == '__main__':
    with open('./dataset/sample_rosalind_rna.txt') as f:
        t = f.read()
    u = transcribe(t)
    print(u)
    with open('./dataset/rosalind_rna.txt') as f:
        t = f.read()
    u = transcribe(t)
    print(u)
    with open('./submission/transcribing_dna_into_rna.txt', mode='w') as f:
        f.write(u)
