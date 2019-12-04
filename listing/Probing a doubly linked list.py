# Given the head, tail, and probe references, probe the list for a target.

# Make sure the list is not empty.
if head is None :
    return False
# If probe is null, initialize it to the first node.
elif probe is None :
    probe = head

# If the target comes before the probe node, we traverse backward;
# otherwise traverse forward.
if target < probe.data :
    while probe is not None and target <= probe.data :
        if target == probe.data :
            return True
        else :
            probe = probe.prev
else :
    while probe is not None and target >= probe.data :
        if target == probe.data :
            return True
        else :
            probe = probe.next

# If the target is not found in the list, return False.
return False
