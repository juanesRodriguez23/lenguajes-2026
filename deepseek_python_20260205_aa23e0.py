from collections import defaultdict
from typing import List, Dict, Set

class ProductRecommendationSystem:
    def __init__(self):
        # Estructuras de datos para almacenar relaciones
        self.user_purchases = defaultdict(set)  # usuario -> set(productos comprados)
        self.product_users = defaultdict(set)   # producto -> set(usuarios que lo compraron)
        self.all_products = set()              # Conjunto de todos los productos
    
    def add_purchase(self, user_id: str, product_id: str):
        """Registra una compra de un usuario"""
        # Actualizar compras del usuario
        self.user_purchases[user_id].add(product_id)
        
        # Actualizar usuarios que compraron el producto
        self.product_users[product_id].add(user_id)
        
        # Añadir producto a la lista de todos los productos
        self.all_products.add(product_id)
        
        print(f"Compra registrada: Usuario '{user_id}' compró '{product_id}'")
    
    def get_recommendations(self, user_id: str, max_recommendations: int = 5) -> List[str]:
        """Obtiene recomendaciones para un usuario basado en compras similares"""
        if user_id not in self.user_purchases:
            print(f"Usuario '{user_id}' no encontrado")
            return []
        
        # Productos ya comprados por el usuario
        user_products = self.user_purchases[user_id]
        
        if not user_products:
            return []
        
        # Contador de productos recomendados
        product_scores = defaultdict(int)
        
        # Para cada producto comprado por el usuario
        for product in user_products:
            # Buscar usuarios que también compraron este producto
            users_who_bought = self.product_users[product]
            
            # Para cada usuario que también compró este producto
            for other_user in users_who_bought:
                if other_user == user_id:
                    continue  # Saltar al mismo usuario
                
                # Obtener productos comprados por el otro usuario
                other_user_products = self.user_purchases[other_user]
                
                # Incrementar puntuación para productos que el usuario actual NO ha comprado
                for other_product in other_user_products:
                    if other_product not in user_products:
                        product_scores[other_product] += 1
        
        # Ordenar productos por puntuación (de mayor a menor)
        sorted_products = sorted(product_scores.items(), key=lambda x: x[1], reverse=True)
        
        # Tomar los productos mejor puntuados
        recommendations = [product for product, score in sorted_products[:max_recommendations]]
        
        return recommendations
    
    def get_similar_users(self, user_id: str) -> List[str]:
        """Encuentra usuarios con patrones de compra similares"""
        if user_id not in self.user_purchases:
            return []
        
        user_products = self.user_purchases[user_id]
        user_similarity = defaultdict(int)
        
        # Buscar productos comprados por el usuario
        for product in user_products:
            # Para cada usuario que también compró este producto
            for other_user in self.product_users[product]:
                if other_user != user_id:
                    user_similarity[other_user] += 1
        
        # Ordenar por similitud
        similar_users = sorted(user_similarity.items(), key=lambda x: x[1], reverse=True)
        
        return [user for user, score in similar_users]
    
    def get_popular_products(self, top_n: int = 5) -> List[str]:
        """Obtiene los productos más populares"""
        if not self.product_users:
            return []
        
        # Contar compras por producto
        product_counts = {product: len(users) for product, users in self.product_users.items()}
        
        # Ordenar por popularidad
        sorted_products = sorted(product_counts.items(), key=lambda x: x[1], reverse=True)
        
        return [product for product, count in sorted_products[:top_n]]

# Ejemplo de uso
def demo_recomendacion():
    print("\n=== DEMO SISTEMA DE RECOMENDACIÓN ===")
    
    # Crear sistema de recomendación
    rec_system = ProductRecommendationSystem()
    
    # Datos de ejemplo: compras de usuarios
    compras = [
        ("usuario1", "laptop"),
        ("usuario1", "mouse"),
        ("usuario1", "teclado"),
        ("usuario2", "laptop"),
        ("usuario2", "monitor"),
        ("usuario2", "webcam"),
        ("usuario3", "tablet"),
        ("usuario3", "fundas"),
        ("usuario3", "mouse"),
        ("usuario4", "smartphone"),
        ("usuario4", "fundas"),
        ("usuario4", "cargador"),
        ("usuario5", "laptop"),
        ("usuario5", "monitor"),
        ("usuario5", "webcam"),
        ("usuario5", "altavoces"),
    ]
    
    # Registrar todas las compras
    for usuario, producto in compras:
        rec_system.add_purchase(usuario, producto)
    
    print("\n" + "="*50)
    
    # Obtener recomendaciones para cada usuario
    usuarios = ["usuario1", "usuario2", "usuario3", "usuario4", "usuario5"]
    
    for usuario in usuarios:
        print(f"\nRecomendaciones para {usuario}:")
        recomendaciones = rec_system.get_recommendations(usuario)
        
        if recomendaciones:
            for i, producto in enumerate(recomendaciones, 1):
                print(f"  {i}. {producto}")
        else:
            print("  No hay recomendaciones disponibles")
    
    print("\n" + "="*50)
    
    # Mostrar productos más populares
    print("\nProductos más populares:")
    populares = rec_system.get_popular_products()
    for i, producto in enumerate(populares, 1):
        usuarios_producto = rec_system.product_users[producto]
        print(f"  {i}. {producto} ({len(usuarios_producto)} compras)")
    
    print("\n" + "="*50)
    
    # Mostrar usuarios similares
    print("\nUsuarios similares:")
    for usuario in usuarios[:3]:  # Solo primeros 3 para no saturar
        similares = rec_system.get_similar_users(usuario)
        if similares:
            print(f"  Usuarios similares a {usuario}: {', '.join(similares[:3])}")
    
    # Demo de nueva compra y actualización de recomendaciones
    print("\n--- Simulación de nueva compra ---")
    rec_system.add_purchase("usuario1", "webcam")
    
    print(f"\nNuevas recomendaciones para usuario1:")
    nuevas_rec = rec_system.get_recommendations("usuario1")
    for i, producto in enumerate(nuevas_rec, 1):
        print(f"  {i}. {producto}")

if __name__ == "__main__":
    # Ejecutar todas las demostraciones
    demo_navegador()
    demo_autocomplete()
    demo_recomendacion()