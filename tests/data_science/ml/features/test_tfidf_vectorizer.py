from scipy.sparse import csr_matrix

from data_science.ml.features.tfidf_vectorizer import (
    TfidfVectorizerAdapter,
)

def test_fit_transform_returns_sparse_matrix():
    # Arrange
    documents = [
        "python es un lenguaje",
        "java es otro lenguaje",
        "python y java",
    ]
    vectorizer = TfidfVectorizerAdapter()

    # Act
    X = vectorizer.fit_transform(documents)

    # Assert
    assert isinstance(X, csr_matrix)
    assert X.shape[0] == len(documents)
    assert X.shape[1] > 0
    assert X.nnz > 0