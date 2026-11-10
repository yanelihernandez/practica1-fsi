# run.py
import time
import search

casos_evaluacion = [
    (1, 'Arad', 'A', 'Bucharest', 'B'),
    (2, 'Oradea', 'O', 'Eforie', 'E'),
    (3, 'Giurgiu', 'G', 'Zerind', 'Z'),
    (4, 'Neamt', 'N', 'Dobreta', 'D'),
    (5, 'Mehadia', 'M', 'Fagaras', 'F')
]

algoritmos = [
    ("Amplitud", search.breadth_first_graph_search),
    ("Profundidad", search.depth_first_graph_search),
    ("Ramificación y Acotación", search.branch_and_bound_graph_search),
    ("Ramificación y Acotación con subestimación", search.branch_and_bound_subestimation_graph_search)
]

print("=" * 105)
print("EVALUACIÓN EXPERIMENTAL: MÉTRICAS Y TIEMPOS DE EJECUCIÓN")
print("=" * 105)

for num_id, nom_orig, cod_orig, nom_dest, cod_dest in casos_evaluacion:
    print(f"\nID: {num_id} | Trayectoria: {nom_orig} ({cod_orig}) -> {nom_dest} ({cod_dest})")
    print("-" * 105)
    
    problema = search.GPSProblem(cod_orig, cod_dest, search.romania)
    
    for nombre_alg, func in algoritmos:
        t_inicio = time.perf_counter()
        nodo, gen, vis, exp = func(problema)
        t_fin = time.perf_counter()
        
        tiempo_ms = (t_fin - t_inicio) * 1000
        costo = nodo.path_cost if nodo else 0
        ruta_str = str(nodo.path()) if nodo else "[]"
        
        print(f"[{nombre_alg}]")
        print(f"Generados: {gen} | Visitados: {vis} | Costo total: {costo} | Tiempo: {tiempo_ms:.4f} ms (Expandidos: {exp})")
        print(f"Ruta: {ruta_str}\n")