1. Since the output is a list of lists, it is a good idea to create each sub-list (i.e., each boundary) and then append it to the main list. You can think of it as a matrix too—an `n × 2` matrix where there are `n` boundaries.
2. At some point, we have to test if the next index is not strictly one more than the current index.
3. First, we should think about how to fill `current_boundary`.
4. When we are done with a whole boundary, immediately add the next element in the list as a new starting boundary.
5. **Now:** If the next number is not strictly one greater than the current number, then the current number is the ending boundary. Here, we have found a complete boundary (start and end point), so we append this list to the main list, which stores boundaries. Then, we empty `current_boundary`.
6. **Out of index error:** We cannot check both conditions together. If we reach the end of the list, the last number is the end boundary. If we check both conditions simultaneously, the last boundary will not have an end boundary.

 if (idx + 1 == len(list)):  
        #     current_boundary.append(list[idx])
        #     boundary_summarised.append(current_boundary)
        #     return boundary_summarised

#