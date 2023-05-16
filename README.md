# Plain Image Generator

The Plain Image Generator is a Python script that generates plain color images of custom dimensions and colors. It can be used to create images for testing purposes, placeholder images, or any other application that requires simple plain color images.

## Features

- Generate plain color images with custom width, height, and color.
- Add dimensions text to the generated images.
- Save the generated images as JPEG files.
- Simple and easy-to-use command-line interface.

## Prerequisites

Before running the script, make sure you have the following dependencies installed:

- Python 3.x
- PIL (Python Imaging Library)
- tqdm (for the progress bar animation)

You can install the dependencies by running the following command:

```
pip install -r requirements.txt
```

## Usage

To generate a plain color image, run the following command:

```
python app.py --width <width> --height <height> --color <color>
```

Replace `<width>`, `<height>`, and `<color>` with your desired values. Here are some examples:

```
python app.py --width 500 --height 500 --color red
```
```
python app.py --width 800 --height 400 --color #00ff00
```
```
python app.py --width 300 --height 200 --color rgb(100, 150, 200)
```

The generated image will be saved in the `output` directory with a unique filename.

## Configuration

You can configure the font used for the dimensions text by replacing the `arial.ttf` file in the `assets` directory with your desired TrueType font file.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to use and modify this script according to your needs.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please create an issue or submit a pull request.

## Acknowledgements

This project uses the following libraries:

- [PIL (Python Imaging Library)](https://pillow.readthedocs.io/)
- [tqdm](https://github.com/tqdm/tqdm)

## Author

[Shah Swood](https://github.com/shahsawoodshinwari)
