# run.py
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

print("=" * 100)
print("EVALUACIÓN Y GENERACIÓN DE RESULTADOS PARA LA TABLA DE RUMANÍA")
print("=" * 100)

for num_id, nom_orig, cod_orig, nom_dest, cod_dest in casos_evaluacion:
    print(f"\nID: {num_id} | Trayectoria: {nom_orig} ({cod_orig}) -> {nom_dest} ({cod_dest})")
    print("-" * 100)
    
    problema = search.GPSProblem(cod_orig, cod_dest, search.romania)
    
    for nombre_alg, func in algoritmos:
        nodo, gen, vis, exp = func(problema)
        costo = nodo.path_cost if nodo else 0
        ruta_str = str(nodo.path()) if nodo else "[]"
        
        print(f"[{nombre_alg}]")
        # Formato exacto para copiar y pegar en la tabla .docx
        print(f"Generados: {gen} | Visitados: {vis} | Costo total: {costo} | Expandidos: {exp}")
        print(f"Ruta: {ruta_str}\n")