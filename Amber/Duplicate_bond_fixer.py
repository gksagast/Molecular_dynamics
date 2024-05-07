from pdbfixer import PDBFixer
from openmm.app import PDBFile

def fix_pdb(file_path):
    # Initialize PDBFixer with the given PDB file
    fixer = PDBFixer(filename=file_path)

    # Find missing residues and add them
    fixer.findMissingResidues()
    fixer.findMissingAtoms()
    fixer.addMissingAtoms()

    # Optionally remove heterogens
    fixer.removeHeterogens(keepWater=False)

    # Save the fixed PDB file
    output_path = file_path.replace('.pdb', '_fixed.pdb')
    with open(output_path, 'w') as f:
        PDBFile.writeFile(fixer.topology, fixer.positions, f)

    print(f"Fixed PDB saved to {output_path}")

if __name__ == "__main__":
    path_to_pdb = '/home/maria/Amber/Carlo_test/Shc1-PTB_1OY2.pdb'  # Update this path
    fix_pdb(path_to_pdb)
