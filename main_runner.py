import threading
from circular_queue import CircularQueue
from password_checker import PassWordChecker
from word_frequency import WordFrequency

def word_frequency_example():
    try:
        wf = WordFrequency()
        wf.word_frequency("which is better python 2 or python 3")
    except Exception as e:
        print(f"Error in word_frequency_example: {e}")

def circular_queue_example():
    try:
        cq = CircularQueue(5)
        for i in range(6):
            cq.enqueue(i)
            print(f"Queue after enqueuing {i}:")
            cq.display()
        for _ in range(3):
            dequeued = cq.dequeue()
            print(f"Dequeued element: {dequeued}")
            print("Queue after dequeuing:")
            cq.display()
    except Exception as e:
        print(f"Error in circular_queue_example: {e}")

def password_checker_example():
    try:
        input_passwords = "Abc@1,HelloWorld,Pass123#,A1b2C3#"
        valid_passwords = PassWordChecker.check_password_validity(input_passwords)
        print("Valid Passwords:", ', '.join(valid_passwords))
    except Exception as e:
        print(f"Error in password_checker_example: {e}")

def main():
    threads = []
    try:
        # Creating threads
        for func in [word_frequency_example, circular_queue_example, password_checker_example]:
            thread = threading.Thread(target=func)
            threads.append(thread)
            thread.start()

        # Waiting for all threads to complete
        for thread in threads:
            thread.join()
    except Exception as e:
        print(f"Error in main thread: {e}")

if __name__ == "__main__":
    main()
