#!/bin/python3
import numpy
import math
import argparse

argparser = argparse.ArgumentParser(prog = "sigen.py", description = "Generate sinus wave(s) (or their linear combination)", epilog="Copyright 2022 (c) Michał Gibas");

argparser.add_argument("filename", help="Path to the output file")
argparser.add_argument("-f", "--freq", nargs="+", type=float, required=True, help="Frequency(ies) in Hz of the sinus waves to be generated")
argparser.add_argument("-n", "--nsamples", type=int, help="Number of samples to be generated", required=True)
argparser.add_argument("-sr", "--sampling-rate", type=float, help="Sampling rate of the generated signal", required=True)

args = argparser.parse_args()

fs = args.sampling_rate

time = numpy.linspace(0.0, args.nsamples / fs, args.nsamples)

output = numpy.sin(time * numpy.pi * args.freq[0])

for freq in args.freq[1::]:
    sinwave = numpy.sin(time * numpy.pi * freq)
    output = numpy.add(output, sinwave)


with open(args.filename, "w") as file:
    for value in output:
        file.write(str(value))
        file.write("\n");
