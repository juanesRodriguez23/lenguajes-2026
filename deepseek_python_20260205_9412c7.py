class TrieNode:
    def __init__(self):
        self.children = {}      # Diccionario de nodos hijos
        self.is_end_of_word = False
        self.words = []         # Lista de palabras completas desde este nodo

class AutocompleteSystem:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        """Inserta una palabra en el Trie"""
        node = self.root
        word_lower = word.lower()
        
        for char in word_lower:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.words.append(word)  # Añadimos la palabra a cada nodo
        
        node.is_end_of_word = True
    
    def autocomplete(self, prefix, max_results=10):
        """Devuelve todas las palabras que comienzan con el prefijo"""
        node = self.root
        prefix_lower = prefix.lower()
        
        # Navegar hasta el último carácter del prefijo
        for char in prefix_lower:
            if char not in node.children:
                return []  # Prefijo no encontrado
            node = node.children[char]
        
        # Devolver las palabras almacenadas en este nodo (limitado por max_results)
        return sorted(set(node.words))[:max_results]
    
    def _collect_all_words(self, node, current_prefix):
        """Método auxiliar para recolectar todas las palabras desde un nodo"""
        words = []
        if node.is_end_of_word:
            words.append(current_prefix)
        
        for char, child_node in node.children.items():
            words.extend(self._collect_all_words(child_node, current_prefix + char))
        
        return words

# Ejemplo de uso con dataset de ejemplo
def demo_autocomplete():
    print("\n=== DEMO SISTEMA DE AUTOCOMPLETADO ===")
    
    # Crear sistema de autocompletado
    ac_system = AutocompleteSystem()
    
    # Lista de palabras de ejemplo (podría ser una lista más grande)
    palabras = [
        "python", "programación", "programa", "procesador", "proyecto",
        "java", "javascript", "json", "jupyter", "juego",
        "data", "database", "datos", "dato", "datacamp",
        "machine", "machine learning", "mac", "macbook", "macos",
        "web", "website", "webinar", "webrtc", "webpack"
    ]
    
    # Insertar todas las palabras
    for palabra in palabras:
        ac_system.insert(palabra)
    
    # Probar diferentes prefijos
    test_prefijos = ["pro", "ja", "dat", "mac", "web", "xyz"]
    
    for prefijo in test_prefijos:
        resultados = ac_system.autocomplete(prefijo)
        print(f"\nPrefijo: '{prefijo}'")
        print(f"Resultados ({len(resultados)}): {resultados}")
    
    # Demo interactiva
    print("\n--- Demo Interactiva ---")
    print("Escribe prefijos para autocompletar (escribe 'salir' para terminar)")
    
    while True:
        prefijo = input("\nIngresa un prefijo: ").strip()
        if prefijo.lower() == 'salir':
            break
        
        resultados = ac_system.autocomplete(prefijo)
        if resultados:
            print(f"Sugerencias para '{prefijo}':")
            for i, palabra in enumerate(resultados, 1):
                print(f"  {i}. {palabra}")
        else:
            print(f"No se encontraron sugerencias para '{prefijo}'")

if __name__ == "__main__":
    demo_autocomplete()