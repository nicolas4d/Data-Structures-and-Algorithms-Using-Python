from usingTailReference import ListNode

box = None
temp = None

for i in range( 4 ) :
    if i % 3 != 0 :
        temp = ListNode( i )
        temp.next = box
        box = temp

print(box)
print(box.item)
print(box.next.item)
print(box.next.next.item)
