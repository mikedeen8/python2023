def years_old():
    i = 0
    s = 0
    count = 0
    for i in range(150):
        t = s + i
        # print(t)
        for p in range(150):
            if t <= s or t < 18:# or (t + i) > 100:
                break
            t += 1
            s += 1
            if str(s).zfill(2) == str(t)[::-1]:
                count += 1
                # print(s, t, count, i)
            if str(s).zfill(2) == str(t)[::-1] and count == 6:
                m = s
                # n = t
            if count == 8:
                return m
        i += 1
        s = 0
        t = 0

print(years_old())