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
import time

ab = search.GPSProblem('A', 'B', search.romania)

print("=" * 70)
print("PRÁCTICA 1 - PARTE 1: Comparativa No Informada")
print("=" * 70)

# ALGORITMO BFS
inicio_bfs = time.perf_counter()
resultado_bfs, generated_bfs, visited_bfs = search.breadth_first_graph_search(ab)
fin_bfs = time.perf_counter()
tiempo_bfs = (fin_bfs - inicio_bfs) * 1_000_000  # Convertir a microsegundos
print("BFS:", resultado_bfs.path(), f"| Coste: {resultado_bfs.path_cost} | Generados: {generated_bfs} | Visitados: {visited_bfs} | Tiempo: {tiempo_bfs:.1f} μs")

# ALGORITMO DFS
inicio_dfs = time.perf_counter()
resultado_dfs, generated_dfs, visited_dfs = search.depth_first_graph_search(ab)
fin_dfs = time.perf_counter()
tiempo_dfs = (fin_dfs - inicio_dfs) * 1_000_000  # Convertir a microsegundos
print("DFS:", resultado_dfs.path(), f"| Coste: {resultado_dfs.path_cost} | Generados: {generated_dfs} | Visitados: {visited_dfs} | Tiempo: {tiempo_dfs:.1f} μs")

# ALGORITMO BRANCH AND BOUND
inicio_bnb = time.perf_counter()
resultado_bnb, generated_bnb, visited_bnb = search.branch_and_bound_search(ab)
fin_bnb = time.perf_counter()
tiempo_bnb = (fin_bnb - inicio_bnb) * 1_000_000  # Convertir a microsegundos
print("BnB:", resultado_bnb.path(), f"| Coste: {resultado_bnb.path_cost} | Generados: {generated_bnb} | Visitados: {visited_bnb} | Tiempo: {tiempo_bnb:.1f} μs")


print("\n" + "=" * 70)
print("PRÁCTICA 1 - PARTE 2: Ramificación y Acotación con Subestimación")
print("=" * 70)

# ALGORITMO BRANCH AND BOUND CON SUBESTIMACIÓN
inicio_bnb_sub = time.perf_counter()
resultado_bnb_sub, generated_bnb_sub, visited_bnb_sub = search.branch_and_bound_subestimation_search(ab)
fin_bnb_sub = time.perf_counter()
tiempo_bnb_sub = (fin_bnb_sub - inicio_bnb_sub) * 1_000_000  # Convertir a microsegundos
print("BnB con Subestimación (A*):", resultado_bnb_sub.path(), f"| Coste: {resultado_bnb_sub.path_cost} | Generados: {generated_bnb_sub} | Visitados: {visited_bnb_sub} | Tiempo: {tiempo_bnb_sub:.1f} μs")
