import tkinter as tk
from tkinter import filedialog
from scapy.all import *
import networkx as nx
from bokeh.io import output_file, show
from bokeh.models import Plot, Range1d, MultiLine, Circle, HoverTool, BoxZoomTool, ResetTool, LabelSet, ColumnDataSource
from bokeh.plotting import from_networkx
from bokeh.palettes import Spectral4
import webbrowser

class PCAPAnalyzer(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("PCAP Network Map Generator")
        self.geometry("800x800")

        self.open_button = tk.Button(self, text="Open PCAP", command=self.open_pcap)
        self.open_button.pack(pady=20)

        self.generate_button = tk.Button(self, text="Generate Network Map", command=self.generate_map, state=tk.DISABLED)
        self.generate_button.pack(pady=20)

    def open_pcap(self):
        self.pcap_path = filedialog.askopenfilename(title="Select PCAP File", filetypes=[("PCAP Files", "*.pcap;*.pcapng")])
        if self.pcap_path:
            self.generate_button.config(state=tk.NORMAL)

    def generate_map(self):
        pcap = rdpcap(self.pcap_path)
        G = nx.DiGraph()

        for packet in pcap:
            if IP in packet:
                src_ip = packet[IP].src
                dst_ip = packet[IP].dst
                G.add_edge(src_ip, dst_ip)

        # Relabel nodes with integer labels
        mapping = {node: i for i, node in enumerate(G.nodes())}
        G_relabeled = nx.relabel_nodes(G, mapping)

        # Create a new position dictionary with integer keys
        pos = nx.spring_layout(G, k=0.15, iterations=20)
        pos_relabeled = {mapping[node]: pos[node] for node in pos}

        plot = Plot(width=400, height=400,
                    x_range=Range1d(-1.1, 1.1), y_range=Range1d(-1.1, 1.1))
        plot.title.text = "Network Map"

        graph_renderer = from_networkx(G_relabeled, pos_relabeled, scale=1, center=(0, 0))
        graph_renderer.node_renderer.glyph = Circle(size=15, fill_color=Spectral4[0])
        graph_renderer.edge_renderer.glyph = MultiLine(line_alpha=0.8, line_width=1)
        plot.renderers.append(graph_renderer)

        plot.add_tools(HoverTool(tooltips=None), BoxZoomTool(), ResetTool())


        source = ColumnDataSource(data=dict(
            x=[pos[0] for pos in pos.values()],
            y=[pos[1] for pos in pos.values()],
            label=list(G.nodes())
        ))

        # Create a LabelSet with the labels from the ColumnDataSource
        labels = LabelSet(x='x', y='y', text='label', source=source,
                  text_font_size='10pt', x_offset=5, y_offset=5)


        # Add the labels to the plot
        plot.add_layout(labels)
        
        output_file("network.html")
        show(plot)  # This will save the plot to network.html and open it in the web browser

        self.save_button = tk.Button(self, text="Save Network Map", command=lambda: self.save_map(plot))
        self.save_button.pack(pady=20)

    def save_map(self, plot):
        file_path = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML Files", "*.html")])
        if file_path:
            output_file(file_path)
            show(plot)

if __name__ == "__main__":
    app = PCAPAnalyzer()
    app.mainloop()
