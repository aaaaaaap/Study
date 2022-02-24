
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 공부하고 있어요")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())



for i in range(1, 11):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 - \n".format(i) )
        report_file.write("부서 : \n")
        report_file.write("이름 : \n")
        report_file.write("업무요약 : \n")
