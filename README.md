# Mini Project 3: Typing Speed Tester

**Author:** **Gurnoor Singh Arora**

## Project Overview

The **Typing Speed Tester** is a beginner-friendly Python project that measures a user's typing performance. The program displays a random sentence, records the time taken to type it, calculates the typing speed in **Words Per Minute (WPM)**, and evaluates typing **accuracy** by comparing the typed text with the original sentence. This project provides hands-on experience with Python fundamentals while simulating a real-world typing test application.

---

## Objective

The objective of this project is to:
- Measure the user's typing speed.
- Calculate Words Per Minute (WPM).
- Evaluate typing accuracy.
- Practice Python programming concepts such as functions, modules, string handling, and time measurement.

---

## Features

- Displays a random sentence for typing.
- Measures the total typing time.
- Calculates typing speed in Words Per Minute (WPM).
- Calculates typing accuracy based on character-by-character comparison.
- Simple command-line interface.
- Beginner-friendly and easy to understand.

---

## Technologies Used

- Python 3
- `time` module
- `random` module

---

## Python Concepts Used

- Functions
- Lists
- Random module
- Time module
- String methods
- User input and output
- Generator expressions
- `zip()` function
- Arithmetic operations

---

## Project Structure

```text
Typing-Speed-Tester/
│
├── typing_speed_tester.py
└── README.md
```

---

## How It Works

1. A random sentence is selected from a predefined list.
2. The sentence is displayed to the user.
3. The user presses **Enter** to start the test.
4. The timer starts automatically.
5. The user types the displayed sentence.
6. The timer stops after the user presses **Enter**.
7. The program calculates:
   - Time taken
   - Number of words
   - Typing Speed (WPM)
   - Accuracy percentage
8. The results are displayed on the screen.

---

## Formula Used

### Typing Speed (WPM)

```
Words Per Minute = Number of Words ÷ (Time Taken in Seconds ÷ 60)
```

### Accuracy

```
Accuracy = (Correct Characters ÷ Total Characters in Original Sentence) × 100
```

The program compares each character typed by the user with the original sentence using the `zip()` function and counts the number of matching characters.

---

## Sample Output

```text
Type the following sentence as fast as you can:

The quick brown fox jumps over the lazy dog.

Press Enter when you are ready...

Start typing:
The quick brown fox jumps over the lazy dog.

Results:
Time taken: 8.24 seconds
Words typed: 9
Typing speed: 65.53 words per minute
Accuracy: 100.00%
```

---

## Learning Outcomes

By completing this project, you will learn:

- How to measure execution time using `time.time()`.
- How to randomly select data using `random.choice()`.
- How to compare strings character by character.
- How to use `zip()` to iterate over two sequences simultaneously.
- How generator expressions work with `sum()`.
- How to calculate typing speed and accuracy.
- How to organize code using functions.

---

## Future Improvements

- Add multiple difficulty levels.
- Display typing mistakes separately.
- Save user scores and history.
- Add a countdown timer before the test starts.
- Support paragraph-based typing tests.
- Build a graphical user interface (GUI) using Tkinter or PyQt.
- Store results in a file or database for progress tracking.

---

## License

This project is developed for educational and learning purposes. You are free to modify and enhance it for your own practice.

---

**Author:** **Gurnoor Singh Arora**
