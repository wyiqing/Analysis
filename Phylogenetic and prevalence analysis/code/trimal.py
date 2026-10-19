
import subprocess

# Create a dedicated Conda environment and install trimAl
subprocess.run([
    "conda", "create", "-n", "trimal_env",
    "-c", "conda-forge", "-c", "bioconda",
    "trimal", "-y"
], check=True)

# Verify installation
subprocess.run([
    "conda", "run", "-n", "trimal_env",
    "trimal", "-h"
], check=True)

print("trimAl environment setup completed.")
