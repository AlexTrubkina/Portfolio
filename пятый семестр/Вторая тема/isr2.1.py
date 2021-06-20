def fib_num(n_max):

    f_num = 0
    s_num = 1
    seq = [f_num, s_num]

    while(1):
        
        buff = f_num
        f_num = s_num
        s_num = buff + f_num
        
        seq.append(s_num)
        if s_num >= n_max:
            break
    return(seq)
