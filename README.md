# Read_Imaris_zstack
Python scripts to read Imaris outputs in csv format, it generates csv files containing the respective dendrite volume and branch level data for the analyzed cells. 

Imaris generates two .csv files for each z-stack, containing the respective dendrite volume and branch level data for the analyzed cells. 
For each z-stack .csv file, run the scripts DendrditeVolume.py and DendriteBranchLevel.py as follows:

    - python3 DendriteScript.py pathtocsvfile1 pathtocsvfile2 pathtocsvfile3 …to select specific sample’s outputs for comparison.
    - python3 DendriteScript.py pathtocsvfolder/* to analyze all samples located in a folder together.
    - In case no input files are supplied, the script will try to analyze all csv files located in the script’s path.
    
This will output the total dendrite volume (Dendrite Volume) and the total number of branches for each level (DendriteBranchLevel) for the same microglial cell (Filament ID). 

The Dendrite Volume output shows in the first line the name of the .csv file. Under it, there are two columns; the first displays the ID of the microglial cell, and the second represents the total sum of the dendrite volume.

The Dendrite Branch Level output also shows in the first line the name of the .csv file. Below, the second line represents the Filament ID of the microglial cell. Then, the column of the left represents the Branch Level (being 1 the first ramification from the soma), and the one next to the number of branches for that level.
