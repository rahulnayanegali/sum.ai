# Voice Assistant LLM

This project records meeting notes, summarizes them using a language model, and saves the summary to a DOCX file.

<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&random=false&width=435&lines=SUM.io;By+Team+R+Stack;Aspiring+AI%2FML+Developers" alt="Typing SVG" /></a>

"Welcome to sum.io, the AI-powered meeting summarization tool that's revolutionizing how teams communicate and collaborate. Created for the Llama 3 hackathon, sum.io addresses a common pain point in today's digital workplace: the need for efficient, accurate, and timely meeting summaries.

Our innovative application leverages the power of Llama 3 to provide real-time summarization of meetings, ensuring that no crucial information is lost. But we don't stop there. sum.io takes it a step further by automatically sending customized email summaries to relevant participants, keeping everyone in the loop, even those who couldn't attend.

Let's dive into what makes sum.io unique:

First, our application of technology. We've seamlessly integrated Llama 3's advanced language model into our platform, allowing for real-time transcription and summarization. This ensures that our summaries are not just fast, but also incredibly accurate and contextually relevant.

Second, the business value. In today's fast-paced work environment, time is money. sum.io saves countless hours that would otherwise be spent on manual note-taking and summary creation. It also improves team alignment and reduces miscommunication, leading to more efficient decision-making processes.

Third, our originality. While there are other summarization tools out there, sum.io stands out with its real-time capabilities and automated email distribution. We've created a comprehensive solution that doesn't just summarize, but actively enhances team communication.

Lastly, let's talk about the potential impact. sum.io isn't just a tool; it's a game-changer for businesses of all sizes. From small startups to large corporations, our solution can dramatically improve productivity, ensure better information retention, and facilitate smoother collaboration across teams and time zones.

In conclusion, sum.io represents the future of meeting management. By harnessing the power of Llama 3, we're not just summarizing meetings; we're transforming how teams communicate, collaborate, and succeed in the digital age.

Thank you for your time, and we look forward to your questions."


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
