# YouTube Transcript Processing

This project processes YouTube video transcripts using the `youtube-transcript-api` and `llama-index` libraries. It retrieves transcripts, processes them, and saves the results to a local directory.

## Project Structure

```
.env .gitignore data-transcript/ buong-bo.txt g3CvsPAF3_0.txt jgnYTHYGNhI.txt README.md youtube-transcript.ipynb
```


## Requirements

- Python 3.10
- [`youtube-transcript-api`](command:_github.copilot.openSymbolFromReferences?%5B%22youtube-transcript-api%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2FUsers%2Fngocp%2FDocuments%2Fprojects%2Fpyml%2Fyoutube-summarize%2Fyoutube-transcript.ipynb%22%2C%22external%22%3A%22file%3A%2F%2F%2FUsers%2Fngocp%2FDocuments%2Fprojects%2Fpyml%2Fyoutube-summarize%2Fyoutube-transcript.ipynb%22%2C%22path%22%3A%22%2FUsers%2Fngocp%2FDocuments%2Fprojects%2Fpyml%2Fyoutube-summarize%2Fyoutube-transcript.ipynb%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A11%2C%22character%22%3A38%7D%7D%2C%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2FUsers%2Fngocp%2FDocuments%2Fprojects%2Fpyml%2Fyoutube-summarize%2Fyoutube-transcript.ipynb%22%2C%22external%22%3A%22file%3A%2F%2F%2FUsers%2Fngocp%2FDocuments%2Fprojects%2Fpyml%2Fyoutube-summarize%2Fyoutube-transcript.ipynb%22%2C%22path%22%3A%22%2FUsers%2Fngocp%2FDocuments%2Fprojects%2Fpyml%2Fyoutube-summarize%2Fyoutube-transcript.ipynb%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A150%2C%22character%22%3A18%7D%7D%5D%5D "Go to definition")
- [`llama-index`](command:_github.copilot.openSymbolFromReferences?%5B%22llama-index%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2FUsers%2Fngocp%2FDocuments%2Fprojects%2Fpyml%2Fyoutube-summarize%2Fyoutube-transcript.ipynb%22%2C%22external%22%3A%22file%3A%2F%2F%2FUsers%2Fngocp%2FDocuments%2Fprojects%2Fpyml%2Fyoutube-summarize%2Fyoutube-transcript.ipynb%22%2C%22path%22%3A%22%2FUsers%2Fngocp%2FDocuments%2Fprojects%2Fpyml%2Fyoutube-summarize%2Fyoutube-transcript.ipynb%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A56%2C%22character%22%3A142%7D%7D%2C%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2FUsers%2Fngocp%2FDocuments%2Fprojects%2Fpyml%2Fyoutube-summarize%2Fyoutube-transcript.ipynb%22%2C%22external%22%3A%22file%3A%2F%2F%2FUsers%2Fngocp%2FDocuments%2Fprojects%2Fpyml%2Fyoutube-summarize%2Fyoutube-transcript.ipynb%22%2C%22path%22%3A%22%2FUsers%2Fngocp%2FDocuments%2Fprojects%2Fpyml%2Fyoutube-summarize%2Fyoutube-transcript.ipynb%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A151%2C%22character%22%3A18%7D%7D%5D%5D "Go to definition")
- [`dotenv`](command:_github.copilot.openSymbolFromReferences?%5B%22dotenv%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2FUsers%2Fngocp%2FDocuments%2Fprojects%2Fpyml%2Fyoutube-summarize%2Fyoutube-transcript.ipynb%22%2C%22external%22%3A%22file%3A%2F%2F%2FUsers%2Fngocp%2FDocuments%2Fprojects%2Fpyml%2Fyoutube-summarize%2Fyoutube-transcript.ipynb%22%2C%22path%22%3A%22%2FUsers%2Fngocp%2FDocuments%2Fprojects%2Fpyml%2Fyoutube-summarize%2Fyoutube-transcript.ipynb%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A167%2C%22character%22%3A12%7D%7D%5D%5D "Go to definition")

## Setup

1. Clone the repository.
2. Install the required packages:
    ```sh
    pip install youtube-transcript-api llama-index python-dotenv
    ```
3. Create a [`.env`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fngocp%2FDocuments%2Fprojects%2Fpyml%2Fyoutube-summarize%2F.env%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/ngocp/Documents/projects/pyml/youtube-summarize/.env") file in the root directory and add your OpenAI API key:
    ```
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

1. Open the [`youtube-transcript.ipynb`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fngocp%2FDocuments%2Fprojects%2Fpyml%2Fyoutube-summarize%2Fyoutube-transcript.ipynb%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/ngocp/Documents/projects/pyml/youtube-summarize/youtube-transcript.ipynb") notebook in Jupyter or any compatible environment.
2. Run the cells sequentially to:
    - Load environment variables.
    - Retrieve the transcript for a specified YouTube video.
    - Process the transcript.
    - Save the processed transcript to the [`data-transcript`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fngocp%2FDocuments%2Fprojects%2Fpyml%2Fyoutube-summarize%2Fdata-transcript%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/ngocp/Documents/projects/pyml/youtube-summarize/data-transcript") directory.

## Key Functions

- **Loading Environment Variables**:
    ```python
    dotenv.load_dotenv('./.env')
    apiKey = os.getenv("OPENAI_API_KEY")
    ```

- **Retrieving Transcript**:
    ```python
    video_id = 'g3CvsPAF3_0'
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
    ```

- **Processing Transcript**:
    ```python
    combined_text = ' '.join([entry['text'] for entry in transcript])
    ```

- **Saving Transcript**:
    ```python
    def output_transcript(transcript, output_file):
        with open(output_file, 'w') as f:
            for entry in transcript:
                f.write(entry['text'] + '\n')

    path_dir = './data-transcript/'
    output_transcript(transcript, path_dir + video_id + '.txt')
    ```

## Example

To retrieve and save the transcript of a YouTube video with ID [`g3CvsPAF3_0`](command:_github.copilot.openSymbolFromReferences?%5B%22g3CvsPAF3_0%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2FUsers%2Fngocp%2FDocuments%2Fprojects%2Fpyml%2Fyoutube-summarize%2Fyoutube-transcript.ipynb%22%2C%22external%22%3A%22file%3A%2F%2F%2FUsers%2Fngocp%2FDocuments%2Fprojects%2Fpyml%2Fyoutube-summarize%2Fyoutube-transcript.ipynb%22%2C%22path%22%3A%22%2FUsers%2Fngocp%2FDocuments%2Fprojects%2Fpyml%2Fyoutube-summarize%2Fyoutube-transcript.ipynb%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A203%2C%22character%22%3A17%7D%7D%5D%5D "Go to definition"):

1. Set the [`video_id`](command:_github.copilot.openSymbolFromReferences?%5B%22video_id%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2FUsers%2Fngocp%2FDocuments%2Fprojects%2Fpyml%2Fyoutube-summarize%2Fyoutube-transcript.ipynb%22%2C%22external%22%3A%22file%3A%2F%2F%2FUsers%2Fngocp%2FDocuments%2Fprojects%2Fpyml%2Fyoutube-summarize%2Fyoutube-transcript.ipynb%22%2C%22path%22%3A%22%2FUsers%2Fngocp%2FDocuments%2Fprojects%2Fpyml%2Fyoutube-summarize%2Fyoutube-transcript.ipynb%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A203%2C%22character%22%3A5%7D%7D%5D%5D "Go to definition") variable:
    ```python
    video_id = 'g3CvsPAF3_0'
    ```

2. Retrieve the transcript:
    ```python
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
    ```

3. Save the transcript:
    ```python
    output_transcript(transcript, path_dir + video_id + '.txt')
    ```

## License

This project is licensed under the MIT License.