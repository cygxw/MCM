from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd


def main():
    project_dir = Path(__file__).resolve().parent
    stations = pd.read_csv(project_dir / "data" / "stations.csv")

    for row in stations.itertuples(index=False):
        print(f"station={row.station}, count={row.count}")
    print(f"Mean: {stations['count'].mean():g} rentals/station")

    figures_dir = project_dir / "figures"
    figures_dir.mkdir(exist_ok=True)
    figure, axis = plt.subplots(figsize=(6, 4))
    axis.bar(stations["station"].astype(str), stations["count"])
    axis.set_xlabel("Station")
    axis.set_ylabel("Count (rentals)")
    figure.tight_layout()

    output_path = figures_dir / "stations.png"
    figure.savefig(output_path, dpi=150)
    plt.close(figure)
    print(f"Saved plot: {output_path}")


if __name__ == "__main__":
    main()
