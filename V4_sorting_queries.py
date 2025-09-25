def nl_to_sql(natural_query):
    nq = natural_query.lower()

    # ORDER BY queries
    if "order by marks" in nq:
        if "descending" in nq or "highest first" in nq:
            return "SELECT * FROM Students ORDER BY Marks DESC;"
        elif "ascending" in nq or "lowest first" in nq:
            return "SELECT * FROM Students ORDER BY Marks ASC;"
        else:
            return "SELECT * FROM Students ORDER BY Marks;"
    
    elif "order by name" in nq:
        if "descending" in nq or "z to a" in nq:
            return "SELECT * FROM Students ORDER BY Name DESC;"
        else:
            return "SELECT * FROM Students ORDER BY Name ASC;"
    
    # Default
    elif "all students" in nq:
        return "SELECT * FROM Students;"
    else:
        return "Sorry, I don’t understand the query."

# Example usage
queries = [
    "Show me all students order by marks descending",
    "List all students order by marks ascending",
    "Display students order by name",
    "Get the average marks of students"
]

for q in queries:
    print("Natural Language:", q)
    print("SQL Query:", nl_to_sql(q))
    print()
