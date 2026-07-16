import os
import cv2
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

def load_image(image_path, image_size):
    """
    Membaca gambar dan mengubahnya menjadi tensor
    yang siap digunakan oleh model.
    """

    image = tf.keras.utils.load_img(
        image_path,
        target_size=image_size
    )

    image = tf.keras.utils.img_to_array(image)

    image = image.astype("float32") / 255.0

    image = np.expand_dims(
        image,
        axis=0
    )

    return image

def predict_image(model, image):
    """
    Melakukan prediksi satu gambar.
    """

    prediction = model.predict(
        image,
        verbose=0
    )

    predicted_index = int(
        np.argmax(prediction[0])
    )

    confidence = float(
        np.max(prediction[0])
    )

    return (
        predicted_index,
        confidence,
        prediction
    )

def generate_heatmap(
    model,
    image,
    last_conv_layer_name
):
    """
    Membuat heatmap Grad-CAM.
    """

    # Pastikan model sudah dipanggil
    _ = model(image, training=False)

    # Bangun ulang forward pass secara manual (layer-by-layer)
    # supaya conv_output dan prediction berada di jalur graph yang SAMA.
    # Cara lama (pakai model.get_layer(name).output langsung) membuat
    # dua cabang komputasi terpisah di Keras 3 untuk model Sequential,
    # sehingga gradiennya None.
    x = model.inputs[0]
    conv_output_tensor = None
    for layer in model.layers:
        x = layer(x)
        if layer.name == last_conv_layer_name:
            conv_output_tensor = x

    if conv_output_tensor is None:
        raise ValueError(
            f"Layer '{last_conv_layer_name}' tidak ditemukan di model."
        )

    grad_model = tf.keras.Model(
        inputs=model.inputs,
        outputs=[conv_output_tensor, x]
    )

    with tf.GradientTape() as tape:

        conv_outputs, predictions = grad_model(
            image,
            training=False
        )

        predicted_index = tf.argmax(
            predictions[0]
        )

        class_score = predictions[:, predicted_index]

    # Hitung gradien
    gradients = tape.gradient(
        class_score,
        conv_outputs
    )

    # Validasi gradien
    if gradients is None:
        raise ValueError(
            "Gradients bernilai None. "
            "Periksa nama layer konvolusi terakhir."
        )

    # Global Average Pooling pada gradien
    pooled_gradients = tf.reduce_mean(
        gradients,
        axis=(0, 1, 2)
    )

    # Ambil feature map
    conv_outputs = conv_outputs[0]

    # Kalikan setiap channel dengan bobot gradien
    heatmap = tf.reduce_sum(
        conv_outputs * pooled_gradients,
        axis=-1
    )

    # ReLU
    heatmap = tf.maximum(
        heatmap,
        0
    )

    # Normalisasi
    max_value = tf.reduce_max(
        heatmap
    )

    if max_value > 0:
        heatmap = heatmap / max_value

    return heatmap.numpy()

def save_gradcam(
    image_path,
    heatmap,
    output_dir,
    alpha=0.20
):
    """
    Menyimpan:
    - Original Image
    - Heatmap
    - Overlay
    """

    os.makedirs(output_dir, exist_ok=True)

    filename = os.path.splitext(
        os.path.basename(image_path)
    )[0]

    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    h, w = image.shape[:2]

    heatmap = cv2.resize(
        heatmap,
        (w, h)
    )

    heatmap_uint8 = np.uint8(255 * heatmap)

    heatmap_color = cv2.applyColorMap(
        heatmap_uint8,
        cv2.COLORMAP_JET
    )

    heatmap_color = cv2.cvtColor(
        heatmap_color,
        cv2.COLOR_BGR2RGB
    )

    overlay = cv2.addWeighted(
        image,
        1 - alpha,
        heatmap_color,
        alpha,
        0
    )

    # ==========================
    # Simpan Original
    # ==========================

    plt.figure(figsize=(6, 6))
    plt.imshow(image)
    plt.axis("off")
    plt.tight_layout()

    plt.savefig(
        os.path.join(
            output_dir,
            f"{filename}_original.png"
        ),
        dpi=300,
        bbox_inches="tight",
        pad_inches=0
    )

    plt.close()

    # ==========================
    # Simpan Heatmap
    # ==========================

    plt.figure(figsize=(6, 6))
    plt.imshow(heatmap_color)
    plt.axis("off")
    plt.tight_layout()

    plt.savefig(
        os.path.join(
            output_dir,
            f"{filename}_heatmap.png"
        ),
        dpi=300,
        bbox_inches="tight",
        pad_inches=0
    )

    plt.close()

    # ==========================
    # Simpan Overlay
    # ==========================

    plt.figure(figsize=(6, 6))
    plt.imshow(overlay)
    plt.axis("off")
    plt.tight_layout()

    plt.savefig(
        os.path.join(
            output_dir,
            f"{filename}_overlay.png"
        ),
        dpi=300,
        bbox_inches="tight",
        pad_inches=0
    )

    plt.close()

    print("\nGrad-CAM berhasil disimpan.")