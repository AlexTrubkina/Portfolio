from itertools import takewhile

def fib_num(n_max):

    f_num = 0
    s_num = 1
    seq = [f_num, s_num]

    while(s_num < n_max):
        
        buff = f_num
        f_num = s_num
        s_num = buff + f_num
        
        seq.append(s_num)
    =
    return(seq)

seq = fib_num(200)


ans = list(takewhile(lambda x: x < 10, seq))
