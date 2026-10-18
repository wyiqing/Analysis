# Create a dedicated Conda environment
conda create -n blast_env -c conda-forge -c bioconda blast -y

# Activate the environment
conda activate blast_env

# Verify the installation
blastp -version
