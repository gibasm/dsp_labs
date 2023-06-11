#!/bin/python3
from matplotlib import pyplot
import numpy
import sys
import argparse
import csv


def load_ecg_data(filename : str) -> list:
    ecg_data = []

    with open(args.filename, 'r') as file:
        line = file.readline()
        row = list(filter(lambda x : x != '', line.split(" ")))
        for val in row:
            ecg_data.append([float(val)])

        for line in file:
            row = list(filter(lambda x : x != '', line.split(" ")))
            for col_idx in range(0, len(row)):
                ecg_data[col_idx].append(float(row[col_idx]))
    
    return ecg_data


def plot_ecg_with_t(samples : list, time : list):
    fig, ax = pyplot.subplots()
    ax.plot(time, samples)
    ax.set_xlabel("t[s]")
    ax.set_ylabel("V", rotation = 0)
    pyplot.show()


def plot_ecg(samples : list, fs : int):
    t_stop = len(samples) / float(fs)
    t = numpy.linspace(0.0, t_stop, len(samples))
    
    plot_ecg_with_t(samples, t)    
    


argparser = argparse.ArgumentParser(prog = "ecg.py", description = "Utility script for plotting ECG signals", epilog="Copyright 2022 (c) Michał Gibas");

argparser.add_argument("filename", help="Path to the file containing the ecg samples")
argparser.add_argument("-sr", "--sampling-rate", type=int, default=300, help="Sampling rate in Hz for selected ecg signal")
argparser.add_argument("-t", action="store_true", help="Treat the first column as values on the time axis")
argparser.add_argument("-ch", "--channel", type=int, default=0, help="Channel to select from the ecg sample file")

args = argparser.parse_args()


data = load_ecg_data(args.filename)

if args.t:
    plot_ecg_with_t(data[args.channel+1], data[0])
else:
    plot_ecg(data[args.channel], args.sampling_rate)
