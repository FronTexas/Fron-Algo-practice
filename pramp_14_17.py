def meeting_planner(slotsA, slotsB, dur):
  i_A = 0 
  i_B = 0 
  while (i_A < len(slotsA) and i_B < len(slotsB)):
    overlap_begin = max(slotsA[i_A][0],slotsB[i_B][0])
    overlap_end = min(slotsA[i_A][1],slotsB[i_B][1])
    
    if overlap_end - overlap_begin >= dur:
      return [overlap_begin,overlap_begin + dur]
    
    if (slotsB[i_B][1] < slotsA[i_A][1]): 
      i_B += 1 
    elif (slotsA[i_A][1] < slotsB[i_B][1]):
      i_A += 1 
  return []
