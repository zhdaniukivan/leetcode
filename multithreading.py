# import threading
import threading
import time


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

ti = time.time()

th1 = threading.Thread(target=cal_sqre, args=(arr, ))
th2 = threading.Thread(target=cal_cube, args=(arr, ))
th1.start()
th2.start()
th1.join()
th2.join()

print('Total time take by thread is: ', time.time()-ti)