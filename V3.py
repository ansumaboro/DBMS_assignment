def nl_to_sql(natural_query):
    nq = natural_query.lower()

    if "average marks" in nq or "avg marks" in nq:
        return "SELECT AVG(Marks) FROM Students;"
    elif "maximum marks" in nq or "highest marks" in nq:
        return "SELECT MAX(Marks) FROM Students;"
    elif "minimum marks" in nq or "lowest marks" in nq:
        return "SELECT MIN(Marks) FROM Students;"
    elif "total marks" in nq or "sum of marks" in nq:
        return "SELECT SUM(Marks) FROM Students;"
    elif "count students" in nq or "number of students" in nq:
        return "SELECT COUNT(*) FROM Students;"
    elif "all students" in nq:
        return "SELECT * FROM Students;"
    else:
        return "Sorry, I don’t understand the query."

# Example usage
queries = [
    "Find the average marks of the students",
    "Show me the count students",
    "What is the number of students",
    "Get the highest marks",
]

for q in queries:
    print("Natural Language:", q)
    print("SQL Query:", nl_to_sql(q))
    print()
