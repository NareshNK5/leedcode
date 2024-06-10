'''
182. Duplicate Emails

# Write your MySQL query statement below
select email as Email
from Person
group by email
having count(email)>1
'''
from collections import Counter

# Get the emails from the Person table
emails = [row['email'] for row in Person]

# Count the occurrences of each email
email_counts = Counter(emails)

# Get the emails that appear more than once
duplicate_emails = [email for email, count in email_counts.items() if count > 1]

# Return the emails as a list
print([{'Email': email} for email in duplicate_emails])

