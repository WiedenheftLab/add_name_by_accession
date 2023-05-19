# add_name_by_accession

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
