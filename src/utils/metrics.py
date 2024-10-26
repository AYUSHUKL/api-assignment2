import time

def measure_latency(model_func, *args):
    start_time = time.time()
    result = model_func(*args)
    latency = time.time() - start_time
    return result, latency
