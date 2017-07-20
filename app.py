from argparse import *
from plagiarism_detection import PlagiarismDetection


def main():
    """ Creates Arguments -f to accept 2 files and -s to accept 1 file, both
    as required arguments. Optional -t for tuple size is also added as an
    argument.

    Creates a Plagiarism Detection class with given files and information and
    calls and prints the plagiarized percentage of file 2 compared to file 1.
    All having in perspective the possible synonyms. """

    parser = ArgumentParser(description='Plagiarism Detection Command-Line Tool')

    parser.add_argument('-f', '-file', required=True, nargs=2,
                        metavar=('File1', 'File2'), type=FileType('r'),
                        help='Pass FilePath1 and FilePath2 after -f')

    parser.add_argument('-s', '-syns', required=True, metavar='Synonyms_Path',
                        type=FileType('r'), help='Pass SynonymsPath after -s')

    parser.add_argument('-t', '-tuple', type=int, metavar='Tuple_Size',
                        help='Pass TupleSize after -t')

    parser = parser.parse_args()

    [file1, file2] = parser.f
    syns = parser.s
    tuple_size = parser.t

    plagiarism = PlagiarismDetection(file1.name, file2.name, syns.name,
                                     tuple_size)

    print "Welcome to the Plagiarism Detection Command-Line Tool\n"

    print "File Path 1:\t", file1.name
    print "File Path 2:\t", file2.name
    print "Synonyms Path:\t", syns.name

    # tuple_size is None when there is no -t used to give a custom tuple size.
    if tuple_size is None:
        print "Tuple Size:\t", PlagiarismDetection.DEFAULT_PHRASE_SIZE
    else:
        print "Tuple Size:\t", tuple_size

    print "\nPercentage Plagiarized\n"

    print "%.2f%% of File 2(%s) was plagiarized from File 1(%s)\n" % \
        (plagiarism.get_plagiarized_percentage(), file2.name, file1.name)


if __name__ == '__main__':
    main()
