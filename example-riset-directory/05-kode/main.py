import time
import pandas as pd

from src.data.dataset_loader import load_dataset
from src.data.preprocessing import preprocess_dataset

from src.models.cnn_model import build_model
from src.models.train import compile_model, train_model

from src.evaluation.evaluate import evaluate_model

from src.utils.history import save_history
from src.visualization.plot_history import plot_history

from config import (
    HISTORY_PATH,
    FIGURE_PATH
)


def main():

    # =====================================
    # Mulai menghitung waktu eksekusi
    # =====================================
    start_time = time.time()

    print("=" * 60)
    print("Tomato Leaf Disease Classification using CNN")
    print("=" * 60)

    # =====================================
    # Load Dataset
    # =====================================

    train_ds, test_ds, class_names = load_dataset()

    print(f"\nJumlah kelas : {len(class_names)}")
    print(class_names)

    # =====================================
    # Preprocessing
    # =====================================

    train_ds, test_ds = preprocess_dataset(
        train_ds,
        test_ds
    )

    print("\nDataset berhasil diproses.")

    # =====================================
    # Build Model
    # =====================================

    model = build_model()

    print("\nModel Summary\n")
    model.summary()

    # =====================================
    # Compile Model
    # =====================================

    model = compile_model(model)

    # =====================================
    # Training Model
    # =====================================

    history = train_model(
        model,
        train_ds,
        test_ds
    )
    # ======================================
    # Simpan history ke CSV
    # ======================================

    history_df = pd.DataFrame(history.history)

    history_df.index += 1
    history_df.index.name = "epoch"

    history_df.to_csv(
    "outputs/history/history.csv"
    )

    print("\nHistory CSV berhasil disimpan.")

    # =====================================
    # Evaluasi Model
    # =====================================

    evaluation_result = evaluate_model(
        model,
        test_ds,
        class_names
    )
    # =====================================
    # Simpan Model
    # =====================================

    try:

        model.save("outputs/models/tomato_cnn.keras")

        print("\nModel berhasil disimpan.")

    except Exception as e:

        print("\nModel tidak berhasil disimpan.")
        print(e)
    # =====================================
    # Simpan History
    # =====================================

    save_history(
        history,
        HISTORY_PATH
    )

    # =====================================
    # Plot Accuracy & Loss
    # =====================================

    plot_history(
        HISTORY_PATH,
        FIGURE_PATH
    )

    # =====================================
    # Selesai
    # =====================================

    end_time = time.time()

    execution_time = end_time - start_time

    minutes = int(execution_time // 60)
    seconds = execution_time % 60

    print("\n============================================")
    print("Training selesai.")
    print(f"Waktu eksekusi : {minutes} menit {seconds:.2f} detik")
    print("============================================")

    return evaluation_result


if __name__ == "__main__":
    main()