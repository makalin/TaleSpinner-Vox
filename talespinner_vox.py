import json
import pyttsx3
import time
import os

class TaleSpinnerVox:
    def __init__(self, story_file, voiceover=False):
        self.engine = pyttsx3.init() if voiceover else None
        self.voiceover = voiceover
        self.state = {"inventory": [], "current_scene": "start"}
        self.story_file = story_file
        self.story = self.load_story(story_file)
        self.save_file = "savegame.json"

    def load_story(self, story_file):
        with open(story_file, 'r') as f:
            return json.load(f)

    def speak(self, text):
        if self.voiceover and self.engine:
            self.engine.say(text)
            self.engine.runAndWait()
        print(text)

    def display_image(self, image_lines):
        """Display ASCII art or text-based image."""
        for line in image_lines:
            print(line)
            if self.voiceover and self.engine:
                self.engine.say(line)  # Narrate each line for dramatic effect
                self.engine.runAndWait()
            time.sleep(0.1)  # Slight delay for readability

    def save_game(self):
        """Save current state to a file."""
        with open(self.save_file, 'w') as f:
            json.dump(self.state, f, indent=2)
        self.speak("Game saved successfully!")

    def load_game(self):
        """Load state from a file if it exists."""
        if os.path.exists(self.save_file):
            with open(self.save_file, 'r') as f:
                self.state = json.load(f)
            self.speak("Game loaded successfully!")
            return True
        self.speak("No save file found.")
        return False

    def play(self):
        while True:
            scene = self.story.get(self.state["current_scene"], {"text": "The end.", "choices": []})
            
            # Display optional mini scene image
            if "image" in scene:
                self.display_image(scene["image"])
            
            self.speak(scene["text"])

            if not scene["choices"]:
                break

            # Add save/load options to every scene
            self.speak("0. Save game | -1. Load game")
            for i, choice in enumerate(scene["choices"], 1):
                self.speak(f"{i}. {choice['text']}")

            try:
                choice = int(input("Choose an option: "))
                if choice == 0:
                    self.save_game()
                elif choice == -1:
                    self.load_game()
                elif 1 <= choice <= len(scene["choices"]):
                    choice_idx = choice - 1
                    next_scene = scene["choices"][choice_idx]["next"]
                    if "item" in scene["choices"][choice_idx]:
                        self.state["inventory"].append(scene["choices"][choice_idx]["item"])
                        self.speak(f"Added {scene['choices'][choice_idx]['item']} to inventory.")
                    self.state["current_scene"] = next_scene
                else:
                    self.speak("Invalid choice, try again.")
            except ValueError:
                self.speak("Please enter a number.")

# Example usage
if __name__ == "__main__":
    # Updated sample JSON story with images (save as 'story.json')
    sample_story = {
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
            "image": [
                "    ---+---    ",
                "   /       \\   ",
                "  /         \\  "
            ],
            "choices": [
                {"text": "Go left", "next": "beast"},
                {"text": "Go right", "next": "village"}
            ]
        },
        "beast": {
            "text": "A bear attacks! Do you fight or flee?",
            "image": [
                "   (__/)      ",
                "   (o^-^o)    ",
                "   (o o)      "
            ],
            "choices": [
                {"text": "Fight (if you have a sword)", "next": "victory" if "sword" in {"inventory": []} else "death"},
                {"text": "Flee", "next": "forest_path"}
            ]
        },
        "village": {
            "text": "You find a peaceful village. The adventure ends here.",
            "image": [
                "   /\\  /\\    ",
                "  /__\\/__\\   ",
                "  |  ||  |   "
            ],
            "choices": []
        },
        "victory": {
            "text": "You slay the beast and emerge victorious!",
            "choices": []
        },
        "death": {
            "text": "Without a weapon, the bear overwhelms you. Game over.",
            "choices": []
        }
    }

    # Save sample story to a file
    with open("story.json", "w") as f:
        json.dump(sample_story, f, indent=2)

    # Start the game with voiceover mode enabled
    game = TaleSpinnerVox("story.json", voiceover=True)
    game.play()