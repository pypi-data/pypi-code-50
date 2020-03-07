from numpy import *
import pandas as pd

def topk_performance(model,n_topk,x_train,y_train,x_test,y_test,yencoder):
    """
    This function computes Top-k performance results based on the given model and the train and test data. The function trains
    on the x data and the target value, and then runs the model on the test data. It selects k possible matches which have the
    highest probability of being a match. It then computes the positive prediction value (PPV) for each class, from worst to
    best, as well as the Top-k accuracy, where the model is considered a success if the the target class is one of the k
    matches selected by the model. Therefore, Top-k accuracy will have the highest probabiity because it includes all three
    classes. PPVs are calculated by by adding all the instances where the prediction was correct divided by the total number
    of predictions.
    
    Parameters
    ..........
    
    model: model object
    any model that returns prediction probabilities for each class

    n_topk: integer
    number of Top-k classes to predict

    x_train: dataframe
    x data (attributes) to train on

    y_train: dataframe
    target values to train on

    x_test: dataframe
    x data (attributes) to test the model

    y_test: dataframe
    target values to test the model

    yencoder: function
    encoder used to transform target values to classes
    """

    model.fit(x_train,y_train)
    y_pred = model.predict(x_test)
    cat_class = yencoder.inverse_transform(model.classes_)
    prob_vals = model.predict_proba(x_test)
    sort_ind = argsort(prob_vals, axis=1)[:,-n_topk:]
    prob_sort = array([x[i] for i,x in zip(sort_ind,prob_vals)])
    m_class_sort = model.classes_[sort_ind]
    class_sort = cat_class[sort_ind]
    accuracy = [0. for i in range(n_topk+1)]
    for_tup = [0. for i in range(n_topk+1)]
    
    for i in range(y_test.shape[0]):
        for j in range(n_topk+1):
            if j==n_topk:   
                if y_test[i] in m_class_sort[i,:n_topk]:
                    accuracy[j] += 1./y_test.shape[0]
                    for_tup[j] = 'Top-%d accuracy'%(j)
            else:
                if y_test[i] in m_class_sort[i,j:j+1]:
                    accuracy[j] += 1./y_test.shape[0]
                    for_tup[j] = 'PPV Rank %d'%(n_topk-j)
    p_res=list(zip(for_tup,accuracy))
    print('Performance {0}: {1}\n'.format(model.__class__.__name__,p_res))
                                                       
    return y_pred, p_res, class_sort, prob_sort


def best_topk_model(topk_models,n_topk,x_train,y_train,x_test,y_test,yencoder):
    """
    This function uses the topk_performance function above to compute Top-k accuracy measurements for different models and then
    selects the best performing model.
    
    Parameters
    ..........
    
    topk_models: model object list
    Models that return prediction probabilities for each class
    
    n_topk: integer
    number of Top-k classes to predict
    
    x_train: dataframe
    x data (attributes) to train on
    
    y_train: dataframe
    target values to train on
    
    x_test: dataframe
    x data (attributes) to test the model
    
    y_test: dataframe
    target values to test the model
    
    yencoder: function
    encoder used to transform target values to classes
    """
    
    model_prob_max, accuracy_max, best_model = 0., 0., ''
    for i in range(len(topk_models)):
        y_pred, p_res, class_sort, prob_sort = topk_performance(topk_models[i],n_topk,x_train,y_train,x_test,y_test,yencoder)
        if p_res[n_topk][1] > accuracy_max:
            accuracy_max = p_res[n_topk][1]
            model_prob_max = p_res
            best_model = topk_models[i].__class__.__name__
            ypred_max, p_res_max, class_sort_max, prob_sort_max = y_pred, p_res, class_sort, prob_sort       
    print('Best model: {0}, {1}\n'.format(best_model,model_prob_max))
    return ypred_max, p_res_max, class_sort_max, prob_sort_max
 
