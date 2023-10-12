#ReverseComplement#
def ReverseComplement(seq):
    seq = seq.upper()
    seq = seq.replace('A', 't')
    seq = seq.replace('T', 'a')
    seq = seq.replace('C', 'g')
    seq = seq.replace('G', 'c')
    seq = seq[::-1]  # Reverse
    return seq.upper()
#Test example#
seq = "ATCGatcgATCGatcg"
print(ReverseComplement(seq))