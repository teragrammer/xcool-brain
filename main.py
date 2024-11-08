from student_state import StudentState
from knowledge_engine import load_context
from adaptive_engine import generate_explanation

name = str(input("Enter student name: "))
score = int(input("Enter score (0-100): "))
topic = str(input("Select your topic (filename only): "))

student = StudentState(name)

context = load_context(topic)
student.update_master(topic, score)

explanation = generate_explanation(student, context)

print("\n-- Personalized explanation --\n")
print(explanation)
