pdb-tools
================================================
Set of utility scripts in python to manipulate PDB files

About
---------

Manipulating PDB files is a pain. Libraries like Biopython exist but sometimes all that is needed is a quick
and dirty manipulation to the structure, such as extracting chains, renumbering, etc..

These scripts are the descendant of a set of old FORTRAN77 programs in use in our lab at Utrecht that had the 
particular advantage of being used with 'pipes' (e.g. cat mypdb.pdb | program_x). FORTRAN77 is a pain too,
so I rewrote the scripts in Python.

Scripts
-----------
* pdb_chain / pdb_seg / pdb_b / pdb_occ

   Set the chain/segment/b-factor/occupancy fields to a particular string. Chains are restricted to 1 character, segments to four, b-factor and occupancy are floats.
                                                                                                                   
* pdb_reres / pdb_reatom

   Renumber the PDB file either on a residue basis or on an atom basis.

* pdb_selchain / pdb_selseg

   Extract a portion of the PDB file that matches a particular chain/segment identifier

* pdb_chainxseg / pdb_segxchain

   Swap the chain/segment identifier. Restricts the segment identifier to the first character to comply with PDB format.

* pdb_harmonize

   Compares the atoms of two PDB files and keeps only those common to both structures. Useful for RMSD calculations.

* pdb_delocc

   Removes multiple occupancies from PDB file. Keeps the first atomic location found.

* pdb_toseq
   
   Extracts the amino acid sequence as present in the ATOM lines of the PDB file.
   
Requirements
------------

* Python 2.5+ (not tested, might work on earlier versions)
                                                             
Examples
------------

```
# Renumber structure from 1 to n
cat 1CTF.pdb | pdb_reres.py -1  

# Extract chain A from PDB file
cat 1brs.pdb | pdb_selchain.py -A
./pdb_selchain.py -A 1brs.pdb

# Combine extraction and renumbering
./pdb_selchain.py -D 1brs.pdb | ./pdb_reres -1
```
