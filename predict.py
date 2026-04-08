import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Load model
model = load_model('model/plant_model.h5')

IMG_SIZE = (224, 224)

def predict_image(img_path):
    img = image.load_img(img_path, target_size=IMG_SIZE)
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)[0][0]

    if prediction > 0.5:
        return f"🌿 Poisonous ({prediction*100:.2f}%)"
    else:
        return f"✅ Non-Poisonous ({(1-prediction)*100:.2f}%)"

# Test
print(predict_image("test.jpg"))
