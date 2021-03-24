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
    def __init__(self, value, weight, parent, left, right):
        self.value = value
        self.weight = weight
        self.parent = parent
        self.left = left
        self.right = right

    def create_new_node(value, weight, parent, left, right):
        new_node = Node( value, weight, parent, left, right )
        node_list.append(new_node)
        return new_node

###########################################################################
###########################################################################
###########################################################################

def find_two_min():
    min_value_1 = 10000
    min_value_2 = 10000
    for char in weights_dic:
        if( weights_dic[char] < min_value_1 ):
            min_value_1 = weights_dic[char]
            min_key_1 = char
        elif( weights_dic[char] < min_value_2 ):
            min_value_2 = weights_dic[char]
            min_key_2 = char

    weights_dic.pop(min_key_1)
    weights_dic.pop(min_key_2)
    return (min_key_1, min_value_1, min_key_2, min_value_2)

###########################################################################

def find_node(value):
    for node in node_list:
        if node.value == value:
            return node
    return 0

###########################################################################

def create_tree():
    weight = 0
    while( weight < tree_weight ):
        min_key_1, min_value_1, min_key_2, min_value_2 = find_two_min()
        weight = min_value_1 + min_value_2
        weights_dic[weight] = weight

        new_node_1 = find_node(min_key_1)
        if new_node_1 == 0:
            new_node_1 = Node.create_new_node( min_key_1, min_value_1, None, None, None )

        new_node_2 = find_node(min_key_2)
        if new_node_2 == 0:
            new_node_2 = Node.create_new_node( min_key_2, min_value_2, None, None, None )

        if( new_node_1.weight < new_node_2.weight ):
            new_parent = Node.create_new_node( weight, weight, None, new_node_1, new_node_2 )
        else:
            new_parent = Node.create_new_node( weight, weight, None, new_node_2, new_node_1 )
        new_node_1.parent = new_parent
        new_node_2.parent = new_parent

###########################################################################

def get_code_of_char(char):
    code = ""
    node_list.reverse()
    for node in node_list:
        if( node.value == char ):
            break
    while( node.weight != tree_weight ): 
        if node == node.parent.left:
            code = "0"+code
        else:
            code = "1"+code
        node = node.parent
        
    return code

###########################################################################

def get_char_of_code(code):
    node = node_list[len(node_list)-1]
    for num in code:
        if int(num) == 0:
            node = node.left
        else:
            node = node.right
    return node.value

###########################################################################

create_tree()
