import tfcoreml as tf_converter
import coremltools
coreml_model = tf_converter.convert(tf_model_path = 'mnist_model.pb',
                                    mlmodel_path = 'Mnist.mlmodel',
                                    input_name_shape_dict= {'x:0': [1, 28, 28, 1], 'y:0': [1, 10] },
                                    output_feature_names = ['predictions:0'],
                                    class_labels=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                                    image_input_names='x:0')
coreml_model.author = 'Luciano Almeida'
coreml_model.license = 'MIT'
coreml_model.short_description = 'A simple classifier of mnist handwritten digits'
coreml_model.save('Mnist.mlmodel')