maria@gcs-hpc:~/Amber/Mtor_test$ antechamber -j 5 -at sybyl -dr no -i run_1.pdb -fi pdb -o ligand.mol2 -fo mol2

Welcome to antechamber 22.0: molecular input file processor.

Info: The atom type is set to sybyl; the options available to the -at flag are
      gaff, gaff2, amber, bcc, and sybyl.



maria@gcs-hpc:~/Amber/Mtor_test$ antechamber -j 5 -at sybyl -dr no -i run_1.pdb -fi pdb -o ligand.mol2 -fo mol2

Welcome to antechamber 22.0: molecular input file processor.

Info: The atom type is set to sybyl; the options available to the -at flag are
      gaff, gaff2, amber, bcc, and sybyl.



maria@gcs-hpc:~/Amber/Mtor_test$ parmchk2 -i ligand.mol2 -f mol2 -o ligand.frcmod
Atom type of N.3 does not exist in PARMCHK.DAT
maria@gcs-hpc:~/Amber/Mtor_test$ c;ear
c: command not found

Command 'ear' not found, but can be installed with:

sudo apt install ecere-dev

maria@gcs-hpc:~/Amber/Mtor_test$ cd ..
maria@gcs-hpc:~/Amber$ ls
150  Ahn  Carlo_test  Github  Mtor_test  Tutorial
maria@gcs-hpc:~/Amber$ cd 150
maria@gcs-hpc:~/Amber/150$ pdb4amber -i Shc1-PTB_1OY2.pdb -o pro.pdb --dry --reduce

==================================================
Summary of pdb4amber for: Shc1-PTB_1OY2.pdb
===================================================

----------Chains
The following (original) chains have been found:
A

---------- Alternate Locations (Original Residues!))

The following residues had alternate locations:
None
-----------Non-standard-resnames


---------- Missing heavy atom(s)

None
maria@gcs-hpc:~/Amber/150$ antechamber -i run_1.pdb -fi pdb -o ligand.mol2 -fo mol2 -pf y -nc 0 -c bcc

Welcome to antechamber 22.0: molecular input file processor.

Info: acdoctor mode is on: check and diagnose problems in the input file.
Info: The atom type is set to gaff; the options available to the -at flag are
      gaff, gaff2, amber, bcc, and sybyl.

-- Check Format for pdb File --
   Status: pass
-- Check Unusual Elements --
   Status: pass
-- Check Open Valences --
   Status: pass
-- Check Geometry --
      for those bonded   
      for those not bonded   
   Status: pass
-- Check Weird Bonds --
   Status: pass
-- Check Number of Units --
   Status: pass
acdoctor mode has completed checking the input file.

Warning: The assigned bond types may be wrong, please :
(1) double check the structure (the connectivity) and/or 
(2) adjust atom valence penalty parameters in APS.DAT, and/or 
(3) increase PSCUTOFF in define.h and recompile bondtype.c
    (be cautious, using a large value of PSCUTOFF (>100) will 
    significantly increase the computation time).
Info: Total number of electrons: 182; net charge: 0

Running: /opt/amber/amber22/bin/sqm -O -i sqm.in -o sqm.out
Info: The number of path atoms exceeded MAXPATHATOMNUM for atom (ID: 11, Name: C7).
      Automatically increasing to 10000.
Info: The number of path atoms exceeded MAXPATHATOMNUM for atom (ID: 13, Name: C9).
      Automatically increasing to 10000.
Info: The number of path atoms exceeded MAXPATHATOMNUM for atom (ID: 16, Name: C12).
      Automatically increasing to 10000.
Info: The number of path atoms exceeded MAXPATHATOMNUM for atom (ID: 26, Name: C20).
      Automatically increasing to 10000.
Info: The number of path atoms exceeded MAXPATHATOMNUM for atom (ID: 27, Name: C21).
      Automatically increasing to 10000.
Info: The number of path atoms exceeded MAXPATHATOMNUM for atom (ID: 28, Name: C22).
      Automatically increasing to 10000.
Info: The number of path atoms exceeded MAXPATHATOMNUM for atom (ID: 29, Name: C23).
      Automatically increasing to 10000.
Info: The number of path atoms exceeded MAXPATHATOMNUM for atom (ID: 30, Name: C24).
      Automatically increasing to 10000.

maria@gcs-hpc:~/Amber/150$ parmchk2 -i ligand.mol2 -f mol2 -o ligand.frcmod
maria@gcs-hpc:~/Amber/150$ tleap
-I: Adding /opt/amber/amber22/dat/leap/prep to search path.
-I: Adding /opt/amber/amber22/dat/leap/lib to search path.
-I: Adding /opt/amber/amber22/dat/leap/parm to search path.
-I: Adding /opt/amber/amber22/dat/leap/cmd to search path.

Welcome to LEaP!
(no leaprc in search path)
> source leaprc.protein.ff19SB
----- Source: /opt/amber/amber22/dat/leap/cmd/leaprc.protein.ff19SB
----- Source of /opt/amber/amber22/dat/leap/cmd/leaprc.protein.ff19SB done
Log file: ./leap.log
Loading parameters: /opt/amber/amber22/dat/leap/parm/parm19.dat
Reading title:
PARM99 + frcmod.ff99SB + frcmod.parmbsc0 + OL3 for RNA + ff19SB
Loading parameters: /opt/amber/amber22/dat/leap/parm/frcmod.ff19SB
Reading force field modification type file (frcmod)
Reading title:
ff19SB AA-specific backbone CMAPs for protein 07/25/2019
Loading library: /opt/amber/amber22/dat/leap/lib/amino19.lib
Loading library: /opt/amber/amber22/dat/leap/lib/aminoct12.lib
Loading library: /opt/amber/amber22/dat/leap/lib/aminont12.lib
> source leaprc.gaff
----- Source: /opt/amber/amber22/dat/leap/cmd/leaprc.gaff
----- Source of /opt/amber/amber22/dat/leap/cmd/leaprc.gaff done
Log file: ./leap.log
Loading parameters: /opt/amber/amber22/dat/leap/parm/gaff.dat
Reading title:
AMBER General Force Field for organic molecules (Version 1.81, May 2017)
> source leaprc.water.opc  
----- Source: /opt/amber/amber22/dat/leap/cmd/leaprc.water.opc
----- Source of /opt/amber/amber22/dat/leap/cmd/leaprc.water.opc done
Loading library: /opt/amber/amber22/dat/leap/lib/atomic_ions.lib
Loading library: /opt/amber/amber22/dat/leap/lib/solvents.lib
Loading parameters: /opt/amber/amber22/dat/leap/parm/frcmod.opc
Reading force field modification type file (frcmod)
Reading title:
Parameters for OPC water (JPCL, 2014, 5 (21), pp 3863-3871)
Loading parameters: /opt/amber/amber22/dat/leap/parm/frcmod.ionslm_126_opc
Reading force field modification type file (frcmod)
Reading title:
Li/Merz ion parameters of atomic ions for the OPC water model (12-6 set)
> prot = loadpdb pro.pdb
Loading PDB file: ./pro.pdb
  total atoms in file: 2941
> fmod = loadamberparams ligand.frcmod
Loading parameters: ./ligand.frcmod
Reading force field modification type file (frcmod)
Reading title:
Remark line goes here
>  lig = loadmol2 ligand.mol2
Loading Mol2 file: ./ligand.mol2
Reading MOLECULE named UNL
> complex = combine {prot lig}
> savepdb complex complex_dry.pdb\
> savepdb complex complex_dry.pdb 

Error: savePdb: Improper number of arguments!
usage:  savePdb <object> <filename>
> complex = combine {prot lig}    
> savepdb complex complex_dry.pdb
Writing pdb file: complex_dry.pdb

Warning:  Converting N-terminal residue name to PDB format: NGLY -> GLY

Warning:  Converting C-terminal residue name to PDB format: CARG -> ARG
> solvatebox complex OPCBOX 15  
  Solute vdw bounding box:              68.631 53.288 43.123
  Total bounding box for atom centers:  98.631 83.288 73.123
  Solvent unit box:                     18.865 18.478 19.006
  Total vdw box size:                   101.606 86.604 76.543 angstroms.
  Volume: 673534.796 A^3 
  Total mass 337374.312 amu,  Density 0.832 g/cc
  Added 17542 residues.
> addions complex Na+ 0

Warning: addIons: 1st Ion & target unit have charges of the same sign:
     unit charge = 6.002; ion1 charge = 1;
     can't neutralize.
> addions complex Cl- 0
6 Cl- ions required to neutralize.
Adding 6 counter ions to "complex" using 1A grid
Grid extends from solute vdw + 4.51  to  10.50
Resolution:      1.00 Angstrom.
Solvent present: replacing closest with ion
	 when steric overlaps occur
Calculating grid charges
(Replacing solvent molecule)
Placed Cl- in complex at (35.86, 11.46, 3.28).
(Replacing solvent molecule)
Placed Cl- in complex at (15.51, 6.91, -13.91).
(Replacing solvent molecule)
Placed Cl- in complex at (30.28, -7.49, 14.34).
(Replacing solvent molecule)
Placed Cl- in complex at (-7.95, -15.19, 11.94).
(Replacing solvent molecule)
Placed Cl- in complex at (33.76, 12.05, -8.21).
(Replacing solvent molecule)
Placed Cl- in complex at (29.38, 5.36, 14.51).

Done adding ions.
> saveamberparm complex complex.prmtop complex.rst7
Checking Unit.

Note: Ignoring the warnings from Unit Checking.

Building topology.
Building atom parameters.
Building bond parameters.
Building angle parameters.
Building proper torsion parameters.
!FATAL ERROR----------------------------------------
!FATAL:    In file [/opt/amber/amber22_src/AmberTools/src/leap/src/leap/unitio.c], line 1955
!FATAL:    Message: 1-4: cannot add bond 2971 2972
This may be caused by duplicate bond specifications;
for example, explicit bond commands in addition to PDB conect records.
!
!ABORTING.
maria@gcs-hpc:~/Amber/150$ s