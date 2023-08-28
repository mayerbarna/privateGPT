import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

techstacks = ["Python", "JavaScript", "Java", "C#", "Ruby", "PHP", "Swift", "HTML/CSS", "React", "Vue.js", "Angular",
              "Node.js"]
assignees = ["User1", "User2", "User3", "User4", "User5"]

it_issue_keywords = ["server", "network", "database", "security", "software", "hardware", "integration", "performance"]


def generate_it_issue():
    issue_keyword = random.choice(it_issue_keywords)
    title = f"{issue_keyword.capitalize()} Issue: {fake.sentence(nb_words=random.randint(3, 6))}"
    description = f"Encountering {issue_keyword} issues that are affecting {fake.sentence(nb_words=random.randint(10, 20))}"
    techstack = random.choice(techstacks)
    date = fake.date_time_between(start_date="-1y", end_date="now").strftime("%Y-%m-%d %H:%M:%S")
    assignee = random.choice(assignees)

    issue = {
        "title": title,
        "description": description,
        "techstack": techstack,
        "date": date,
        "assignee": assignee
    }
    return issue


num_issues = 1000

issues = [generate_it_issue() for _ in range(num_issues)]

with open("docs/generated_issues.txt", "w") as file:
    for issue in issues:
        file.write(f"Title: {issue['title']}, ")
        file.write(f"Description: {issue['description']}, ")
        file.write(f"Tech Stack: {issue['techstack']}, ")
        file.write(f"Date: {issue['date']}, ")
        file.write(f"Assignee: {issue['assignee']}, ")
        file.write("\n\n")

print(f"{num_issues} issues generated and saved to 'generated_issues.txt'.")