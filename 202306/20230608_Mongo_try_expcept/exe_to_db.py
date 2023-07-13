def execute_with_retry(func):    
    max_retries = 3    
    retries = 0    

    while retries < max_retries:        
        try:            
            # Execute the provided function   
            func()            
            break  # If execution is successful, exit the loop        
        except Exception as e:            
            print(f"Execution failed: {e}")            
            retries += 1            
            print(f"Retrying... (Attempt {retries}/{max_retries})")    
    else:        
        print("Maximum retries exceeded. Giving up.")
        
        
# Example usage:
def my_function():    
        # # Your code here    
    print("Executing my_function")

execute_with_retry(my_function)