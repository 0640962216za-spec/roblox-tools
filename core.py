import time

def optimized_function(data):
    start_time = time.time()  
    processed_data = [process_item(item) for item in data]
    execution_time = time.time() - start_time
    print(f"Execution time: {execution_time:.4f} seconds")
    return processed_data

def process_item(item):
    return item ** 2  # Example processing, can be adjusted

if __name__ == "__main__":
    data = range(100000)
    results = optimized_function(data)
    print(results[:10])  # Display first 10 results for quick check