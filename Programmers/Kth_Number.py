def solution(array, commands):
    answer = []

    for cmds in commands:
        arr_crop = array[cmds[0]-1:cmds[1]]
        crop_sort = sorted(arr_crop)
        answer.append(crop_sort[cmds[2]-1])
    return answer


print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

