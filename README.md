# asthma-tech-guide
## Table of Contents
| Table of Contents |
|------------|
| 1. [Overview](#overview)|
| 2. [Requirements](#requirements)|
| 3. [Setting Up the Environment](#setting-up-the-environment)|
| 4. [Updating the Environment](#updating-the-environment)|

## Overview
The guide aims to enable both clinicians and laypersons to explore the topic of Social Determinants of Health (SDOH) and their correlation with asthma exacerbation.
It uses Python with `conda` for environment management.

## Requirements
- [Anaconda](https://www.anaconda.com/products/individual) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) installed.

## Setting Up the Environment

To recreate the Conda environment with all the necessary dependencies, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/leeleetan88/asthma-tech-guide.git
   cd asthma-tech-guide
   ```
2. **Create the Conda environment from the environment.yml file:**
   ```bash
   conda env create -f environment.yml
   ```
3. **Activate the environment:**
   ```bash
   conda activate geo_env
   ```

## Updating the Environment
If you make changes to your environment (such as installing new packages), you can update the environment.yml file:
```bash
conda env export --no-builds > environment.yml
```

Others can then update their environment to match the changes by running:
```bash
conda env update -f environment.yml
```

