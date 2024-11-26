book_data = {}
while True:
    record = input("Enter book record (Title - Days Borrowed) or 'done' to finish: ").strip()
    if record.lower() == "done":
        break
    try:
        title, days = record.split(" - ")
        days = int(days)
        if title in book_data:
            book_data[title] += days
        else:
            book_data[title] = days
    except ValueError:
        print("Invalid input format. Please use 'Title - Days Borrowed'.")
if book_data:
    most_borrowed = max(book_data, key=book_data.get)
    least_borrowed = min(book_data, key=book_data.get)
    total_days = sum(book_data.values())
    average_days = total_days / len(book_data)
    unique_titles = set(book_data.keys())
    sorted_books = sorted(book_data.items(), key=lambda x: x[1], reverse=True)
    print("\n--- Library Analysis Results ---")
    print(f"Most Borrowed Book: {most_borrowed} ({book_data[most_borrowed]} days)")
    print(f"Least Borrowed Book: {least_borrowed} ({book_data[least_borrowed]} days)")
    print(f"Average Borrowing Days: {average_days:.2f}")
    print("Unique Titles:", ", ".join(unique_titles))
    print("\nBooks sorted by borrowing days:")
    for title, days in sorted_books:
        print(f"{title} - {days} days")
else:
    print("No data was entered.")  