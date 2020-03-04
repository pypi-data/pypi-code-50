import tensorflow as tf, numpy as np 

### consider having functions below in models.AuxiliaryFunctions 
def custom_metric(y_true, y_pred): 
    return tf.keras.backend.mean(y_pred, axis=1) 
def custom_loss(y_true, y_pred): 
    return tf.math.reduce_sum(y_pred, axis=0) 
def dummy_loss(y_true, y_pred): 
    return float(0) 

def TrainCLModel(model_params, Dtrain, Dval, i): 
    ### train CL model depending on the type given in model_params 
    
    ### Input: 
    ###   model_params - dictionary of model parameters 
    ###   Dtrain - dict() containing training data
    ###   i - integer, ith itheration of random initialization (for fix keras naming issue) 
    
    ### Return:
    ###   trained_model - the trained model data structure (keras/sklearn)
    ###   val_loss - validation loss of this model on validation set
        
    if model_params['model_name'] == 'DPCM':
        trained_model = DefineKerasDPCMModel(Dtrain['D_tre'].shape[1], 1, Dtrain['D_tre'].shape[0], \
                             activation=tf.nn.tanh, quantile=model_params['quantile'], temp=model_params['temp'])
    elif model_params['model_name'] == 'STC':
        trained_model = DefineKerasSimpleTCModel(Dtrain['D_tre'].shape[1], 1, Dtrain['D_tre'].shape[0], activation=tf.nn.tanh)
    
    opt = tf.keras.optimizers.Adam(learning_rate=0.01) 
        
    ### this part is a temporary solution for the naming of output node in Keras 
    if i == 0: 
        main_output_str = 'tf_op_layer_main_output' 
    else: 
        main_output_str = 'tf_op_layer_main_output_'+str(i) 
    
    trained_model.compile(loss={main_output_str:custom_loss, 'score_output':dummy_loss}, 
                                   loss_weights={main_output_str:1.0, 'score_output':0.0}, 
                                   optimizer=opt) 
    
    y_train_zeros = np.zeros((Dtrain['D_tre'].shape[0], 1)) ## used to create absolute difference to zero and minimize 
    y_val_zeros = np.zeros((Dval['D_tre'].shape[0], 1)) ## used to create absolute difference to zero and minimize
    print('->fitting model for '+str(model_params['num_optimize_iterations'])+' iterations')
    history = trained_model.fit([\
                                 Dtrain['D_tre'], Dtrain['D_unt'], \
                                 Dtrain['c_tre'], Dtrain['c_unt'], \
                                 Dtrain['o_tre'], Dtrain['o_unt'] \
                                ],\
                                [y_train_zeros, y_train_zeros], \
                                validation_data=[[Dval['D_tre'], Dval['D_unt'], \
                                                  Dval['c_tre'], Dval['c_unt'], \
                                                  Dval['o_tre'], Dval['o_unt']], \
                                                 [y_val_zeros, y_val_zeros]\
                                ], \
                                batch_size=Dtrain['D_tre'].shape[0], \
                                epochs=model_params['num_optimize_iterations'], \
                                validation_freq=model_params['num_optimize_iterations'], ## not much need to be customized \
                                verbose=0)
    
    return trained_model, history.history['val_loss'][-1]

def DefineKerasSimpleTCModel(input_dim, num_hidden, sample_size, activation=tf.nn.tanh): 
    ## define the simple TC model from scratch
    
    inputs_tr = tf.keras.Input(shape=(input_dim,)) 
    inputs_co = tf.keras.Input(shape=(input_dim,)) 
    #print('inputs_tr :' + str(inputs_tr.shape)) 
    
    c_tr = tf.keras.Input(shape=(1,)) 
    c_co = tf.keras.Input(shape=(1,)) 
    g_tr = tf.keras.Input(shape=(1,)) 
    g_co = tf.keras.Input(shape=(1,)) 
    
    weight_layer = tf.keras.layers.Dense(num_hidden, activation=activation, name='score_output') 
    x_tr = weight_layer(inputs_tr) 
    x_co = weight_layer(inputs_co) 
    #print('x_tr :' + str(x_tr.shape))
    
    scores = x_tr
    
    sm_layer_batchaxis = tf.keras.layers.Softmax(axis=0) 
    
    s_tr = sm_layer_batchaxis(x_tr) 
    s_co = sm_layer_batchaxis(x_co) 
    #print('s_tr :' + str(s_tr.shape))
    
    dc_tr = tf.reduce_sum(tf.multiply(s_tr, c_tr), axis=0) 
    dc_co = tf.reduce_sum(tf.multiply(s_co, c_co), axis=0) 
    
    dg_tr = tf.reduce_sum(tf.multiply(s_tr, g_tr), axis=0) 
    dg_co = tf.reduce_sum(tf.multiply(s_co, g_co), axis=0) 
    
    #print('dc_tr :' + str(dc_tr.shape))
    #print('dg_tr :' + str(dg_tr.shape))
    
    outputs = tf.divide(dc_tr - dc_co, dg_tr - dg_co, name='main_output') 
    
    #print('outputs :')
    #print(outputs)
    
    #print('outputs size : ' + str(outputs.shape))
    
    model = tf.keras.Model(inputs=[inputs_tr, inputs_co, c_tr, c_co, g_tr, g_co], outputs=[outputs, scores]) 
    return model 

def DefineKerasDPCMModel(input_dim, num_hidden, sample_size, activation=tf.nn.tanh, quantile=0.3, temp=2.0): 
    ## define the simple TC model from scratch 
    
    inputs_tr = tf.keras.Input(shape=(input_dim,)) 
    inputs_co = tf.keras.Input(shape=(input_dim,)) 
    #print('inputs_tr :' + str(inputs_tr.shape))
    
    c_tr = tf.keras.Input(shape=(1,)) 
    c_co = tf.keras.Input(shape=(1,)) 
    g_tr = tf.keras.Input(shape=(1,)) 
    g_co = tf.keras.Input(shape=(1,)) 
    
    weight_layer = tf.keras.layers.Dense(num_hidden, activation=activation, name='score_output') 
    x_tr = weight_layer(inputs_tr) 
    x_co = weight_layer(inputs_co) 
    #print('x_tr :' + str(x_tr.shape))
    
    scores = x_tr
    
    ### adopt a sorting operator that's also differentiable 
    ### for application of back-propagation and gradient optimization 
    h_tre_sorted = tf.sort(x_tr, axis=0, direction='DESCENDING') 
    h_unt_sorted = tf.sort(x_co, axis=0, direction='DESCENDING') 
    
    top_k_tre = tf.cast(tf.math.ceil(sample_size * quantile), tf.int32) 
    top_k_unt = tf.cast(tf.math.ceil(sample_size * quantile), tf.int32) 
    
    intercept_tre = tf.slice(h_tre_sorted, [top_k_tre - 1, 0], [1, 1]) 
    intercept_unt = tf.slice(h_unt_sorted, [top_k_unt - 1, 0], [1, 1]) 
    
    ### stop gradients at the tunable intercept for sigmoid 
    ### to stabilize gradient-based optimization 
    intercept_tre = tf.stop_gradient(intercept_tre) 
    intercept_unt = tf.stop_gradient(intercept_unt) 
    
    ### use sigmoid to threshold top-k candidates 
    h_tr = tf.math.sigmoid(temp * (x_tr - intercept_tre)) 
    h_co = tf.math.sigmoid(temp * (x_co - intercept_unt)) 
    
    sm_layer_batchaxis = tf.keras.layers.Softmax(axis=0) 
    
    s_tr = sm_layer_batchaxis(h_tr) 
    s_co = sm_layer_batchaxis(h_co) 
    #print('s_tr :' + str(s_tr.shape))
    
    dc_tr = tf.reduce_sum(tf.multiply(s_tr, c_tr), axis=0) 
    dc_co = tf.reduce_sum(tf.multiply(s_co, c_co), axis=0) 
    
    dg_tr = tf.reduce_sum(tf.multiply(s_tr, g_tr), axis=0) 
    dg_co = tf.reduce_sum(tf.multiply(s_co, g_co), axis=0) 
    
    #print('dc_tr :' + str(dc_tr.shape))
    #print('dg_tr :' + str(dg_tr.shape))
    
    outputs = tf.divide(dc_tr - dc_co, dg_tr - dg_co, name='main_output') 
    
    #print('outputs :')
    #print(outputs)
    
    #print('outputs size : ' + str(outputs.shape))
    
    model = tf.keras.Model(inputs=[inputs_tr, inputs_co, c_tr, c_co, g_tr, g_co], outputs=[outputs, scores]) 
    return model 
