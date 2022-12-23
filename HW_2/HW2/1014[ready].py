from typing import List

def maxScoreSightseeingPair(self, values: List[int]):
    """Сложность - O(n) - т.к. один цикл

    Args:
        values (List[int]): список с "рейтингом" достопримечательностей,
                            а разница индексов между ними - расстояние.

    Returns:
        result: максимальная оценка (с учетом "рейтинга" и расстояния по
        условию values[i] + values[j] + i - j) паре достопримечательностей.
    """
    current_max = values[0]
    result = 0
    for i in range(1,len(values)):
        result = max(result,current_max+values[i]-i)
        current_max = max(current_max,values[i]+i)
    return result

