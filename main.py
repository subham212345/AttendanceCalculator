import math


def attendance(total_class, missed_class):
    print("You need to have a minimum of 75% of attendance to be eligible to sit in the exam.")
    attended_class = total_class - missed_class
    print(f"You have attended {attended_class} classes out of {total_class} classes.")
    attended_class = (attended_class / total_class) * 100
    print("Your attendance is ","{:.2f}".format(attended_class))

    if attended_class > 75:
        class_required = math.ceil((75*total_class)/100)
        minimum_class = total_class - class_required
        if minimum_class == 0:
            print("You can not miss anymore classes.")
        else:
            print(f"You can miss {minimum_class} classes.")

    elif attended_class == 75:
        print("You can not miss anymore classes.")

    elif attended_class < 75:
        # factor is calculated based on minimum attendance, since 100-75= 25. so factor = 100/25 = 4
        # if minimum attendance was 85%, then 100- 85 = 15, then factor = 100/15
        factor = 4
        tot_can_miss = missed_class * factor
        class_required = tot_can_miss - total_class
        print(f"You need to attend {class_required} classes to get minimum attendance.")


tot_class = int(input("Enter the total number of classes: "))
miss_class = int(input("Enter the number of classes you have missed so far: "))
attendance(tot_class, miss_class)

