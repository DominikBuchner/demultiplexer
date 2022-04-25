# demultiplexer
Demultiplexer is a python script to demultiplex Illumina reads that are tagged in addition to the index reads.
This could be different primers sequenced on one lane or additional inline tags combined with index reads.
Demultiplexer takes demultiplexed (by index read) files as input and searches for patterns at the beginning
and/or end of the reads and outputs as many files as there are provided in the sample sheet.

Demultiplexer can be run via GUI or as a commandline tool. It will run on all major operating systems
since it's programmed in pure python.

## Installation
To install:

`pip install demultiplexer`

To update:

`pip install --upgrade demultiplexer`

## How to use
We highly recommend creating the input files via the GUI since it makes things really easy.
To run demultiplexer on a server simply move all files there and then call demultiplexer via
the commandline interface.

To start all files to demultiplex have to be loaded by demultiplexer. In the tutorial data
there are 20 gzipped fastq files that will be used in this tutorial.
Taking a look at "1_r1.fastq.gz" different tags can be recognized:

![](https://github.com/DominikBuchner/demultiplexer/blob/main/tutorial_data/pics/file%20preview.PNG?raw=true)

Tag 5: TCTCA, Tag 6: AGCTA, Tag 1: CTGT, Tag 9: GTCCTA.
The reverse reads are tagged in a similar manner. All files in the tutorial dataset share those tags and can be seperated by demultiplexer.

To do so, the dataset has to be loaded into demultiplexer. Files can be selected via the filebrowse button. After selection the files have to be loaded.
Demutliplexer will automatically find all files pairs of forward and reverse reads as long as the are seperated by an equal ending (e.g. _r1 - _r2; 1 - 2; A - B).

![](https://github.com/DominikBuchner/demultiplexer/blob/main/tutorial_data/pics/loaded%20files.PNG?raw=true)

When the files are loaded a primersets has to be created which contains all needed information about the tagging. Primer sets will be saved and can be reused,
so that a specific primerset only needs to be created once. 4 primers were used for the tutorial dataset. A new window to enter the primer information will pop up
when clicking "Create primer set".

![](https://github.com/DominikBuchner/demultiplexer/blob/main/tutorial_data/pics/primer%20generator.PNG?raw=true)

To run the program download the tutorial data from the repository.  
Load the files into demultiplexer.  
Load the primerset containing the information for the dataset.  
New primersets can be costumized for your needs with the create primerset button.  
Create a new tagging scheme with the loaded files and select all combinations used in your dataset.  
Fill in the samples in the tagging scheme.  
Hit the demultiplex button. If needed the tags can be removed from the sequences.  
