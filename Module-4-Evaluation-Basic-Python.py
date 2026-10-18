
# Project: Survey Feedback Analyzer

# Step 1: Preloaded feedback data
feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': [
        'Ravi', 'Meera', 'Sam', 'Anu', 'Raj',
        'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'
    ],
    'Feedback': [
        ' Very GOOD Service!!!',
        'poor support, not happy ',
        'GREAT experience! will come again.',
        'okay okay...',
        ' not BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],
    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}

# Step 2: Add new feedbacks
n = int(input("How many more feedbacks do you want to add? "))

for i in range(n):
    print(f"\nFeedback {i + 1}")

    name = input("Enter name: ")
    feedback = input("Enter written feedback: ")

    rating = int(input("Enter rating (1-5): "))

    while rating < 1 or rating > 5:
        print("Invalid rating. Enter a number from 1 to 5.")
        rating = int(input("Enter rating (1-5): "))

    s_no = len(feedback_data['S_No']) + 1

    feedback_data['S_No'].append(s_no)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data['Rating'].append(rating)


# Step 3: Clean feedback text
def clean_feedback(text):
    text = text.lower()

    for mark in ['.', ',', '!', '?']:
        text = text.replace(mark, '')

    text = ' '.join(text.split())

    return text


for i in range(len(feedback_data['Feedback'])):
    feedback_data['Feedback'][i] = clean_feedback(
        feedback_data['Feedback'][i]
    )


# Step 4: Count feedbacks containing a word
def count_word_in_feedbacks(word):
    count = 0

    for feedback in feedback_data['Feedback']:
        words = feedback.split()

        if word.lower() in words:
            count += 1

    return count


print("\n--- Word Count Insights ---")
print("Feedbacks containing 'good':",
      count_word_in_feedbacks("good"))
print("Feedbacks containing 'poor':",
      count_word_in_feedbacks("poor"))
print("Feedbacks containing 'excellent':",
      count_word_in_feedbacks("excellent"))


# Step 5A: Display cleaned data
print("\n--- Final Cleaned Feedback Data ---")
print(feedback_data)


# Step 5B: Calculate average rating
total_rating = sum(feedback_data['Rating'])
total_feedbacks = len(feedback_data['Rating'])

average_rating = total_rating / total_feedbacks

print("\nAverage Rating:", round(average_rating, 2))


# Step 5C: Find the longest feedback by word count
longest_feedback = ""
max_words = 0

for feedback in feedback_data['Feedback']:
    word_count = len(feedback.split())

    if word_count > max_words:
        max_words = word_count
        longest_feedback = feedback

print("\n--- Longest Feedback ---")
print("Feedback:", longest_feedback)
print("Word Count:", max_words)


# Step 5D: Find unique words
unique_words = []

for feedback in feedback_data['Feedback']:
    for word in feedback.split():
        if word not in unique_words:
            unique_words.append(word)

print("\n--- Unique Words ---")
print(sorted(unique_words))


# Step 6 (Optional): Sort feedbacks by rating
entries = list(zip(
    feedback_data['S_No'],
    feedback_data['Name'],
    feedback_data['Feedback'],
    feedback_data['Rating']
))

sorted_entries = sorted(
    entries,
    key=lambda x: x[3],
    reverse=True
)

print("\n--- Feedbacks Sorted by Rating ---")

for entry in sorted_entries:
    print(entry)
