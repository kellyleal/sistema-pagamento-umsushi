# Use o mesmo arquivo onde a classe Carrinho está definida

class Carrinho:
    def __init__(self, usuario_id: str):
        self.usuario_id = usuario_id
        # Usa um DICIONÁRIO para armazenar o item e sua quantidade
        self._pedidos = {} 

    @property
    def itens(self):
        """Retorna uma lista dos itens no carrinho para visualização."""
        return list(self._pedidos.items())

    def adicionar_item(self, item: ItemMenu, quantidade: int = 1):
        """Adiciona um item ao carrinho ou incrementa sua quantidade."""
        if quantidade <= 0:
            print("Quantidade deve ser positiva.")
            return

        # Se o item já existe, soma a quantidade. Senão, adiciona.
        self._pedidos[item] = self._pedidos.get(item, 0) + quantidade
        print(f"{quantidade}x '{item.nome}' adicionado(s) ao carrinho.")

    def remover_item(self, item: ItemMenu, quantidade: int = 1):
        """Remove uma certa quantidade de um item ou o remove completamente."""
        if item not in self._pedidos:
            print(f"'{item.nome}' não está no carrinho.")
            return

        if quantidade <= 0:
            print("Quantidade deve ser positiva.")
            return

        # Diminui a quantidade
        self._pedidos[item] -= quantidade

        # Se a quantidade for zerada ou negativa, remove o item do carrinho
        if self._pedidos[item] <= 0:
            del self._pedidos[item]
            print(f"Item '{item.nome}' removido do carrinho.")
        else:
            print(f"{quantidade}x '{item.nome}' removido(s). Restam: {self._pedidos[item]}.")


    def total_pedido(self) -> float:
        """Calcula o total considerando o preço de cada item e sua quantidade."""
        if not self._pedidos:
            return 0.0
        
        total = sum(item.preco * quantidade for item, quantidade in self._pedidos.items())
        return total
