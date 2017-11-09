def paint(w,h):
	return 2*(w * h + (h*(h+1)) / 2)

w,h = raw_input().split()
w,h = int(w),int(h)
print paint(w,h)
