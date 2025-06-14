import time

def min_coins(n, coins=[25, 10, 5, 1]):
    count = 0
    used = {}

    for coin in coins:
        if n >= coin:
            num = n // coin
            count += num
            used[coin] = num
            n -= coin * num
        if n == 0:
            break

    return count, used


n = 63
start_time = time.perf_counter()
count, used = min_coins(n)
end_time = time.perf_counter()

print(f"Сумма: {n} коп.")
print(f"Минимальное количество монет: {count}")
print("Использованные монеты:")
for coin, num in used.items():
    print(f"{coin} коп.: {num} шт.")
print(f"Время выполнения: {(end_time - start_time) * 1000:.4f} мс")