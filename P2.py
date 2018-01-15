def main():
    fibValues = [1, 2]
    tsum = 2
    n = 2
    x = 3

    while x <= 4000000:
        fibValues.append(fibValues[n - 1] + fibValues[n - 2])
        x = fibValues[n]
        n += 1
        if x % 2 == 0:
            tsum += x
        # print(n, fibValues[n])
    print(tsum)
    # for i in fibValues:
    #     print(i)

if __name__=='__main__':
    main()