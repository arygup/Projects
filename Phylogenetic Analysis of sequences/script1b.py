from alignment.sequence import Sequence
from alignment.vocabulary import Vocabulary
from alignment.sequencealigner import SimpleScoring, GlobalSequenceAligner
from Bio import pairwise2
from Bio.SubsMat.MatrixInfo import blosum62
from Bio.Seq import Seq
from Bio import Align
from Bio.SubsMat import MatrixInfo as matlist
aligner = Align.PairwiseAligner(match_score = 1.0)
from ete3 import Tree

def lowest_cell(table):
    min_cell = float("inf")
    x, y = -1, -1
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] < min_cell:
                min_cell = table[i][j]
                x, y = i, j
    return x, y

def join_labels(labels, a, b):
    if b < a:
        a, b = b, a
    labels[a] = "(" + labels[a] + "," + labels[b] + ")"
    del labels[b]

def join_table(table, a, b):
    if b < a:
        a, b = b, a
    row = []
    for i in range(0, a):
        row.append((table[a][i] + table[b][i])/2)
    table[a] = row
    for i in range(a+1, b):
        table[i][a] = (table[i][a]+table[b][i])/2
    for i in range(b+1, len(table)):
        table[i][a] = (table[i][a]+table[i][b])/2
        del table[i][b]
    del table[b]

def UPGMA(table, labels):
    while len(labels) > 1:
        x, y = lowest_cell(table)
        join_table(table, x, y)
        join_labels(labels, x, y)
    return labels[0]

def alpha_labels(start, end):
    labels = []
    for i in range(ord(start), ord(end)+1):
        labels.append(chr(i))
    return labels




#10 input Nucleotide

n1 = "ATATAAATATGGGAAAGAGAATGGGGAAATTTCTACCAGTCTTCATCTCTGAGAGCAAACTTCTCTGCATCTCTTTCTCTCTTCTCTGGGCCTCCCCCAGCTCATCATGGCTCTCTGGATCCGATCACTGCCTCTTCTGGCTCTCCTTGTCTTTTCTGGCCCTGGAACCAGCTATGCAGCTGCCAACCAGCACCTCTGTGGCTCCCACTTGGTGGAGGCTCTCTACCTGGTGTGTGGAGAGCGTGGCTTCTTCTACTCCCCCAAAGCCCGACGGGATGTCGAGCAGCCCCTAGTGAGCAGTCCCTTGCGTGGCGAGGCAGGAGTGCTGCCTTTCCAGCAGGAGGAATACGAGAAAGTCAAGCGAGGGATTGTTGAGCAATGCTGCCATAACACGTGTTCCCTCTACCAACTGGAGAACTACTGCAACTAGCCAAGAAGCCGGAAGCGGGCACAGACATACACTTACTCTATCGCACCTTCAAAGCATTTGAATAAACCTTGTTGGTCTACTGGAAGACTTGTGCC"
n2 = "CACCCCGACACGGCCGGCAAACAGGTCGCCATGGCCCTCTGGATGCGCCTCCTGCCCCTGCTGGCCCTGCTGGCCCTCTGGGCGCCCGCGCCCACCCGAGCCTTCGTTAACCAGCACCTGTGTGGCTCCCACCTGGTAGAGGCTCTGTACCTGGTGTGCGGGGAGCGCGGCTTCTTCTACACGCCTAAGGCCCGCCGGGAGGTGGAGGACCTGCAGGTGAGGGACGTGGAGCTGGCCGGGGCGCCTGGCGAGGGCGGCCTGCAGCCCCTGGCCCTGGAGGGGGCCCTGCAGAAGCGAGGCATCGTGGAGCAGTGCTGCACCAGCATCTGCTCCCTCTACCAGCTGGAGAATTACTGCAACTAGGGGCGCGGGGGGCAGGACGTGGCAGCACCTGCTGCAGGTCACGGTGGCCGCAAGCCTTCGGCTCTCTGCACCCCAAGTGATTCAATAAACCCTCTGAATG"
n3 = "CCGATGTGCTCTGAAAGCCTGGATGCAAAAACACCTTCTCTTGTCTACCATCTCTACCATTCCTTGTCCTCTGCTGCAAGAACAGTGTGACCATGGCAGTGTGGCTCCAGGCTGGTGCTCTTTTGTTCTTGTTGGCCGTCTCCAGTGTGAACGCTAACGCAGGGGCCCCACAGCATCTGTGTGGATCTCATCTGGTCGATGCCCTCTACCTGGTCTGTGGTCCAACAGGATTCTTCTACAACCCCAAGAGAGATGTTGACCCTCTTATGGGTTTCCTTCCTCCAAAATCTGCCCAGGAAACTGAGGTGGCTGACTTTGCATTTAAAGATCATGCCGAGGTGATAAGGAAGAGAGGCATTGTGGAGCAGTGTTGCCACAAACCCTGCAGTATCTTTGAGCTGCAGAACTACTGTAACTAAAGAACCTGCACATGTCTTGTGACAACTGCCAGTGACTTTACCACCTGTTTGCACACAGGTATCATGGGAATTACGAGAACTAAACAAAAAGTATCTTTTATTTTAAAATAGTTTACTTTT"
n4 = "ATGGCCCTGTGGATGCGCCTCCTGCCCCTGCTGGCGCTGCTGGCCCTCTGGGGACCTGACCCAGCCGCAGCCTTTGTGAACCAACACCTGTGCGGCTCACACCTGGTGGAAGCTCTCTACCTAGTGTGCGGGGAACGAGGCTTCTTCTACACACCCAAGACCCGCCGGGAGGCAGAGGACCTGCAGGTGGGGCAGGTGGAGCTGGGCGGGGGCCCTGGTGCAGGCAGCCTGCAGCCCTTGGCCCTGGAGGGGTCCCTGCAGAAGCGTGGCATTGTGGAACAATGCTGTACCAGCATCTGCTCCCTCTACCAGCTGGAGAACTACTGCAACTAG"
n5 = "AACCCTAAGTGACCAGCTACAATCATAGACCATCAGCAAGCAGGTCATTGTTCCAACATGGCCCTGTGGATGCGCTTCCTGCCCCTGCTGGCCCTGCTCGTCCTCTGGGAGCCCAAGCCTGCCCAGGCTTTTGTCAAACAGCACCTTTGTGGTCCTCACCTGGTGGAGGCTCTGTACCTGGTGTGTGGGGAACGTGGTTTCTTCTACACACCCAAGTCCCGTCGTGAAGTGGAGGACCCGCAAGTGCCACAACTGGAGCTGGGTGGAGGCCCGGAGGCCGGGGATCTTCAGACCTTGGCACTGGAGGTTGCCCGGCAGAAGCGTGGCATTGTGGATCAGTGCTGCACCAGCATCTGCTCCCTCTACCAACTGGAGAACTACTGCAACTGAGTCCACCACTCCCCGCCCACCCCTCTGCAATGAATAAAGCCTTTGAATGAGCACCAAAAAAAAAAAAAAAAAA"
n6 = "AGCCCTCTGGGACCAGCTGTGTTCCCAGGCCACCGGCAAGCAGGTCCTCACCCCCCGCCATGGCCCTGTGGACGCGCCTCCTGCCCCTGCTGGCCCTGCTGGCCCTCTGGGCGCCCGCCCCGGCCCAGGCCTTCGTGAACCAGCACCTGTGCGGCTCCCACCTGGTGGAGGCGCTGTACCTGGTGTGCGGGGAGCGCGGCTTCTTCTACACGCCCAAGGCCCGTCGGGAGGCGGAGAACCCTCAGGCAGGTGCCGTGGAGCTGGGCGGAGGCCTGGGCGGCCTGCAGGCCCTGGCGCTGGAGGGGCCCCCGCAGAAGCGTGGCATCGTGGAGCAGTGCTGCACCAGCATCTGTTCCCTCTACCAGCTGGAGAACTACTGCAACTAGGCCGCCCCTGAGGGCGCCTGCTGCTCCCCGCACCCCAAAACCCAATAAA"
n7 = "AGCCCCCCGCCCTCAGGACCGGCTGCATTCGAGGCTGCCAGCAAGCAGGTCCTCGCAGCCCCGCCATGGCCCTGTGGACACGCCTGGCGCCCCTGCTGGCCCTGCTGGCGCTCTGGGCCCCCGCCCCGGCCCGCGCCTTCGTCAACCAGCATCTGTGTGGCTCCCACCTGGTGGAGGCGCTGTACCTGGTGTGCGGAGAGCGCGGCTTCTTCTACACGCCCAAGGCCCGCCGGGAGGTGGAGGGCCCCCAGGTGGGGGCGCTGGAGCTGGCCGGAGGCCCGGGCGCGGGCGGCCTGGAGGGGCCCCCGCAGAAGCGTGGCATCGTGGAGCAGTGCTGTGCCAGCGTCTGCTCGCTCTACCAGCTGGAGAACTACTGTAACTAGGCCTGCCCCCGACACCAATAAACCCCTTGACGAGCCCTGCAAAAAAAAAAA"
n8 = "AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGATCACTGTCCTTCTGCCATGGCCCTGTGGATGCGCCTCCTGCCCCTGCTGGTGCTGCTGGCCCTCTGGGGACCTGACCCAGCCTCGGCCTTTGTGAACCAACACCTGTGCGGCTCCCACCTGGTGGAAGCTCTCTACCTAGTGTGCGGGGAACGAGGCTTCTTCTACACACCCAAGACCCGCCGGGAGGCAGAGGACCTGCAGGTGGGGCAGGTGGAGCTGGGCGGGGGCCCTGGTGCAGGCAGCCTGCAGCCCTTGGCCCTGGAGGGGTCCCTGCAGAAGCGTGGTATCGTGGAACAATGCTGTACCAGCATCTGCTCCCTCTACCAGCTGGAGAACTACTGCAACTAGATGGAATAAAGCCCTTGAACCAGC"
n9 = "GCATTCTGAGGCATTCTCTAACAGGTTCTCGACCCTCCGCCATGGCCCCGTGGATGCATCTCCTCACCGTGCTGGCCCTGCTGGCCCTCTGGGGACCCAACTCTGTTCAGGCCTATTCCAGCCAGCACCTGTGCGGCTCCAACCTAGTGGAGGCACTGTACATGACATGTGGACGGAGTGGCTTCTATAGACCCCACGACCGCCGAGAGCTGGAGGACCTCCAGGTGGAGCAGGCAGAACTGGGTCTGGAGGCAGGCGGCCTGCAGCCTTCGGCCCTGGAGATGATTCTGCAGAAGCGCGGCATTGTGGATCAGTGCTGTAATAACATTTGCACATTTAACCAGCTGCAGAACTACTGCAATGTCCCTTAGACACCTGCCTTGGGCCTGGCCTGCTGCTCTGCCCTGGCAACCAATAAACCCCTTGAATGAG"
n10 = "TCATCGGCTCTGCACCATGGCCTCCCTGGCCGCGCTCCTGCCCCTGCTGGCCCTGCTGGTCCTCTGCAGACTGGATCCTGCCCAGGCCTTCGTCAACCAGCACCTGTGCGGCTCTCACCTGGTGGAGGCGCTGTACCTGGTGTGCGGGGAGCGCGGCTTTTTTTATACACCCAAGTCCCGCCGCGAGGTGGAGGAGCTGCAGGTGGGGCAGGCGGAGCTGGGCGGGGGGCCCGGCGCGGGCGGCCTGCAGCCCTCGGCGCTGGAGCTGGCCCTGCAGAAGCGCGGCATCGTGGAGCAGTGTTGCACCAGCATCTGCTCGCTCTACCAGCTGGAGAACTACTGCAACTAGGGGTGCCCCCCACCCACCCCTGCCCGCGCCCCCCACGCCCCCCGCCCTCGCCCCCACCCAATAAACCCCTCCACGCGCCCCGGG"

n = []
n.append(n1)
n.append(n2)
n.append(n3)
n.append(n4)
n.append(n5)
n.append(n6)
n.append(n7)
n.append(n8)
n.append(n9)
n.append(n10)


dm = []

matrix = matlist.blosum62

for i in range(0, 10):
    dl = []
    for j in range(0, 10):
        if i == j:
            break
        x = aligner.score(n[i], n[j])
        al = pairwise2.align.globalxx(n[i], n[j])
        y = (al[0][4] - al[0].score)/al[0][4]
        dl.append(y)
    dm.append(dl)

M_labels = alpha_labels("A", "J")   #A through J 10 sequences

up = []
up = UPGMA(dm, M_labels)
print(up) 

upg = ""
for ele in up: 
        upg += ele
upg += ';'
unrooted_tree = Tree( upg )
print(unrooted_tree)