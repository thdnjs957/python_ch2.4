count = 1
while count < 11:
    print(count, end=' ')
    if count == 5:
        break
    count += 1
else: # 루프가 다 정상적으로 돌면
    print('ok')

# break, continue, else문 적용
i = 0
while i < 10:
    i += 1
    if i < 5:
        continue
    if i > 10:
        break

    print(i, end=' ')
else:
    print('ok')

# 무한루프
i = 0
while True:
    if i > 5:
        break
    print(i, end=' ')
    i += 1
else:
    print('end else')