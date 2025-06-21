class SearchSuggestionSystem {
    constructor(products) {
        this.products = products.sort();
    }

    getSuggestions(searchWord) {
        const result = [];
        let currentPrefix = "";

        for (let i = 0; i < searchWord.length; i++) {
            currentPrefix += searchWord[i];
            const suggestionsForPrefix = [];

            for (const product of this.products) {
                if (product.startsWith(currentPrefix)) {
                    suggestionsForPrefix.push(product);
                }

                if (suggestionsForPrefix.length === 3) {
                    break;
                }
            }
            result.push(suggestionsForPrefix);
        }

        return result;
    }
}