from subprocess import run

# Run all unit tests

if __name__ == "__main__":
    try:
        run("python test_auto_score.py")
        run("python test_extract.py")
        run("python test_get_numeric_score.py")
    except Exception as e:
        print(f"Error: {e}")