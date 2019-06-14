#!/usr/bin/python3
#
# wavtoopx: convert wav to OPZ or OP1 sample/synth bank
# Copyright (C) 2019 Nathan Fraser
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import sys
import soundfile as sf

# Constants
VERSION = '1.0.0'

def main():
    parser = argparse.ArgumentParser(
                description='Convert an audio file to OP-1/OP-Z sample file.')
    parser.add_argument('infile',
                        type=argparse.FileType('rb'),
                        help='input audio file')
    parser.add_argument('outfile',
                        nargs='?',
                        help='OP-1/OP-Z AIFF output file',
                        default=sys.stdout) 
    ## set channel in source

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-d','--drum',action='store_true',
                       help='set the type to drum')
    group.add_argument('-s','--sampler',action='store_true',
                       help='set the type to sampler')
    parser.add_argument('-r', '--randomise',
                        action='store_true',
                        help='randomise all parameters')
    parser.add_argument('-c','--channel', type=int, default=1,
                        help='specify input channel number')
    parser.add_argument('-o','--offset', type=float,
                        help='set the start offset (seconds)')
    parser.add_argument('-l','--length', type=float,
                        help='truncate the length (seconds)')
    parser.add_argument('-v', '--version',
                        action='version',
                        help='print version',
                        version='%(prog)s ' + VERSION)
    args = parser.parse_args()

    infile = sf.SoundFile(args.infile)
    print('opened: ' + repr(args.infile.name))
    print('channels: ' + repr(infile.channels))
    print('samplerate: ' + repr(infile.samplerate))
    print('format: ' + repr(infile.format))
    print('        ' + repr(infile.format_info))
    print('subtype: ' + repr(infile.subtype))
    print('        ' + repr(infile.subtype_info))
    print('endian: ' + repr(infile.endian))
    print('sections: ' + repr(infile.sections))
    print('name: ' + repr(infile.name))
    print('extra_info: \n\n' + infile.extra_info)

if __name__ == '__main__':
    main()
