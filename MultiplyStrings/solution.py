def solution(num1, num2):
    if num1 == '0' or num2 == '0':
        return '0'

    def decode(num):
        ans = 0
        for i in num:
            ans = ans*10 +(ord(i) - ord('0'))
        return ans

    def encode(s):
        news = ''
        while s:
            a = s % 10
            s = s // 10
            news = chr(ord('0') + a) + news
        return news

    return encode(decode(num1)*decode(num2))

if __name__ == "__main__":
    print(solution("20","1000")) # insert input in the quotes
    print(solution("123","456"))
