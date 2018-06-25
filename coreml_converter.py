import tfcoreml as tf_converter
tf_converter.convert(tf_model_path = 'mnist_model.pb',
                     mlmodel_path = 'mnist_model.mlmodel',
                     output_feature_names = ['predictions:0'],
                     input_name_shape_dict = {'x:0' : [1, 28, 28, 1]})