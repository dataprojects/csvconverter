**csvconverter**

--------------------------


The package is used to convert the anonymised_search.log file 
to csv format. After the conversion a user gets three csv files contained
in the directory called data:


 data/::
 
         query.csv
         filters.csv
         user.csv



*Usage:*

1. Download and extract the csvconverter package to the local directory

2. Open the directory where you extracted  the project. 

3. Into command line enter:

    $ tree

you have to see the project structure as follows::


		.
		├── csvconverter
		│   ├── cleaner.py
		│   ├── converters.py
		│   ├── csvwriter.py
		│   ├── data
		│   │   └── readme.txt
		│   ├── distributor.py
		│   ├── filestructures.py
		│   ├── __init__.py
		│   └── log
		│       └── anonymised_search.log
		├── csvconverter.py
		├── MANIFEST.in
		└── README.rst



4. The project directory contaisn the file csvconverter.py

5. Run the program from the command line:

    $ python3.4 csvconverter.py

