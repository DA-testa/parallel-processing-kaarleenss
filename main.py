# python3
    


def parallel_processing(n, m, data):
    

    output = []
    a = 0
    zeros = [0] * n
    # max = int(m//n) + 0.5
    for i in range(-(-m//n)):
        # print(i)
        for j in range(n):
            # print(j)
            output.append((j, i))
            zeros[j] = zeros[j] + data[a]
            a = a + 1
            if a >= m:
                break
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    text = list(map(int, input().split()))
    n = text[0]
    m = text[1]
    # print(n, m)

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))
    if(len(data) > m):
        print("invalid input")
    
    # print(data)

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for x, y in result:
        print(x, y)


if __name__ == "__main__":
    main()
