
dna_rna_nucleotides = str.maketrans({
    'T': 'A',
    'A': 'U',
    'C': 'G',
    'G': 'C',
    't': 'a',
    'a': 'u',
    'c': 'g',
    'g': 'c'
})

rna_AA = {
    "UUU": "Phe",
    "UUC": "Phe",
    "UUA": "Leu",
    "UUG": "Leu",
    "CUU": "Leu",
    "CUC": "Leu",
    "CUA": "Leu",
    "CUG": "Leu",
    "AUU": "Ile",
    "AUC": "Ile",
    "AUA": "Ile",
    "AUG": "Met",  # or start
    "GUU": "Val",
    "GUC": "Val",
    "GUA": "Val",
    "GUG": "Val",
    "UCU": "Ser",
    "UCC": "Ser",
    "UCA": "Ser",
    "UCG": "Ser",
    "CCU": "Pro",
    "CCC": "Pro",
    "CCA": "Pro",
    "CCG": "Pro",
    "ACU": "Thr",
    "ACC": "Thr",
    "ACA": "Thr",
    "ACG": "Thr",
    "GCU": "Ala",
    "GCC": "Ala",
    "GCA": "Ala",
    "GCG": "Ala",
    "UAU": "Tyr",
    "UAC": "Tyr",
    "UAA": "Stop",  # stop
    "UAG": "Stop",  # stop
    "CAU": "His",
    "CAC": "His",
    "CAA": "Gln",
    "CAG": "Gln",
    "AAU": "Asn",
    "AAC": "Asn",
    "AAA": "Lys",
    "AAG": "Lys",
    "GAU": "Asp",
    "GAC": "Asp",
    "GAA": "Glu",
    "GAG": "Glu",
    "UGU": "Cys",
    "UGC": "Cys",
    "UGA": "Stop",  # stop
    "UGG": "Trp",
    "CGU": "Arg",
    "CGC": "Arg",
    "CGA": "Arg",
    "CGG": "Arg",
    "AGU": "Ser",
    "AGC": "Ser",
    "AGA": "Arg",
    "AGG": "Arg",
    "GGU": "Gly",
    "GGC": "Gly",
    "GGA": "Gly",
    "GGG": "Gly",
    "uuu": "Phe",
    "uuc": "Phe",
    "uua": "Leu",
    "uug": "Leu",
    "cuu": "Leu",
    "cuc": "Leu",
    "cua": "Leu",
    "cug": "Leu",
    "auu": "Ile",
    "auc": "Ile",
    "aua": "Ile",
    "aug": "Met",  # or start
    "guu": "Val",
    "guc": "Val",
    "gua": "Val",
    "gug": "Val",
    "ucu": "Ser",
    "ucc": "Ser",
    "uca": "Ser",
    "ucg": "Ser",
    "ccu": "Pro",
    "ccc": "Pro",
    "cca": "Pro",
    "ccg": "Pro",
    "acu": "Thr",
    "acc": "Thr",
    "aca": "Thr",
    "acg": "Thr",
    "gcu": "Ala",
    "gcc": "Ala",
    "gca": "Ala",
    "gcg": "Ala",
    "uau": "Tyr",
    "uac": "Tyr",
    "uaa": "Stop",  # stop
    "uag": "Stop",  # stop
    "cau": "His",
    "cac": "His",
    "caa": "Gln",
    "cag": "Gln",
    "aau": "Asn",
    "aac": "Asn",
    "aaa": "Lys",
    "aag": "Lys",
    "gau": "Asp",
    "gac": "Asp",
    "gaa": "Glu",
    "gag": "Glu",
    "ugu": "Cys",
    "ugc": "Cys",
    "uga": "Stop",  # stop
    "ugg": "Trp",
    "cgu": "Arg",
    "cgc": "Arg",
    "cga": "Arg",
    "cgg": "Arg",
    "agu": "Ser",
    "agc": "Ser",
    "aga": "Arg",
    "agg": "Arg",
    "ggu": "Gly",
    "ggc": "Gly",
    "gga": "Gly",
    "ggg": "Gly",
}


def dna_to_pre_rna(dna_string: str) -> str:
    return dna_string.translate(dna_rna_nucleotides)


def rna_to_AA(rna_string: str):
    pp_chain = []
    buf = ""
    for char in rna_string:
        buf += char
        if len(buf) == 3:
            pp_chain.append(rna_AA[buf.lower()])
            buf = ""
    if len(buf) != 0:
        raise Exception("rna_string #nucleotides is not a multiple of 3")

    return list(pp_chain)



a = dna_to_pre_rna("TAC AAT GTA GAG CAA CAG AAA GAC CAA TGA TAT CGA CTC TAT AAT GAT TAA TAA TAC TCC").split(" ")
# print(a)
# a = "TAC AAT GTA GAG CAA CAG AAA GAC CAA TGA TAT CGA CTC TAT AAT GAT TAA TAA TAC TCC".split(" ")
print(*rna_to_AA(a))
