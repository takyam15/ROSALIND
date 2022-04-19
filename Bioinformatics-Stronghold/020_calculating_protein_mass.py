monoisotopic_masses = {}
with open('./monoisotopic_mass_table.txt') as f:
    for line in f:
        amino_acid, mass = line.strip().split('   ')
        monoisotopic_masses[amino_acid] = mass


def calculate_mass(s, masses=monoisotopic_masses):
    mass = 0
    for aa in s:
        mass += float(masses[aa])
    return mass


if __name__ == '__main__':
    with open('./dataset/sample_rosalind_prtm.txt') as f:
        s = f.read().strip()
    mass = calculate_mass(s)
    print(mass)
    with open('./dataset/rosalind_prtm.txt') as f:
        s = f.read().strip()
    mass = calculate_mass(s)
    print(mass)
    with open('./submission/calculating_protein_mass.txt', mode='w') as f:
        f.write(str(mass))
