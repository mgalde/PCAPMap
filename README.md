# PCAPMap

PCAPMap is a graphical tool designed to visualize network traffic captured in PCAP files. By leveraging the power of Python and libraries such as Tkinter, Scapy, NetworkX, and Bokeh, PCAPMap provides an intuitive interface for users to load PCAP files, generate network maps, and interact with the visualized data.

## Getting Started

### Prerequisites

Ensure you have the following installed on your machine:

- Python 3.x
- Tkinter
- Scapy
- NetworkX
- Bokeh

![image](https://github.com/mgalde/PCAPMap/assets/30883926/4cc093b4-f750-448e-80f5-d23099a8de84)

You can install the necessary libraries using pip:

```bash
pip install scapy networkx bokeh
```

### Installation

1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Run the `PCAPAnalyzer.py` script to launch the application.

## Usage

1. Launch the application by executing the `PCAPAnalyzer.py` script.
2. Click on the "Open PCAP" button to load a PCAP file.
3. Once a PCAP file is loaded, the "Generate Network Map" button will become active. Click on it to generate the network map.
4. The network map will be displayed in a new browser tab.
5. Optionally, click on the "Save Network Map" button to save the network map to an HTML file.
6. Click on the "Exit" button to close the application.

![image](https://github.com/mgalde/PCAPMap/assets/30883926/e377bad0-70e9-4ff4-afeb-d675c8dfb3ce)



![image](https://github.com/mgalde/PCAPMap/assets/30883926/0ec7b546-99e7-46fd-a0ab-ec27c538b989)


## Limitations

- The program may struggle with very large PCAP files due to memory and processing limitations.
- The generated network map is static and does not support real-time updates.
- The visualization may become cluttered and hard to interpret with a high number of nodes and edges.

## Contributing

Feel free to fork the project, open issues, and submit pull requests. Your contributions are welcome!

## License

[MIT License](LICENSE)
