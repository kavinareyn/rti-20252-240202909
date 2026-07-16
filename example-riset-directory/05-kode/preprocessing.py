import tensorflow as tf

AUTOTUNE = tf.data.AUTOTUNE


def preprocess_dataset(train_ds, test_ds):

    normalization = tf.keras.layers.Rescaling(1.0 / 255)

    train_ds = train_ds.map(
        lambda x, y: (normalization(x), y),
        num_parallel_calls=AUTOTUNE
    )

    test_ds = test_ds.map(
        lambda x, y: (normalization(x), y),
        num_parallel_calls=AUTOTUNE
    )

    train_ds = train_ds.cache().prefetch(AUTOTUNE)
    test_ds = test_ds.cache().prefetch(AUTOTUNE)

    return train_ds, test_ds