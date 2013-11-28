#!/usr/bin/env python

"""
Extracts each chain of a PDB file to a separate file.

usage: python pdb_splitchain.py <pdb file>
example: python pdb_splitchain.py 1CTF.pdb

This program is part of the PDB tools distributed with HADDOCK
or with the HADDOCK tutorial. The utilities in this package
can be used to quickly manipulate PDB files, with the benefit
of 'piping' several different commands. This is a rewrite of old
FORTRAN77 code that was taking too much effort to compile. RIP.
"""

from itertools import chain as ichain
import os
import re
import sys

__author__ = "Joao Rodrigues"

USAGE = "usage: " + sys.argv[0] + " <pdb file>\n"

def check_input(args):
    """Checks whether to read from stdin/file and validates user input/options."""
    
    if not len(args):
        # Read from pipe
        if not sys.stdin.isatty():
            pdbfh = sys.stdin
        else:
            sys.stderr.write(USAGE)
            sys.exit(1)
    elif len(args) == 1:
        # Read from file
        if not os.path.exists(args[0]):
            sys.stderr.write('File not found: ' + args[0] + '\n')
            sys.stderr.write(USAGE)
            sys.exit(1)
        pdbfh = open(args[0], 'r')
    else:
        sys.stderr.write(USAGE)
        sys.exit(1)
 
    return pdbfh

# def _extract_chains(fhandle):
#     """Enclosing logic in a function to speed up a bit"""              
# 
#     coord_re = re.compile('^(ATOM|HETATM)')
#     prev_chain, cur_chain = None, []
#     fname_root = fhandle.name[:-4] if fhandle.name != '<stdin>' else 'output'
#            
#     for line in fhandle:
#         if coord_re.match(line):
#             if prev_chain != line[21]:
#                 # Chain Change
#                 # Open a new file if we have data to store
#                 if len(cur_chain) >= 1:
#                     output_handle.write(''.join(cur_chain))
#                     output_handle.write('END\n')
#                     output_handle.close()
#                     output_handle = open(fname_root + '_' + line[21].strip() + '.pdb', 'w')
#                 else:
#                     # For first chain only
#                     output_handle = open(fname_root + '_' + line[21].strip() + '.pdb', 'w')
#                 prev_chain = line[21]
#                 cur_chain = [line]
#             cur_chain.append(line)  

def _extract_chains(fhandle):
    """"""              

    coord_re = re.compile('^(ATOM|HETATM)')
    fname_root = fhandle.name[:-4] if fhandle.name != '<stdin>' else 'output'
    prev_chain, chain_atoms = None, []

    for line in fhandle:
        if coord_re.match(line):
            # ATOM/HETATM line
            if prev_chain != line[21]:
                if chain_atoms:
                    # Write chain to file
                    output_handle = open(fname_root + '_' + prev_chain + '.pdb', 'w')
                    output_handle.write(''.join(chain_atoms))
                    output_handle.write('END\n')
                    output_handle.close()
                    chain_atoms = []
                chain_atoms.append(line)
                prev_chain = line[21]
            else:
                chain_atoms.append(line)

    # Output last chain to file
    output_handle = open(fname_root + '_' + chain_atoms[-1][21] + '.pdb', 'w')
    output_handle.write(''.join(chain_atoms))
    output_handle.write('END\n')
    output_handle.close()
    
if __name__ == '__main__':
    # Check Input
    pdbfh = check_input(sys.argv[1:])

    # Do the job
    _extract_chains(pdbfh)
    
    # last line of the script
    # We can close it even if it is sys.stdin
    pdbfh.close()
    sys.exit(0)