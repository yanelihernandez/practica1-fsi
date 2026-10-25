"""
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

resultado_bnb, nodos_bnb = search.branch_and_bound_search(ab)
print(resultado_bnb.path())
print("Nodos expandidos (BnB):", nodos_bnb)

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
"""

import search

ab = search.GPSProblem('A', 'B', search.romania)

print("=" * 70)
print("PRÁCTICA 1 - PARTE 1: Comparativa No Informada")
print("=" * 70)

resultado_bfs, generated_bfs, visited_bfs = search.breadth_first_graph_search(ab)
print("BFS:", resultado_bfs.path(), f"| Coste: {resultado_bfs.path_cost} | Generados: {generated_bfs} | Visitados: {visited_bfs}")

resultado_dfs, generated_dfs, visited_dfs = search.depth_first_graph_search(ab)
print("DFS:", resultado_dfs.path(), f"| Coste: {resultado_dfs.path_cost} | Generados: {generated_dfs} | Visitados: {visited_dfs}")

resultado_bnb, generated_bnb, visited_bnb = search.branch_and_bound_search(ab)
print("BnB:", resultado_bnb.path(), f"| Coste: {resultado_bnb.path_cost} | Generados: {generated_bnb} | Visitados: {visited_bnb}")


print("\n" + "=" * 70)
print("PRÁCTICA 1 - PARTE 2: Ramificación y Acotación con Subestimación")
print("=" * 70)

resultado_bnb_sub, generated_bnb_sub, visited_bnb_sub = search.branch_and_bound_subestimation_search(ab)
print("BnB con Subestimación (A*):", resultado_bnb_sub.path(), f"| Coste: {resultado_bnb_sub.path_cost} | Generados: {generated_bnb_sub} | Visitados: {visited_bnb_sub}")
