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

When the primerset is saved demultiplexer will show the path where it's saved. All primersets will be saved in demultiplexer's data folder.

![](https://github.com/DominikBuchner/demultiplexer/blob/main/tutorial_data/pics/Primerset%20saved.PNG?raw=true)

Now it's time to create a tagging scheme. All information that is needed to demultiplex the dataset is in there. It's a plain excel file
that contains information about all samples combined with all primer combinations. To create a tagging scheme enter the number of primer combinations
used and click on "Create tagging scheme". A new window will pop up.

![](https://github.com/DominikBuchner/demultiplexer/blob/main/tutorial_data/pics/Tagging%20scheme%20generator.PNG?raw=true)

When the tagging scheme is saved demultiplexer will also show the path where it's saved. All tagging scheme will be saved in demultiplexer's data folder.

![](https://github.com/DominikBuchner/demultiplexer/blob/main/tutorial_data/pics/Tagging%20scheme%20saved.PNG?raw=true)

It can be selected via file browse and then opened via the "Modify selected scheme button". In the tagging scheme the file paths of all input files, the detected
file names as well as all selected primer combinations are displayed. Simply enter the sample names you want demultiplexer to create (e.g. 1a - 10d) and save the tagging scheme.

![](https://github.com/DominikBuchner/demultiplexer/blob/main/tutorial_data/pics/Tagging%20scheme.PNG?raw=true)

One the tagging scheme is saved and an output folder is selected the demultiplexing can be started. The tags may be removed during demultiplexing, depending on your application.
If inline barcodes where used they can be removed but if the demultiplexing is done primer-wise they can be kept, since primer/adapter removal is usually done within the
subsequent data processing steps.

## GUI based processing
Once everything is set just click the "Demultiplex" button. Demultiplexer will use all but one available cores.

![](https://github.com/DominikBuchner/demultiplexer/blob/main/tutorial_data/pics/Output%20GUI.PNG?raw=true)

## Commandline usage via Python API
If you set up all files needed for demultiplexer via the GUI you can move them anywhere. Remember to change the filepaths of the files to demultiplex in the tagging
scheme. In this example the path files are stored on an ubuntu server and the paths were changed accordingly.
