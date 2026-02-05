class WebNavigator:
    def __init__(self):
        self.history = []      # Historial completo de páginas visitadas
        self.back_stack = []   # Páginas para retroceder
        self.forward_stack = [] # Páginas para avanzar
        self.current_page = None
    
    def load_page(self, url):
        """Carga una nueva página"""
        print(f"Cargando página: {url}")
        
        # Si hay una página actual, la movemos a la pila de retroceso
        if self.current_page:
            self.back_stack.append(self.current_page)
        
        # Establecemos la nueva página como actual
        self.current_page = url
        self.history.append(url)
        
        # Limpiamos la pila de avance cuando cargamos nueva página
        self.forward_stack.clear()
        
        return self.current_page
    
    def go_back(self):
        """Retrocede a la página anterior"""
        if not self.back_stack:
            print("No hay páginas anteriores para retroceder")
            return self.current_page
        
        # Movemos la página actual a la pila de avance
        if self.current_page:
            self.forward_stack.append(self.current_page)
        
        # Tomamos la última página del stack de retroceso
        self.current_page = self.back_stack.pop()
        print(f"Retrocediendo a: {self.current_page}")
        
        return self.current_page
    
    def go_forward(self):
        """Avanza a la página siguiente"""
        if not self.forward_stack:
            print("No hay páginas siguientes para avanzar")
            return self.current_page
        
        # Guardamos la página actual en el stack de retroceso
        if self.current_page:
            self.back_stack.append(self.current_page)
        
        # Tomamos la última página del stack de avance
        self.current_page = self.forward_stack.pop()
        print(f"Avanzando a: {self.current_page}")
        
        return self.current_page
    
    def get_history(self):
        """Devuelve el historial completo"""
        return self.history
    
    def get_current_page(self):
        """Devuelve la página actual"""
        return self.current_page

# Ejemplo de uso
def demo_navegador():
    print("=== DEMO SISTEMA DE NAVEGACIÓN ===")
    navegador = WebNavigator()
    
    # Cargar páginas
    navegador.load_page("google.com")
    navegador.load_page("facebook.com")
    navegador.load_page("twitter.com")
    
    print(f"\nPágina actual: {navegador.get_current_page()}")
    print(f"Historial: {navegador.get_history()}")
    
    # Retroceder
    navegador.go_back()  # Debería ir a facebook.com
    navegador.go_back()  # Debería ir a google.com
    
    # Intentar retroceder más allá del historial
    navegador.go_back()  # Debería mostrar mensaje de error
    
    # Avanzar
    navegador.go_forward()  # Debería ir a facebook.com
    navegador.go_forward()  # Debería ir a twitter.com
    
    # Intentar avanzar más allá del historial
    navegador.go_forward()  # Debería mostrar mensaje de error
    
    # Cargar nueva página (limpia forward stack)
    navegador.load_page("github.com")
    
    # Intentar avanzar después de nueva carga
    navegador.go_forward()  # No debería haber páginas para avanzar

if __name__ == "__main__":
    demo_navegador()