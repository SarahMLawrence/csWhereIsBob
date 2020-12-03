def csSquareAllDigits(n):
    sq_num = ''.join(str(int(num) **2) for num in str(n)) 
    return int(sq_num)
    
