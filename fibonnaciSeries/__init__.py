def fibonacci_series_iterative(n):
    """
    Generates the first 'n' Fibonacci numbers using an iterative approach.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        series = [0, 1]
        for _ in range(2, n):
            next_num = series[-1] + series[-2]
            series.append(next_num)
        return series