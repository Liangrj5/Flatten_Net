import argparse
# import template

parser = argparse.ArgumentParser(description='EDSR and MDSR')


parser.add_argument('--cfg', dest='cfg_file', required=True,
                    help='Config file for training (and optionally testing)')

parser.add_argument('--set', dest='set_cfgs',
                    help='Set config keys. Key value sequence seperate by whitespace.'
                    'e.g. [key] [value] [key] [value]',
                    default=[], nargs='+')

parser.add_argument('--no_cuda', dest='cuda', 
     help='Do not use CUDA device', action='store_false')



parser.add_argument('--device_ids',help='list of gpu device',
     nargs='+', default=[0,1,2,3,4,5,6,7], type=int)



parser.add_argument('--bs', dest='batch_size',
   help='Explicitly specify to overwrite the value comed from cfg_file.',
   type=int)

parser.add_argument('--nw', dest='num_workers',
        help='Explicitly specify to overwrite number of workers to load data. Defaults to 4',
        type=int)

parser.add_argument('--optimizer', dest='optimizer', help='Training optimizer.',   default=None)
parser.add_argument('--lr', 
     help='Base learning rate.',default=None, type=float)
parser.add_argument('--lr_decay_gamma',
     help='Learning rate decay rate.',default=None, type=float)

parser.add_argument('--epochs', type=int, default=100,
                    help='number of epochs to train')

parser.add_argument('--name', default=None, type=str)

parser.add_argument(
        '--debug', dest='debug', action='store_true')

args = parser.parse_args()



