from rdkit import Chem
import os

# Load the main .sdf file
sdf_path = ''
supplier = Chem.SDMolSupplier(sdf_path)

# Get the output directory from the user
output_directory = ''

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Iterate through molecules in the .sdf file
for mol in supplier:
    if mol is not None:
        # Get molecule name from the second column
        molecule_name = mol.GetProp("_Name")
        
        # Save .sdf file in the output directory
        output_sdf_path = os.path.join(output_directory, f'{molecule_name}.sdf')
        writer = Chem.SDWriter(output_sdf_path)
        writer.write(mol)
        writer.close()

print("Splitting complete.")
