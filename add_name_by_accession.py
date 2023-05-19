#!/usr/bin/python

from Bio import SeqIO
import argparse
import sys
import os
import tqdm
import subprocess
import re
import textwrap

parser = argparse.ArgumentParser(prog='add_name_by_accession',
      formatter_class=argparse.RawDescriptionHelpFormatter,
      epilog=textwrap.dedent('''\

      	Author: Murat Buyukyoruk
      	Associated lab: Wiedenheft lab

        add_name_by_accession help:

This script is developed to add header/additional info for the sequences by using a list of information lined to the accessions. 

SeqIO package from Bio is required to fetch sequences. Additionally, tqdm is required to provide a progress bar since some multifasta files can contain long and many sequences.
        
Syntax:

        add_name_by_accession -i demo.fasta -l demo_sub_list.txt -o demo_sub_list.fasta

seq_fetch dependencies:
	Bio module and SeqIO available in this package      refer to https://biopython.org/wiki/Download
	tqdm                                                refer to https://pypi.org/project/tqdm/
	
Input Paramaters (REQUIRED):
----------------------------
	-i/--input		FASTA			Specify a fasta file. FASTA file requires headers starting with accession number. (i.e. >NZ_CP006019 [fullname])

	-l/--list		List			Specify a list of accession and tap separated entry of info to add into the header. i,e,. Accession\tdescription\n.

	-o/--output		output file	    Specify a output file name that should contain sequences with final header informations.
	
Basic Options:
--------------
	-h/--help		HELP			Shows this help text and exits the run.

	
      	'''))
parser.add_argument('-i', '--input', required=True, type=str, dest='filename',
                        help='Specify a original fasta file.\n')
parser.add_argument('-l', '--list', required=True, type=str, dest='list',
                        help='Specify a list of accession numbers with name.\n')
parser.add_argument('-o', '--output', required=True, dest='out',
                        help='Specify a output fasta file name.\n')

results = parser.parse_args()
filename = results.filename
list = results.list
out = results.out

os.system('> ' + out)

acc_list = []
info_list = []

proc = subprocess.Popen("wc -l < " + list, shell=True, stdout=subprocess.PIPE, )
length = int(proc.communicate()[0].split('\n')[0])

with tqdm.tqdm(range(length+1)) as pbar:
    pbar.set_description('Reading...')
    with open(list,'rU') as file:
        for line in file:
            pbar.update()
            arr = line.split()
            acc_a = arr[0].split('>')[1]
            acc_list.append(acc_a)
            acc_name = "_".join(arr[1:])
            info_list.append(acc_name)

proc = subprocess.Popen("grep -c '>' " + filename, shell=True, stdout=subprocess.PIPE, )
length = int(proc.communicate()[0].split('\n')[0])

with tqdm.tqdm(range(length)) as pbar:
    pbar.set_description('Writing...')
    for record in SeqIO.parse(filename, "fasta"):
        pbar.update()
        id = record.id.split('#')[0]
        acc_parse = id.split('_')[0:-1]

        if len(acc_parse) > 1:
            acc = "_".join(acc_parse[0:])

        else:
            acc = acc_parse[0]
        ind = acc_list.index(acc)

        f = open(out,'a')
        sys.stdout = f

        print '>' + id + '#' + info_list[ind] +  '#NA'
        print re.sub("(.{60})", "\\1\n", str(record.seq), 0, re.DOTALL)


