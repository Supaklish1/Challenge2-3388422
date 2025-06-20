class SearchSuggestionSystem:

    def __init__(self, products: list[str]):
        """
        Initializes the system with a list of product names.
        The products list is sorted lexicographically for efficient suggestion retrieval.
        """
        self.products = sorted(products)

    def getSuggestions(self, searchWord: str) -> list[list[str]]:
        """
        Returns a list of lists. Each inner list contains up to 3 product names
        with the current prefix (based on characters typed so far in searchWord),
        sorted lexicographically.
        """
        result = []
        current_prefix = ""
        for char in searchWord:
            current_prefix += char
            suggestions_for_prefix = []
            
            # Iterate through the already sorted products to find matches
            for product in self.products:
                if product.startswith(current_prefix):
                    suggestions_for_prefix.append(product)
                
                # Optimization: if we already have 3 suggestions, we can stop for this prefix
                if len(suggestions_for_prefix) == 3:
                    break
            
            result.append(suggestions_for_prefix)
        
        return result