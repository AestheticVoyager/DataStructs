# DomirScire
from stack import Stack
# Push remainders to the stack and then pop the stack off and you'll get the binary value of the integer

def div_by_2(dec_num):
    s = Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2

    bin_num = ''
    while not s.is_empty():
        bin_num += str(s.pop())
    return bin_num

if __name__ == "__main__":
    print(div_by_2(242))
