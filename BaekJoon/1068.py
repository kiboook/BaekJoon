from collections import deque


def BFS(tree, start):
    leaf_node = 0
    queue = deque([start])

    while queue:
        now = queue.popleft()
        if len(tree[now]) == 0:
            leaf_node += 1

        for node in tree[now]:
            queue.append(node)

    return leaf_node


def solution():
    # 1. 트리 생성
    tree = {node: [] for node in range(N)}
    for node, parent in enumerate(parent_info):
        if parent != -1:
            tree[parent].append(node)

    # 2. 전체 리프노드 개수 세기
    all_leaf_node = 0
    for child in tree.values():
        if len(child) == 0:
            all_leaf_node += 1

    # 3. 지우는 노드부터 탐색하여 리프노드 개수 세기
    remove_leaf_node = BFS(tree, remove_node)

    # 4. 첫번째 지우는 노드의 부모가 리프노드가 되는지 확인
    if parent_info[remove_node] != -1 and len(tree[parent_info[remove_node]]) == 1:
        remove_leaf_node -= 1

    return all_leaf_node - remove_leaf_node


if __name__ == "__main__":
    N = int(input())
    parent_info = list(map(int, input().rsplit()))
    remove_node = int(input())

    print(solution())