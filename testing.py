from plagiarism_detection import PlagiarismDetection
import unittest


class TestPlagiarismDetection(unittest.TestCase):
    """
    Unit Tests for functions get_plagiarized_percentage(), get_phrase_map(),
    word_to_synonym(), and to_lowercase_alphas().

    Three tests are made for each unit test.
    """

    test_path = "testfiles/"  # Path to folder with all test files
    pass_file = "pass.txt"    # File mocks Source, Target, and Synonyms file.

    def test_get_plagiarized_percentage(self):
        tests = [
            ("testfile1_1.txt", "testfile2_1.txt", "testsyns_1.txt", 3, 50.0),
            ("testfile1_2.txt", "testfile2_2.txt", "testsyns_2.txt", 1, 80.0),
            ("testfile1_3.txt", "testfile2_3.txt", "testsyns_3.txt", 5, 100.0),
        ]
        for index, test in enumerate(tests):
            PD = PlagiarismDetection(self.test_path+test[0],
                                     self.test_path+test[1],
                                     self.test_path+test[2],
                                     test[3])
            actual = round(PD.get_plagiarized_percentage(), 2)
            expected = round(test[4], 1)
            self.assertEqual(expected, actual,
                             "Plagiarize Percentage not matching" +
                             " for test in index: " + str(index))

    def test_get_phrase_map(self):
        tuples = [
            [("tuple1"), ("tuple2")],
            [("just"), ("test"), ("here")],
            []
        ]
        expected_maps = [
            {("tuple1"): True, ("tuple2"): True},
            {("just"): True, ("test"): True, ("here"): True},
            {}
        ]
        tests = [
            (tuples[0], expected_maps[0]),
            (tuples[1], expected_maps[1]),
            (tuples[2], expected_maps[2])
        ]

        pass_path = self.test_path + self.pass_file
        PD = PlagiarismDetection(pass_path, pass_path, pass_path)

        for index, test in enumerate(tests):
            actual = PD.get_phrase_map(test[0])
            expected = test[1]
            self.assertEqual(expected, actual, "Not getting correct "
                             + "tuple map for test at index: " + str(index))

    def test_word_to_synonym(self):
        tests = [
            ("testsyns_1.txt", "sprint", "run"),
            ("testsyns_2.txt", "nickname", "name"),
            ("testsyns_3.txt", "nothere", "nothere")
        ]

        pass_path = self.test_path + self.pass_file

        for index, test in enumerate(tests):
            PD = PlagiarismDetection(pass_path, pass_path,
                                     self.test_path+test[0])
            actual = PD.word_to_synonym(test[1])
            expected = test[2]
            self.assertEqual(expected, actual, "Word to synonym not "
                             + "matching for test at index: " + str(index))

    def test_to_lowercase_alphas(self):
        tests = [
            ("Hello!!!", "hello"),
            (".!#@@!!!...A..!#", "a"),
            ("goodbye", "goodbye")
        ]
        pass_path = self.test_path + self.pass_file
        PD = PlagiarismDetection(pass_path, pass_path, pass_path)
        for index, test in enumerate(tests):
            actual = PD.to_lowercase_alphas(test[0])
            expected = test[1]
            self.assertEqual(expected, actual, "To lowercase alphas not "
                             + "matching for test at index: " + str(index))
