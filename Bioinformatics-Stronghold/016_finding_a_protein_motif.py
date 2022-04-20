import re
import time

import requests


def get_sequence(protein_id):
    endpoint = f'https://www.uniprot.org/uniprot/{protein_id}.fasta'
    response = requests.get(endpoint)
    time.sleep(1)
    if response.status_code == 200:
        fasta = response.content.decode()
        sequence = ''
        for line in fasta.split('\n'):
            if not line.startswith('>'):
                sequence += line.strip()
        return sequence


if __name__ == '__main__':
    motif_idx = {}
    with open('./dataset/sample_rosalind_mprt.txt') as f:
        for line in f:
            if line.strip():
                sequence = get_sequence(line.strip())
                motifs = re.finditer('(?=N[^P][ST][^P])', sequence)
                motif_idx[line.strip()] = [motif.span()[0]+1 for motif in motifs]
    answer = ''
    for protein, motifs in motif_idx.items():
        if motifs:
            answer += f'{protein}\n{" ".join([str(motif) for motif in motifs])}\n'
    print(answer)
    motif_idx = {}
    with open('./dataset/rosalind_mprt.txt') as f:
        for line in f:
            if line.strip():
                sequence = get_sequence(line.strip())
                motifs = re.finditer('(?=N[^P][ST][^P])', sequence)
                motif_idx[line.strip()] = [motif.span()[0]+1 for motif in motifs]
    answer = ''
    for protein, motifs in motif_idx.items():
        if motifs:
            answer += f'{protein}\n{" ".join([str(motif) for motif in motifs])}\n'
    print(answer)
    with open('./submission/finding_a_protein_motif.txt', mode='w') as f:
        f.write(answer)
