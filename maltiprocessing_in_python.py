import time
import multiprocessing


def cal_sqre(num):
    print('calculate the square root of the given number')
    for n in num:
        time.sleep(0.3)
        print('Square is : ', n * n)


def cal_cube(num):
    print('calculate the cube root of the given number')
    for n in num:
        time.sleep(0.3)
        print('Cube is :', n * n * n)


arr = [1, 2, 3, 4, 5]
arr2 = [5, 4, 3, 2, 1]

ti = time.time()

p1 = multiprocessing.Process(target=cal_sqre,  args=(arr, ))
p2 = multiprocessing.Process(target=cal_sqre, args=(arr2, ))
p1.start()
p2.start()
p1.join()
p2.join()



print('Total time take by thread is: ', time.time()-ti)