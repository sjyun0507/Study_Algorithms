class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 3을 가진 Node 를 만드려면 아래와 같이 하면 됩니다!
node = Node(3) # 현재는 next 가 없이 하나의 노드만 있습니다. [3]
print(node.data, node.next) # 3 None

first_node = Node(5) # 현재는 next 가 없이 하나의 노드만 있습니다. [5]
second_node = Node(12) # [12] 를 들고 있는 노드를 만듭니다.
first_node.next = second_node # 그리고, [5]의 next 를 [12]로 지정합니다. [5] -> [12]

third_node = Node(7)
fourth_node = Node(6)
second_node.next = third_node
third_node.next = fourth_node
'''
이 노드들을 일일이 계속 연결해주려면 변수를 지정하고 
위와 같은 코드를 반복해야 하는데, 너무 번거롭습니다!

따라서 LinkedList 라는 클래스를 한 번 만들어볼게요!
LinkedList 는 head node 만 딱 들고 있습니다.

기차를 다시 떠올려보면, 맨 앞 칸만 저장해두는 거에요.
다음 칸을 보기 위해서는 next를 통해서 다음 노드에 접근해야 합니다!

정리하면,
1) LinkdList 는 self.head 에 시작하는 노드를 저장한다.
2) 다음 노드를 보기 위해서는 각 노드의 next 를 조회해서 찾아가야 한다.

그럼 이제 한 번 만들어보겠습니다!
'''
# ["기관실"] -> ["시멘트"] -> ["자갈"] -> ["밀가루"] -> ["우편"]

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)  # head 에 시작하는 Node 를 연결합니다.

# Likendlist의 가장 끝에 있는 노드에 새로운 노드를 연결해줘
    def append(self, value):
        cur = self.head
        while cur.next != None:
            cur = cur.next

        cur.next = Node(value)
    # linked_list에 저장한 head를 따라가면서 현재 있는 노드들을 전부 출력해주는 함수
    def print_all(self):
        cur = self.head
        while cur!= None:
            print(cur.data)
            cur = cur.next

linked_list = LinkedList(5)
print(linked_list.head.data) # 5가 출력됩니다!

# 현재 LinkedList 는 (5) 만 존재합니다!

linked_list.append(6)
linked_list.append(12)
# [5]->[6]->[12]
linked_list.print_all()