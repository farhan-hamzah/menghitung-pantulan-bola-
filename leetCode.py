h = int(input())
bounce = float(input())
window = float(input())
if (h < 0) or (bounce < 0 or bounce >= 1) or (window > h):
    print(-1)
else:
    hasil = 3*(abs(window - bounce/ bounce - window))
    print(hasil)