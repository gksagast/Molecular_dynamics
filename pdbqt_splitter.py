import easygui
import subprocess
import os

def split_pdbqt(filename, output_dir):
    # Initialize variables
    run_number = 0
    lines_for_run = []
    writing_run = False

    # Open and read the .pdbqt file
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith("MODEL"):
                run_number += 1
                if writing_run:
                    output_path = f"{output_dir}/run_{run_number - 1}.pdbqt"
                    with open(output_path, 'w') as out_file:
                        out_file.writelines(lines_for_run)
                lines_for_run = []
                writing_run = True

            if line.startswith("ENDMDL"):
                lines_for_run.append(line)
                output_path = f"{output_dir}/run_{run_number}.pdbqt"
                with open(output_path, 'w') as out_file:
                    out_file.writelines(lines_for_run)
                lines_for_run = []
                writing_run = False
                continue

            if writing_run:
                lines_for_run.append(line)

def convert_pdbqt_to_pdb(output_dir, num_files):
    for i in range(1, num_files+1):
        input_file = f"{output_dir}/run_{i}.pdbqt"
        output_file = f"{output_dir}/run_{i}.pdb"
        
        # Use obabel to convert pdbqt file to pdb
        subprocess.run(["obabel", input_file, "-O", output_file])

if __name__ == "__main__":
    # Get the input file path
    input_file_path = easygui.fileopenbox(
        msg="Choose input file", title="Select Input Path", default="*.pdbqt"
    )
    
    # Get the output directory path
    output_dir_path = easygui.diropenbox(
        msg="Choose output directory", title="Select Output Directory"
    )
    
    # Perform the splitting
    if input_file_path and output_dir_path:
        split_pdbqt(input_file_path, output_dir_path)
        
        # Convert to pdb
        convert_pdbqt_to_pdb(output_dir_path, 9)  # Replace 9 with the actual number of files you have.
    else:
        print("Operation cancelled or paths not specified.")
