import yaml
import numpy as np
import matplotlib.pyplot as plt

def create_phonon_figure(
    band_files,
    colors=None,
    labels=None,
    branches_to_show=None,
    save_png=None,
    sym_labels=None  # optional custom symmetry point labels
):
    """
    Create a phonon dispersion figure using Matplotlib from YAML files.

    Parameters:
    - band_files: list of str, paths to phonon YAML files
    - colors: list of str, optional colors for each dataset
    - labels: list of str, optional labels for each dataset
    - branches_to_show: list of int, indices of branches to include (0-based)
    - save_png: str or None, file path to save the figure as PNG
    - sym_labels: list of str, optional symmetry point labels for x-axis

    Returns:
    - fig, ax: Matplotlib figure and axis
    """

    if colors is None:
        colors = ['black', 'blue', 'red', 'green', 'orange', 'purple']
    if labels is None:
        labels = [f"Dataset {i+1}" for i in range(len(band_files))]
    if branches_to_show is None:
        branches_to_show = []  # plot all branches if empty

    fig, ax = plt.subplots(figsize=(6, 6))
    all_freqs = []
    segment_positions = []

    # Collect segment start positions for symmetry lines
    for band_file in band_files:
        with open(band_file) as f:
            data = yaml.safe_load(f)
        phonons = data["phonon"]
        seg_nq = data.get("segment_nqpoint", [len(phonons)])
        start_idx = 0
        for seg_len in seg_nq:
            segment_positions.append(phonons[start_idx]["distance"])
            start_idx += seg_len

    # Plot all datasets
    for file_idx, band_file in enumerate(band_files):
        with open(band_file) as f:
            data = yaml.safe_load(f)

        phonons = data["phonon"]
        n_bands = len(phonons[0]["band"])
        seg_nq = data.get("segment_nqpoint", [len(phonons)])

        # Plot segment by segment
        start = 0
        first_branch = True
        for seg_len in seg_nq:
            segment = phonons[start:start+seg_len]
            start += seg_len

            x_vals = [p["distance"] for p in segment]
            freqs = np.array([[b["frequency"] * 4.1357 for b in p["band"]] for p in segment]).T
            all_freqs.append(freqs)

            # Determine branches
            branch_indices = branches_to_show if branches_to_show else range(min(6, n_bands))

            for i in branch_indices:
                branch = freqs[i]

                # First dataset wide & transparent
                if file_idx == 0:
                    lw, alpha, ls = 1.5, 1, "dashed"
                else:
                    lw, alpha, ls = 1, 0.7, "solid"

                ax.plot(
                    x_vals, branch,
                    color=colors[file_idx % len(colors)],
                    linewidth=lw,
                    alpha=alpha,
                    linestyle=ls,
                    label=labels[file_idx] if first_branch else None
                )
                first_branch = False

    # Flatten all frequencies for y-limits
    all_freqs_flat = np.concatenate(all_freqs).flatten()
    min_freq, max_freq = all_freqs_flat.min(), all_freqs_flat.max()

    # Vertical dashed lines at segment positions
    for x in segment_positions:
        ax.axvline(x=x, color='black', linestyle='--', linewidth=1)

    # X-axis labels
    xticks_pos = [
        segment_positions[0],
        segment_positions[1],
        segment_positions[2],
        phonons[-1]["distance"]]
        
    sym_labels = ['Γ', 'M', 'K', 'Γ']

    ax.set_xticks(xticks_pos)
    ax.set_xticklabels(sym_labels)

    # Labels, title, limits
    ax.set_ylabel("$\hbar\omega$ [meV]")
    ax.set_xlim(phonons[0]["distance"], phonons[-1]["distance"])
    # ax.set_ylim(in_freq - 1, max_freq + 1)
    ax.legend()
    ax.grid(False)

    if save_png:
        fig.savefig(save_png, dpi=300, bbox_inches='tight')

    return fig, ax



fig = create_phonon_figure(
    band_files=["./phonon_data/bi_AB_0/6-WTe2/band-mono-vasp.yaml", "./phonon_data/bi_AB_0/6-WTe2/band-mono-omat-small.yaml",
                "./phonon_data/bi_AB_0/6-WTe2/band-mono-omat-small-ft.yaml"],
    colors=["black", "blue", "orange"],
    labels=["DFT", "MACE-OMAT-small", "MACE-OMAT-small-FT"],
    branches_to_show = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
    save_png="phonon_WTe2_bi_AB0.png"
)