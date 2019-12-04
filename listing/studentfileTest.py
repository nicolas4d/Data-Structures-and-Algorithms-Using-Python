from studentfile import *
import unittest
import _io

class StudentFileReaderTest(unittest.TestCase):
    def test__init__(self):
        sfr = StudentFileReader("students.txt")
        self.assertEqual(sfr._inputSrc, "students.txt")
        self.assertEqual(sfr._inputFile, None)

    def test_open(self):
        sfr = StudentFileReader("students.txt")
        sfr.open()
        # print(type(sfr._inputFile))
        openedFileType = _io.TextIOWrapper
        #print((isinstance(sfr._inputFile, openedFileType)))
        self.assertEqual(type(sfr._inputFile), openedFileType)
        sfr._inputFile.close()

    def test_close(self):
        sfr = StudentFileReader("students.txt")
        sfr.open()
        # print(type(sfr._inputFile))
        sfr.close()
        # print(sfr)
        self.assertEqual(sfr._inputFile, None)

    def test_fetchRecord(self):
        sfr = StudentFileReader("students.txt")
        sfr.open()
        # print(sfr._inputFile)
        # print(sfr.fetchRecord().idNum)
        self.assertEqual(sfr.fetchRecord().idNum, 10015)
        sfr.close()

    def test_fetchAll(self):
        sfr = StudentFileReader("students.txt")
        sfr.open()
        # print(sfr.fetchAll()[0].idNum)
        self.assertEqual(sfr.fetchAll()[0].idNum, 10015)
        sfr.close()

class StudentRecordTest(unittest.TestCase):
    sr = StudentRecord()

    def test__init__(self):
        self.assertEqual(self.sr.idNum, 0)

unittest.main()
