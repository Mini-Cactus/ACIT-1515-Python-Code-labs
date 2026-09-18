KB = 1024
MB = 1048576
GB = 1073741824

num_entries = float(input("Please enter the number of entries per second: "))
entry_size = float(input("Please enter the average number of bytes per entry: "))

kb_size = (num_entries * entry_size) / KB
mb_size = (num_entries * entry_size) / MB
gb_size = (num_entries * entry_size) / GB

print("Storage Estimates:")
print(f"Per minute: {kb_size*60}KB")
print(f"Per hour: {mb_size*3600}MB")
print(f"Per day: {gb_size*86400}GB")