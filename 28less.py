import numpy as np
import time


def find_subset(items, target):
    if items is None or len(items) == 0 or target < 0:
        return None

    try:
        items = np.array(items, dtype=np.int64)
        k = len(items)

        dp = np.zeros((k + 1, target + 1), dtype=bool)
        dp[0, 0] = True

        for i in range(1, k + 1):
            for j in range(target + 1):
                if dp[i - 1, j]:
                    dp[i, j] = True
                elif j >= items[i - 1] and dp[i - 1, j - items[i - 1]]:
                    dp[i, j] = True

        if not dp[k, target]:
            return None

        subset = []
        i, j = k, target
        while j > 0 and i > 0:
            if j >= items[i - 1] and dp[i - 1, j - items[i - 1]]:
                subset.append(int(items[i - 1]))
                j -= items[i - 1]
            i -= 1

        return subset if subset else None

    except Exception as e:
        print(f"Ошибка при выполнении: {e}")
        return None


if __name__ == "__main__":
    items = [2, 3, 7, 8]
    target = 11

    print(f"Предметы: {items}")
    print(f"Целевая сумма: {target}")

    start_time = time.perf_counter()
    result = find_subset(items, target)
    end_time = time.perf_counter()

    print(f"\nРезультат: {result}")
    print(f"Время выполнения: {end_time - start_time:.6f} сек")