import subprocess

# Create a dedicated Conda environment and install IQ-TREE 2
subprocess.run([
    "conda", "create", "-n", "iqtree2_env",
    "-c", "conda-forge", "-c", "bioconda",
    "iqtree", "-y"
], check=True)

# Verify installation
subprocess.run([
    "conda", "run", "-n", "iqtree2_env",
    "iqtree2", "--version"
], check=True)

print("IQ-TREE 2 environment setup completed.")
