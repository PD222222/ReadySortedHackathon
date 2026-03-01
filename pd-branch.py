import random
from datetime import datetime
from collections import Counter

def greet(name):
    """Greet a user with the current time."""
    current_time = datetime.now().strftime("%H:%M:%S")
    return f"Hello, {name}! Current time: {current_time}"

def fibonacci(n):
    """Generate fibonacci sequence up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence

def analyze_text(text):
    """Analyze word frequency in text."""
    words = text.lower().split()
    return Counter(words)

def main():
    print(greet("World"))
    print(f"Fibonacci(10): {fibonacci(10)}")
    
    sample_text = "python is great python is fun programming is awesome"
    word_freq = analyze_text(sample_text)
    print(f"Word frequency: {word_freq.most_common(3)}")

if __name__ == "__main__":
    main()