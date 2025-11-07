from utils.plot_phonon import create_phonon_figure
import plotly.io as pio

# Example YAML file
band_files = ["band.yaml"]  # Replace with your actual path

# Optional: set colors, labels, and branches to show
colors = ['blue']
labels = ['DFT']
branches_to_show = []  # empty means all branches

# Generate the figure
fig = create_phonon_figure(
    band_files=band_files,
    colors=colors,
    labels=labels,
    branches_to_show=branches_to_show
)

# Show in browser
fig.show()

# Optional: save as html
pio.write_html(fig, file="phonon_test.html", auto_open=True)
