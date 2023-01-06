import argparse
import givenData
import numpy as np


def get_args_heuristic():
    parser = argparse.ArgumentParser(description='Heuristic function arguments')

    parser.add_argument('--evaluation-episodes', type=int, default=10, metavar='N', help='Number of episodes evaluated')
    parser.add_argument('--load-dataset', action='store_true',
                        help='Load an existing dataset, otherwise the data is generated on the fly')
    parser.add_argument('--dataset-path', type=str, help='The path to load dataset')
    parser.add_argument('--heuristic', type=str, default='OnlineBPH', help='Options: LSAH DBL MACS OnlineBPH HM BR RANDOM')

    args = parser.parse_args()
    args.container_size = givenData.container_size
    args.item_size_set = givenData.item_size_set
    args.evaluate = True

    args.internal_node_length = 6
    if args.evaluate:
        args.num_processes = 1
    args.normFactor = 1.0 / np.max(args.container_size)

    return args
