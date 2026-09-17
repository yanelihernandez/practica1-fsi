# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

resultado_bfs, nodos_bfs = search.breadth_first_graph_search(ab)
print(resultado_bfs.path())
print("Nodos expandidos (BFS):", nodos_bfs)

resultado_dfs, nodos_dfs = search.depth_first_graph_search(ab)
print(resultado_dfs.path())
print("Nodos expandidos (DFS):", nodos_dfs)

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450