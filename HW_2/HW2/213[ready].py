from typing import List

def rob(nums: List[int]):
    """Сложность - O(n), т.к. один цикл

    Args:
        nums (List[int]): получаем целочисленный массив с кол-вом денег 
        в каждом доме

    Returns:
        max(sub_rob(nums[:-1]), sub_rob(nums[1:])): с помощью подфункции
        sub_rob мы ходим по домам так, чтобы не поставить на уши мусоров,
        однако дома стоят в кольце, поэтому первый и последний элемент массива - 
        это рядомстоящие дома. Чтобы исключить возможность попадания двух крайних
        элементов массива в вывод, мы ищем максимальное значение от двух
        ограниченных подфункций.
    """
    if len(nums) == 1:
        return nums[0]
    def sub_rob(nums):
        house_1, house_2 = 0, 0
        for i in nums:
            temp = max(i + house_1, house_2)
            house_1 = house_2
            house_2 = temp
        return house_2
    
    return max(sub_rob(nums[:-1]), sub_rob(nums[1:]))
