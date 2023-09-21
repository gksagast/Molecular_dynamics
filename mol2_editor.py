import easygui
import sys

def rename_molecule(input_file, output_file, new_molecule_name):
    with open(input_file, 'r') as f:
        content = f.readlines()

    with open(output_file, 'w') as f:
        atom_section = False
        skip_next_line = False

        for line in content:
            # Skip the line if it's marked to be skipped (for the asterisks)
            if skip_next_line:
                skip_next_line = False
                continue

            # Detect the start of the @<TRIPOS>MOLECULE section
            if line.startswith('@<TRIPOS>MOLECULE'):
                f.write(line)
                f.write(new_molecule_name + '\n')
                skip_next_line = True  # Set to skip the next line (asterisks)
                atom_section = False
                continue

            # Detect the start of the @<TRIPOS>ATOM section
            elif line.startswith('@<TRIPOS>ATOM'):
                f.write(line)
                atom_section = True
                continue
            
            # Handle renaming in the ATOM section
            if atom_section:
                split_line = line.split()
                if len(split_line) > 7 and split_line[7] == "UNL1":
                    line = line.replace("UNL1", new_molecule_name)
            
            # Write the processed line to the output
            f.write(line)

if __name__ == "__main__":
    input_filepath = easygui.fileopenbox("Select the input .mol2 file")
    if input_filepath is None:
        sys.exit("No input file selected. Exiting.")
        
    output_filepath = easygui.filesavebox("Select the output .mol2 file")
    if output_filepath is None:
        sys.exit("No output file selected. Exiting.")
        
    new_molecule_name = easygui.enterbox("Enter the new molecule name")
    if new_molecule_name is None:
        sys.exit("No new molecule name entered. Exiting.")
        

    rename_molecule(input_filepath, output_filepath, new_molecule_name)
