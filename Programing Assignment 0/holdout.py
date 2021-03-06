# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 23:26:46 2020

@author: Pree T.
@email: pree.t@cmu.ac.th
This program is to demonstrate the numpy and the concept of the
simple hold out sampling method.

"""
import sys
import numpy as np


def toydata(row, col):
    
    print('Creating a toy dataset...')
    ind = np.random.randint(100, size=(row, col))
    dep = arr1 = np.random.randint(2,size=(row, 1))
    indexer = np.arange(row)

    arr = np.append(ind, dep, axis=1)
    arr = np.concatenate((indexer[:, np.newaxis], arr), axis=1)
    return arr

def holdout(arr, test_size, shuffle, **random):
    print('Performing a simple hold-out method..')
    print('shuffle state is', shuffle)
    print('random state is', random)
    
    random = random.pop('random', None)
    
    if test_size >= 0.5 or test_size < 0 :
        print('Error: test size can not be less than 50% and below 0')
        sys.exit(1)
        
    elif random and shuffle:
        np.random.seed(random)
        np.random.shuffle(arr)
        
    elif shuffle:
        np.random.shuffle(arr)
    r, c = arr.shape    
    
    train_size = int(r - (r*test_size));
    train = arr[0:train_size, 0:c-1]
    train_y = train[:,-1]  
    test =  arr[train_size:, 0:c-1]
    test_y = test[:, -1]

    return train, train_y, test, test_y
    
def main(argv):
    if len(argv) != 4:
        print ('Error: wrong number of arguments.')
        sys.exit(1)
    rows = int(argv[0])
    cols = int(argv[1])
    shuffle = int(argv[2])
    seed = int(argv[3])
    
    arr = toydata(rows, cols)
    print('array shape is:\n', arr.shape)
    print('Top 5 row is:\n', arr[:5])
    print('Buttom 5 row is:\n', arr[-5:])
    print()
    train, train_y, test, test_y = holdout(arr, 0.2, shuffle, random=seed)
    
    print('After the simple holdout method:')
    
    print('Training set:')
    print('top 5 row(train) is:\n', train[0:5])
    print('buttom 5 row(train) is:\n', train[-5:])
    print('top 5 row(train_y) is:\n', train_y[:5])
    print('buttom 5 row(train_y) is:\n', train_y[-5:])
    print()
    
    print('Testing set:')
    print('top 5 row(test) is:\n', test[0:5])
    print('buttom 5 row(test) is:\n', test[-5:])
    print('top 5 row(test_y) is:\n', test_y[:5])
    print('buttom 5 row(test_y) is:\n', test_y[-5:])
    print()
    
    print('train shape:', train.shape)
    print('train_y shape:' ,train_y.shape)
    print('test shape', test.shape)
    print('test_y shape', test_y.shape)
    return train, train_y, test, test_y
if __name__ == "__main__":
     main(sys.argv[1:])
    
print('program terminated properly.')