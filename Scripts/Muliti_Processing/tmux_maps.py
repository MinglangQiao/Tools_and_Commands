## this is a demo scripts, print 0-1000 unsing N tmux windows at the same time

import subprocess
import argparse
import sys


def parse_args():
    # hyper-parameters 
    parser = argparse.ArgumentParser(
        description='mutli task')

    parser.add_argument('--cmd', choices=['train', 'test'], default='test')
    parser.add_argument('--workers', default=1, type=int, metavar='N',
                        help='number of data loading workers (default: 4 )') # Metavar: It provides a different name for optional argument in help messages.
    parser.add_argument('--start', default=0, type=int, metavar='S',
                        help='start index of the sequences') # Metavar: It provides a different name for optional argument in help messages
    parser.add_argument('--end', default=1, type=int, metavar='E',
                        help='end index of the sequences') # Metavar: It provides a different name for optional argument in help messages.
    parser.add_argument('--i_worker', default=1, type=int, metavar='i',
                        help='worker index of the sequences') # Metavar: It provides a different name for optional argument in help messages.

    args = parser.parse_args()

    return args

def test_function(worker, start, end):
    
    ## print funtion
    for i in range(start, end):
        print('>>>>>>>>now running worker: {}, i: {} in [{}, {}]'.format(worker, i, start, end))

def main():
    
    args = parse_args()

    if len(sys.argv) == 1:
        
        print('>>>>>>>>>>>>> Run in 1 workerflow !')
    elif len(sys.argv) == 2:
        # python tmux_mps.py --workers=4
        print('>>>>>>>>>>>>> Initialzation, workers_num: {}'.format(args.workers))

        ## using tmux to impliment mutiprocesing
        subprocess.call(['tmux new -s task -d'], shell=True)
        subprocess.call(["tmux rename-window -t 'task:0' task_0"], shell=True)

        Num_workers = args.workers

        Num_total_len = 1000
        num_images_of_each_session = int(Num_total_len/Num_workers) 

        for i_worker in range(Num_workers):

            if i_worker < (Num_workers - 1):

                one_session_start = i_worker * num_images_of_each_session
                one_session_end = (i_worker + 1) * num_images_of_each_session
            elif i_worker == (Num_workers - 1):

                one_session_start = i_worker * num_images_of_each_session
                one_session_end = Num_total_len-1

            ## create new window
            if i_worker > 0:
                create_new_window_command = "tmux neww -a -n task_%d -t task"%i_worker
                subprocess.call([create_new_window_command], shell=True)

            session_command = ("tmux send -t 'task:task_%d' 'python tmux_maps.py --start=%d --end=%d --i_worker=%d\n' "%(i_worker,
                               one_session_start, one_session_end, i_worker))
            subprocess.call([session_command], shell=True)

    elif len(sys.argv) == 4:
        # python tmux_mps.py --S 
        i_worker = args.i_worker
        one_session_start = args.start
        one_session_end = args.end

        test_function(i_worker, one_session_start, one_session_end)

    else:
        print(t)

    # print(sys.argv, args.workers)
    


if __name__ == "__main__":
    main()

    ## frequently used command 
    # python tmux_mps.py --workers=4
    # tmux attach -t task
    # tmux kill-session -t task