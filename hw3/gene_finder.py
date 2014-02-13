# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Susan Grimshaw
"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons
from random import shuffle

def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """             
        
    i=0
    j=0
    x= ''
    l=0
    while i<(len(dna)-2):
        substr = dna[i:i+3]
        for j in range(0,len(codons)):
            for l in range(0, len(codons[j])):
                if codons [j][l] == substr:
                    x = x+ aa[j]  
        i = i +3
    return x


def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """
        
    print "input: ATGCGA, expected output: MR, actual output: " + coding_strand_to_AA ("ATGCGA")
    print "input: ATGCCCGCTTT, expected output: MPA, actual output: " + coding_strand_to_AA ("ATGCCCGCTTT")

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    
    i=0
    x = ''
    for i in range(0,len(dna)):
        substr2 = dna[i:i+1]
        if substr2 == 'A' or substr2 == 'a':
            x=x+"T"
        elif substr2 == 'T' or substr2 == 't':
            x = x+ "A"
        elif substr2 == "C" or substr2 == 'c':
            x = x+ "G"
        elif substr2 == "G" or substr2 =='g':
            x = x + "C"
    return x[::-1]
    
def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """
        
    print "input: ATGCCCGCTTT, expected output: AAAGCGGGCAT, actual output: " + get_reverse_complement("ATGCCCGCTTT")
    print "input: CCGCGTTCA, expected output: TGAACGCGG, actual output: " + get_reverse_complement("CCGCGTTCA")   

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    
    i=0    
    while i<(len(dna)-2):
        substr = dna[i:i+3]
        if substr == "TAG" or substr== "TAA" or substr == "TGA":
            return dna[0:i]
        else: i=i+3
    return dna

def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
        
    print "input: ATGTGAA, expected output: ATG, actual output: " + rest_of_ORF("ATGTGAA")
    print "input: ATGAGATAGG, expected output: ATGAGA, actual output: " + rest_of_ORF("ATGAGATAGG")
    print "input: ATGAGA, expected output: ATGAGA, actual output: " + rest_of_ORF("ATGAGA")
        
def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    
    i=0 
    L=[]
    while i<(len(dna)-2):
        if dna[i:i+3] == "ATG":
            subdna = rest_of_ORF(dna[i:])
            L.append (subdna)
            i+=3
        else: i+=3
    return L

        
     
def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """

    print "input: ATGCATGAATGTAGATAGATGTGCCC, expected output: ['ATGCATGAATGTAGA', 'ATGTGCCC'], actual output: " , find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    
    L=[]     
    for i in range (0,3):
        x= find_all_ORFs_oneframe (dna[i:])
        for item in x:
            L.append(item)
    return L
    

def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
        
    print "input: ATGCATGAATGTAG, expected output: ['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG'], actual output: " , find_all_ORFs("ATGCATGAATGTAG")

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    
    L=[]
    x=find_all_ORFs(dna)
    y=find_all_ORFs(get_reverse_complement(dna))
    for item1 in x:
        L.append (item1)
    for item2 in y:
        L.append (item2)
    return L
        
        

def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """

    print "input: ATGCGAATGTAGCATCAAA, expected output: ['ATGCGAATG', 'ATG', 'ATGCTACATTCGCAT'], actual output: " , find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""
        
    x=0  
    y=find_all_ORFs_both_strands(dna)
    z=[]

    for i in range (0,len(y)):
        if len(y[i]) >x:
            x=len(y[i])
            z.append (y[i])
    return z[(len(z)-1)]
            

def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """

    print "input: ATGCGAATGTAGCATCAAA, expected output: 'ATGCTACATTCGCAT', actual output: " , longest_ORF("ATGCGAATGTAGCATCAAA")

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """

    listDna=list(dna) 
    L=[]
    x=0
    z=[]
    
    for j in range (0,num_trials):
        if j<num_trials:      
            shuffle (listDna)
            yy=collapse (listDna)
            zz=longest_ORF (yy)
            L.append (zz)
            
    for i in range (0,len(L)):
        if len(L[i]) >x:
            x=len(L[i])
            z.append (L[i])
            
    return z[-1]
        

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """

            
    y=find_all_ORFs_both_strands(dna)
    z=[]
    L=[]

    for i in range (0,len(y)):
        if len(y[i]) >threshold:
            z.append (y[i])
    for j in range (0,len(z)):
        L.append (coding_strand_to_AA (z[j]))
    return L
        