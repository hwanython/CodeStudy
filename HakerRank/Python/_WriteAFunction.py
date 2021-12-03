def is_leap(year):
    # leap = False

    return year % 4 == 0 and (year % 400 == 0 or year % 100 !=0)
    # if year % 100 == 0:
    #     leap = False
    # if year % 4 == 0:
    #     if year % 400 == 0:
    #         # Write your logic here
    #         leap = True
    #
    #     return leap



year = int(input())

print(is_leap(year))