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

To run the program download the tutorial data from the repository.  
Load the files into demultiplexer.  
Load the primerset containing the information for the dataset.  
New primersets can be costumized for your needs with the create primerset button.  
Create a new tagging scheme with the loaded files and select all combinations used in your dataset.  
Fill in the samples in the tagging scheme.  
Hit the demultiplex button. If needed the tags can be removed from the sequences.  
