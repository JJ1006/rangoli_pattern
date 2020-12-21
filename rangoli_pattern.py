import string
def print_rangoli(n):
    width = 4 * n - 3
    alpha = string.ascii_lowercase
    for i in list(range(n))[::-1] + list(range(1, n)):
        print('-'.join(alpha[n-1:i:-1] + alpha[i:n]).center(width, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)