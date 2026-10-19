
import subprocess

# Create a dedicated Conda environment and install MAFFT
subprocess.run([
    "conda", "create", "-n", "mafft_env",
    "-c", "conda-forge", "-c", "bioconda",
    "mafft", "-y"
], check=True)

# Verify installation
subprocess.run([
    "conda", "run", "-n", "mafft_env",
    "mafft", "--version"
], check=True)

print("MAFFT environment setup completed.")
