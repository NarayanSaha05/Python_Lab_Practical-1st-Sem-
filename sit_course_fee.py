def CalculateSITcourseFees(course_code, TIGans, entrance_test, male):
    # Step 1: Assign fees based on course code
    if course_code == 1:
        course_name = "BTech"
        sem = 8
        admission_fee = 100000
        remaining_fee = 75000
        level = "UG"
    elif course_code == 2:
        course_name = "BCA"
        sem = 8
        admission_fee = 70000
        remaining_fee = 50000
        level = "UG"
    elif course_code == 3:
        course_name = "BBA"
        sem = 8
        admission_fee = 70000
        remaining_fee = 50000
        level = "UG"
    elif course_code == 4:
        course_name = "BHHA"
        sem = 6
        admission_fee = 60000
        remaining_fee = 45000
        level = "UG"
    elif course_code == 5:
        course_name = "BSc"
        sem = 6
        admission_fee = 50000
        remaining_fee = 30000
        level = "UG"
    elif course_code == 6:
        course_name = "MBA"
        sem = 4
        admission_fee = 140000
        remaining_fee = 100000
        level = "PG"
    elif course_code == 7:
        course_name = "MCA"
        sem = 4
        admission_fee = 120000
        remaining_fee = 80000
        level = "PG"
    else:
        print("Invalid course code")
        return


    if TIGans == 1: 
        if level == "UG":
            admission_fee -= 10000
            remaining_fee -= 10000
        else: 
            admission_fee -= 15000
            remaining_fee -= 15000
        total = admission_fee + (sem - 1) * remaining_fee
    else:
        total = admission_fee + (sem - 1) * remaining_fee

        # Entrance test scholarship (only if not TIGan)
        if entrance_test == 1:
            total -= 15000

        # Female scholarship (only if not TIGan)
        if male == 0:
            total -= 10000

    print("Course Name:", course_name)
    print("Total Course Fees: ₹", format(total, ",.2f"))


CalculateSITcourseFees(1, 1, 0, 1) 
