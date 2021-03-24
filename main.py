###########################################################################
###########################################################################
###########################################################################

node_list = list()
tree_weight = 550
weights_dic = {
    'q' : 1,
    'w' : 3,
    'e' : 5,
    'r' : 7,
    't' : 9,
    'y' : 2,
    'u' : 4,
    'i' : 6,
    'o' : 8,
    'p' : 22,
    'a' : 12,
    's' : 32,
    'd' : 42,
    'f' : 52,
    'g' : 13,
    'h' : 23,
    'j' : 33,
    'k' : 43,
    'l' : 53,
    'z' : 11,
    'x' : 21,
    'c' : 31,
    'v' : 41,
    'b' : 51,
    'n' : 10,
    'm' : 15,
}

###########################################################################
###########################################################################
###########################################################################

class Node:
    def __init__(self, value, weight, left, right):
        self.value = value
        self.weight = weight
        self.left = left
        self.right = right

    def create_new_node(value, weight, left, right):
        new_node = Node( value, weight, left, right )
        node_list.append(new_node)
        return new_node

###########################################################################
###########################################################################
###########################################################################

def find_min():
    min_value = 10000
    for char in weights_dic:
        if( weights_dic[char] < min_value ):
            min_value = weights_dic[char]
            min_key = char
    weights_dic.pop(min_key)
    return min_key, min_value

def create_tree():
    min_key_1, min_value_1 = find_min()
    min_key_2, min_value_2 = find_min()
    weight = min_value_1 + min_value_2
    new_node = Node.create_new_node( min_key_1, min_value_1, None, None )
    new_node = Node.create_new_node( min_key_2, min_value_2, None, None )
    new_parent = Node.create_new_node( weight, weight, min_key_1, min_key_2 )

    while weight < tree_weight:
        min_key_1, min_value_1 = find_min()
        new_node = Node.create_new_node( min_key_1, min_value_1, None, None )
        weight = min_value_1 + new_parent.weight
    
        if min_value_1 < new_parent.weight:
            new_parent = Node.create_new_node( weight, weight, new_node, new_parent )
        else:
            new_parent = Node.create_new_node( weight, weight, new_parent, new_node )


create_tree()
print(node_list[len(node_list)-1])