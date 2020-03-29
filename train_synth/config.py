"""
Config containing all hardcoded parameters for training strong supervised model on synth-text
"""
from config import *


path_images = 'dataset/train_images'
path_labels = 'dataset/train.csv'
ratio_split = 0.8
#
num_cuda = "0"
save_path = './model'
use_cuda = True #False

batch_size = {
	'train': 4*len(num_cuda.split(',')),
	'test': 8*len(num_cuda.split(',')),
}

num_workers = {
	'train': 0,
	'test': 0
}

pretrained = True #False
pretrained_path = './model/original.pkl'
pretrained_loss_plot_training = './logs/loss_plot_training.npy'

optimizer_iteration = 4//len(num_cuda.split(','))

lr = {
	1: 1e-4,
	8000*optimizer_iteration: 5e-5,
	16000*optimizer_iteration: 2e-5,
	32000*optimizer_iteration: 1e-5,
	48000*optimizer_iteration: 1e-6,
}

num_epochs_strong_supervision = 1.2

periodic_fscore = 300*optimizer_iteration
periodic_output = 3000*optimizer_iteration
periodic_save = 3000*optimizer_iteration

visualize_generated = True
visualize_freq = 21000

weight_threshold = 0.5

model_architecture = 'craft'
