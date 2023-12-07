import unittest

from main_function import *


class TestLicensePlateDetection(unittest.TestCase):
    def setUp(self):
        # Load an image for testing
        self.test_image_path = 'dataset/test/0418.jpg'
        self.test_image = cv2.imread(self.test_image_path, 1)

    def test_findLP_img(self):
        result_image = findLP_img(self.test_image)
        # Add assertions based on the expected result
        self.assertIsNotNone(result_image)
        # Add more assertions if needed

    def test_detect(self):
        plate_number = detect(self.test_image)
        # Add assertions based on the expected result
        self.assertIsInstance(plate_number, str)
        # Add more assertions if needed

    def test_sortNumber(self):
        # Add test cases for the sortNumber function
        # Ensure that the function returns a string
        # Ensure that the sorted string is correct based on known input
        sorted_string = sortNumber()
        self.assertIsInstance(sorted_string, str)
        # Add more assertions if needed

    def test_takeSecond(self):
        # Add test cases for the takeSecond function
        # Ensure that the function sorts tuples correctly based on the second element
        example_list = [(1, 5), (2, 3), (3, 8)]
        sorted_list = sorted(example_list, key=takeSecond)
        self.assertEqual(sorted_list, [(2, 3), (1, 5), (3, 8)])
        # Add more assertions if needed

    def test_takeFirst(self):
        # Add test cases for the takeFirst function
        # Ensure that the function sorts tuples correctly based on the first element
        example_list = [(1, 5), (2, 3), (3, 8)]
        sorted_list = sorted(example_list, key=takeFirst)
        self.assertEqual(sorted_list, [(1, 5), (2, 3), (3, 8)])
        # Add more assertions if needed

    def test_takeChar(self):
        # Add test cases for the takeChar function
        # Ensure that the function sorts tuples correctly based on the third element
        example_list = [(1, 5, 'b'), (2, 3, 'a'), (3, 8, 'c')]
        sorted_list = sorted(example_list, key=takeChar)
        self.assertEqual(sorted_list, [(2, 3, 'a'), (1, 5, 'b'), (3, 8, 'c')])
        # Add more assertions if needed

    def test_compare_results(self):
        # Test to compare detected results with actual results
        actual_plate_number = '69C118915'
        img, plate_num = findLP_img(self.test_image)
        # Compare the detected plate number with the actual plate number
        self.assertEqual(actual_plate_number, plate_num)


if __name__ == '__main__':
    unittest.main()
