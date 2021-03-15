from src.CezarFunctions import CezarFunctions
# Unit tests for CezarFunctions made with pytest


def testPrepareString():
    preparedText = CezarFunctions.prepareString('a b. c, d;e f[19290830 GH')
    assert preparedText == 'abcdefgh'


def testMakeMove():
    encryptedText = CezarFunctions.makeMove('abcd', 4)
    assert encryptedText == 'efgh'


def testMakeOppositeMove():
    encryptedText = CezarFunctions.makeMove('efgh', -4)
    assert encryptedText == 'abcd'


def testEncryption():
    sampleText = 'GitHub is built for collaboration.'
    assert CezarFunctions.encryption(sampleText, 15) == 'vxiwjqxhqjxaiudgrdaapqdgpixdc'


def testDecryption():
    sampleText = 'vxiwjqxhqjxaiudgrdaapqdgpixdc'
    assert CezarFunctions.decryption(sampleText, 15) == 'githubisbuiltforcollaboration'


def testFullDecryption():
    result = CezarFunctions.fullDecryption('abcd')
    assumedResult = ['bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl', 'jklm', 'klmn', 'lmno', 'mnop',
                     'nopq', 'opqr',
                     'pqrs', 'qrst', 'rstu', 'stuv', 'tuvw', 'uvwx', 'vwxy', 'wxyz', 'xyza', 'yzab', 'zabc', 'abcd']

    assert result == assumedResult


def testCalculateLettersProbability():
    assert CezarFunctions.calculateLettersProbability('abcd') == 5.034266341020051


def testAutomaticDecryption():
    result = CezarFunctions.automaticDecryption(
        'jllxamrwpcxvhljuldujcrxwbfnanbcruucfxcqxdbjwmyxdwmbbqxacbvjacexljkdujahanujcnmfxambjwmyqajbnb')
    assert result == 'accordingtomycalculationswerestilltwothousandpoundsshortsmartvocabularyrelatedwordsandphrases'
