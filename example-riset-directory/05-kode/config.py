IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32

TRAIN_DIR = "dataset/train"
TEST_DIR = "dataset/test"

EPOCHS = 20
LEARNING_RATE = 0.001
SEED = 42

NUM_CLASSES = 10

MODEL_PATH = "outputs/models/tomato_cnn.keras"
HISTORY_PATH = "outputs/history/history.pkl"
FIGURE_PATH = "outputs/figures"
EVALUATION_PATH = "outputs/evaluation"

# =====================================
# Grad-CAM
# =====================================

GRADCAM_PATH = "outputs/gradcam"

LAST_CONV_LAYER = "conv2d_2"