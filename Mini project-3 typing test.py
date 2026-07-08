import random
import time 

#write code for typing test game
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.", 
]

def measure_accuracy(user_input, original_sentence):
    user_words = user_input.split()
    original_words = original_sentence.split()
    correct_words = sum(1 for u, o in zip(user_words, original_words) if u == o)
    accuracy = (correct_words / len(original_words)) * 100
    return accuracy


def count_words(user_input):
    return len(user_input.split())


def typing_test():
    print("Welcome to the Typing Test Game!")
    print("You will be given a sentence to type. Type it as fast and accurately as you can.")
    print("Press Enter when you're ready to start.")
    input()

    # Select a random sentence
    original_sentence = random.choice(sentences)
    print("\nType the following sentence:")
    print(original_sentence)

    # Start the timer
    start_time = time.time()
    
    # Get user input
    user_input = input("\nYour input: ")
    
    # Stop the timer
    end_time = time.time()
    
    # Calculate time taken
    time_taken = end_time - start_time
    
    # Measure accuracy and word count
    accuracy = measure_accuracy(user_input, original_sentence)
    word_count = count_words(user_input)
    
    # Display results
    print(f"\nTime taken: {time_taken:.2f} seconds")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Word count: {word_count}")


if __name__ == "__main__":
    typing_test()
    
