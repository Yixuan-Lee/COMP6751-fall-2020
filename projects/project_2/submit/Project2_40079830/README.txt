------------------------------------------------------------------------------
ReadMe

Assignment number: 2

  Student id,name: 40079830, Yixuan Li

     NLTK version: 3.5

Comments:

There are 2 main files in the code directory:

* main_base.py: base version (use pos tagger and name entity chunker in NLTK)
* main_stan.py: enhanced version (use external StanfordPOSTagger and 
StanfordNERTagger)

There are 2 reports in the report directory:

* P2_Report1_Pipeline.pdf: show the pipeline, modules, limitations, references
* P2_Report2_Demo.pdf: show the result of test cases

In "main_base.py", there are two TODOs. By default, it downloads 
maxent_ne_chunker and words modules in NLTK at the very beginning.

TODO_1: download "maxent_ne_chunker" and "words" modules

TODO_2: change data_path to try different test files.

Note: 
The parse tree diagrams are saved as ".ps" files in the 
"code/results/" direcotry. It is necessary to install ImageMagick and use a 
command to view the saved diagrams. Please see the "V. Appendix" section 
in "P2_Report1_Pipeline.pdf".

External models and jars are put in the "code/stanford/" directory, and 
main_stan.py import the models and jars from the directory.

------------------------------------------------------------------------------