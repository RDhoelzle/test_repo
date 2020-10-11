#!/usr/bin/env python3
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
__maintainer__ = 'Michael Imelfort'
__script_name__ = 'NAME ME'
__version__ = '0.0.1'
__profiling__ = False
import argparse
import sys
import gzip
import os
def do_work( args ):
    seq_number = 1
    with open(args.out_filename, 'a') as out_fh:
        with gzip.open(args.filename, 'rt') as fh:
            for line in fh:
                if line.startswith('>'):
                    # line_fields = line.rstrip()[:1].split(' ')
                    # ">dhjkgfsdj fdlhjfsl f ffdsfsd"
                    # ["dhjkgfsdj", "fdlhjfsl", "f", "ffdsfsd"]
                    line = line.rstrip()[:1]
                    gtid = os.path.basename(args.filename).replace('_genomic.fna.gz', '')
                    out_fh.write('>%s_%s\n' % (gtid, seq_number))
                    seq_number+=1
                else:
                    out_fh.write(line)
    return 0
###############################################################################
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='Input file to parse')
    parser.add_argument('out_filename', help='File to write to')
    #-------------------------------------------------
    # get and check options
    args = None
    if(len(sys.argv) == 1):
        parser.print_help()
        sys.exit(0)
    elif(sys.argv[1] == '-v' or \
         sys.argv[1] == '--v' or \
         sys.argv[1] == '-version' or \
         sys.argv[1] == '--version'):
        print('%s: version: %s' % (__script_name__, __version__))
        sys.exit(0)
    elif(sys.argv[1] == '-h' or \
         sys.argv[1] == '--h' or \
         sys.argv[1] == '-help' or \
         sys.argv[1] == '--help'):
        parser.print_help()
        sys.exit(0)
    else:
        args = parser.parse_args()
    try:
        if(__profiling__):
            import cProfile
            import pstats
            cProfile.run('do_work(args)', 'prof')
            p = pstats.Stats('prof')
            p.sort_stats('cumulative').print_stats(10)
            p.sort_stats('time').print_stats(10)
        else:
            do_work(args)
    except:
        print('Unexpected error:', sys.exc_info()[0])
        raise
