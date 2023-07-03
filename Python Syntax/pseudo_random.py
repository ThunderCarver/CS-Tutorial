# Talking about the principle of random.seed()



import numpy as np


def functionn(size):
    x = np.random.randint(len(size))
    print(f"x={x}")
    a = determine_no_loop_cell([1, 2, 3], [4, 5, 2, 1])


def determine_no_loop_cell(path, cell_pool):
    np.random.seed(0)
    cell = np.random.choice(cell_pool, 1)[0]
    print(cell)
    # while cell_pool:
    #     cell = np.random.choice(cell_pool, 1)[0]
    #     print(cell)
    #     if cell in path:
    #         cell_pool.remove(cell)
    #     else:
    #         return cell


def queal():
    while True:
        x = [1, 2, 3, 4, 4]
        x = np.random.randint(len(x))
        print(f"x={x}")
        y=[4,5,2,1]
        np.random.seed(0)
        while y:
            cell = np.random.choice(y, 1)[0]
            print(cell)
            if cell in [1, 2, 3]:
                y.remove(cell)
            else:
                break


if __name__ == '__main__1':
    # while True:
    #     x = [1, 2, 3, 4, 4]
    #     functionn(x)
    # p=queal()
    print("ok")
    i = 0
    while i<5:
        x = [1, 2, 3, 4, 4]
        functionn(x)
        i = i+1



if __name__ == '__main__':
    i = 0
    np.random.seed(0)
    while i < 5 :
        o = np.random.randint(5)
        print(f"o={o}")
        # cell = np.random.choice(x, 1)[0]
        cell = np.random.randint(10)
        print(cell)
        i = i+1
    ##################################
    np.random.seed(0)
    m = np.random.randint(10)
    print(m)	
    m = np.random.randint(10)
    print(m)	
    m = np.random.randint(10)
    print(m)	
    print('##################################')
    ##################################
    np.random.seed(0)
    m = np.random.randint(10)
    print(m)
    np.random.seed(0)
    m = np.random.randint(10)
    print(m)
    np.random.seed(0)
    m = np.random.randint(10)
    print(m)
    print('##################################')
    ##################################
    np.random.seed(0)
    for i in range(3):
        m = np.random.randint(10)
        print(m)
    print('##################################')
    ##################################
    for i in range(3):
        np.random.seed(0)
        m = np.random.randint(10)
        print(m)
    print('##################################')

