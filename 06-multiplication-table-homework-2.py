# 1) 사용자로부터 몇 단을 출력할 지 맏을 것
# 2) 해당 단을 곱하기 1에서 곱하기 9까지 실행할 것
# 3) 해당 단의 제한두기 (2단~9단)
# 4) 무한루프

dan = int(input("몇 단을 출력하시겠습니까?"))
while (dan):
    if dan < 2:
        print("2단부터 입력가능합니다")
        dan = int(input("몇 단을 출력하시겠습니까?"))

    elif dan >= 10:
        print("9단까지 입력 가능합니다")
        dan = int(input("몇 단을 출력하시겠습니까?"))

    else :
        for num in range(1, 10):
            print("{} * {} = {}".format(dan, num, dan * num))
        dan = int(input("몇 단을 출력하시겠습니까?"))
