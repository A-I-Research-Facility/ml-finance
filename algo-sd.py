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
        p1 = percentChange(avgLine[y - 30], avgLine[y - 29])
        p2 = percentChange(avgLine[y - 30], avgLine[y - 28])
        p3 = percentChange(avgLine[y - 30], avgLine[y - 27])
        p4 = percentChange(avgLine[y - 30], avgLine[y - 26])
        p5 = percentChange(avgLine[y - 30], avgLine[y - 25])
        p6 = percentChange(avgLine[y - 30], avgLine[y - 24])
        p7 = percentChange(avgLine[y - 30], avgLine[y - 23])
        p8 = percentChange(avgLine[y - 30], avgLine[y - 22])
        p9 = percentChange(avgLine[y - 30], avgLine[y - 21])
        p10 = percentChange(avgLine[y - 30], avgLine[y - 20])

        p11 = percentChange(avgLine[y - 30], avgLine[y - 19])
        p12 = percentChange(avgLine[y - 30], avgLine[y - 18])
        p13 = percentChange(avgLine[y - 30], avgLine[y - 17])
        p14 = percentChange(avgLine[y - 30], avgLine[y - 16])
        p15 = percentChange(avgLine[y - 30], avgLine[y - 15])
        p16 = percentChange(avgLine[y - 30], avgLine[y - 14])
        p17 = percentChange(avgLine[y - 30], avgLine[y - 13])
        p18 = percentChange(avgLine[y - 30], avgLine[y - 12])
        p19 = percentChange(avgLine[y - 30], avgLine[y - 11])
        p20 = percentChange(avgLine[y - 30], avgLine[y - 10])

        p21 = percentChange(avgLine[y - 30], avgLine[y - 9])
        p22 = percentChange(avgLine[y - 30], avgLine[y - 8])
        p23 = percentChange(avgLine[y - 30], avgLine[y - 7])
        p24 = percentChange(avgLine[y - 30], avgLine[y - 6])
        p25 = percentChange(avgLine[y - 30], avgLine[y - 5])
        p26 = percentChange(avgLine[y - 30], avgLine[y - 4])
        p27 = percentChange(avgLine[y - 30], avgLine[y - 3])
        p28 = percentChange(avgLine[y - 30], avgLine[y - 2])
        p29 = percentChange(avgLine[y - 30], avgLine[y - 1])
        p30 = percentChange(avgLine[y - 30], avgLine[y])

        outcomeRange = avgLine[y + 20 : y + 30]
        currentPoint = avgLine[y]

        try:
            avgOutcome = (reduce(lambda x, y : x + y, outcomeRange) / len(outcomeRange))
        except:
            print("Exception triggered")
            avgOutcome = 0

        futureOutcome = percentChange(currentPoint, avgOutcome)
        
        pattern.append(p1)
        pattern.append(p2)
        pattern.append(p3)
        pattern.append(p4)
        pattern.append(p5)
        pattern.append(p6)
        pattern.append(p7)
        pattern.append(p8)
        pattern.append(p9)
        pattern.append(p10)

        pattern.append(p11)
        pattern.append(p12)
        pattern.append(p13)
        pattern.append(p14)
        pattern.append(p15)
        pattern.append(p16)
        pattern.append(p17)
        pattern.append(p18)
        pattern.append(p19)
        pattern.append(p20)

        pattern.append(p21)
        pattern.append(p22)
        pattern.append(p23)
        pattern.append(p24)
        pattern.append(p25)
        pattern.append(p26)
        pattern.append(p27)
        pattern.append(p28)
        pattern.append(p29)
        pattern.append(p30)
        
        patternArr.append(pattern)
        performanceArr.append(futureOutcome)

        y += 1
    
    patEndTime = time.time()
    print (len(patternArr))
    print (len(performanceArr))
    print('Pattern storage took : ', patEndTime - patStartTime, ' seconds')

def currentPattern():
    currPatt_1 = percentChange(avgLine[-31], avgLine[-30])
    currPatt_3 = percentChange(avgLine[-31], avgLine[-29])
    currPatt_4 = percentChange(avgLine[-31], avgLine[-28])
    currPatt_2 = percentChange(avgLine[-31], avgLine[-27])
    currPatt_5 = percentChange(avgLine[-31], avgLine[-26])
    currPatt_6 = percentChange(avgLine[-31], avgLine[-25])
    currPatt_7 = percentChange(avgLine[-31], avgLine[-24])
    currPatt_8 = percentChange(avgLine[-31], avgLine[-23])
    currPatt_9 = percentChange(avgLine[-31], avgLine[-22])
    currPatt_10 = percentChange(avgLine[-31], avgLine[-21])

    currPatt_11 = percentChange(avgLine[-31], avgLine[-20])
    currPatt_12 = percentChange(avgLine[-31], avgLine[-19])
    currPatt_13 = percentChange(avgLine[-31], avgLine[-18])
    currPatt_14 = percentChange(avgLine[-31], avgLine[-17])
    currPatt_15 = percentChange(avgLine[-31], avgLine[-16])
    currPatt_16 = percentChange(avgLine[-31], avgLine[-15])
    currPatt_17 = percentChange(avgLine[-31], avgLine[-14])
    currPatt_18 = percentChange(avgLine[-31], avgLine[-13])
    currPatt_19 = percentChange(avgLine[-31], avgLine[-12])
    currPatt_20 = percentChange(avgLine[-31], avgLine[-11])

    currPatt_21 = percentChange(avgLine[-31], avgLine[-10])
    currPatt_22 = percentChange(avgLine[-31], avgLine[-9])
    currPatt_23 = percentChange(avgLine[-31], avgLine[-8])
    currPatt_24 = percentChange(avgLine[-31], avgLine[-7])
    currPatt_25 = percentChange(avgLine[-31], avgLine[-6])
    currPatt_26 = percentChange(avgLine[-31], avgLine[-5])
    currPatt_27 = percentChange(avgLine[-31], avgLine[-4])
    currPatt_28 = percentChange(avgLine[-31], avgLine[-3])
    currPatt_29 = percentChange(avgLine[-31], avgLine[-2])
    currPatt_30 = percentChange(avgLine[-31], avgLine[-1])

    pattForRec.append(currPatt_1)
    pattForRec.append(currPatt_2)
    pattForRec.append(currPatt_3)
    pattForRec.append(currPatt_4)
    pattForRec.append(currPatt_5)
    pattForRec.append(currPatt_6)
    pattForRec.append(currPatt_7)
    pattForRec.append(currPatt_8)
    pattForRec.append(currPatt_9)
    pattForRec.append(currPatt_10)

    pattForRec.append(currPatt_11)
    pattForRec.append(currPatt_12)
    pattForRec.append(currPatt_13)
    pattForRec.append(currPatt_14)
    pattForRec.append(currPatt_15)
    pattForRec.append(currPatt_16)
    pattForRec.append(currPatt_17)
    pattForRec.append(currPatt_18)
    pattForRec.append(currPatt_19)
    pattForRec.append(currPatt_20)

    pattForRec.append(currPatt_21)
    pattForRec.append(currPatt_22)
    pattForRec.append(currPatt_23)
    pattForRec.append(currPatt_24)
    pattForRec.append(currPatt_25)
    pattForRec.append(currPatt_26)
    pattForRec.append(currPatt_27)
    pattForRec.append(currPatt_28)
    pattForRec.append(currPatt_29)
    pattForRec.append(currPatt_30)

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