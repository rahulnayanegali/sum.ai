# Voice Assistant LLM

This project records meeting notes, summarizes them using a language model, and saves the summary to a DOCX file.

## Prerequisites

- Python 3.9+
- Pip

## Installation

1. Clone the repository:
    ```sh
    git clone <your-repo-url>
    cd <your-repo-directory>
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Download the LLaMA model:
    ```sh
    python download_llama_model.py
    ```

## Usage

1. Run the main script:
    ```sh
    python app1.py
    ```

2. Follow the prompts to start and stop recording.

3. The summary will be saved to `summary.docx`.

## Files

- **app1.py**: Main script for recording and summarizing.
- **components.py**: Helper functions.
- **download_llama_model.py**: Downloads the LLaMA model.
- **requirements.txt**: Dependencies.

## Notes

- Ensure your microphone is configured properly.
- Adjust `buffer_limit` in `app1.py` to change how often text is saved.

## Troubleshooting

- Check internet connection for downloading models.
- Check microphone permissions if there are audio errors.

## License

MIT License
