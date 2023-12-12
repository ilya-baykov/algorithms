def triangle_check(side_1: int, side_2: int, side_3: int) -> str:
    if side_1 + side_2 > side_3 and side_1 + side_3 > side_2 and side_3 + side_2 > side_1:
        return 'YES'
    return 'NO'
