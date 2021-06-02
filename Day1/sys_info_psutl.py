import psutil
 
print(f"Memory :{psutil.virtual_memory()}")
print("cpu :",psutil.cpu_stats())