# TaleSpinner Vox

A console-based text adventure maker and player, built in Python. Create and play interactive stories in the terminal with a JSON-based story format, enhanced by a unique "voiceover mode" using text-to-speech for dramatic narration. Features include save/load functionality and mini scene images (ASCII art) for added immersion.

## Features
- **JSON Story Format**: Define scenes, choices, and items in a simple, editable JSON file.
- **Voiceover Mode**: Toggle text-to-speech narration for a dramatic, immersive experience.
- **State Management**: Tracks inventory and current scene, with save/load support.
- **Mini Scene Images**: Add ASCII art to scenes for visual flair, narrated in voiceover mode.
- **Cross-Platform**: Runs in any terminal with Python installed.

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/makalin/talespinner-vox.git
   cd talespinner-vox
   ```
2. **Install Python**: Ensure Python 3.6+ is installed ([Download](https://www.python.org/downloads/)).
3. **Install Dependencies**:
   ```bash
   pip install pyttsx3
   ```
   - Note: On Linux, you may need `espeak` or `libespeak` for `pyttsx3` to work (`sudo apt install espeak`).

## Usage
1. **Run the Game**:
   ```bash
   python talespinner_vox.py
   ```
   - By default, it loads `story.json` with voiceover enabled.
   - To disable voiceover: Edit the `game = TaleSpinnerVox("story.json", voiceover=False)` line.

2. **Game Controls**:
   - Enter a number (e.g., `1`, `2`) to choose an option.
   - `0`: Save the game to `savegame.json`.
   - `-1`: Load a saved game from `savegame.json`.

3. **Create Your Own Story**:
   - Edit `story.json` (see [Story Format](#story-format) below) or create a new JSON file and pass it to `TaleSpinnerVox("your_story.json")`.

## Story Format
Stories are defined in a JSON file (e.g., `story.json`). Here’s the structure:

```json
{
  "start": {
    "text": "You wake up in a dark forest. A rusty sword lies nearby.",
    "image": [
      "      /\\      ",
      "     /  \\     ",
      "    /____\\    ",
      "      ||||    ",
      "      ||||    "
    ],
    "choices": [
      {"text": "Pick up the sword", "next": "forest_path", "item": "sword"},
      {"text": "Leave it and walk away", "next": "forest_path"}
    ]
  },
  "forest_path": {
    "text": "You reach a fork. A growl echoes from the left.",
    "choices": [
      {"text": "Go left", "next": "beast"},
      {"text": "Go right", "next": "village"}
    ]
  }
}
```

- **`key`**: Scene ID (e.g., `"start"`, `"forest_path"`).
- **`text`**: Narrative text for the scene.
- **`image`** (optional): List of strings for ASCII art.
- **`choices`**: List of options:
  - `text`: Choice description.
  - `next`: Next scene ID.
  - `item` (optional): Item added to inventory if chosen.

## Example Gameplay
```
      /\
     /  \
    /____\
      ||||
      ||||
You wake up in a dark forest. A rusty sword lies nearby.
0. Save game | -1. Load game
1. Pick up the sword
2. Leave it and walk away
Choose an option: 1
Added sword to inventory.
```

## Contributing
We welcome contributions! Here’s how to get started:
1. Fork the repository.
2. Create a branch (`git checkout -b feature/your-idea`).
3. Commit your changes (`git commit -m "Add cool feature"`).
4. Push to your branch (`git push origin feature/your-idea`).
5. Open a Pull Request.

Ideas for contributions:
- Add sound effects (e.g., via `playsound`).
- Support conditional branching (e.g., "next" depends on inventory).
- Improve voiceover with pitch/speed adjustments.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
