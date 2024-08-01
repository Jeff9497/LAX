# LAX - Local AI eXecution

Welcome to the **LAX - Local AI eXecution** repository! This project provides a straightforward method for loading and running AI models locally on your machine. With this setup, you can interact with the GPT-2 model directly from your terminal, enabling a local AI execution environment.

## Overview

The repository contains a Python script that uses the `transformers` library to load and interact with the GPT-2 model. The script features a text generation function and a chat loop for real-time interaction.

  
## Requirements

### Hardware

- **CPU**: A modern multi-core processor is recommended.
- **RAM**: Minimum of 4GB of RAM required. 8GB or more is recommended for better performance.
- **Storage**: Sufficient disk space to download and store model weights (approximately 500MB for GPT-2).

### Software

- **Python**: Python 3.7 or later.
- **Dependencies**: The script requires the following Python packages:
  - `torch`
  - `transformers`

## Installation and Setup

1. **Clone the Repository**

   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Jeff9497/LAX.git
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd LAX
   ```

3. **Create and Activate a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

4. **Install the Required Packages**

   Install dependencies using `pip`:

   ```bash
   pip install torch transformers
   ```

## Running the Script

1. **Run the Script**

   ```bash
   python GPT2Model.py
   ```

2. **Interact with the Model**

   - Type your messages into the terminal and press Enter.
   - Type `exit` or `quit` to end the chat session.

## Future Updates

We plan to expand this repository by introducing additional AI models. Future updates will include options for:

- **GPT-2 XL**: An extended version of GPT-2 with more parameters for improved performance.
- **DistilBERT**: A lighter version of BERT for faster inference and lower resource consumption.
- **T5 (Text-To-Text Transfer Transformer)**: A versatile model for various NLP tasks.

You will be able to select and switch between these models according to your needs.

## Power and Performance Considerations

Running AI models locally requires significant computational resources. While the script can operate with 4GB of RAM, better performance is achieved with more RAM and a faster CPU. Ensure your machine meets the recommended specifications for optimal results.

## Contributing

Contributions are welcome! If you have suggestions, improvements, or encounter issues, please submit issues or pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, reach out to [your-email@example.com](mailto:jeffkamau9497@gmail.com).
