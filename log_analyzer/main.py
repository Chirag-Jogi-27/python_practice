import datetime
import random
from collections import Counter, defaultdict

def generate_sample_logs(num_logs=100):
    """Generates a list of dictionaries simulating server logs."""
    
    # 1. Define our possible data points
    log_levels = ["INFO", "INFO", "INFO", "WARNING", "ERROR"] 
    # Notice we put more "INFO"s so they appear more frequently than errors!
    
    messages = {
        "INFO": ["User logged in", "Page rendered", "Data saved", "Connection established"],
        "WARNING": ["High memory usage", "Deprecation warning", "Slow response time"],
        "ERROR": ["Database connection failed", "File not found", "Authentication error", "Timeout"]
    }
    
    user_ids = [f"user_{i}" for i in range(1, 21)] # Creates user_1 to user_20
    
    logs = []
    base_time = datetime.datetime.now()
    
    # 2. Build the logs one by one
    for _ in range(num_logs):
        level = random.choice(log_levels)
        message = random.choice(messages[level])
        user = random.choice(user_ids)
        
        # Add random minutes to make timestamps differ
        time = base_time - datetime.timedelta(minutes=random.randint(1, 1440)) 
        
        # 3. Create the log entry dictionary and add it to our list
        log_entry = {
            "timestamp": time.isoformat(),
            "log_level": level,
            "message": message,
            "user_id": user
        }
        logs.append(log_entry)
        
    return logs

def filter_logs_by_level(logs, level_to_find):
    """Filters logs to find only those matching a specific level."""
    # List comprehension: 'keep this log' 'for every log in our list' 'IF the level matches'
    filtered = [log for log in logs if log["log_level"] == level_to_find]
    return filtered


def count_log_levels(logs):
    """Counts how many times each log level occurs."""
    # Generator expression: Grabs just the "log_level" string from every dictionary in the list
    level_counts = Counter(log["log_level"] for log in logs)
    
    # Counter returns a special dictionary-like object, we'll convert it to a normal dict for simplicity
    return dict(level_counts) 

def find_most_active_user(logs):
    """Finds the single user_id that appears most frequently."""
    # We use Counter again, but this time on the user_id
    user_counts = Counter(log["user_id"] for log in logs)
    
    # most_common(1) returns a list with one item: [('user_x', count)]
    # We use [0] to grab just that tuple from the list
    if user_counts:
        return user_counts.most_common(1)[0]
    return (None, 0)


def group_errors_by_hour(logs):
    """Groups all ERROR logs by the hour (0-23) they occurred."""
    # First, let's use our previous function to get ONLY the errors
    errors = filter_logs_by_level(logs, "ERROR")
    
    # We create a dictionary where every new key automatically starts as an empty list []
    hours_dict = defaultdict(list)
    
    for error in errors:
        # Convert our text timestamp back into a real Python datetime object
        dt = datetime.datetime.fromisoformat(error["timestamp"])
        
        # Grab the hour (e.g., 14 for 2:00 PM) and append the error to that list
        hours_dict[dt.hour].append(error)
        
    return dict(hours_dict)

def generate_summary(logs):
    """Generates the final summary report tying everything together."""
    total_logs = len(logs)
    
    # 1. Calculate the Error Rate
    counts = count_log_levels(logs)
    error_count = counts.get("ERROR", 0) # Use .get() safely in case there are 0 errors!
    error_rate = (error_count / total_logs * 100) if total_logs > 0 else 0
    
    # 2. Find the top 5 most common specific error messages
    errors = filter_logs_by_level(logs, "ERROR")
    error_messages = Counter(error["message"] for error in errors)
    top_5_errors = error_messages.most_common(5)
    
    # 3. Find the peak error hour using our previous function
    errors_by_hour = group_errors_by_hour(logs)
    
    # This finds the 'key' (hour) that has the maximum 'value length' (number of errors)
    peak_hour = max(errors_by_hour.keys(), key=lambda k: len(errors_by_hour[k]), default=None)
    
    return {
        "Total logs processed": total_logs,
        "Error rate percentage": f"{error_rate:.2f}%",
        "Top 5 most common error messages": top_5_errors,
        "Time period with most errors (Hour)": peak_hour
    }

# --- The Final Application ---
if __name__ == "__main__":
    print("Generating 10,000 sample logs for production simulation...")
    my_logs = generate_sample_logs(10000) 
    
    print("\n==================================")
    print("      LOG ANALYSIS REPORT         ")
    print("==================================")
    
    summary = generate_summary(my_logs)
    
    # Formatting the output nicely
    for key, value in summary.items():
        if isinstance(value, list):
            print(f"\n{key}:")
            for item, count in value:
                print(f"  - {item}: {count} times")
        else:
            print(f"{key}: {value}")
            
    # Add our active user in
    active_user, active_user_count = find_most_active_user(my_logs)
    print(f"\nMost active user: {active_user} ({active_user_count} logs)")
    print("==================================")
