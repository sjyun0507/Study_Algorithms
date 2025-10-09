class Node:                           # '노드'라는 자료구조(연결 리스트의 한 칸)를 정의
    def __init__(self, data):         # Node가 만들어질 때 초기화 함수(생성자)
        self.data = data              # 이 노드가 담을 실제 값 저장
        self.next = None              # 다음 노드를 가리키는 포인터(처음엔 없음)

class LinkedList:                     # 연결 리스트 전체를 관리하는 클래스
    def __init__(self, value):        # LinkedList 생성 시 처음 값 하나로 시작
        self.head = Node(value)       # 맨 앞 노드(head)를 만든 뒤 리스트의 시작으로 설정

    def append(self, value):          # 리스트 끝에 값을 추가하는 메서드
        cur = self.head               # 탐색을 head부터 시작
        while cur.next is not None:   # 다음 노드가 존재하는 동안(끝이 아닐 때까지)
            cur = cur.next            # 한 칸씩 앞으로 이동
        cur.next = Node(value)        # 마지막 노드의 next에 새 노드를 연결(끝에 추가)

    def print_all(self):              # 전체 노드를 순서대로 출력하는 메서드
        cur = self.head               # head부터 시작
        while cur is not None:        # 현재 노드가 있을 때까지 반복
            print(cur.data)           # 현재 노드의 값을 출력
            cur = cur.next            # 다음 노드로 이동

    def get_node(self, index):        # index번째(0부터 시작) 노드를 반환
        cur = self.head               # head부터 세기 시작
        cur_index = 0                 # 현재 위치(인덱스) 0으로 시작
        while cur_index != index:     # 원하는 인덱스에 도달할 때까지
            cur = cur.next            # 다음 노드로 이동
            cur_index += 1            # 현재 인덱스 +1
        return cur                    # 목표 인덱스의 노드 반환

    def add_node(self, index, value):          # 특정 위치(index)에 새 노드를 추가하는 메서드
        new_node = Node(value)                 # 새 노드를 생성하고, 값(value)을 담음
        if index == 0:                         # 만약 맨 앞(0번째 위치)에 삽입하려면
            new_node.next = self.head          # 새 노드의 next가 기존 head를 가리키게 하고
            self.head = new_node               # head를 새 노드로 변경
            return                             # 삽입 완료 후 함수 종료

        prev_node = self.get_node(index - 1)   # 삽입할 위치의 이전 노드를 찾음
        next_node = prev_node.next             # 이전 노드가 가리키던 다음 노드를 저장
        prev_node.next = new_node              # 이전 노드가 새 노드를 가리키도록 연결
        new_node.next = next_node              # 새 노드가 원래 다음 노드를 가리키도록 연결

    def delete_node(self, index):              # 특정 위치(index)의 노드를 삭제하는 메서드
        if index == 0:                         # 맨 앞(0번째 노드)을 삭제할 경우
            self.head = self.head.next         # head를 다음 노드로 바꿔서 첫 노드를 제거
            return                             # 삭제 완료 후 함수 종료
        node = self.get_node(index - 1)        # 삭제할 노드의 이전 노드를 찾음
        node.next = node.next.next             # 이전 노드가 삭제 대상의 다음 노드를 가리키도록 변경

# ---- 사용 예시 ----
linked_list = LinkedList(5)           # 값 5로 시작하는 연결 리스트 생성 → head.data == 5
linked_list.append(12)                # 끝에 12 추가 → 5 -> 12 구조가 됨
linked_list.append(8)                # 끝에 12 추가 → 5 -> 12 구조가 됨


# -> 5를 들고 있는 노드를 반환해야 합니다!
print(linked_list.get_node(0).data)   # 0번째 노드(head)의 data 출력 → 5

linked_list.add_node(0, 3)
linked_list.print_all()

linked_list.delete_node(1)
linked_list.print_all()