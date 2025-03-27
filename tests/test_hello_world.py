import logging

expected_message = "Hello World! This is real Navdeep, testing pytest is running"

def test_hello():
    actual_correct_message = "Hello World! This is real Navdeep, testing pytest is running"
    logging.info(f"Message is '{actual_correct_message}'")
    print(f"Message is '{actual_correct_message}'")
    assert actual_correct_message == expected_message

def test_fail_hello():
    incorrect_message = "Hello World!, I am fake Navdeep"
    logging.info(f"Incorrect Message is '{incorrect_message}'")
    print(f"Incorrect Message is '{incorrect_message}'")
    assert incorrect_message == expected_message