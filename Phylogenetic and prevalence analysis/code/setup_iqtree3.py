
import subprocess

# Create a dedicated Conda environment and install IQ-TREE 3
subprocess.run([
    "conda", "create", "-n", "iqtree3_env",
    "-c", "conda-forge", "-c", "bioconda",
    "iqtree", "-y"
], check=True)

# Verify installation
subprocess.run([
    "conda", "run", "-n", "iqtree3_env",
    "iqtree3", "--version"
], check=True)

print("IQ-TREE 3 environment setup completed.")
