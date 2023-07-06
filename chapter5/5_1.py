import time
t = time.time()
# print(t)
hours = int((t // 3600) % 24)
minutes = int((t // 60) % 60)
seconds = int(t % 60) 
days = int(t // (24 * 60 * 60))
print(hours, ':', minutes, ':', seconds, '  ', days, 'days')