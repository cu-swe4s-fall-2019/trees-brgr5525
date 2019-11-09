import sys
import time
import binary_tree as bt
import argparse
sys.path.insert(1, "./hash_tables")
import hash_tables as ht
import hash_functions as hf
sys.path.insert(1, "./avl_tree")
import avl


def main():

    keys = []

    try:
        for l in open(args.dataset):
            keys.append(l.rstrip())
    except FileNotFoundError:
        print('dataset file could not be found')
        sys.exit(1)
    except Exception:
        print('something went wrong with reading the dataset file')
        sys.exit(1)

    t1 = time.time()

    if args.data_structure == 'binary':
        t1 = time.time()

        root = None
        try:
            # insert
            for i in range(len(keys)):
                root = bt.insert(root, keys[i])

            t2 = time.time()

            # search (in database)
            for i in range(args.data_points):
                bt.search(root, keys[i])

            t3 = time.time()

            # search (not in database)
            for i in range(args.data_points):
                # add 's' because the entries were not converted to ints
                bt.search(root, keys[i]+'s')

            t4 = time.time()
        except Exception:
            print('Something went wrong')
            sys.exit(1)

    elif args.data_structure == 'hash':
        t1 = time.time()

        table = ht.ChainedHash(100000, hf.h_rolling)
        try:
            # insert
            for i in range(len(keys)):
                table.add(keys[i], None)

            t2 = time.time()
            # search (in database)
            for i in range(args.data_points):
                table.search(keys[i])

            t3 = time.time()

            # search (not in database)
            for i in range(args.data_points):
                # add 's' because the entries were not converted to ints
                table.search(keys[i]+'s')

            t4 = time.time()
        except Exception:
            print('Something went wrong')
            sys.exit(1)

    elif args.data_structure == 'avl':
        t1 = time.time()

        node = avl.AVL()
        try:
            # insert
            for i in range(len(keys)):
                node.insert(keys[i])

            t2 = time.time()

            # search (in database)
            for i in range(args.data_points):
                node.find(keys[i])

            t3 = time.time()

            # search (not in database)
            for i in range(args.data_points):
                # add 's' because the entries were not converted to ints
                node.find(keys[i]+'s')

            t4 = time.time()
        except Exception:
            print('Something went wrong')
            sys.exit(1)

    else:
        print('--data_structure must be binary, hash, or avl')
        sys.exit(1)

    t_insert = t2-t1
    t_search1 = t3-t2
    t_search2 = t4-t3

    print('Time to insert all data:             ', t_insert)
    print('Time to search for existent keys:    ', t_search1)
    print('Time to search for nonexistent keys: ', t_search2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                description='Input data structrue, data set,' +
                            ' and number of data points',
                prog='insert_key_value_pairs')

    parser.add_argument('--data_structure',
                        type=str,
                        help='Name of the desired data stucture',
                        required=True)
    parser.add_argument('--dataset',
                        type=str,
                        help='Name of file that contains the dataset',
                        required=True)
    parser.add_argument('--data_points',
                        type=int,
                        help='number of data points to use',
                        required=True)

    args = parser.parse_args()

    main()
