from sklearn.base import TransformerMixin, BaseEstimator

class DenseTransformer(TransformerMixin):
    """A sklearn transformer turning
    sparse matrix into dense ndarrays"""
    def fit(self, X, y=None, **fit_params):
        return self

    def transform(self, X, y=None, **fit_params):
        return X.todense()
    
class PassThrough(BaseEstimator, TransformerMixin):
    """A sklearn transforme just keeping the 
    input dataset as it is. 
    """
    def fit(self, X, y=None, **fit_params):
        return self

    def transform(self, X, y=None, **fit_params):
        return X

    
def print_raop_request(raop_request):
    """Take one row of our raop data frame and print it a nice way"""
    print(f"Requester got pizza : {raop_request.requester_received_pizza}")
    print("\n##########")
    print("request title")
    print("##########")
    print(raop_request.request_title)
    print("\n##########")
    print("request text edit aware")
    print("##########")
    print(raop_request.request_text_edit_aware)
    print("\n##########")
    print("request text")
    print("##########")
    print(raop_request.request_text)