##########################
# Cifar10 이미지 추출
##########################
'''
호출 방법: 
cifar10_dataset_file_path = 'test_batch'
features, labels = load_cfar10_batch(cifar10_dataset_file_path)        

sample_id = 10
feature, label = display_img(features,labels, sample_id )
참조 소스:
CIFAR-10 Image Classification in TensorFlow
- https://towardsdatascience.com/cifar-10-image-classification-in-tensorflow-5b501f7dc77c
'''
import sys
import pickle 
import matplotlib.pyplot as plt




def load_label_names():
    return ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

def load_cfar10_batch(file_name):
    print("file_name: ", file_name)
    with open(file_name, mode='rb') as file:
        # note the encoding type is 'latin1'
        batch = pickle.load(file, encoding='latin1')
        
    features = batch['data'].reshape((len(batch['data']), 3, 32, 32)).transpose(0, 2, 3, 1)
    labels = batch['labels']
        
    return features, labels
    

def display_img(features,labels, sample_id ):
        
    label_names = load_label_names()
    
    sample_image = features[sample_id]
    sample_label = labels[sample_id]
    
    print('\nExample of Image {}:'.format(sample_id))
    print('Image - Shape: {}'.format(sample_image.shape))
    print('Label - Label Id: {} Name: {}'.format(sample_label, label_names[sample_label]))
    
    plt.imshow(sample_image)    
    return sample_image, sample_label


