def getMaximumGenerated(n: int):
    """Сложность алгоритма - O(n), т.к. один цикл

    Args:
        n (int): целочисленное значение.

    Returns:
        max(nums) - возвращает максимальное целое число в массиве nums.
    """
    if not n: 
        return 0
    nums = [0, 1]
    for i in range(2, n+1):
        if i % 2 == 0:
            nums.append(nums[i//2])
        else:
            nums.append(nums[(i-1)//2]+ nums[(i+1)//2])
    
    return max(nums)