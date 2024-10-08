def manage_courses():

    courses = {
        "CSE101": {"Course name": "Introduction to Programming", "Credits": 3, "Instructor": "Dr. Alice"},
        "CSE102": {"Course name": "Data Structures", "Credits": 4, "Instructor": "Dr. Bob"},
        "CSE103": {"Course name": "Database Systems", "Credits": 3, "Instructor": "Dr. Carol"}
    }
    
    courses["CSE102"]["Instructor"] = "Dr. Bob Jr."
    
    courses["CSE104"] = {"Course name": "Algorithms", "Credits": 4, "Instructor": "Dr. Dave"}
    
    del courses["CSE101"]
    
    for course_code, details in courses.items():
        print(f"Course Code: {course_code}")
        for key, value in details.items():
            print(f"  {key}: {value}")
    return courses

manage_courses()