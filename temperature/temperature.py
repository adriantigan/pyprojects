from sys import argv

def K_to_C(temp):
        return temp + 273.15

def C_to_F(temp): 
        return (temp * (9/5)) + 32
K = 286

C = K_to_C(K)

F = C_to_F(C)

