# Printable GIF 🎇

## Overview

The Printable GIF project is a tool that allows users to convert GIF animations into a printable image. This project takes a GIF file as input and generates an overlayed image of multiple frames, which movement can be seen through a moving frame.

## Reference video

- https://www.youtube.com/shorts/VQVPJLh7Bqc


## Installation

To install the Printable GIF project, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/Holeekey/printable_gif.git
    ```
2. Navigate to the project directory:
    ```sh
    cd printable_gif
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To run the script, use the following command:

```sh
python main.py --path C:/your/path/to/input.gif --frames 5 --offset 2 --output C:/your/path/to/output-folder --interval 1.5 --hm 20 --vm 15 --extension 2.0
```

## Parameters

- `--path`: **(Required)** The path to the GIF file to be processed.
  - **Example**: `--path ./input.gif`

- `--frames`: The number of frames to extract from the GIF.
  - **Default**: `5`
  - **Example**: `--frames 10`

- `--offset`: The number of frames to skip before starting to extract frames.
  - **Default**: `0`
  - **Example**: `--offset 2`

- `--output`: The output folder where the generated files will be saved.
  - **Default**: `./output`
  - **Example**: `--output ./output_folder`

- `--interval`: The interval width of the shown frame.
  - **Default**: `1`
  - **Example**: `--interval 1.5`

- `--hm`: The horizontal margin in pixels.
  - **Default**: `30`
  - **Example**: `--hm 20`

- `--vm`: The vertical margin in pixels.
  - **Default**: `10`
  - **Example**: `--vm 15`

- `--extension`: The moving frame extension in relation to the GIF width.
  - **Default**: `1.5`
  - **Example**: `--extension 2.0`

## Contributing

We welcome contributions to the Printable GIF project! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
