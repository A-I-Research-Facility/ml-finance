from functools import reduce
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
import time

# Name of file
filename = 'GBPUSD1d.txt'

scriptStartTime = time.time()

date, bid, ask = np.loadtxt(filename, unpack=True, delimiter=',', converters={0: lambda x: mdates.datestr2num(x)})

def percentChange(startPoint, currentPoint):
    try:
        x = ((float(currentPoint) - startPoint)/abs(startPoint)) * 100.0
        if x == 0.0:
            return 0.000000001
        else:
            return x
    except:
        return 0.000000001

def patternStorage():
    patStartTime = time.time()
    x = len(avgLine) - 60
    y = 31
    while y < x:
        pattern = []
        counter = 29

        while counter > 0:
            temp = percentChange(avgLine[y - 30], avgLine[y - counter])
            pattern.append(temp)
            counter -= 1

        outcomeRange = avgLine[y + 20 : y + 30]
        currentPoint = avgLine[y]

        try:
            avgOutcome = (reduce(lambda x, y : x + y, outcomeRange) / len(outcomeRange))
        except:
            print("Exception triggered")
            avgOutcome = 0

        futureOutcome = percentChange(currentPoint, avgOutcome)
        
        patternArr.append(pattern)
        performanceArr.append(futureOutcome)

        y += 1
    
    patEndTime = time.time()
    print (len(patternArr))
    print (len(performanceArr))
    print('Pattern storage took : ', patEndTime - patStartTime, ' seconds')

def currentPattern():
    counter = -30
    while counter < -1:
        temp = percentChange(avgLine[-31], avgLine[counter])
        counter += 1
        pattForRec.append(temp)

    print(pattForRec)

def patternRecognition():
    pattFound = 0
    plotPattArr = []
    
    for pattern in patternArr:
        similarity_1 = 100.0 - abs(percentChange(pattern[0], pattForRec[0]))
        similarity_2 = 100.0 - abs(percentChange(pattern[1], pattForRec[1]))
        similarity_3 = 100.0 - abs(percentChange(pattern[2], pattForRec[2]))
        similarity_4 = 100.0 - abs(percentChange(pattern[3], pattForRec[3]))
        similarity_5 = 100.0 - abs(percentChange(pattern[4], pattForRec[4]))
        similarity_6 = 100.0 - abs(percentChange(pattern[5], pattForRec[5]))
        similarity_7 = 100.0 - abs(percentChange(pattern[6], pattForRec[6]))
        similarity_8 = 100.0 - abs(percentChange(pattern[7], pattForRec[7]))
        similarity_9 = 100.0 - abs(percentChange(pattern[8], pattForRec[8]))
        similarity_10 = 100.0 - abs(percentChange(pattern[9], pattForRec[9]))

        similarity_11 = 100.0 - abs(percentChange(pattern[10], pattForRec[10]))
        similarity_12 = 100.0 - abs(percentChange(pattern[11], pattForRec[11]))
        similarity_13 = 100.0 - abs(percentChange(pattern[12], pattForRec[12]))
        similarity_14 = 100.0 - abs(percentChange(pattern[13], pattForRec[13]))
        similarity_15 = 100.0 - abs(percentChange(pattern[14], pattForRec[14]))
        similarity_16 = 100.0 - abs(percentChange(pattern[15], pattForRec[15]))
        similarity_17 = 100.0 - abs(percentChange(pattern[16], pattForRec[16]))
        similarity_18 = 100.0 - abs(percentChange(pattern[17], pattForRec[17]))
        similarity_19 = 100.0 - abs(percentChange(pattern[18], pattForRec[18]))
        similarity_20 = 100.0 - abs(percentChange(pattern[19], pattForRec[19]))

        similarity_21 = 100.0 - abs(percentChange(pattern[20], pattForRec[20]))
        similarity_22 = 100.0 - abs(percentChange(pattern[21], pattForRec[21]))
        similarity_23 = 100.0 - abs(percentChange(pattern[22], pattForRec[22]))
        similarity_24 = 100.0 - abs(percentChange(pattern[23], pattForRec[23]))
        similarity_25 = 100.0 - abs(percentChange(pattern[24], pattForRec[24]))
        similarity_26 = 100.0 - abs(percentChange(pattern[25], pattForRec[25]))
        similarity_27 = 100.0 - abs(percentChange(pattern[26], pattForRec[26]))
        similarity_28 = 100.0 - abs(percentChange(pattern[27], pattForRec[27]))
        similarity_29 = 100.0 - abs(percentChange(pattern[28], pattForRec[28]))
        similarity_30 = 100.0 - abs(percentChange(pattern[29], pattForRec[29]))

        howSimilar = (similarity_1
                      +similarity_2
                      +similarity_3
                      +similarity_4
                      +similarity_5
                      +similarity_6
                      +similarity_7
                      +similarity_8
                      +similarity_9
                      +similarity_10
                      +similarity_11
                      +similarity_12
                      +similarity_13
                      +similarity_14
                      +similarity_15
                      +similarity_16
                      +similarity_17
                      +similarity_18
                      +similarity_19
                      +similarity_20
                      +similarity_21
                      +similarity_22
                      +similarity_23
                      +similarity_24
                      +similarity_25
                      +similarity_26
                      +similarity_27
                      +similarity_28
                      +similarity_29
                      +similarity_30) / 30.0

        if howSimilar > 70:
            pattdex = patternArr.index(pattern)
            pattFound = 1

            print('Predicted outcome : ', performanceArr[pattdex])
            
            xp = [i for i in range(1, 31)]
            # xp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            #       11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
            #       21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
            plotPattArr.append(pattern)

    if pattFound == 1:
        fig = plt.figure(figsize=(10, 6))

        for pattern in plotPattArr:
            futurePoints = patternArr.index(pattern)

            if performanceArr[futurePoints] > pattForRec[29]:
                pcolor = 'green'
            else:
                pcolor = 'red'

            plt.plot(xp, pattern)
            plt.scatter(35, performanceArr[futurePoints], c=pcolor, alpha=0.4)

        realOutcomeRange = allData[limit + 20 : limit + 30]
        realAvgOutcome = reduce(lambda x, y : x + y, realOutcomeRange) / len(realOutcomeRange)
        realMovement = percentChange(allData[limit], realAvgOutcome)

        plt.scatter(40, realMovement, c='cyan', s=25)

        plt.plot(xp, pattForRec, 'cyan', linewidth = 3)
        plt.grid(True)
        plt.title('Pattern Recognition')
        plt.show()

def graphRawFX():
    fig = plt.figure(figsize = (10, 7))
    ax1 = plt.subplot2grid((40, 40), (0, 0), rowspan = 40, colspan = 40)

    ax1.plot(date, bid)
    ax1.plot(date, ask)

    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)

    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y %H:%M:%S'))
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    ax1_2 = ax1.twinx()
    ax1_2.fill_between(date, 0, (ask-bid), facecolor='g', alpha=0.3)

    plt.subplots_adjust(bottom=0.23)

    plt.grid(True)
    plt.show()

dataLength = int(bid.shape[0])
print("Data length is : ", dataLength)

limit = 37000
allData = ((bid + ask) / 2)

while limit < dataLength:
    avgLine = allData[:limit]

    patternArr = []
    performanceArr = []
    pattForRec = []

    patternStorage()
    currentPattern()
    patternRecognition()

    moveOn = input('press ENTER to continue')

    limit += 1

totalTime = time.time() - scriptStartTime
print("Total processing time : ", totalTime)