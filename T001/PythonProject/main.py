'''
def top_5_grades(grades):
    result = sorted(grades, reverse=True)
    return result[:5]

def bottom_10_grades(grades):
    result = sorted(grades, reverse=False)
    return result[:10]


grades = [80, 25, 90, 77, 67, 69, 67, 20, 99, 90, 75, 25, 30, 42, 10]
print(top_5_grades(grades))
print(bottom_10_grades(grades))
print(grades)


def sort_grades(grades):
    if sorting == "desc":
        grades.reverse()
    result = sorted(grades)
    return result[:amount_of_grades]


grades =input("Enter grades separated by comma:")
grades = grades.split(",")
sorting = input("Enter sorting order (desc / asc):")

amount_of_grades = int(input("Enter amount of grades:"))
print(sort_grades(grades))



#
# GMT TO GMT + 4 CONVERSION
# 02.11.2026 (Term 1)
#


def gmt_to_gmt4(gmt_time):
    gmt_time = gmt_time.split(":")
    gmt4_hour = (int(gmt_time[0]) + 4) % 24 # Hours +4, but after 23 go to 0
    gmt4_minutes = int(gmt_time[1])
    result = f"{gmt4_hour:02d}:{gmt4_minutes:02d}" # Concattenating hours and numbers and making sure to add a 0 upfront if the number does not have 2 digits
    return result

test_zeit = "22:22"
output = gmt_to_gmt4(test_zeit)
print("Das Ergebnis ist:", output)


'''




