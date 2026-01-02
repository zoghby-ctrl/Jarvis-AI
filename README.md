# Jarvis: Local AI Assistant

## Description
Jarvis is a voice-activated AI assistant designed to run locally on your PC. Unlike cloud-based assistants (like Siri or Alexa), Jarvis runs its "brain" (LLM) entirely on your own hardware using Ollama, ensuring privacy and speed. It features high-quality neural voice output and can control applications on your computer.

## Features
* **100% Local Intelligence:** Powered by Llama 3.2 or Phi-3 running on your GPU.
* **Neural Voice:** Uses Microsoft Edge-TTS for realistic, human-like speech (British/American accents).
* **Voice Activation:** Listens for commands via microphone and transcribes audio in real-time.
* **App Control:** Can launch applications (e.g., "Open Spotify", "Open Calculator").
* **Conversation Memory:** Remembers context from previous turns in the conversation.
* **Privacy-First:** No conversational data is sent to OpenAI or Google servers (when using local Speech-to-Text).

## Technology Stack
* **Language:** Python 3.12
* **AI Engine:** [Ollama](https://ollama.com/) (running Llama 3.2 or Phi-3)
* **Libraries:**
    * `speech_recognition` (Audio input)
    * `edge-tts` (Neural voice output)
    * `pygame` (Audio playback)
    * `AppOpener` (System control)

## Prerequisites
* **Python 3.12** (Avoid 3.14 for compatibility)
* **Ollama** installed and running (`ollama server`)
* A working microphone and speakers.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/zoghby-ctrl/Jarvis-AI.git](https://github.com/zoghby-ctrl/Jarvis-AI.git)
    cd Jarvis-AI
    ```

2.  **Install Dependencies:**
    ```bash
    pip install ollama speechrecognition AppOpener edge-tts asyncio pygame
    ```

3.  **Download the Brain:**
    Open your terminal and pull the model you want to use:
    ```bash
    ollama run llama3.2
    ```

## How to Run
1.  Ensure your microphone is connected.
2.  Run the script:
    ```bash
    py -3.12 main.py
    ```
3.  **Speak!** Try saying:
    * *"Open Notepad"*
    * *"Who was Tony Stark?"*
    * *"Explain quantum physics in one sentence."*

## License
This project is licensed under the MIT License - see the LICENSE file for details.
