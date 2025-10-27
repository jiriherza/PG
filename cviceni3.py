# def for_enumerate(iterable, start=0):
#     result = []
#     index = start
#     for el in iterable:
#         result.append((index, el))
#         index += 1
#     return result






# if __name__ == "__main__":
#     text ="abcdef"
#     print(list(enumerate(text, 10)))
#     print(for_enumerate(text, 10))

def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)
    

if __name__ == "__main__":
    print(faktorial(0))
    print(faktorial(1))
    print(faktorial(5))
    print(faktorial(100))
