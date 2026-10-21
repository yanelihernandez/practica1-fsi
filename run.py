import time
import search

def medir_algoritmo(nombre, funcion_busqueda, problema):
    """
    Ejecuta un algoritmo de busqueda midiendo su tiempo de ejecucion en milisegundos,
    coste de la ruta, nodos expandidos y camino obtenido.
    """
    t_inicio = time.perf_counter()
    nodo_solucion, expandidos = funcion_busqueda(problema)
    t_fin = time.perf_counter()
    
    tiempo_ms = (t_fin - t_inicio) * 1000  # Convertimos a milisegundos
    
    if nodo_solucion:
        # Reconstruimos el camino invirtiendo la lista (origen -> destino)
        camino = [n.state for n in nodo_solucion.path()]
        camino.reverse()
        coste = nodo_solucion.path_cost
    else:
        camino = []
        coste = float('inf')
        
    return {
        "nombre": nombre,
        "coste": coste,
        "expandidos": expandidos,
        "tiempo_ms": tiempo_ms,
        "camino": camino
    }

def evaluar_trayectoria(origen, destino):
    print("=" * 115)
    print(f"PROBLEMA EVALUADO: Ruta de '{origen}' a '{destino}'")
    print("=" * 115)
    
    problema = search.GPSProblem(origen, destino, search.romania)
    
    algoritmos = [
        ("Primero en Anchura (BFS)", search.breadth_first_graph_search),
        ("Primero en Profundidad (DFS)", search.depth_first_graph_search),
        ("Ramif. y Acotación (RyA)", search.branch_and_bound_graph_search),
        ("RyA con Subestimación (A*)", search.branch_and_bound_subestimation_graph_search)
    ]
    
    resultados = []
    for nombre, fn in algoritmos:
        res = medir_algoritmo(nombre, fn, problema)
        resultados.append(res)
        
    # Cabecera de la tabla comparativa
    print(f"{'Algoritmo':<30} | {'Coste':<6} | {'Expandidos':<10} | {'Tiempo (ms)':<12} | {'Camino Solución'}")
    print("-" * 115)
    
    for r in resultados:
        camino_str = " -> ".join(r["camino"])
        print(f"{r['nombre']:<30} | {r['coste']:<6} | {r['expandidos']:<10} | {r['tiempo_ms']:<12.4f} | {camino_str}")
        
    print()
    
    # Análisis de eficiencia RyA vs RyA con Subestimación
    rya = resultados[2]
    ryas = resultados[3]
    ahorro_nodos = rya['expandidos'] - ryas['expandidos']
    pct_ahorro = (ahorro_nodos / rya['expandidos'] * 100) if rya['expandidos'] > 0 else 0
    
    print(f">> Ahorro por Heurística (RyA vs RyA con Subestimación):")
    print(f"   * Nodos no expandidos: {ahorro_nodos} (-{pct_ahorro:.1f}%)")
    print(f"   * Optimalidad comprobada: {'Sí (coste idéntico)' if rya['coste'] == ryas['coste'] else 'No'}")
    print()


if __name__ == '__main__':
    # Batería de pruebas representativas en el mapa de Rumanía
    rutas_prueba = [
        ('A', 'B'),  # Arad -> Bucarest (Caso estándar de la asignatura)
        ('O', 'E'),  # Oradea -> Eforie (Travesía completa de noroeste a sureste)
        ('T', 'B'),  # Timisoara -> Bucarest (Ruta suroeste)
        ('D', 'N')   # Dobreta -> Neamt (Ruta sur a noreste)
    ]
    
    for origen, destino in rutas_prueba:
        evaluar_trayectoria(origen, destino)

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
