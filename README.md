<h1>Plagiarism Detection Command-Line Tool</h1>
<br>
************************
<h3>Description</h3>
************************

The algo performs plagiarism detection using a N-tuple comparison algorithm allowing for synonyms in the text.

The program takes in 3 required arguments, and one optional.  In other cases such as no arguments, the program prints out usage instructions.

1) file name for a list of synonyms

2) input file 1

3) input file 2

4) (optional) the number N, the tuple size.  If not supplied, the default should be N=3.


The synonym file has lines each containing one group of synonyms.  For example a line saying "run sprint jog" means these words should be treated as equal.

The input file1 should be declared plagiarized based on the number of N-tuples in file1 that appear in file2 (in other words we are looking for tuples in file1 that matches a source (file2) against which we are checking the percentage of plagarism in file1), where the tuples are compared by accounting for synonyms as described above.  For example, the text "go for a run" (file1) has two 3-tuples, ["go for a", "for a run"] both of which appear in the text "go for a jog" (file2).

The output of the program should be the percent of tuples in file1 which appear in file2.  So for the above example, the output would be one line saying "100%".  In another example, for texts "go for a run" and "went for a jog" and N=3 we would output "50%" because only one tuple in the first text appears in the second one.

************************
<h3>Requirements</h3>
************************

This program should be executed with Python 2.7. 

************************
<h3>How to Run it</h3>
************************

Run the script by typing in the command line:<br>

```
python app.py -f filepath1 filepath2 -s synspath -t tuplesize
```
The flag -f will be responsible for getting the string input file path of file1 and file2, the -s flag will be responsible for the file path of synonyms.txt, and the OPTIONAL -t flag will be responsible for taking in the integer for the tuple size. 

Example: <br>
```
python app.py -f file1.txt file2.txt -s syns.txt -t 3
```

or
<br>
```
python app.py -f file1.txt file2.txt -s syns.txt
```
<br>
************************
<h3>How to Test it</h3>
************************

To test run 

```
python -m unittest testing
```

This is not the complete unit testing of all the functions. It covers 4 functions.

- get_plagiarized_percentage
- get_phrase_map
- word_to_synonym
- to_lowercase_alphas

Only doing partial testing for the whole class just for some presentation for this Assignment for TripAdvisor. 


************************
<h3>Algorithm</h3>
************************

1) Create a HashMap with all the possible synonyms as key with the value of its FIRST respective synonym.

Example: "run sprint jog"<br>
```
{
    "sprint": "run",
    "run": "run",
    "jog": "run"
}
```

2) Create a HashMap will all the N sized tuples as key of file1 (source file). During this process, before creating each tuple, check if the words are in the synonyms HashMap. If so, change word for its HashMap value. 

This will save us a lot of computing when checking the 2nd file. We know all the possible synonyms will be their first respective synonym and we won't need to check for others. 

Example: "go for a jog"<br>
```
{
    ("go", "for", "a"): True,
    ("for", "a", "run"): True
} 
```

3) Create a list of N sized tuples representing file2 (target file). Just as Step 2, have the Synonyms HashMap to check if any of the words is a synonym. If any of them are, change it to its corresponding value.

Example: "went for a sprint"<br>
```
[("went","for","a"), ("for","a","run")]
```

4) Iterate through the list representing the target file and check if the tuple is in the HashMap representing the source file. Count the total amount of 'hits' we get in this process. 

Example:
```
HashMap Representing Source File

{
    ("go", "for", "a"): True,
    ("for", "a", "run"): True
}

List Representing Target File

[("went","for","a"), ("for","a","run")]

```
Since ("for", "a", "run") are in both, but ("went","for","a") is not in the HashMap, our total amount of hits is 1. 

5) Divide the total amount of hits by the length of the list representing the Target File. Multiply the result by 100. Make any of the variables float to get the decimal percentage.

Example: 
```
plagiarized_percentage = (float(total_amount_of_hits) / length_of_list) * 100
```
************************
<h3>Assumptions</h3>
************************
1) The class will throw Exception if N (tuple size) is bigger than the word size of file2

2) The Synonyms text file must be correctly formatted. It won't throw an error but it might not give the right substitutions if is not in the line by line format as stated. 
