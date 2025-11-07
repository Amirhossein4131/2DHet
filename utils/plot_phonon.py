import yaml
import numpy as np
import plotly.graph_objects as go

def create_phonon_figure(band_files, colors=None, labels=None, branches_to_show=None):
    """
    Create a phonon dispersion Plotly figure from YAML files.

    Parameters:
    - band_files: list of str, paths to phonon YAML files
    - colors: list of str, optional colors for each dataset
    - labels: list of str, optional labels for each dataset
    - branches_to_show: list of int, indices of branches to include (0-based)
    
    Returns:
    - fig: plotly.graph_objects.Figure
    """

    if colors is None:
        colors = ['black', 'blue']
    if labels is None:
        labels = [f"Dataset {i+1}" for i in range(len(band_files))]
    if branches_to_show is None:
        branches_to_show = []  # empty list means plot all branches

    fig = go.Figure()
    
    for file_idx, band_file in enumerate(band_files):
        with open(band_file) as f:
            data = yaml.safe_load(f)

        phonons = data["phonon"]
        n_bands = len(phonons[0]["band"])
        seg_nq = data.get("segment_nqpoint", [len(phonons)])

        # Collect symmetry point labels and positions
        sym_labels, sym_pos = [], []
        for p in phonons:
            if "label" in p:
                lbl = p["label"].replace("G", r"$\Gamma$")
                sym_labels.append(lbl)
                sym_pos.append(p["distance"])

        # Deduplicate labels/positions
        unique_labels, unique_pos = [], []
        for lbl, x in zip(sym_labels, sym_pos):
            if not unique_pos or abs(x - unique_pos[-1]) > 1e-8:
                unique_labels.append(lbl)
                unique_pos.append(x)

        # Plot segment by segment
        start = 0
        first_branch_plotted = False
        for seg_n in seg_nq:
            segment = phonons[start:start+seg_n]
            start += seg_n

            x_vals = [p["distance"] for p in segment]
            freqs = np.array([[b["frequency"] * 4.1357 for b in p["band"]] for p in segment]).T

            # Determine which branches to plot
            branch_indices = branches_to_show if branches_to_show else range(n_bands)

            for i in branch_indices:
                branch = freqs[i]
                # Only label the first branch of each dataset once
                if not first_branch_plotted:
                    fig.add_trace(go.Scatter(
                        x=x_vals, y=branch, mode='lines',
                        line=dict(color=colors[file_idx], width=2),
                        name=labels[file_idx]
                    ))
                    first_branch_plotted = True
                else:
                    fig.add_trace(go.Scatter(
                        x=x_vals, y=branch, mode='lines',
                        line=dict(color=colors[file_idx], width=2),
                        showlegend=False
                    ))

    # Add vertical lines at symmetry points
    for x in unique_pos:
        fig.add_shape(
            type="line",
            x0=x, y0=min(freqs.flatten()), x1=x, y1=max(freqs.flatten()),
            line=dict(color="gray", width=1, dash="dash")
        )

    # Update layout
    fig.update_layout(
        title="Phonon Dispersion",
        xaxis_title="q-point",
        yaxis_title=r"Energy [meV]",
        template="plotly_white",
        xaxis=dict(tickvals=unique_pos, ticktext=unique_labels),
    )

    return fig
