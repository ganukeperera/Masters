from general import General
from academic import Academic
from student import Student

def main():
    # student = Student("123", "John", "SID_125")
    # student.display_info()

    # acedemic = Academic("322", "Acedemic James", "A_34222", "AT_34234", "Publications")
    # acedemic.display_info()

    # general = General("g_6234", "g_12311", "s_6342212", "t_5223334", "23 per hour")
    # general.display_info()


    student = Student("123", "John", "SID_125")
    student.greet()

if __name__ == "__main__":
    main()