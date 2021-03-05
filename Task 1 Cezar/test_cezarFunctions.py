from cezarFunctions import *


def testPrepareString():
    preparedText = prepareString('a b. c, d;e f[19290830 GH')
    assert preparedText == 'abcdefgh'


def testMakeMove():
    encryptedText = makeMove('abcd', 4)
    assert encryptedText == 'efgh'


def testEncryption():
    sampleText = 'GitHub is built for collaboration.'
    assert encryption(sampleText, 15) == 'vxiwjqxhqjxaiudgrdaapqdgpixdc'


def testDecryption():
    sampleText = 'vxiwjqxhqjxaiudgrdaapqdgpixdc'
    assert decryption(sampleText, 15) == 'githubisbuiltforcollaboration'


def testFullDecryption():
    result = fullDecryption('abcd')
    assumedResult = ['bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl', 'jklm', 'klmn', 'lmno', 'mnop', 'nopq', 'opqr',
     'pqrs', 'qrst', 'rstu', 'stuv', 'tuvw', 'uvwx', 'vwxy', 'wxyz', 'xyza', 'yzab', 'zabc', 'abcd']

    assert result == assumedResult


def testCalculateLettersProbability():
    assert calculateLettersProbability('abcd') == 5.034266341020051


def testAutomaticDecryption():
    result = automaticDecryption('jllxamrwpcxvhljuldujcrxwbfnanbcruucfxcqxdbjwmyxdwmbbqxacbvjacexljkdujahanujcnmfxambjwmyqajbnb')
    assert result == 'accordingtomycalculationswerestilltwothousandpoundsshortsmartvocabularyrelatedwordsandphrases'
