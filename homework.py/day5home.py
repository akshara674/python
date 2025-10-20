frontend_students = {"Alice", "Bob", "Charlie"}
backend_students = {"David", "Eve", "Frank"}


backend_students.add("Grace")


frontend_students.remove("Bob") 

both_courses = frontend_students & backend_students
print("Students in both courses:", both_courses)


only_backend = backend_students - frontend_students
print("Students only in Backend:", only_backend)
    


total_students = frontend_students | backend_students
print("Total unique students:", len(total_students))


course_counts = {
    "Frontend": len(frontend_students),
    "Backend": len(backend_students)
}


for course, count in course_counts.items():
    print(f"{course}: {count} students")


course_counts_fullstack = {**course_counts, "Fullstack": len(frontend_students | backend_students)}
print(course_counts_fullstack)