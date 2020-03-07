#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import csv
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
from datetime import datetime, timedelta
import seaborn as sns
from sklearn.cluster import KMeans
from collections import Counter
################################################################
# this function runs the data file analysis work
################################################################
def parseDataLogFile(datafilename):
    ################################################################
    # extract data in the comma seperated data log file (CSV) and save the content in each column into one float-type variable 
    ################################################################
    with open(datafilename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        timestampS = []
        fAccelHwUnit_x = []
        fAccelHwUnit_y = []
        fAccelHwUnit_z = []
        fGyroHwUnit_x = []
        fGyroHwUnit_y = []
        fGyroHwUnit_z = []
        fMagHwUnit_x = []
        fMagHwUnit_y = []
        fMagHwUnit_z = []
        fRPYdeg_r = []
        fRPYdeg_p = []
        fRPYdeg_y = []
        for row in readCSV:
            try:
                x = datetime.strptime(row[0].split(',')[0],'%H:%M:%S.%f')
                timestampS.append(timedelta(hours=x.hour,minutes=x.minute,seconds=x.second,microseconds=x.microsecond).total_seconds())
                fAccelHwUnit_x.append(float(row[1][4:]))
                fAccelHwUnit_y.append(float(row[2]))
                fAccelHwUnit_z.append(float(row[3]))
                fGyroHwUnit_x.append(float(row[4]))
                fGyroHwUnit_y.append(float(row[5]))
                fGyroHwUnit_z.append(float(row[6]))
                fMagHwUnit_x.append(float(row[7]))
                fMagHwUnit_y.append(float(row[8]))
                fMagHwUnit_z.append(float(row[9]))
                fRPYdeg_r.append(float(row[10]))
                fRPYdeg_p.append(float(row[11]))
                fRPYdeg_y.append(float(row[12]))
            except:
                pass
        timestampS = np.asarray(timestampS)
        timestampS = timestampS - timestampS[0]
        fAccelHwUnit_x = np.asarray(fAccelHwUnit_x)
        fAccelHwUnit_y = np.asarray(fAccelHwUnit_y)
        fAccelHwUnit_z = np.asarray(fAccelHwUnit_z)
        fGyroHwUnit_x = np.asarray(fGyroHwUnit_x)
        fGyroHwUnit_y = np.asarray(fGyroHwUnit_y)
        fGyroHwUnit_z = np.asarray(fGyroHwUnit_z)
        fMagHwUnit_x = np.asarray(fMagHwUnit_x)
        fMagHwUnit_y = np.asarray(fMagHwUnit_y)
        fMagHwUnit_z = np.asarray(fMagHwUnit_z)
        fRPYdeg_r = np.asarray(fRPYdeg_r)
        fRPYdeg_p = np.asarray(fRPYdeg_p)
        fRPYdeg_p = fRPYdeg_p - np.mean(fRPYdeg_p)
        fRPYdeg_y = np.asarray(fRPYdeg_y)  

    ################################################################
    # we need accurate estimate of the sampling frequency for precise oscillation period estimate
    ################################################################
    FsHz = getSamplingIntervalS(timestampS)
    ################################################################
    # use pitch component in the attitude heading reference system output for pendulum period analysis
    ################################################################
    analyze_timeSequence(timestampS,fRPYdeg_p,FsHz,'pitch')
    ################################################################
    # use acceleromter raw measurement output for pendulum period analysis
    ################################################################
    analyze_timeSequence(timestampS,fAccelHwUnit_x,FsHz,'accel')
    ################################################################
    # use gyro raw measurement output for pendulum period analysis
    ################################################################
    analyze_timeSequence(timestampS,fGyroHwUnit_y,FsHz,'gyro')
    print('done, congratulations :-)')
    plt.show()
   
################################################################
# in bluetooth communication process, there is a rare chance that the data comm packet could be lost
# we use K-mean to isolate the 20Hz meaurement data from outliers, which are caused by dropped packet 
# dive into "signal and system for more details"
################################################################
def getSamplingIntervalS(timestampS):
    plt.figure()
    sampleIntervalS = np.diff(timestampS)
    sns.distplot(sampleIntervalS)
    plt.ylabel('histogram')
    plt.xlabel('measurement interval(s)')
    clusterCnt = 5
    km = KMeans(n_clusters = clusterCnt)
    km.fit(sampleIntervalS.reshape(-1,1))
    centroids = km.cluster_centers_
    elemCnt = Counter(km.labels_)
    occurrenceCnt = []
    for ii in range(clusterCnt):
        occurrenceCnt.append(elemCnt[ii])
    FsHz = 1/centroids[occurrenceCnt.index(max(occurrenceCnt))]
    return FsHz

################################################################
# use spectrometer, i.e., short time FFT to get the frequency component, peak bin is our best estimate of pendulum oscillation
################################################################
def analyze_timeSequence(timestampS,timeSeqData,FsHz,strComment):
    fig, (ax1, ax2) = plt.subplots(nrows=2)
    ax1.plot(timestampS, timeSeqData, marker='o', markerfacecolor='blue', markersize=2, color='skyblue', linewidth=1)
    ax1.set_title("pendulum time domain measurement -- %s"%strComment)
    ax1.set_xlabel("sampling time(second)")
    ax1.set_ylabel(strComment);
    NFFT = 2048  # the length of the windowing segments

    Pxx, freqs, bins, im = ax2.specgram(timeSeqData, NFFT=NFFT, Fs=FsHz, noverlap=NFFT/2)
    ax2.set_title("Spectrogram")
    ax2.set_xlabel("samples")
    ax2.set_ylabel("frequency(Hz)");

    # The `specgram` method returns 4 objects. They are:
    # - Pxx: the periodogram
    # - freqs: the frequency vector
    # - bins: the centers of the time bins
    # - im: the matplotlib.image.AxesImage instance representing the data in the plot
    pkresult = np.where(Pxx == np.amax(Pxx))
    oscFreqHz = freqs[pkresult[0][0]]
    print('pendulum oscillation Freq(Hz)=%f, Period(Sec)=%f, estimation data source: %s'%(oscFreqHz,1/oscFreqHz,strComment))
    return 1/oscFreqHz

################################################################
# should we run this program independently, i.e., not being called by pendulum1.py,
# we define a default log data file name to be analyzed
################################################################
if __name__ == "__main__":
    defaultFilename = './PendulumTestData.txt'
    import os.path
    if os.path.isfile(defaultFilename):
        parseDataLogFile(defaultFilename)
    else:
        print ("default log file %s not existing"%defaultFilename)
    
