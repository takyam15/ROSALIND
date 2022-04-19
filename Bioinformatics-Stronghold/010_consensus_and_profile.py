import pandas as pd


def get_dnas(file_path):
    dnas_dict = {}
    with open(file_path) as f:
        for line in f:
            if line.startswith('>'):
                label = line.strip().replace('>', '')
                dnas_dict[label] = ''
            else:
                dnas_dict[label] += line.strip()
    return dnas_dict


def create_dataframe(dnas_dict):
    dnas_series = {}
    for dna in dnas_dict:
        dnas_series[dna] = [s for s in dnas_dict[dna]]
    df_dnas = pd.DataFrame(dnas_series).transpose()
    dnas_counts = {}
    for col in df_dnas.columns:
        dnas_counts[col] = df_dnas[col].value_counts()
    df_counts = pd.DataFrame(dnas_counts).fillna(0).astype(int)
    return df_counts


def create_consensus_string(df_counts):
    consensus_string = ''
    for col in df_counts.columns:
        consensus_string += df_counts[df_counts[col] == df_counts[col].max()].index[0]
    return consensus_string


def create_output(consensus_string, df_counts):
    output = f'{consensus_string}\n'
    nucreotides = ['A', 'C', 'G', 'T']
    for nucreotide in nucreotides:
        output += f'{nucreotide}: {" ".join(df_counts.loc[nucreotide].astype(str).tolist())}\n'
    return output


if __name__ == '__main__':
    dnas_dict = get_dnas('./dataset/sample_rosalind_cons.txt')
    df_counts = create_dataframe(dnas_dict)
    consensus_string = create_consensus_string(df_counts)
    answer = create_output(consensus_string, df_counts)
    print(answer)
    dnas_dict = get_dnas('./dataset/rosalind_cons.txt')
    df_counts = create_dataframe(dnas_dict)
    consensus_string = create_consensus_string(df_counts)
    answer = create_output(consensus_string, df_counts)
    print(answer)
    with open('./submission/consensus_and_profile.txt', mode='w') as f:
        f.write(answer)
