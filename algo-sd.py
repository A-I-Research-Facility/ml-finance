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
        while counter >= 0:
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
    # print (len(patternArr))
    # print (len(performanceArr))
    print('Pattern storage took : ', patEndTime - patStartTime, ' seconds')

def currentPattern():
    counter = -30
    while counter < 0:
        temp = percentChange(avgLine[-31], avgLine[counter])
        counter += 1
        pattForRec.append(temp)

    # print(pattForRec)

def patternRecognition():
    pattFound = 0
    plotPattArr = []
    
    for pattern in patternArr:
        counter = 0
        similarSum = 0
        while counter < 30:
            temp = 100.0 - abs(percentChange(pattern[counter], pattForRec[counter]))
            counter += 1
            similarSum += temp

        howSimilar = similarSum / 30.0

        if howSimilar > 70:
            pattdex = patternArr.index(pattern)
            pattFound = 1

            # print('Predicted outcome : ', performanceArr[pattdex])
            
            xp = [i for i in range(1, 31)]
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