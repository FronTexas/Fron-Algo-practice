def find_smallest_edit_distance(s1,s2, cache):
	
	if (s1, s2) in cache[(s1, s2)]: return cache[(s1, s2)]

	head_1, head_2 = 0, 0 
	tail_1, tail_2 = len(s1) - 1, len(s2) - 1

	while head_1 < len(s1) and head_2 < len(s2) and s1[head_1] == s2[head_2]:
		head_1 += 1
		head_2 += 1

	if head_1 == len(s1) and head_2 == len(s2): return 0
	
	while tail_1 >= 0 and tail_2 >= 0 and s1[tail_1] == s2[tail_2]:
		tail_1 -= 1
		tail_2 -= 1

	if tail_1 == 0 and tail_2 == 0: return 0

	insert = min(find_smallest_edit_distance(s2[0] + s1, s2), find_smallest_edit_distance(s1 + s2[-1], s2))
	remove = min(find_smallest_edit_distance(s1[head_1 + 1:], s2), find_smallest_edit_distance(s1[:tail_1], s2))
	replace = min(find_smallest_edit_distance(replace(s1, 0, s2[0]), s2), find_smallest_edit_distance(replace(s1, len(s1) - 1, s2[-1]), s2))

	cache[(s1, s2)] = min(insert, remove, replace)

	return min(insert, remove, replace)







