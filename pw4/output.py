def listStudents(manager):
    for s in manager.students:
        print(s.toString())

def listCourses(manager):
    for c in manager.courses:
        print(c.toString())

def listMarks(manager):
    cid = input("Course ID: ")
    if cid not in manager.marks:
        print("No marks.")
        return

    for s in manager.students:
        print(
            f"{s.getName()}: {manager.marks[cid].get(s.getId(), 'N/A')}"
        )

def sortByGPA(manager):
    data = []
    for s in manager.students:
        gpa = manager.calculateGPA(s.getId())
        if gpa is not None:
            data.append((s.getId(), s.getName(), gpa))

    data.sort(key=lambda x: x[2], reverse=True)
    for sid, name, gpa in data:
        print(f"{sid} | {name} | GPA: {gpa}")
