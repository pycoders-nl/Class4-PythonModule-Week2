# 1.lucky numbers:
# Write a programme to generate the lucky numbers from the range(n).
# These are generated starting with the sequence s=[1,2,...,n].
# At the first pass, we remove every second element from the sequence, resulting in s2.
# At the second pass, we remove every third element from the sequence s2, resulting in s3,
# and we proceed in this way until no elements can be removed. The resulting sequence
# are the numbers lucky enough to have survived elimination.
# The following example describes the entire process for n=22:

# Original sequence: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
# Remove 2nd elements: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
# Remove 3rd elements: [1, 3, 7, 9, 13, 15, 19, 21]
# Remove 4th elements: [1, 3, 7, 13, 15, 19]
# Remove 5th elements: [1, 3, 7, 13, 19]
# We cannot remove every other 6th element as there is no 6th element.
# Input>>> 22
# Output>>> Lucky numbers are [1, 3, 7, 13, 19]

sequence = int(input("enter a number: "))               # user dan input aldim.
original_sequence = [i for i in range(1, sequence+1)]   # 1 den baslayarak, input dahil sayilari listeledim.

print("Original sequence: ", original_sequence)         # Original sequence

dummy_original = original_sequence                      # orijinal liseyi kopyasini olusturdum.(kukla ya atadim)
removed_element_index = 1                               # ilk silinecek item lerin indexini(2.element) assign ettim.
while True:                                             # else girerse while dongusunden cikar.
    if len(original_sequence) > removed_element_index:  # listenin len i silinecek ogenin index inden buyuk ise calis
        j = removed_element_index                       # removed_element_index i j ye assign ettim.
        for i in original_sequence:                     # ilgili liseyi for ile pass ettim.
            if len(original_sequence) > j:              # liste uzunlugu remove edilen item indexinden buyukse calisir
                dummy_original.remove(dummy_original[j])   # ilgili index teki item i remove ettim.
                original_sequence = dummy_original         # kalan listeyi original listeye atadim.
                j += removed_element_index              # j yi silinecek elementin index degeri kadar artirdim.
        print("Remove {}nd elements: ".format(removed_element_index + 1), original_sequence)
        removed_element_index += 1
    else:
        removed_element_index += 1
        print("there is no {}. element. we can not remove.".format(removed_element_index))
        break
print("LUCKY numbers: ",original_sequence)

