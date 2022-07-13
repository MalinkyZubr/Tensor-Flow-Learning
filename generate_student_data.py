
import random
import csv
import os

pwd = os.path.dirname(os.path.abspath(__file__))
student_file = os.path.join(pwd, r'student_data.csv')

def get_finals(midterms_tuple:tuple) -> int:
    midterm_1, midterm_2 = midterms_tuple
    final_grade = sum(midterms_tuple) / len(midterms_tuple)
    return final_grade

def generate_data(dataset_size:int) -> dict:
    midterms_1 = [random.randint(50, 100) for midterm_1 in range(dataset_size)]
    midterms_2 = [random.randint(50, 100) for midterm_2 in range(dataset_size)]
    final_grades = list(map(get_finals, zip(midterms_1, midterms_2)))

    data_set = {"midterm_1":midterms_1, "midterm_2":midterms_2, "final_grade":final_grades}
    
    return data_set

def write_csv(dataset):
    with open(student_file, 'w') as sf:
        fieldnames = list(dataset.keys())
        writer = csv.DictWriter(sf, fieldnames=fieldnames)

        writer.writeheader()
        
        for midterm_1, midterm_2, final in list(zip(list(dataset.values())[0], list(dataset.values())[1], list(dataset.values())[2])):
            writer.writerow({list(dataset.keys())[0]:midterm_1, list(dataset.keys())[1]:midterm_2,list(dataset.keys())[2]:final})


write_csv(generate_data(1000000))
