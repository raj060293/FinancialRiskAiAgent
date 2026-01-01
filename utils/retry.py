import time

def retry_call(fn, retries: int = 2, delay: float = 1.0) :
    """
    Retries a function call on exception
    """
    last_error = None

    for attempt in range(retries + 1):
        try:
            return fn()
        except Exception as e:
            last_error = e
            print(f"[Retry] Attempt {attempt + 1} failed: {e}")
            time.sleep(delay)


    raise last_error