from admin import patients

illnesses = ["Hyza","Influenza","Maria"]
for i in patients:
    for j in  (i.print_symptoms()):
            

def count_symptoms_repetitions(string):
    word_counts = {}
    words = string.split()

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

repetition_counts = count_symptoms_repetitions(j)
print(repetition_counts)
