
def remove_duplicates_from_list(l):
    if len(l) == 0:
        return []
    
    if len(l) == 1:
        return l
    
    else:
        if l[0] == l[1]:
            return remove_duplicates_from_list(l[1:])
    return [l[0]] + remove_duplicates_from_list(l[1:])

def main():
    lst = [int(i) for i in input("Enter the elements into the list: ").split(",")]
    output = remove_duplicates_from_list(lst)
    print(output)

main()
    