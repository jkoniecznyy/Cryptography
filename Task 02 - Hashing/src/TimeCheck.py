import timeit
from src.HashFunctions import HashFunctions
import plotly.graph_objects as go


class TimeCheck:

    def __init__(self):
        pass

    @staticmethod
    def fullTimeCheck(cleartext: bytes, nr: int):
        names = HashFunctions.getAlgorithmNames()
        times = []
        times.append(timeit.timeit(lambda: HashFunctions.blake2bHashing(cleartext), number=nr))
        times.append(timeit.timeit(lambda: HashFunctions.blake2sHashing(cleartext), number=nr))
        times.append(timeit.timeit(lambda: HashFunctions.md5Hashing(cleartext), number=nr))
        times.append(timeit.timeit(lambda: HashFunctions.sha1Hashing(cleartext), number=nr))
        times.append(timeit.timeit(lambda: HashFunctions.sha224Hashing(cleartext), number=nr))
        times.append(timeit.timeit(lambda: HashFunctions.sha256Hashing(cleartext), number=nr))
        times.append(timeit.timeit(lambda: HashFunctions.sha384Hashing(cleartext), number=nr))
        times.append(timeit.timeit(lambda: HashFunctions.sha3224Hashing(cleartext), number=nr))
        times.append(timeit.timeit(lambda: HashFunctions.sha3256Hashing(cleartext), number=nr))
        times.append(timeit.timeit(lambda: HashFunctions.sha3384Hashing(cleartext), number=nr))
        times.append(timeit.timeit(lambda: HashFunctions.sha3512Hashing(cleartext), number=nr))
        times.append(timeit.timeit(lambda: HashFunctions.sha512Hashing(cleartext), number=nr))
        times.append(timeit.timeit(lambda: HashFunctions.shake128Hashing(cleartext, 20), number=nr))
        times.append(timeit.timeit(lambda: HashFunctions.shake256Hashing(cleartext, 20), number=nr))
        return [names, times]

    @staticmethod
    def manualFullTimeCheck():
        print('Type the text to be hashed for testing')
        content = bytes(input(), encoding='utf8')
        if not content:
            content = b'Awwwhh yaaaach! - Bob Marley on hash.'
        fullTime = TimeCheck.fullTimeCheck(content, 10)
        for i in range(len(fullTime[0])):
            print(f'{i} Name: {fullTime[0][i]}, time: {fullTime[1][i]}')

    @staticmethod
    def drawTimeToLengthGraph(data, numberOfExecutions):
        length = []
        time = []

        for content in data:
            length.append(len(content))
            fullTime = TimeCheck.fullTimeCheck(content, numberOfExecutions)
            timeSum = 0
            for i in range(len(fullTime[0])):
                timeSum += fullTime[1][i]
            time.append(timeSum)

        fig = go.Figure(data=go.Bar(x=length, y=time))
        fig.write_html('timeLengthGraph.html', auto_open=True)
