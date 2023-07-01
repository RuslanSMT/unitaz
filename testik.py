hobot = tail = foot = ear = eye = mouth = 0
count = 0
while True:
    n = int(input())
    s = input()
    if s == 'ОБЕД':
        break
    if s == "хобот":
        hobot += n
    elif s == "хвост":
        tail += n
    elif s == "нога":
        foot += n
    elif s == "ухо":
        ear += n
    elif s == "глаз":
        eye += n
    elif s == "рот":
        mouth += n
    if hobot > 0 and tail > 0 and foot >= 4 and ear >= 2 and eye >= 2 and mouth >= 1:
        while hobot > 0 and tail > 0 and foot >= 4 and ear >= 2 and eye >= 2 and mouth >= 1:
            count += 1
            hobot -= 1
            tail -= 1
            foot -= 4
            ear -= 2
            eye -= 2
            mouth -= 1
        print('Есть слон!')
        print(count)
        break
if count == 0:
    print("Какие-то слоны целые. Пошли обедать.")
