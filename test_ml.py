import pytest
# TODO: add necessary import
import pickle
from sklearn.ensemble import RandomForestClassifier
from ml.model import save_model, load_model, train_model

# TODO: implement the first test. Change the function name and input as needed
def test_save_model(tmp_path):
    """
    # add description for the first test
    # tests the model saving function with pickle
    """
    #making simple test model
    model = RandomForestClassifier().fit([[0], [1]], [0, 1])

    #calling save function
    file_path = tmp_path / "model.pkl" #temp path
    save_model(model, file_path)

    #checking for file
    assert file_path.exists(), "File not created"


# TODO: implement the second test. Change the function name and input as needed
def test_load_model(tmp_path):
    """
    # add description for the second test
    # tests the model loading function with pickle
    """
    #creating a test model
    model = RandomForestClassifier().fit([[0], [1]], [0, 1])
    file_path = tmp_path / "model.pkl" #temp path
    save_model(model, file_path)

    #calling load function
    loaded_model = load_model(file_path)

    #checking if load succeeded
    assert loaded_model is not None, "No model was loaded"

    #checking if loaded model
    assert hasattr(loaded_model, 'predict'), "Model missing 'predict' method"

    


# TODO: implement the third test. Change the function name and input as needed
def test_train_model():
    """
    # add description for the third test
    # tests to see if model training works
    """
    #test training data
    X_train = [[0], [1], [2], [3]]
    y_train = [0, 1, 2, 3]

    #training
    model = train_model(X_train, y_train)

    #was model returned
    assert model is not None, "train_model() returned None"

    #proper model was used
    assert hasattr(model, "predict"), "Returned object lacks predict method"

    #checking predictions
    preds = model.predict([[4]])
    assert preds[0] == 3, "Classifier did not correctly predict from input"
