def pay_fees(student, amount):
    student.fees_paid += amount
    print(f"${amount} added. Total fees paid: ${student.fees_paid}")
